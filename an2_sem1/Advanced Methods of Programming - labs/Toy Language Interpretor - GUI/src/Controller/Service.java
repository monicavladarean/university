package Controller;
import Repository.*;
import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Value.*;
import Model.Statement.*;

import java.io.IOException;
import java.sql.Ref;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Service
{
    private IRepository repo;
    private ExecutorService executor=null;
    private List<PrgState> prgList;

    public Service(IRepository repo)
    {
        this.repo = repo;
    }

    private void executeGarbageCollector(List<PrgState> completedProgramList)
    {
        //list with all adresses in all SymTables
        List<Integer> symtable=completedProgramList.stream()
                .map(e->e.getSymTable().getContent().values())
                .map(e->getAddrFromSymTable(e))
                .reduce(Stream.of(0).collect(Collectors.toList()), (s1,s2)->Stream.concat(s1.stream(),s2.stream()).collect(Collectors.toList()));

        //we take the values from the heap (heap same for all prg's)
        Collection<Value> heapTableValues = completedProgramList.get(0).getHeap().getContent().values();

        //take from heap only what is an ok refference
        List<Integer> heap=heapTableValues.stream()
                .filter(v->v instanceof RefValue)
                .map(v->{RefValue val=(RefValue) v; return val.getAddress();})
                .collect(Collectors.toList());
        symtable.addAll(heap);
        completedProgramList.get(0).getHeap().setContent(unsafeGarbageCollector(symtable,completedProgramList.get(0).getHeap().getContent()));
    }

    private Map<Integer,Value> unsafeGarbageCollector(List<Integer> symTableAddr, Map<Integer,Value> heap)
    {
        return heap.entrySet().stream().filter(e->symTableAddr.contains(e.getKey())).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    private List<Integer> getAddrFromSymTable(Collection<Value> symTableValues){
        return symTableValues.stream().filter(v-> v instanceof RefValue).map(v-> {RefValue v1 = (RefValue)v; return v1.getAddress();}).collect(Collectors.toList());
    }

    public void oneStepForAllPrg(List<PrgState> prgList)  {
        //prints the PrgState List into file
        prgList.forEach(prg -> {
            try
            {
                repo.logPrgStateExec(prg);
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        });

        //runs concurently oneStep, for each thread(PrgState)
        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>)(() -> {return p.oneStep();}))
                .collect(Collectors.toList());

        //starts the execution of the callables
        try
        {
            List<PrgState> newPrgList = executor.invokeAll(callList). stream()
                    .map(future -> {
                                try {
                                    return future.get();
                                } catch (InterruptedException | ExecutionException e) {
                                    System.out.println(e.getMessage());
                                }
                                return null;
                                }
                    ).filter(p -> p!=null)
                                .collect(Collectors.toList());

            //add the new create threads to the list of existing threads
            prgList.addAll(newPrgList);

            prgList.forEach(prg -> {
                try
                {
                    repo.logPrgStateExec(prg);
                }
                catch (IOException e)
                {
                    e.printStackTrace();
                }
            });

            //save the current programs in the repo
            repo.setPrgList(prgList);
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }
    }

    public void allStep() throws MyException {
        executor = Executors.newFixedThreadPool(2);
        removeCompletedPrg(repo.getPrgList());
        List<PrgState> prgs=repo.getPrgList();
        if(prgs.size()>0)
        {
            this.executeGarbageCollector(prgs);
            oneStepForAllPrg(prgs);
            removeCompletedPrg(repo.getPrgList());
            executor.shutdownNow();
        }
    }

    public List<PrgState> removeCompletedPrg(List<PrgState> inPrgList)
    {
        return inPrgList.stream().filter(p -> p.isNotCompleted()).collect(Collectors.toList());
    }

    public List<PrgState> getPrgStatesList()
    {
        return repo.getPrgList();
    }
}
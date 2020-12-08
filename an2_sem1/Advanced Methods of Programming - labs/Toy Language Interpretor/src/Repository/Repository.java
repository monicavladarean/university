package Repository;
import Model.ADT_utils.*;
import Model.Exceptions.*;

import java.awt.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepository
{
    private List<PrgState> repo;
    private String logFilePath;

    public Repository(String path)
    {
        this.repo = new ArrayList<PrgState>();
        this.logFilePath=path;
    }

    @Override
    public String toString()
    {
        return "Repository{" +
                "repo=" + repo +
                '}';
    }

    @Override
    public void addPrgState(PrgState prg)
    {
        this.repo.add(prg);
    }

    public String getLogFilePath()
    {
        return logFilePath;
    }

    @Override
    public void logPrgStateExec(PrgState PrgState2) throws IOException
    {
        PrintWriter pw = new PrintWriter(new FileOutputStream(new File(logFilePath),true));
        pw.println(PrgState2.toString());
        pw.flush();
    }

    @Override
    public List<PrgState> getPrgList() {
        return this.repo;
    }

    @Override
    public void setPrgList(List<PrgState> PrgState2) {
        this.repo=PrgState2;
    }
}

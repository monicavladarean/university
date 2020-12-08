package Model.Statement;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Type.Type;
import Model.Value.StringValue;
import Model.Value.Value;

import java.io.BufferedReader;
import java.util.Map;

public class ForkStmt implements IStmt
{
    private IStmt stmt;

    public ForkStmt(IStmt stmt)
    {
        this.stmt = stmt;
    }

    @Override
    public String toString() {
        return "ForkStmt{" +
                "stmt=" + stmt +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IFileTable<StringValue, BufferedReader> fileTbl=state.getFileTable();
        IHeap<Integer, Value> heap=state.getHeap();

        MyIStack<IStmt> stk2=new MyStack<>();
        MyIDictionary<String,Value> symTbl2= new MyDictionary<>();

        for(Map.Entry<String,Value> entry:symTbl.getContent().entrySet())
        {
            symTbl2.put(entry.getKey(),entry.getValue().deepCopy());
        }

        PrgState prgState2=new PrgState(stk2,symTbl2,out,fileTbl,heap,this.stmt);
        return prgState2;
    }

    @Override
    public IStmt deepCopy() {
        return new ForkStmt(this.stmt.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        MyIDictionary<String, Type> typeEnv1=stmt.typecheck(typeEnv);
        return typeEnv;
    }
}

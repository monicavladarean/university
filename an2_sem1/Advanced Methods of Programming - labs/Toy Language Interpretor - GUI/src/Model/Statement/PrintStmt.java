package Model.Statement;
import Model.Expression.*;
import Model.Exceptions.*;
import Model.ADT_utils.*;
import Model.Value.*;
import Model.Type.*;

public class PrintStmt implements IStmt
{
    private Exp exp;

    @Override
    public String toString()
    {
        return "PrintStmt{" +
                "exp=" + exp +
                '}';
    }

    public PrintStmt(Exp exp)
    {
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IHeap<Integer,Value>heap=state.getHeap();
        Value val=this.exp.eval(symTbl,heap);
        out.add(val);

        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new PrintStmt(this.exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typ = exp.typecheck(typeEnv);
        return typeEnv;
    }
}

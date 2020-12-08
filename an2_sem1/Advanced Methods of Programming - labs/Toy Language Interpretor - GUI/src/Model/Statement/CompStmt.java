package Model.Statement;
import Model.ADT_utils.*;
import Model.Exceptions.*;
import Model.Type.Type;

public class CompStmt implements IStmt
{
    private IStmt first;
    private IStmt second;

    @Override
    public String toString()
    {
        return "CompStmt{" +
                "first=" + first +
                ", second=" + second +
                '}';
    }

    public CompStmt(IStmt first, IStmt second)
    {
        this.first = first;
        this.second = second;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        stk.push(second);
        stk.push(first);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new CompStmt(this.first.deepCopy(),this.second.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        return second.typecheck(first.typecheck(typeEnv));
    }
}

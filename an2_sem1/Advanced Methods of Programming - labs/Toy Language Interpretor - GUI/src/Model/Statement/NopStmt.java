package Model.Statement;

import Model.ADT_utils.MyIDictionary;
import Model.ADT_utils.PrgState;
import Model.Exceptions.MyException;
import Model.Type.Type;

public class NopStmt implements IStmt
{
    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        return state;
    }

    @Override
    public String toString()
    {
        return "NopStmt{}";
    }

    public NopStmt()
    {
    }

    @Override
    public IStmt deepCopy() {
        return new NopStmt();
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        return typeEnv;
    }
}

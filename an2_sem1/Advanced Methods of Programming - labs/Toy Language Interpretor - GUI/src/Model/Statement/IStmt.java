package Model.Statement;
import Model.ADT_utils.MyIDictionary;
import Model.ADT_utils.PrgState;
import Model.Exceptions.MyException;
import Model.ICopy;
import Model.Type.Type;

public interface IStmt extends ICopy<IStmt>
{
    public PrgState execute (PrgState state) throws MyException;
    MyIDictionary<String,Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException;
}


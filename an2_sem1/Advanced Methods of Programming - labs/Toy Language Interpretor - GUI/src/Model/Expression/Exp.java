package Model.Expression;
import Model.Exceptions.MyException;
import Model.ICopy;
import Model.Type.Type;
import Model.Value.*;
import Model.ADT_utils.*;

public interface Exp extends ICopy<Exp>
{
    public Value eval(MyIDictionary<String,Value> tbl,IHeap<Integer,Value>heap) throws MyException;
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException;

}

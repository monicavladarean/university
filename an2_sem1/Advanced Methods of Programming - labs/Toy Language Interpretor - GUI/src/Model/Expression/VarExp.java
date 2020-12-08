package Model.Expression;
import Model.ADT_utils.IHeap;
import Model.ADT_utils.MyIDictionary;
import Model.Exceptions.MyException;
import Model.Type.Type;
import Model.Value.*;

public class VarExp implements Exp
{
    private String id;

    public VarExp(String id)
    {
        this.id = id;
    }

    @Override
    public String toString()
    {
        return "VarExp{" +
                "id='" + id + '\'' +
                '}';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap<Integer,Value> heap) throws MyException
    {
        return tbl.lookup(id);
    }

    @Override
    public Exp deepCopy() {
        return new VarExp(this.id);
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        return typeEnv.lookup(id);
    }
}




package Model.Expression;
import Model.Type.Type;
import Model.Value.*;
import Model.ADT_utils.*;
import Model.Exceptions.MyException;

public class ValueExp implements Exp
{
    private  Value e;

    public ValueExp(Value e)
    {
        this.e = e;
    }

    @Override
    public String toString() {
        return "ValueExp{" +
                "e=" + e +
                '}';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl,IHeap<Integer,Value>heap) throws MyException
    {
        return this.e;
    }

    @Override
    public Exp deepCopy() {
        return new ValueExp(this.e.deepCopy());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        return e.getType();
    }
}

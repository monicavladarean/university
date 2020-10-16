package Model.Value;
import Model.Type.*;

public class IntValue implements Value
{
    private int val=0;

    public IntValue(int v)
    {
        val=v;
    }


    public int getVal()
    {
        return val;
    }

    @Override
    public String toString() {
        return "IntValue{" +
                "val=" + val +
                '}';
    }

    @Override

    public Type getType()
    {
        return new IntType();
    }

    public boolean equals(Object obj)
    {
        if (obj instanceof IntValue)
            if(((IntValue) obj).getVal()==this.val)
                return true;
            else
                return false;
        else
            return false;

    }

    @Override
    public Value deepCopy() {
        return new IntValue(this.val);
    }
}
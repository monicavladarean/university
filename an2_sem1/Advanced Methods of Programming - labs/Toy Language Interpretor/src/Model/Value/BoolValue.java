package Model.Value;
import Model.Type.*;

public class BoolValue implements Value
{
    private boolean val=false;

    public BoolValue(boolean v)
    {
        val=v;
    }

    public boolean getVal()
    {
        return val;
    }

    @Override
    public String toString() {
        return "BoolValue{" +
                "val=" + val +
                '}';
    }

    @Override

    public Type getType()
    {
        return new BoolType();
    }

    @Override
    public boolean equals(Object obj)
    {
        if (obj instanceof BoolValue)
            if(((BoolValue) obj).getVal()==this.val)
                return true;
            else
                return false;
        else
            return false;

    }

    @Override
    public Value deepCopy() {
        return new BoolValue(this.val);
    }
}

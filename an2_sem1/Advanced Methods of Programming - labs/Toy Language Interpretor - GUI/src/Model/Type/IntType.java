package Model.Type;

import Model.Value.BoolValue;
import Model.Value.IntValue;
import Model.Value.Value;

public class IntType implements Type
{
    @Override
    public boolean equals(Object another)
    {
        if (another instanceof IntType)
            return true;
        else
            return false;
    }

    @Override
    public String toString() {
        return "IntType{}";
    }

    @Override
    public Value defaultValue()
    {
        return new IntValue(0);
    }

    @Override
    public Type deepCopy() {
        return new IntType();
    }
}

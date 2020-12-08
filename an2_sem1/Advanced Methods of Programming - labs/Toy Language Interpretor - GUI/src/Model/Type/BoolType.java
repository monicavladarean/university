package Model.Type;

import Model.Value.BoolValue;
import Model.Value.IntValue;
import Model.Value.Value;

public class BoolType implements Type
{
    @Override
    public String toString() {
        return "BoolType{}";
    }

    @Override
    public boolean equals(Object another)
    {
        if(another instanceof BoolType)
            return true;
        else
            return false;
    }

    @Override
    public Value defaultValue()
    {
        return new BoolValue(false);
    }

    @Override
    public Type deepCopy() {
        return new BoolType();
    }
}

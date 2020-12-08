package Model.Type;

import Model.Value.StringValue;
import Model.Value.Value;

public class StringType implements Type
{
    @Override
    public Value defaultValue()
    {
        return new StringValue("");
    }

    @Override
    public String toString()
    {
        return "StringType{}";
    }

    @Override
    public boolean equals(Object obj)
    {
        if (obj instanceof StringType)
            return true;
        else
            return false;
    }

    @Override
    public Type deepCopy() {
        return new StringType();
    }
}

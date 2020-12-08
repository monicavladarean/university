package Model.Type;

import Model.Value.RefValue;
import Model.Value.Value;

public class RefType implements Type
{
    Type inner;

    public RefType(Type inner)
    {
        this.inner = inner;
    }

    public Type getInner()
    {
        return inner;
    }

    @Override
    public String toString()
    {
        return "RefType{" +
                "inner=" + inner +
                '}';
    }

    @Override
    public Value defaultValue()
    {
        return new RefValue(0,inner);
    }

    @Override
    public boolean equals(Object obj)
    {
        if (obj instanceof RefType)
            return inner.equals(((RefType) obj).getInner());
        else
            return false;
    }

    @Override
    public Type deepCopy() {
        return new RefType(this.inner.deepCopy());
    }
}

package Model.Value;
import Model.ICopy;
import Model.Type.*;

public interface Value extends ICopy<Value>
{
    public Type getType();
}


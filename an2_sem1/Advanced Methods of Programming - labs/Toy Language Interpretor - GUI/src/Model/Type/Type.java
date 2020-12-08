package Model.Type;

import Model.ICopy;
import Model.Value.Value;

public interface Type extends ICopy<Type>
{
    public Value defaultValue();
}

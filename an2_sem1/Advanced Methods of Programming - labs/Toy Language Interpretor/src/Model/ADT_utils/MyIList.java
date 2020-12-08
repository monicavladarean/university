package Model.ADT_utils;
import Model.Exceptions.*;

public interface MyIList<T>
{
    public int size();
    public boolean isEmpty();
    public void add(T element);
}

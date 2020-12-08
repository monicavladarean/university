package Model.ADT_utils;
import Model.Exceptions.*;

public interface MyIStack<T>
{
    public boolean isEmpty();
    public T pop() throws MyException;
    public void push(T v);
}

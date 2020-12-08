package Model.ADT_utils;
import java.util.Stack;
import Model.Exceptions.*;

public class MyStack<T> implements MyIStack<T>
{
    private Stack<T> stack;

    public MyStack()
    {
        this.stack = new Stack<T>();
    }

    @Override
    public boolean isEmpty()
    {
        if(this.stack.isEmpty()==true)
            return true;
        else
            return false;
    }

    @Override
    public T pop() throws MyException
    {
        if(this.stack.isEmpty()==true)
            throw new MyException("Collection is empty");
        return this.stack.pop();
    }

    @Override
    public void push(T v)
    {
        this.stack.push(v);
    }

    @Override
    public String toString()
    {
        return "Stack{" +
                "stack=" + stack +
                '}';
    }
}

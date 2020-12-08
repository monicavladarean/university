package Model.ADT_utils;
import Model.Exceptions.*;
import java.util.ArrayList;

public class MyList<T> implements MyIList<T>
{
    private  ArrayList<T> list;

    public MyList()
    {
        this.list=new ArrayList<T>();
    }

    @Override
    public int size()
    {
        return this.list.size();
    }

    @Override
    public boolean isEmpty()
    {
        if(this.list.size()>0)
            return true;
        else
            return false;
    }

    @Override
    public void add(T element)
    {
        this.list.add(element);
    }

    @Override
    public String toString() {
        return "MyList{" +
                "list=" + list +
                '}';
    }
}

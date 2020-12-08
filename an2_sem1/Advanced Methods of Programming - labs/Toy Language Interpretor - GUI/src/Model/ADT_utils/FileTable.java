package Model.ADT_utils;

import Model.Exceptions.MyException;

import java.io.FileDescriptor;
import java.util.HashMap;

public class FileTable<Filename,FileDesc> implements IFileTable<Filename,FileDesc>
{
    private HashMap<Filename,FileDesc> table;

    public FileTable()
    {
        this.table = new HashMap<Filename,FileDesc>();
    }

    @Override
    public String toString()
    {
        return "FileTable{" +
                "table=" + table +
                '}';
    }

    @Override
    public boolean isEmpty()
    {
        return (this.table.isEmpty());
    }

    @Override
    public void put(Filename key, FileDesc value)
    {
        this.table.put(key,value);
    }

    @Override
    public int size()
    {
        return this.table.size();
    }

    @Override
    public boolean isDefined(Filename key)
    {
        return this.table.containsKey(key);
    }

    @Override
    public FileDesc getValue(Filename key) throws MyException
    {
        if(this.table.containsKey(key)==false)
            throw new MyException("No such file exists!");
        else
            return this.table.get(key);
    }

    @Override
    public void remove(Filename f)
    {
        this.table.remove(f);
    }
}

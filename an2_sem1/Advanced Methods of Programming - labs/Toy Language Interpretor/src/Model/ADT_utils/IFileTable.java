package Model.ADT_utils;

import Model.Exceptions.MyException;

import java.security.Key;

public interface IFileTable<Filename,FileDesc>
{
    public boolean isEmpty();
    public void put(Filename key, FileDesc value);
    public int size();
    public boolean isDefined(Filename key);
    public FileDesc getValue(Filename key) throws MyException;
    public void remove(Filename f);
}

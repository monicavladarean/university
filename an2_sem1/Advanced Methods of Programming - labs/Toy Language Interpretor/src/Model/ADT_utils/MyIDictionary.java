package Model.ADT_utils;
import Model.Exceptions.*;

import java.util.Collection;
import java.util.HashMap;

public interface MyIDictionary<Key,T>
{
    public boolean isEmpty();
    public void put(Key key, T value);
    public int size();
    public boolean isDefined(Key key);
    public T getValue(Key key) throws MyException;
    public void update(Key key,T value) throws MyException;
    public T lookup(Key key) throws MyException;
    public Collection<T> values();
    public HashMap<Key, T> getContent();
}

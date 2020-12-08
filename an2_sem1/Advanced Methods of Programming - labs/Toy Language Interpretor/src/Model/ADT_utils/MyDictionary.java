package Model.ADT_utils;
import Model.Exceptions.*;

import java.util.Collection;
import java.util.HashMap;

public class MyDictionary<Key,T> implements MyIDictionary<Key,T>
{
    private  HashMap<Key,T> dictionary;

    public MyDictionary()
    {
        this.dictionary =new HashMap<Key,T>();
    }

    @Override
    public String toString() {
        return "MyDictionary{" +
                "dictionary=" + dictionary +
                '}';
    }

    @Override
    public boolean isEmpty()
    {
        return this.dictionary.isEmpty();
    }

    @Override
    public void put(Key key, T value)
    {
        this.dictionary.put(key,value);
    }

    @Override
    public int size()
    {
        return this.dictionary.size();
    }

    @Override
    public T getValue(Key key) throws MyException
    {
        if(this.dictionary.containsKey(key)==false)
            throw new MyException("No such key in the dictionary");

        return this.dictionary.get(key);
    }

    @Override
    public void update(Key key, T value) throws MyException
    {
        if(this.dictionary.containsKey(key)==false)
         throw new MyException("No such key in the dictionary");
        this.dictionary.replace(key,value);
    }

    @Override
    public T lookup(Key key) throws MyException
    {
        if(this.dictionary.containsKey(key)==false)
            throw new MyException("No such key in the dictionary");
        return this.dictionary.get(key);
    }

    @Override
    public boolean isDefined(Key key)
    {
       return this.dictionary.containsKey(key);
    }

    @Override
    public Collection<T> values() {
        return this.dictionary.values();
    }

    @Override
    public HashMap<Key, T> getContent() {
        HashMap<Key,T> map=new HashMap<>();
        map=this.dictionary;
        return map;
    }
}

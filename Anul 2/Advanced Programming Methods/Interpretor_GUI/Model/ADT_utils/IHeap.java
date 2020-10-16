package Model.ADT_utils;

import Model.Exceptions.MyException;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public interface IHeap<Integer, Value> {
    public boolean isEmpty();
    public void put(Integer address, Value content);
    public int size();
    public boolean isDefined(Integer address);
    public Value getContent(Integer address) throws MyException;
    public void update(Integer address, Value content) throws MyException;
    public int getFreeAddress();
    public Collection<Value> values();
    public HashMap<Integer, Value> getContent();
    public void setContent(Map<Integer, Value> map);
}

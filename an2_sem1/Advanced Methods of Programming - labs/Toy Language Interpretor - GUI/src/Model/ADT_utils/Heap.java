package Model.ADT_utils;

import Model.Exceptions.MyException;
import Model.Value.Value;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class Heap<Integer, Value> implements IHeap <Integer, Value>
{
    private HashMap <Integer, Value> heap;
    private int NewFreeAddress;

    public Heap()
    {
        this.heap =new HashMap<Integer, Value>();
        this.NewFreeAddress=0;
    }

    public HashMap<Integer, Value> getHeap()
    {
        return heap;
    }

    @Override
    public String toString()
    {
        return "Heap{" +
                "heap=" + heap +
                ", NewFreeAddress=" + NewFreeAddress +
                '}';
    }

    @Override
    public boolean isEmpty() {
        return this.heap.isEmpty();
    }

    @Override
    public void put(Integer address, Value content) {
        this.heap.put(address,content);
    }

    @Override
    public int size() {
        return this.heap.size();
    }

    @Override
    public boolean isDefined(Integer address) {
        return this.heap.containsKey(address);
    }

    @Override
    public Value getContent(Integer address) throws MyException {
        if(this.heap.containsKey(address)==false)
            throw new MyException("No such address in the heap");
        return this.heap.get(address);
    }

    @Override
    public void update(Integer address, Value content) throws MyException {
        if(this.heap.containsKey(address)==false)
            throw new MyException("No such address in the heap");
        this.heap.replace(address,content);
    }

    @Override
    public int getFreeAddress() {
        this.NewFreeAddress++;
        return this.NewFreeAddress;
    }

    @Override
    public Collection<Value> values() {
        return this.heap.values();
    }

    @Override
    public HashMap<Integer, Value> getContent() {
        HashMap<Integer, Value> map=new HashMap<>();
        map=this.heap;
        return map;
    }

    @Override
    public void setContent(Map<Integer, Value> map) {
        this.heap=(HashMap<Integer, Value>) map;
    }
}


package Model.ADT_utils;
import Model.Exceptions.MyException;
import Model.Value.*;
import Model.Statement.*;

import java.io.BufferedReader;

public class PrgState
{
    private MyIStack<IStmt> exeStack;
    private MyIDictionary<String, Value> symTable;
    private MyIList<Value> out;
    private IFileTable<StringValue,BufferedReader> fileTable;
    private IHeap<Integer,Value> heap;
    private int id;
    private static int static_id;
    IStmt originalProgram; //optional field, but good to have


    @Override
    public String toString()
    {
        return "PrgState{" +
                "\n id="+id+
                "\n exeStack=" + exeStack +
                ", \n symTable=" + symTable +
                ",\n  out=" + out +
                ",\n  fileTable=" + fileTable +
                ",\n  heap=" + heap +
                '}';
    }

    private synchronized static int getNextId()
    {
        static_id++;
        return static_id;
    }

    public IHeap<Integer, Value> getHeap()
    {
        return heap;
    }

    public void setHeap(IHeap<Integer, Value> heap)
    {
        this.heap = heap;
    }

    public MyIStack<IStmt> getExeStack()
    {
        return exeStack;
    }

    public void setExeStack(MyIStack<IStmt> exeStack)
    {
        this.exeStack = exeStack;
    }

    public MyIDictionary<String, Value> getSymTable()
    {
        return symTable;
    }

    public void setSymTable(MyIDictionary<String, Value> symTable)
    {
        this.symTable = symTable;
    }

    public MyIList<Value> getOut()
    {
        return out;
    }

    public void setOut(MyIList<Value> out)
    {
        this.out = out;
    }

    public IFileTable<StringValue,BufferedReader> getFileTable()
    {
        return fileTable;
    }

    public void setFileTable(IFileTable<StringValue,BufferedReader> fileTable)
    {
        this.fileTable = fileTable;
    }

    public PrgState(MyIStack<IStmt> stk, MyIDictionary<String,Value> symtbl, MyIList<Value> ot, IFileTable<StringValue,BufferedReader> fileT, IHeap<Integer,Value> heapp,IStmt originalProgramm)
    {
        exeStack=stk;
        symTable=symtbl;
        out = ot;
        fileTable=fileT;
        heap=heapp;
        id=getNextId();
        this.originalProgram=originalProgramm.deepCopy();//recreate the entire original prg
        stk.push(originalProgramm);
    }

    public Boolean isNotCompleted()
    {
        if(this.exeStack.isEmpty())
            return false;
        else
            return true;
    }

    public PrgState oneStep() throws MyException
    {
        if(exeStack.isEmpty())
            throw new MyException("Prgstate stack is empty");
        IStmt crtStmt = exeStack.pop();
        return crtStmt.execute(this);
    }
}

package Model.Statement;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Expression.Exp;
import Model.Type.StringType;
import Model.Type.Type;
import Model.Value.StringValue;
import Model.Value.Value;

import java.beans.Expression;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class OpenRFileStmt implements IStmt
{
    Exp exp;

    public OpenRFileStmt(Exp exp)
    {
        this.exp = exp;
    }

    @Override
    public String toString()
    {
        return "OpenRFileStmt{" +
                "exp=" + exp +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IFileTable<StringValue, BufferedReader> fileTbl=state.getFileTable();
        IHeap<Integer,Value>heap=state.getHeap();
        Value value=this.exp.eval(symTbl,heap);

        if(value.getType().equals(new StringType())==false)
            throw new MyException("Invalid type of exp!");
        StringValue strVal=(StringValue) value;
        if(fileTbl.isDefined(strVal)==true)
            throw new MyException("Exp already in the file table!");
        try
        {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(strVal.getStr()));
            fileTbl.put(strVal,bufferedReader);
        }
        catch (IOException e)
        {
            throw new MyException("Error in IO operation!");
        }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new OpenRFileStmt(this.exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typexp=this.exp.typecheck(typeEnv);
        return typeEnv;
    }
}

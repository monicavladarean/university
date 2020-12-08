package Model.Statement;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Expression.Exp;
import Model.Type.StringType;
import Model.Type.Type;
import Model.Value.StringValue;
import Model.Value.Value;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class closeRFileStmt implements IStmt
{
    Exp exp;

    public closeRFileStmt(Exp exp)
    {
        this.exp = exp;
    }

    @Override
    public String toString()
    {
        return "closeRFileStmt{" +
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

        Value val=exp.eval(symTbl,heap);
        if(!(val.getType().equals(new StringType())))
        {
            throw new MyException("Exp is not string!");
        }

        StringValue strVal = (StringValue) val;

        if(!(fileTbl.isDefined(strVal)))
        {
            throw new MyException("String value not found in File table!");
        }

        try
        {
            BufferedReader desc=fileTbl.getValue(strVal);
            desc.close();
            fileTbl.remove(strVal);
        }
        catch (IOException e)
        {
            throw  new  MyException("IO problem with the file!");
        }

        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new closeRFileStmt(this.exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typexp=this.exp.typecheck(typeEnv);
        return typeEnv;
    }
}

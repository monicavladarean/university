package Model.Statement;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Expression.Exp;
import Model.Type.IntType;
import Model.Type.RefType;
import Model.Type.StringType;
import Model.Type.Type;
import Model.Value.IntValue;
import Model.Value.StringValue;
import Model.Value.Value;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class readFileStmt implements IStmt
{
    Exp exp;
    String var_name;

    @Override
    public String toString()
    {
        return "readFileStmt{" +
                "exp=" + exp +
                ", var_name='" + var_name + '\'' +
                '}';
    }

    public readFileStmt(Exp exp, String var_name)
    {
        this.exp = exp;
        this.var_name = var_name;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IFileTable<StringValue, BufferedReader> fileTbl=state.getFileTable();
        IHeap<Integer,Value>heap=state.getHeap();
        if(symTbl.isDefined(var_name)==false)
            throw new MyException("No such file found!");

        StringValue strVal=(StringValue) exp.eval(symTbl,heap);
        try
        {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(strVal.getStr()));
            String strcurrent_line=bufferedReader.readLine();

            if(strcurrent_line==null)
            {
                IntValue val1=new IntValue(0);
                symTbl.update(this.var_name,val1);
            }
            else
            {
                IntValue val1=new IntValue(Integer.parseInt(strcurrent_line));
                symTbl.update(this.var_name,val1);
            }
        }
        catch (NumberFormatException e)
        {
            throw new MyException("Can't convert to int!");
        }
        catch (FileNotFoundException e)
        {
            throw new MyException("File not found!");
        }
        catch (IOException e)
        {
            throw new MyException("Error in reading!");
        }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new readFileStmt(this.exp.deepCopy(),this.var_name);
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typevar = typeEnv.lookup(var_name);
        Type typexp = this.exp.typecheck(typeEnv);
        if (typevar.equals(new IntType()) && typexp.equals(new StringType()))
            return typeEnv;
        else
            throw new MyException("Reading file: wrong variable type ");
    }
}

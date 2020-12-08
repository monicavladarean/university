package Model.Statement;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Expression.Exp;
import Model.Type.RefType;
import Model.Type.Type;
import Model.Value.IntValue;
import Model.Value.RefValue;
import Model.Value.StringValue;
import Model.Value.Value;

import java.beans.Expression;
import java.io.BufferedReader;

public class HeapAllocationStmt implements IStmt {
    private String var_name;
    private Exp expression;

    public HeapAllocationStmt(String var_name, Exp exp)
    {
        this.var_name = var_name;
        this.expression = exp;
    }

    @Override
    public String toString()
    {
        return "HeapAllocationStmt{" +
                "var_name='" + var_name + '\'' +
                ", exp=" + expression +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IFileTable<StringValue, BufferedReader> fileTbl=state.getFileTable();
        IHeap<Integer, Value> heap=state.getHeap();

        if(symTbl.isDefined(this.var_name)==false)
            throw new MyException("Inexistent var");

        Value val=expression.eval(symTbl,heap);
        Value valFromVarName = symTbl.getValue(var_name);
        RefValue refValFromVarName=(RefValue)valFromVarName;
        Type locType=refValFromVarName.getLocationType();
        
        if(!(val.getType().equals(locType)))
            throw new MyException("The expression and the location type of var_name don't have the same type");

        int newHeapAddress=heap.getFreeAddress();
        heap.put(newHeapAddress, val);
        symTbl.update(var_name,new RefValue(newHeapAddress,val.getType()));

        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new HeapAllocationStmt(this.var_name,this.expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typevar = typeEnv.lookup(var_name);
        Type typexp = this.expression.typecheck(typeEnv);
        if (typevar.equals(new RefType(typexp)))
            return typeEnv;
        else
            throw new MyException("Assignment: right hand side and left hand side have different types ");
    }
}

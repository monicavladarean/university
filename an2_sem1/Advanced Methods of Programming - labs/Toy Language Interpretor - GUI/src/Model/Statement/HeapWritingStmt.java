package Model.Statement;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Expression.Exp;
import Model.Type.RefType;
import Model.Type.Type;
import Model.Value.RefValue;
import Model.Value.StringValue;
import Model.Value.Value;

import java.io.BufferedReader;

public class HeapWritingStmt implements IStmt {
    private String var_name;
    private Exp expression;

    public HeapWritingStmt(String var_name, Exp expression) {
        this.var_name = var_name;
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "HeapWritingStmt{" +
                "var_name='" + var_name + '\'' +
                ", expression=" + expression +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IFileTable<StringValue, BufferedReader> fileTbl=state.getFileTable();
        IHeap<Integer, Value> heap=state.getHeap();

        if(!(symTbl.isDefined(var_name)))
            throw new MyException("Var name not defined in SymTable");

        if(!(symTbl.getValue(var_name).getType() instanceof RefType))
            throw new MyException("Var type not a reftype");
        Type typeFromVarName=symTbl.getValue(var_name).getType();
        Value valueFromVarName=symTbl.getValue(var_name);
        RefValue refValFromVarName=(RefValue) valueFromVarName;
        int addressFromVarName=refValFromVarName.getAddress();

        if(!(heap.isDefined(addressFromVarName)))
            throw new MyException("The address of the RefValue associated to var_name in symTbl is not a key in the heap");

        Value val_eval=this.expression.eval(symTbl,heap);

        if(!(val_eval.getType().equals(refValFromVarName.getLocationType())))
            throw new MyException("Evaluation must have same type as the locType of the var_name type");
        heap.update(addressFromVarName,val_eval);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new HeapWritingStmt(this.var_name,this.expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typevar = typeEnv.lookup(var_name);
        Type typexp = this.expression.typecheck(typeEnv);
        if (typevar.equals(new RefType(typexp)))
            return typeEnv;
        else
            throw new MyException("Heap writing: differnt variable's type ");
    }
}

package Model.Statement;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Expression.Exp;
import Model.Type.BoolType;
import Model.Type.Type;
import Model.Value.BoolValue;
import Model.Value.StringValue;
import Model.Value.Value;

import java.io.BufferedReader;

public class WhileStmt implements IStmt
{
   private Exp expression;
   private IStmt statement;

    public WhileStmt(Exp expression, IStmt statement)
    {
        this.expression = expression;
        this.statement = statement;
    }

    @Override
    public String toString() {
        return "WhileStmt{" +
                "expression=" + expression +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {

        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IFileTable<StringValue, BufferedReader> fileTbl=state.getFileTable();
        IHeap<Integer,Value>heap=state.getHeap();

        Value val_eval=this.expression.eval(symTbl,heap);

        if(val_eval instanceof BoolValue)
        {
            BoolValue bool_from_eval=(BoolValue)val_eval;
            if(bool_from_eval.getVal())
            {
                stk.push(new WhileStmt(this.expression,this.statement));
                stk.push(this.statement);
            }
        }
        else
            throw new MyException("Exp in while not boolean");
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new WhileStmt(this.expression.deepCopy(),this.statement.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typexp=this.expression.typecheck(typeEnv);
        if(typexp.equals(new BoolType()))
        {
            MyIDictionary<String, Type> typeEnv1=statement.typecheck(typeEnv);
            return typeEnv;
        }
        else
            throw new MyException("While: exp can't be avaluated to boolean");
    }
}

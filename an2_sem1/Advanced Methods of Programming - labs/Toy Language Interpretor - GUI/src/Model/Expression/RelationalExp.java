package Model.Expression;

import Model.ADT_utils.IHeap;
import Model.ADT_utils.MyIDictionary;
import Model.Exceptions.MyException;
import Model.Type.BoolType;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Value.BoolValue;
import Model.Value.IntValue;
import Model.Value.Value;

public class RelationalExp implements Exp
{
    private Exp exp1;
    private Exp exp2;
    private int operand; // 1-< , 2-<=, 3-==, 4-!=, 5->, 6->=

    public RelationalExp(Exp exp1, Exp exp2, int operand)
    {
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.operand = operand;
    }

    @Override
    public String toString()
    {
        return "RelationalExp{" +
                "exp1=" + exp1 +
                ", exp2=" + exp2 +
                ", operand=" + operand +
                '}';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap<Integer,Value> heap) throws MyException
    {
        Value v1,v2;
        v1=exp1.eval(tbl,heap);
        if (v1.getType().equals(new IntType()))
        {
            v2 = exp2.eval(tbl,heap);
            if (v2.getType().equals(new IntType()))
            {
                IntValue i1 = (IntValue)v1;
                IntValue i2 = (IntValue)v2;
                int n1,n2;
                n1= ((IntValue) v1).getVal();
                n2 = ((IntValue) v2).getVal();
                if (operand==1)
                    return new BoolValue(n1<n2);
                if (operand ==2)
                    return new BoolValue(n1<=n2);
                if(operand==3)
                    return new BoolValue(n1==n2);
                if(operand==4)
                    return new BoolValue(n1!=n2);
                if(operand==5)
                    return new BoolValue(n1>n2);
                if(operand==6)
                    return new BoolValue(n1>=n2);
            }
            else
                throw new MyException("second operand is not an integer");
        }
        else
            throw new MyException("first operand is not an integer");

        return null;
    }

    @Override
    public Exp deepCopy() {
        return new RelationalExp(this.exp1.deepCopy(),this.exp2.deepCopy(),this.operand);
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typ1, typ2;
        typ1=exp1.typecheck(typeEnv);
        typ2=exp2.typecheck(typeEnv);
        if (typ1.equals(new IntType()) )
        {
            if (typ2.equals(new IntType()))
                return new BoolType();

            else
                throw new MyException("second operand is not an integer");
        }
        else
            throw new MyException("first operand is not an integer");
    }
}

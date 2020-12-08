package Model.Expression;
import Model.ADT_utils.IHeap;
import Model.ADT_utils.MyIDictionary;
import Model.Exceptions.MyException;
import Model.Type.*;
import Model.Value.*;

public class LogicExp implements Exp
{
    private Exp e1;
    private Exp e2;
    private int operand; // 1- and ; 2 - or

    public LogicExp(Exp e1, Exp e2, int operand)
    {
        this.e1 = e1;
        this.e2 = e2;
        this.operand = operand;
    }

    @Override
    public String toString()
    {
        return "LogicExp{" +
                "e1=" + e1 +
                ", e2=" + e2 +
                ", operand=" + operand +
                '}';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap<Integer,Value> heap) throws MyException
    {
        Value v1,v2;
        v1= e1.eval(tbl,heap);
        if (v1.getType().equals(new BoolType()))
        {
            v2 = e2.eval(tbl,heap);
            if (v2.getType().equals(new BoolType()))
            {
                BoolValue i1 = (BoolValue)v1;
                BoolValue i2 = (BoolValue)v2;
                boolean b1,b2;
                b1= ((BoolValue) v1).getVal();
                b2 = ((BoolValue) v2).getVal();
                if (operand==1)
                    return new BoolValue(b1&&b2);
                if (operand ==2)
                    return new BoolValue(b1||b2);
            }
            else
                throw new MyException("second operand is not a boolean");
        }
        else
            throw new MyException("first operand is not a boolean");
        return null;

    }

    @Override
    public Exp deepCopy() {
        return new LogicExp(this.e1.deepCopy(),this.e2.deepCopy(),this.operand);
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typ1, typ2;
        typ1=e1.typecheck(typeEnv);
        typ2=e2.typecheck(typeEnv);
        if (typ1.equals(new BoolType()) )
        {
            if (typ2.equals(new BoolType()))
                return new BoolType();

            else
                throw new MyException("second operand is not a boolean");
        }
        else
            throw new MyException("first operand is not a boolean");
    }
}

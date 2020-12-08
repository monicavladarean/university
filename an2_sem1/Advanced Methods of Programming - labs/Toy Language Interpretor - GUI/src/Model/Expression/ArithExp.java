package Model.Expression;
import Model.ADT_utils.IHeap;
import Model.ADT_utils.MyIDictionary;
import Model.Exceptions.MyException;
import Model.Value.*;
import Model.Type.*;

public class ArithExp implements Exp
{
    private Exp e1;
    private Exp e2;
    private int operand; //1-plus, 2-minus, 3-star, 4-divide

    public ArithExp(int operand,Exp e1, Exp e2)
    {
        this.e1 = e1;
        this.e2 = e2;
        this.operand = operand;
    }

    @Override
    public String toString() {
        return "ArithExp{" +
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
        if (v1.getType().equals(new IntType()))
        {
            v2 = e2.eval(tbl,heap);
            if (v2.getType().equals(new IntType()))
            {
                IntValue i1 = (IntValue)v1;
                IntValue i2 = (IntValue)v2;
                int n1,n2;
                n1= ((IntValue) v1).getVal();
                n2 = ((IntValue) v2).getVal();
                if (operand==1)
                    return new IntValue(n1+n2);
                if (operand ==2)
                    return new IntValue(n1-n2);
                if(operand==3)
                    return new IntValue(n1*n2);
                if(operand==4)
                    if(n2==0)
                        throw new MyException("division by zero");
                    else return new IntValue(n1/n2);
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
        return new ArithExp(this.operand,this.e1.deepCopy(),this.e2.deepCopy());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typ1, typ2;
        typ1=e1.typecheck(typeEnv);
        typ2=e2.typecheck(typeEnv);
        if (typ1.equals(new IntType()) )
        {
            if (typ2.equals(new IntType()))
                return new IntType();

            else
                throw new MyException("second operand is not an integer");
        }
        else
            throw new MyException("first operand is not an integer");
    }
}

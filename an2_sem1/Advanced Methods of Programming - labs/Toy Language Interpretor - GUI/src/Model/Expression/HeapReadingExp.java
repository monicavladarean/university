package Model.Expression;

import Model.ADT_utils.IHeap;
import Model.ADT_utils.MyIDictionary;
import Model.Exceptions.MyException;
import Model.Type.RefType;
import Model.Type.Type;
import Model.Value.RefValue;
import Model.Value.Value;

import java.sql.Ref;

public class HeapReadingExp implements Exp {
    Exp expression;

    public HeapReadingExp(Exp expression) {
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "HeapReadingExp{" +
                "expression=" + expression +
                '}';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap<Integer, Value> heap) throws MyException {
        Value val=expression.eval(tbl,heap);
        if(!(val instanceof RefValue))
            throw new MyException("Expression is not e RefValue");
        RefValue refValue=(RefValue) val;
        int address=refValue.getAddress();
        if(!(heap.isDefined(address)))
            throw new MyException("No such address in heapTable!");
        Value valFromAddress=heap.getContent(address);
        return valFromAddress;
    }

    @Override
    public Exp deepCopy() {
        return new HeapReadingExp(this.expression.deepCopy());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typ=expression.typecheck(typeEnv);
        if (typ instanceof RefType)
        {
            RefType reft =(RefType) typ;
            return reft.getInner();
        }
        else
            throw new MyException("the rH argument is not a Ref Type");
    }
}

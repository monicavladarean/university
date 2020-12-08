package Model.Statement;
import Model.Expression.*;
import Model.Exceptions.*;
import Model.ADT_utils.*;
import Model.Value.*;
import Model.Type.*;

public class IfStmt implements IStmt
{
    private Exp exp;
    private IStmt thenS;
    private IStmt elseS;

    @Override
    public String toString()
    {
        return "IfStmt{" +
                "exp=" + exp +
                ", thenS=" + thenS +
                ", elseS=" + elseS +
                '}';
    }

    public IfStmt(Exp exp, IStmt thenS, IStmt elseS)
    {
        this.exp = exp;
        this.thenS = thenS;
        this.elseS = elseS;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIList<Value> out=state.getOut();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IHeap<Integer,Value>heap=state.getHeap();
        Value condition=this.exp.eval(symTbl,heap);

        if ((condition.equals(new BoolType())))
            throw new MyException("conditional expr is not a boolean");
        else
        {
            if(((BoolValue)condition).getVal())
                stk.push(this.thenS);
            else
                stk.push(this.elseS);
        }

        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new IfStmt(this.exp.deepCopy(),this.thenS.deepCopy(),this.elseS.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typexp=exp.typecheck(typeEnv);
        if (typexp.equals(new BoolType()))
        {
            MyIDictionary<String,Type> thenEnv, elseEnv;
            thenEnv = thenS.typecheck(typeEnv);
            elseEnv = elseS.typecheck(typeEnv);
            return typeEnv;
        }
        else
            throw new MyException("The condition of IF has not the type bool");
    }
}

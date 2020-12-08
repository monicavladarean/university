package Model.Statement;
import Model.Expression.*;
import Model.Exceptions.*;
import Model.ADT_utils.*;
import Model.Value.*;
import Model.Type.*;


public class AssignStmt implements IStmt
{
    private String id;
    private Exp exp;

    public AssignStmt(String id, Exp exp)
    {
        this.id = id;
        this.exp = exp;
    }

    @Override
    public String toString()
    {
        return "AssignStmt{" +
                "id='" + id + '\'' +
                ", exp=" + exp +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        IHeap<Integer,Value>heap=state.getHeap();
        Value val = exp.eval(symTbl,heap);
        if (symTbl.isDefined(id))
        {
            Type typId = (symTbl.getValue(id)).getType();
            if (val.getType().equals(typId))
                symTbl.update(id, val);
            else
                throw new MyException("declared type of variable" + id + " and type of the assigned expression do not match");
        }
        else
            throw new MyException("the used variable" +id + " was not declared before");
        return null;

    }

    @Override
    public IStmt deepCopy()
    {
        return new AssignStmt(this.id,this.exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        Type typevar = typeEnv.lookup(id);
        Type typexp = exp.typecheck(typeEnv);
        if (typevar.equals(typexp))
            return typeEnv;
        else
            throw new MyException("Assignment: right hand side and left hand side have different types ");
    }
}
package Model.Statement;
import Model.Expression.*;
import Model.Exceptions.*;
import Model.ADT_utils.*;
import Model.Value.*;
import Model.Type.*;

import java.util.Map;

public class VarDeclStmt implements IStmt
{
    private String name;
    private Type typ;

    public VarDeclStmt(String name, Type typ)
    {
        this.name = name;
        this.typ = typ;
    }

    @Override
    public String toString()
    {
        return "VarDeclStmt{" +
                "name='" + name + '\'' +
                ", typ=" + typ +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException
    {
        MyIStack<IStmt> stk=state.getExeStack();
        MyIDictionary<String,Value> symTbl= state.getSymTable();
        if (symTbl.isDefined(this.name)==true)
            throw new MyException ("variable is already declared");
        else
            {
                if(typ.equals(new IntType()))
                    symTbl.put(name,typ.defaultValue());
                else
                    symTbl.put(name,typ.defaultValue());
            }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new VarDeclStmt(this.name,this.typ.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException
    {
        MyIDictionary<String,Type> newEnv=new MyDictionary<>();
        //making a deepCopy for the dictionary
        for(Map.Entry<String,Type> entry:typeEnv.getContent().entrySet())
            newEnv.put(entry.getKey(),entry.getValue().deepCopy());

        newEnv.put(name,typ);
        return newEnv;
    }
}

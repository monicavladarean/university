package Model.Value;

import Model.Type.StringType;
import Model.Type.Type;

public class StringValue implements Value
{
    private String str="";

    public StringValue(String str)
    {
        this.str = str;
    }

    public String getStr()
    {
        return str;
    }

    @Override
    public String toString()
    {
        return "StringValue{" +
                "str='" + str + '\'' +
                '}';
    }

    @Override
    public Type getType()
    {
        return new StringType();
    }

    public boolean equals(Object obj)
    {
        if (obj instanceof StringValue)
            if(((StringValue) obj).getStr()==this.str)
                return true;
            else
                return false;
        else
            return false;

    }

    @Override
    public Value deepCopy() {
        return new StringValue(this.str);
    }
}

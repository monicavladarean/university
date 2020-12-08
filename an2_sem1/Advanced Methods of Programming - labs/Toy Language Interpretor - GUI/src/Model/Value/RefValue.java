package Model.Value;

import Model.Type.RefType;
import Model.Type.Type;

public class RefValue implements Value {
    int address;
    Type locationType;

    @Override
    public String toString()
    {
        return "RefValue{" +
                "address=" + address +
                ", locationType=" + locationType +
                '}';
    }

    public int getAddress()
    {
        return address;
    }

    public Type getLocationType()
    {
        return locationType;
    }

    public RefValue(int address, Type locationType)
    {
        this.address = address;
        this.locationType = locationType;
    }

    @Override
    public Type getType()
    {
        return new RefType(locationType);
    }

    @Override
    public boolean equals(Object obj)
    {
        if (obj instanceof RefValue)
            if(((RefValue) obj).getAddress()==this.address)
                return true;
            else
                return false;
        else
            return false;
    }

    public void setAddress(int address) {
        this.address = address;
    }

    public void setLocationType(Type locationType) {
        this.locationType = locationType;
    }

    @Override
    public Value deepCopy() {
        return new RefValue(this.address,this.locationType.deepCopy());
    }
}

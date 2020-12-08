package Model.Value;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class IntValueTest {

    @Test
    void getVal()
    {
        IntValue val=new IntValue(5);
        assertEquals(5, val.getVal());
    }

}
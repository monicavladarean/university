package Repository;
import Model.ADT_utils.*;
import Model.Exceptions.*;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public interface IRepository
{
    public void addPrgState(PrgState prg);
    public void logPrgStateExec(PrgState PrgState2) throws IOException;
    public List<PrgState> getPrgList();
    public void setPrgList(List<PrgState> PrgState2);
}

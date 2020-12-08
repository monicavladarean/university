package View;

import Controller.Controller;
import Model.Exceptions.MyException;

public class RunExampleCommand extends Command
{
    private Controller ctr;
    public RunExampleCommand(String key, String desc,Controller ctr)
    {
        super(key, desc);
        this.ctr=ctr;
    }
    @Override
    public void execute()
    {
        try
        {
            ctr.allStep();
        }
        catch (MyException e)
        {
            System.out.println(e.getMessage());
        }
    }
}

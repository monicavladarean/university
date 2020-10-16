package View;

import Controller.Service;
import Model.Exceptions.MyException;

public class RunExampleCommand extends Command
{
    private Service ctr;
    public RunExampleCommand(String key, String desc, Service ctr)
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

package View;

import Model.ADT_utils.*;
import Model.Statement.*;
import Model.Exceptions.MyException;
import Model.Statement.IStmt;
import Model.Value.*;
import Controller.*;
import Repository.Repository;
import Model.Expression.*;
import Model.Type.*;

import java.io.BufferedReader;
import java.util.Scanner;

public class main
{
    public static void main(String[] args)
    {
        try {
            Scanner input = new Scanner(System.in);
            System.out.println("Log file path: ");
            String path = input.next();

            IStmt ex1 = new CompStmt(new VarDeclStmt("v", new IntType()),
                    new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))),
                            new PrintStmt(new VarExp("v"))));
            MyIDictionary<String, Type> envDict1 = new MyDictionary<>();
            envDict1 = ex1.typecheck(envDict1);
            MyStack<IStmt> stk1 = new MyStack<IStmt>();
            MyList<Value> out1 = new MyList<Value>();
            MyDictionary<String, Value> symTbl1 = new MyDictionary<String, Value>();
            FileTable<StringValue, BufferedReader> fileTbl1 = new FileTable<StringValue, BufferedReader>();
            Heap<Integer, Value> heap1 = new Heap<>();
            PrgState prg1 = new PrgState(stk1, symTbl1, out1, fileTbl1, heap1, ex1);
            Repository repo1 = new Repository(path);
            repo1.addPrgState(prg1);
            Service ctrl1 = new Service(repo1);

            IStmt ex2 = new CompStmt(new VarDeclStmt("a", new IntType()),
                    new CompStmt(new VarDeclStmt("b", new IntType()),
                            new CompStmt(new AssignStmt("a", new ArithExp(1,
                                    new ValueExp(new IntValue(2)), new ArithExp(3,
                                    new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                                    new CompStmt(new AssignStmt("b", new ArithExp(1,
                                            new VarExp("a"), new ValueExp(new IntValue(1)))),
                                            new PrintStmt(new VarExp("b"))))));
            MyIDictionary<String, Type> envDict2 = new MyDictionary<>();
            envDict2 = ex2.typecheck(envDict2);
            MyStack<IStmt> stk2 = new MyStack<IStmt>();
            MyList<Value> out2 = new MyList<Value>();
            MyDictionary<String, Value> symTbl2 = new MyDictionary<String, Value>();
            FileTable<StringValue, BufferedReader> fileTbl2 = new FileTable<StringValue, BufferedReader>();
            Heap<Integer, Value> heap2 = new Heap<>();
            PrgState prg2 = new PrgState(stk2, symTbl2, out2, fileTbl2, heap2, ex2);
            Repository repo2 = new Repository(path);
            repo2.addPrgState(prg2);
            Service ctrl2 = new Service(repo2);

            IStmt ex3 = new CompStmt(new VarDeclStmt("a", new BoolType()),
                    new CompStmt(new VarDeclStmt("v", new IntType()),
                            new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                    new CompStmt(new IfStmt(new VarExp("a"), new AssignStmt("v",
                                            new ValueExp(new IntValue(2))), new AssignStmt("v",
                                            new ValueExp(new IntValue(3)))), new PrintStmt(new VarExp("v"))))));
            ;
            MyIDictionary<String, Type> envDict3 = new MyDictionary<>();
            envDict3 = ex3.typecheck(envDict3);
            MyStack<IStmt> stk3 = new MyStack<IStmt>();
            MyList<Value> out3 = new MyList<Value>();
            MyDictionary<String, Value> symTbl3 = new MyDictionary<String, Value>();
            FileTable<StringValue, BufferedReader> fileTbl3 = new FileTable<StringValue, BufferedReader>();
            Heap<Integer, Value> heap3 = new Heap<>();
            PrgState prg3 = new PrgState(stk3, symTbl3, out3, fileTbl3, heap3, ex3);
            Repository repo3 = new Repository(path);
            repo3.addPrgState(prg3);
            Service ctrl3 = new Service(repo3);

            IStmt ex4 = new CompStmt(new VarDeclStmt("varf", new StringType()),
                    new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("test.txt"))),
                            new CompStmt(new OpenRFileStmt(new VarExp("varf")),
                                    new CompStmt(new VarDeclStmt("varc", new IntType()),
                                            new CompStmt(new readFileStmt(new VarExp("varf"), "varc"),
                                                    new CompStmt(new PrintStmt(new VarExp("varc")), new CompStmt(new readFileStmt(new VarExp("varf"), "varc"),
                                                            new CompStmt(new PrintStmt(new VarExp("varc")), new closeRFileStmt(new VarExp("varf"))))))))));

            MyIDictionary<String, Type> envDict4 = new MyDictionary<>();
            envDict4 = ex4.typecheck(envDict4);
            MyStack<IStmt> stk4 = new MyStack<IStmt>();
            MyList<Value> out4 = new MyList<Value>();
            MyDictionary<String, Value> symTbl4 = new MyDictionary<String, Value>();
            FileTable<StringValue, BufferedReader> fileTbl4 = new FileTable<StringValue, BufferedReader>();
            Heap<Integer, Value> heap4 = new Heap<>();
            PrgState prg4 = new PrgState(stk4, symTbl4, out4, fileTbl4, heap4, ex4);
            Repository repo4 = new Repository(path);
            repo4.addPrgState(prg4);
            Service ctrl4 = new Service(repo4);

            IStmt ex5 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                    new CompStmt(new HeapAllocationStmt("v", new ValueExp(new IntValue(20))),
                            new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                    new CompStmt(new HeapAllocationStmt("a", new VarExp("v")),
                                            new CompStmt(new HeapAllocationStmt("v", new ValueExp(new IntValue(30))),
                                                    new PrintStmt(new HeapReadingExp(new HeapReadingExp((new VarExp("a"))))))))));

            MyIDictionary<String, Type> envDict5 = new MyDictionary<>();
            envDict5 = ex5.typecheck(envDict5);
            MyStack<IStmt> stk5 = new MyStack<IStmt>();
            MyList<Value> out5 = new MyList<Value>();
            MyDictionary<String, Value> symTbl5 = new MyDictionary<String, Value>();
            FileTable<StringValue, BufferedReader> fileTbl5 = new FileTable<StringValue, BufferedReader>();
            Heap<Integer, Value> heap5 = new Heap<>();
            PrgState prg5 = new PrgState(stk5, symTbl5, out5, fileTbl5, heap5, ex5);
            Repository repo5 = new Repository(path);
            repo5.addPrgState(prg5);
            Service ctrl5 = new Service(repo5);

            IStmt ex6 = new CompStmt(new VarDeclStmt("v", new IntType()),
                    new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(4))),
                            new CompStmt(new WhileStmt(new RelationalExp(new VarExp("v"),
                                    new ValueExp(new IntValue(0)), 6),
                                    new CompStmt(new PrintStmt(new VarExp("v")),
                                            new AssignStmt("v", new ArithExp(2, new VarExp("v"),
                                                    new ValueExp(new IntValue(1)))))),
                                    new PrintStmt(new VarExp("v")))));

            MyIDictionary<String, Type> envDict6 = new MyDictionary<>();
            envDict6 = ex6.typecheck(envDict6);
            MyStack<IStmt> stk6 = new MyStack<IStmt>();
            MyList<Value> out6 = new MyList<Value>();
            MyDictionary<String, Value> symTbl6 = new MyDictionary<String, Value>();
            FileTable<StringValue, BufferedReader> fileTbl6 = new FileTable<StringValue, BufferedReader>();
            Heap<Integer, Value> heap6 = new Heap<>();
            PrgState prg6 = new PrgState(stk6, symTbl6, out6, fileTbl6, heap6, ex6);
            Repository repo6 = new Repository(path);
            repo6.addPrgState(prg6);
            Service ctrl6 = new Service(repo6);

            IStmt ex7 = new CompStmt(new VarDeclStmt("v", new IntType()),
                    new CompStmt(new VarDeclStmt("a", new RefType(new IntType())),
                            new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(10))),
                                    new CompStmt(new HeapAllocationStmt("a", new ValueExp(new IntValue(22))),
                                            new CompStmt(new ForkStmt(new CompStmt(
                                                    new HeapWritingStmt("a", new ValueExp(new IntValue(30))),
                                                    new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(32))),
                                                            new CompStmt(new PrintStmt(new VarExp("v")),
                                                                    new PrintStmt(new HeapReadingExp(new VarExp("a"))))))),
                                                    new CompStmt(new PrintStmt(new VarExp("v")),
                                                            new PrintStmt(new HeapReadingExp(new VarExp("a")))))))));

            MyIDictionary<String, Type> envDict7 = new MyDictionary<>();
            envDict7 = ex7.typecheck(envDict7);
            MyStack<IStmt> stk7 = new MyStack<IStmt>();
            MyList<Value> out7 = new MyList<Value>();
            MyDictionary<String, Value> symTbl7 = new MyDictionary<String, Value>();
            FileTable<StringValue, BufferedReader> fileTbl7 = new FileTable<StringValue, BufferedReader>();
            Heap<Integer, Value> heap7 = new Heap<>();
            PrgState prg7 = new PrgState(stk7, symTbl7, out7, fileTbl7, heap7, ex7);
            Repository repo7 = new Repository(path);
            repo7.addPrgState(prg7);
            Service ctrl7 = new Service(repo7);

            TextMenu menu = new TextMenu();
            menu.addCommand(new ExitCommand("0", "exit"));
            menu.addCommand(new RunExampleCommand("1", ex1.toString(), ctrl1));
            menu.addCommand(new RunExampleCommand("2", ex2.toString(), ctrl2));
            menu.addCommand(new RunExampleCommand("3", ex3.toString(), ctrl3));
            menu.addCommand(new RunExampleCommand("4", ex4.toString(), ctrl4));
            menu.addCommand(new RunExampleCommand("5", ex5.toString(), ctrl5));
            menu.addCommand(new RunExampleCommand("6", ex6.toString(), ctrl6));
            menu.addCommand(new RunExampleCommand("7", ex7.toString(), ctrl7));
            menu.show();
        }
        catch (MyException e)
        {
            System.out.println(e.getMessage());
        }
        }
}

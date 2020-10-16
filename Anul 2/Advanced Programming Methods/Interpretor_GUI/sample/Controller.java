package sample;

import Model.ADT_utils.*;
import Model.Exceptions.MyException;
import Model.Expression.*;
import Model.Statement.*;
import Model.Type.*;
import Model.Value.BoolValue;
import Model.Value.IntValue;
import Model.Value.StringValue;
import Model.Value.Value;
import Repository.Repository;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ListView;
import javafx.scene.input.MouseEvent;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.stream.Collectors;
import Controller.Service;
import javafx.stage.Modality;
import javafx.stage.Stage;

public class Controller {
    private ArrayList<IStmt> programList=null;
    private Integer idx=null;

    @FXML
    private ListView<String> programsList;

    @FXML
    public void initialize()
    {
        this.createProgramsList();
        this.populateProgramsList();
    }

    @FXML
    public void selectProgramFromListClicked(MouseEvent mouseEvent)
    {
        idx=programsList.getSelectionModel().getSelectedIndex();

    }

    @FXML
    public void selectProgramButtonClicked(MouseEvent mouseEvent) throws MyException, IOException {
        if(idx==null)
        {
            Alert errorBox= new Alert(Alert.AlertType.ERROR);
            errorBox.setHeaderText("EROARE!");
            errorBox.setContentText("Program not selected!");
            errorBox.showAndWait();
            return;
        }
        else
        {
            runProgram(idx);
            idx=null;
        }

    }

    public void createProgramsList()
    {
        programList=new ArrayList<IStmt>();
        IStmt ex1 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))),
                        new PrintStmt(new VarExp("v"))));
        programList.add(ex1);

        IStmt ex2 = new CompStmt(new VarDeclStmt("a", new IntType()),
                new CompStmt(new VarDeclStmt("b", new IntType()),
                        new CompStmt(new AssignStmt("a", new ArithExp(1,
                                new ValueExp(new IntValue(2)), new ArithExp(3,
                                new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                                new CompStmt(new AssignStmt("b", new ArithExp(1,
                                        new VarExp("a"), new ValueExp(new IntValue(1)))),
                                        new PrintStmt(new VarExp("b"))))));
        programList.add(ex2);

        IStmt ex3 = new CompStmt(new VarDeclStmt("a", new BoolType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                        new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                new CompStmt(new IfStmt(new VarExp("a"), new AssignStmt("v",
                                        new ValueExp(new IntValue(2))), new AssignStmt("v",
                                        new ValueExp(new IntValue(3)))), new PrintStmt(new VarExp("v"))))));
        programList.add(ex3);

        IStmt ex4 = new CompStmt(new VarDeclStmt("varf", new StringType()),
                new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("test.txt"))),
                        new CompStmt(new OpenRFileStmt(new VarExp("varf")),
                                new CompStmt(new VarDeclStmt("varc", new IntType()),
                                        new CompStmt(new readFileStmt(new VarExp("varf"), "varc"),
                                                new CompStmt(new PrintStmt(new VarExp("varc")), new CompStmt(new readFileStmt(new VarExp("varf"), "varc"),
                                                        new CompStmt(new PrintStmt(new VarExp("varc")), new closeRFileStmt(new VarExp("varf"))))))))));
        programList.add(ex4);

        IStmt ex5 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new HeapAllocationStmt("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new HeapAllocationStmt("a", new VarExp("v")),
                                        new CompStmt(new HeapAllocationStmt("v", new ValueExp(new IntValue(30))),
                                                new PrintStmt(new HeapReadingExp(new HeapReadingExp((new VarExp("a"))))))))));
        programList.add(ex5);

        IStmt ex6 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new RelationalExp(new VarExp("v"),
                                new ValueExp(new IntValue(0)), 6),
                                new CompStmt(new PrintStmt(new VarExp("v")),
                                        new AssignStmt("v", new ArithExp(2, new VarExp("v"),
                                                new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));
        programList.add(ex6);

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
        programList.add(ex7);
    }

    @FXML
    public void populateProgramsList()
    {
        ObservableList<String> programs= FXCollections.observableArrayList();
        programs.addAll(programList.stream().map(Object::toString).collect(Collectors.toList()));
        programsList.setItems(programs);
    }



    public void runProgram(Integer indx) throws MyException, IOException {
        IStmt program=programList.get(indx);
        MyIDictionary<String, Type> envDict = new MyDictionary<>();
        envDict = program.typecheck(envDict);
        MyStack<IStmt> stk = new MyStack<IStmt>();
        MyList<Value> out = new MyList<Value>();
        MyDictionary<String, Value> symTbl = new MyDictionary<String, Value>();
        FileTable<StringValue, BufferedReader> fileTbl = new FileTable<StringValue, BufferedReader>();
        Heap<Integer, Value> heap = new Heap<>();
        PrgState prg = new PrgState(stk, symTbl, out, fileTbl, heap, program);
        Repository repo = new Repository("log"+indx+".txt");
        repo.addPrgState(prg);
        Service ctrl = new Service(repo);

        Stage secondaryStage=new Stage();
        FXMLLoader loader2=new FXMLLoader(getClass().getResource("sample2.fxml"));
        Parent root = loader2.load();
        Controller2 controller2=loader2.getController();
        controller2.setCtrl(ctrl);
        secondaryStage.setTitle("Program");
        secondaryStage.setScene(new Scene(root, 500, 475));
        secondaryStage.initModality(Modality.APPLICATION_MODAL);
        secondaryStage.showAndWait();
    }
}

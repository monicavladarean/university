package sample;

import Model.ADT_utils.Heap;
import Model.ADT_utils.PrgState;
import Model.Exceptions.MyException;
import Model.Statement.IStmt;
import Model.Value.Value;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.ListView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import Controller.Service;
import javafx.util.Pair;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Controller2 {
    private Service service_ctrl;
    private Integer currentprogram;

    @FXML
    private ListView<String> threadsListListView;

    @FXML
    private TableView<Pair<String,Value>> symTableTableView;

    @FXML
    private TableColumn<Pair<String,Value>, String> symTableVariableNameCollumn;

    @FXML
    private TableColumn<Pair<String,Value>, Value> symTableValueCollumn;

    @FXML
    private TableView<Pair<Integer,Value>> heapTableTableView;

    @FXML
    private TableColumn<Pair<Integer,Value>, Value> heapVallueCollumn;

    @FXML
    private TableColumn<Pair<Integer,Value>, Integer> heapAddressCollumn;

    @FXML
    private ListView<String> outListView;

    @FXML
    private ListView<String> stackListView;

    @FXML
    private ListView<String> fileTableListView;

    @FXML
    TextField nrOfProgramStatesTextField;

    public void setCtrl(Service ctrl)
    {
        this.service_ctrl = ctrl;
        populateThreadLists();
        nrOfProgramStatesTextField.setText(String.valueOf(service_ctrl.getPrgStatesList().size()));
    }

    @FXML
    public void initialize()
    {
        nrOfProgramStatesTextField.setEditable(false);

        heapAddressCollumn.setCellValueFactory(p->new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        heapVallueCollumn.setCellValueFactory(p -> new SimpleObjectProperty<Value>(p.getValue().getValue()));

        symTableVariableNameCollumn.setCellValueFactory(p->new SimpleStringProperty(p.getValue().getKey()));
        symTableValueCollumn.setCellValueFactory(p -> new SimpleObjectProperty<Value>(p.getValue().getValue()));
        //heapAddressCollumn.setCellValueFactory(new PropertyValueFactory<Pair<Integer,Value>, Integer>("Integer"));
        //heapVallueCollumn.setCellValueFactory(new PropertyValueFactory<Pair<Integer,Value>, Value>("Value"));
    }

    public void oneStepButtonClicked(MouseEvent mouseEvent) throws MyException {
        this.service_ctrl.allStep();

        populateAll();
    }

    public void threadsListClicked(MouseEvent mouseEvent)
    {
        currentprogram=threadsListListView.getSelectionModel().getSelectedIndex();

    }

    @FXML
    public void populateThreadLists()
    {
        List<PrgState> prgstatesList = service_ctrl.getPrgStatesList();
        ObservableList<String> programs= FXCollections.observableArrayList();

        for(int i=0;i<prgstatesList.size();i++)
        {
            if(service_ctrl.getPrgStatesList().get(i).getExeStack().isEmpty()==false)
                programs.add(prgstatesList.get(i).getOriginalProgram().toString());
        }
        nrOfProgramStatesTextField.setText(String.valueOf(programs.size()));
        threadsListListView.setItems(programs);

    }

    @FXML
    public void populateOut()
    {
        PrgState prg=service_ctrl.getPrgStatesList().get(currentprogram);
        ObservableList<String> program= FXCollections.observableArrayList();
        program.add(prg.getOut().toString());
        outListView.setItems(program);
    }

    @FXML
    public void populateStack()
    {
        PrgState prg=service_ctrl.getPrgStatesList().get(currentprogram);
        ObservableList<String> program= FXCollections.observableArrayList();
        program.add(prg.getExeStack().toString());
        stackListView.setItems(program);
    }

    @FXML
    public void populateFileTable()
    {
        PrgState prg=service_ctrl.getPrgStatesList().get(currentprogram);
        ObservableList<String> program= FXCollections.observableArrayList();
        program.add(prg.getFileTable().toString());
        fileTableListView.setItems(program);
    }

    @FXML
    public void populateHeap()
    {
        PrgState prg=service_ctrl.getPrgStatesList().get(currentprogram);
    ObservableList<Pair<Integer,Value>> progs= FXCollections.observableArrayList();
        for(Map.Entry<Integer,Value> entry:prg.getHeap().getContent().entrySet())
    {
        progs.add(new Pair<Integer, Value>(entry.getKey(),entry.getValue()));
    }
        heapTableTableView.setItems(progs);
}

    @FXML
    public void populateSymTable()
    {
        PrgState prg=service_ctrl.getPrgStatesList().get(currentprogram);
        ObservableList<Pair<String,Value>> progs= FXCollections.observableArrayList();
        for(Map.Entry<String,Value> entry:prg.getSymTable().getContent().entrySet())
        {
            progs.add(new Pair<String, Value>(entry.getKey(),entry.getValue()));
        }
        symTableTableView.setItems(progs);
    }

    @FXML
    public void populateAll()

    {
        populateThreadLists();
        //nrOfProgramStatesTextField.setText(String.valueOf(service_ctrl.getPrgStatesList().size()));
        populateOut();
        populateStack();
        populateHeap();
        populateSymTable();
        populateFileTable();
    }

}

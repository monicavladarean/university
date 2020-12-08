package domain;

import model.Board;
import model.User;

import java.sql.*;

public class DBManager
{
    Connection connection;

    public DBManager() {
        this.connection = connect();
    }

    public Connection connect()
    {
        try
        {
            Class.forName( "org.postgresql.Driver");
            Connection connection = DriverManager.getConnection( "jdbc:postgresql://localhost:5432/snake", "postgres", "admin" );
            return connection;
        }
        catch (SQLException | ClassNotFoundException e)
        {
            System.out.println("DB connection error!");
            return null;
        }
    }

    public User authenticate(String username, String password)
    {
        ResultSet resultSet;
        User user=null;

        try
        {
            String sql = "select * from users where username=? and password=?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1,username);
            preparedStatement.setString(2,password);
            resultSet=preparedStatement.executeQuery();

            if (resultSet.next())
            {
                user = new User(resultSet.getInt("id"),resultSet.getString("username"),resultSet.getString("password"));
            }
            resultSet.close();
        }
        catch (SQLException e)
        {
            e.printStackTrace();
        }
        return user;
    }

    public void addHistory(Board board, String move,User user)
    {
        String moveStr;
        switch (move) {
            case "-1":
                moveStr = "START";
                break;
            case "1":
                moveStr = "UP";
                break;
            case "2":
                moveStr = "LEFT";
                break;
            case "3":
                moveStr = "RIGHT";
                break;
            case "4":
                moveStr = "DOWN";
                break;
            default:
                moveStr = "error";
                break;
        }
        String sql = "INSERT INTO gamehistory(information ,boardwidth,boardheight,foodx,foody,move,username) VALUES (?,?,?,?,?,?,?)";
        try
        {
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1,board.getSerializedBoard());
            preparedStatement.setInt(2,board.getX());
            preparedStatement.setInt(3,board.getY());
            preparedStatement.setInt(4,board.getFoodX());
            preparedStatement.setInt(5,board.getFoodY());
            preparedStatement.setString(6,moveStr);
            preparedStatement.setString(7,user.getUsername());
            preparedStatement.execute();
        }
        catch (SQLException e)
        {
            e.printStackTrace();
        }
    }

    public void disconnect()
    {
        try
        {
            connection.close();
        }
        catch (SQLException e)
        {
            System.out.println("DB disconnection error!");
        }
        connection = null;
    }

}

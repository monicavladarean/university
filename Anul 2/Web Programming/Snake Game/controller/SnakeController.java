package controller;

import domain.DBManager;
import model.*;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

public class SnakeController extends HttpServlet
{
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
    {
        RequestDispatcher dispatcher = null;
        HttpSession session = request.getSession();
        if(session.getAttribute("board")!=null) {
            Board board = (Board) session.getAttribute("board");
            Snake snake = (Snake) session.getAttribute("snake");
            String move = request.getParameter("move");
            User user = (User) session.getAttribute("user");
            Direction direction;

            switch (move) {
                case "1":
                    direction = Direction.UP;
                    break;
                case "2":
                    direction = Direction.LEFT;
                    break;
                case "3":
                    direction = Direction.RIGHT;
                    break;
                case "4":
                    direction = Direction.DOWN;
                    break;
                default:
                    direction = Direction.UP;
                    break;
            }
            if (!snake.move(direction, board))
                session.setAttribute("status", "over");

            DBManager dbManager = new DBManager();
            dbManager.addHistory(board,move,user);
            dbManager.disconnect();
        }

        dispatcher = request.getRequestDispatcher("/succes.jsp");
        dispatcher.forward(request, response);
    }

}

package controller;

import domain.DBManager;
import model.User;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

public class LoginController extends HttpServlet
{
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        String username = request.getParameter("username");
        String password = request.getParameter("password");
        RequestDispatcher dispatcher = null;

        DBManager dbManager = new DBManager();
        User user = dbManager.authenticate(username, password);
        if (user != null)
        {
            dispatcher = request.getRequestDispatcher("/succes.jsp");

            HttpSession session = request.getSession();
            session.setAttribute("user", user);

        }
        else {
            dispatcher = request.getRequestDispatcher("/error.jsp");
        }
        dispatcher.forward(request, response);
        dbManager.disconnect();
    }
}

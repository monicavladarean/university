<%@ page import="model.BoardPosition" %>
<%@ page import="model.Board" %>
<%@ page import="model.Snake" %>
<%@ page import="java.util.Date" %>
<%@ page import="java.time.Duration" %>
<%@ page import="java.time.LocalDate" %>
<%@ page import="domain.DBManager" %>
<%@ page import="model.User" %><%--
  Created by IntelliJ IDEA.
  User: Monica
  Date: 5/9/2020
  Time: 12:19 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Snake Game</title>
</head>
<body>
<table border="1">
    <%
        if(session.getAttribute("board")==null)
        {
            if(session.getAttribute("status")!=null)
                session.removeAttribute("status");
            Board tabla = new Board();
            session.setAttribute("board", tabla);
            Snake snake = new Snake();
            session.setAttribute("snake", snake);
            snake.addHead(new BoardPosition(5, 5), tabla);
            User user = (User) session.getAttribute("user");

            DBManager dbManager = new DBManager();
            dbManager.addHistory(tabla,"-1",user);
            dbManager.disconnect();
        }

        Snake snake = (Snake) session.getAttribute("snake");
        Board tabla = (Board) session.getAttribute("board");

        for (int i = 0; i < tabla.x; i++) {
            out.print("<tr>");
            for (int j = 0; j < tabla.y; j++) {
                if (tabla.getPieceType(new BoardPosition(j,i))==1 && !snake.isHead(new BoardPosition(j,i)))
                    out.print("<td style=\"width:40px;height:40px;\" bgcolor=\"green\">");
                if (tabla.getPieceType(new BoardPosition(j,i))==1 && snake.isHead(new BoardPosition(j,i)))
                    out.print("<td style=\"width:40px;height:40px;\" bgcolor=\"black\">");
                if (tabla.getPieceType(new BoardPosition(j,i))==0)
                    out.print("<td style=\"width:40px;height:40px;\" bgcolor=\"white\">");
                if (tabla.getPieceType(new BoardPosition(j,i))==2)
                    out.print("<td style=\"width:40px;height:40px;\" bgcolor=\"yellow\">");
                if (tabla.getPieceType(new BoardPosition(j,i))==-1)
                    out.print("<td style=\"width:40px;height:40px;\" bgcolor=\"red\">");
                out.print("</td>");
            }
            out.println("</tr>");
        }
        if(session.getAttribute("status")!=null)
        {
            long spentSeconds = (new Date().getTime() - tabla.getStartTime().getTime())/1000;

            session.removeAttribute("status");
            session.removeAttribute("board");
            session.removeAttribute("snake");
            out.print("<script>alert(\"Game over in " + spentSeconds + " seconds!\");</script>");
        }
    %>
</table>
</body>
</html>

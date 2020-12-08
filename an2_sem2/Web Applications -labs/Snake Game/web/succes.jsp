<%--
  Created by IntelliJ IDEA.
  User: Monica
  Date: 5/7/2020
  Time: 2:44 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>LogIn</title>
</head>
<body>

<script>


</script>

<div style="color: deeppink">
<%
   model.User user = (model.User) session.getAttribute("user");
    out.println("Welcome to the Snake game, "+user.getUsername()+" !");
%>
<BR>
<form action="LogoutController" method="get">
    <input type="submit" value="Log out"/>
</form>
</div>
<div align="center">
    <jsp:include page="tabla.jsp" flush="false" />
</div>
<br> <br>
<div align="center">
    <table>
        <tr>
            <td> </td>
            <td>
                <form action="SnakeController" method="post">
                    <input type="hidden" name="move" value="1" />
                    <input type="submit" value="▲" />
                </form>
            </td>
            <td> </td>
        </tr>
        <tr>
            <td>
                <form action="SnakeController" method="post">
                    <input type="hidden" name="move" value="2" />
                    <input type="submit" value="◄"/>
                </form>
            </td>
            <td></td>
            <td>
                <form action="SnakeController" method="post">
                    <input type="hidden" name="move" value="3" />
                    <input type="submit" value="►" />
                </form>
            </td>
        </tr>
        <tr>
            <td> </td>
            <td>
                <form action="SnakeController" method="post">
                    <input type="hidden" name="move" value="4" />
                    <input type="submit" value="▼" />
                </form>
            </td>
            <td> </td>
        </tr>
    </table>
</div>
</body>
</html>
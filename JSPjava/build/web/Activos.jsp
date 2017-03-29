<%-- 
    Document   : Activos
    Created on : 16/03/2017, 01:17:06 PM
    Author     : Roberto
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%
   /*if(session.getAttribute("sesionusuario")==null){
        response.sendRedirect("index.jsp");
        }*/
        %>
<html>
    <head>
         <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        


        <title>Página JSP</title>
        <meta name="viewport" content="with=device-width, user-scalable=no,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0">
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="estilos.css">
    </head>
    
    <body class="html">
        <div class="container" >
            
            <div class="panel-body" >
        <form action="cerrar.jsp">
            <p align="right">
                <input type="submit" value="cerrar sesion" class="btn btn-success">
            </p>
        </form>
        </div>
            <div class="panel-body">
        <h1 align="center">Bienvenido al Sistema para Agregar Activos!</h1>
        
        <form action="Servlet3" method="post">
            <table align="center">
                <tr>
                    <td>NOMBRE DEL ACTIVO:</td>
                    <td> <input type="text" name="name" class="form-control"/></td>
                </tr>
                 <tr>
                 
                </tr>
            </table>
            <p align="center">
                <textarea cols="50" rows="5" name="area" class="form-control" placeholder="Descripción...."></textarea><br>
                <input type="submit" value="Agregar" class="btn btn-primary" />
                </p>
        </form>
        </div>
        </div>
        <script src="js/jquery.js"></script>
            <script src="js/bootstrap.min.js"></script>
    </body>
</html>

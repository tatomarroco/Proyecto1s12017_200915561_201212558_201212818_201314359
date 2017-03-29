<%-- 
    Document   : menu
    Created on : 17/03/2017, 11:34:11 PM
    Author     : Roberto
--%>

<%@page import="javafx.scene.input.KeyCode"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%
    if(session.getAttribute("sesionusuario")==null){
        response.sendRedirect("index.jsp");
        }
    
        %>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="with=device-width, user-scalable=no,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0">
        <!-- Latest compiled and minified CSS -->
        <title>JSP Page</title>
         
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="estilos.css">
    </head>
    <body>
        <div class="container">
            <img id="estirada" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%" src="blurry-2.jpg" />
            <div class="row"><br><br>
                <div class="col-md-1">  
                    <img id="profile-img" class="usaclogo" src="usaclogo.png" />
                </div>
                
                <div class="panel panel-default" >
                    <div class="col-md-offset-4">
                    <form action="cerrar.jsp" class="form-horizontal" role="form">
                        <p align="right" height="20">
                            <input type="submit"  name="boton" class="btn btn-success"value="Cerrar Sesion" />
                        </p>
                
                    </form>
                            </div>
                    
                    <div class="form-group" >
                        <h1 >Menú de Opciones!</h1>
                        <h1> Bienvenido al Sistema de Gestion  <br>    <%=request.getSession().getAttribute("sesionusuario")%></h1>
                
                        <p>
                            
                            <a  href="Activos.jsp" class="btn btn-primary btn-lg active btn-block" role="buttoon" >Agregar Activos</a>
                             <a  href="Modificar.jsp" class="btn btn-primary btn-lg active btn-block" role="button">Modificar Activos</a>
                             <a href="Eliminar.jsp" class="btn btn-primary btn-lg active btn-block" role="button">Eliminar Activos</a>
                        </p>
        </div>
                </div>
        </div>
        </div>
             <script src="js/jquery.js"></script>
            <script src="js/bootstrap.min.js"></script>
    </body>
</html>

<%-- 
    Document   : Eliminar
    Created on : 16/03/2017, 01:31:50 PM
    Author     : Roberto
--%>

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
        


        <title>Página JSP</title>
        <meta name="viewport" content="with=device-width, user-scalable=no,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0">
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="estilos.css">
    </head>
    <body class="html">
        <form action="cerrar.jsp">
            <p align="right">
            <input type="submit" value="cerrar sesión" class="btn btn-success"/>
            </p>
        </form>
        
        <h3>Bienvenido al sistema de Eliminar Activos! <br>
            <p>
        <%=session.getAttribute("sesionusuario") %>
                </p>

        </h3>
                <div class="container" cass="row" >
                    <div class="col-md-6">
                    <form action="action" >
                        <div class="panel-body">
                        <div class="form-group">
                            <select name="Events" class="form-control" >
                                <option value="0" selected>(Seleccione el Activo:)</option>
                                <option value="100M Run" >100M Run</option>
                                <option value="200M Run">200M Run</option>
                                <option value="400M Run">400M Run</option>
                                <option value="800M Run">800M Run</option>
                            </select><br><br>
                        </div>
                            <div class="form-group">
                                <label for="nombre" class="col-sm-3 control-label">
                                         Nombre:</label>
                                <input type="text" name="nombre" class="form-control" disabled/><br><br>
                            </div>
                            <div class="form-group">
                                <textarea name="area" cols="50" rows="5" class="form-control" disabled>  </textarea><br><br>
                            </div>
                            <input type="submit" value="Eliminar Activo" class="btn btn-primary"/><br>
                        </div>        
                    </form>
                    </div>
                    </div>
    </body>
</html>

<%-- 
    Document   : servidor
    Created on : 15/03/2017, 11:46:06 AM
    Author     : Roberto
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" import="Objetos.Persona" errorPage=""%>
<%@page import="javax.swing.JButton"%>
<%@page import="javax.swing.JOptionPane"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.DriverManager"%>
<!DOCTYPE html>
<% 
        
    String mensaje=" ";
    if(session.getAttribute("sesionError")!=null){
        
        mensaje=String.valueOf(session.getAttribute("sesionError"));
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
    <body >
        
        <br>
        <br>
        <div class="container">
            <img id="estirada" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%" src="blurry-2.jpg" />
            
            <div class="row">
                <div class="facebook">
 
</div>
                <div class="col-md-1">  
                    <img id="profile-img" class="usaclogo" src="usaclogo.png" />
                </div>
                <div class="col-md-4 col-md-offset-7">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                         <span class="glyphicon glyphicon-lock"></span> Login
                                <div>
                                    <img id="profile-img" class="profile-img-card" src="avatar_2x.png" />
                                </div>
                         </div>
                         <div class="panel-body">
                            <form action="Servlet2" method="post" class="form-horizontal" role="form">
                                
                                <div class="form-group">
                                       <label for="name" class="col-sm-3 control-label">
                                     Nombre:</label>
                                    <div class="col-sm-9">
                                        <input type="text" name="name" id="name" class="form-control" placeholder="Nombre" required/>
                                    </div>
                                </div>
                                <div class="form-group">
                                        <label for="pass" class="col-sm-3 control-label">
                                         Contraseña:</label>
                                    <div class="col-sm-9">
                                        <input type="password" name="pass" class="form-control" placeholder="Contraseña" required/>
                                    </div>
                                 </div>
                                <div class="form-group">     
                                        <label for="empresa" class="col-sm-3 control-label">
                                         Empresa:</label>
                                     <div class="col-sm-9">
                                        <input type="text" name="empresa" class="form-control" placeholder="Empresa" required/>
                                    </div>  
                                </div>
                                <div class="form-group">  
                                    <label for="departamento" class="col-sm-3 control-label">
                                    Departamento:</label>
                                    <div class="col-sm-9">
                                       <input type="text" name="departamento" class="form-control" placeholder="Departamento" required />
                                    </div>
                                </div>
                    <p align="center">
                        <input  class="btn btn-success btn-sm" type="submit" name="login" value="LOGIN"/>   
                    </p>
                    
                        <%=mensaje%><br>

                    </form>
                </div>
                        
                        <div class="panel-footer" style="background-color: black">
                            <h5 class="text-primary">Not Registred?</h5><a href="Servlet1">Register here</a></div>
                    </div>
                </div>  
                        
                        <div class="col-md-5" >

</div>
            </div>
       </div>
            <script src="js/jquery.js"></script>
            <script src="js/bootstrap.min.js"></script>
    </body>
    
</html>

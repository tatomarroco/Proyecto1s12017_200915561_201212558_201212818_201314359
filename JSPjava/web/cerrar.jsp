<%-- 
    Document   : cerrar
    Created on : 18/03/2017, 05:44:34 PM
    Author     : Roberto
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<% 
session.setAttribute("sesionusuario", null);
session.setAttribute("sesionempresa", null);
session.setAttribute("sesiondepartamento", null);
session.invalidate();
response.sendRedirect("index.jsp");
%>

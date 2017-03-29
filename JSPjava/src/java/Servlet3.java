/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//import  Servlet1.webClient;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.LinkedList;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Roberto
 */
@WebServlet(urlPatterns = {"/Servlet3"})
public class Servlet3 extends HttpServlet {
String concatenar="";
    public static OkHttpClient webClient = new OkHttpClient();

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            
            out.println("<html>\n" +
"    <head>\n" +
"         <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n" +
"        \n" +
"\n" +
"\n" +
"        <title>Página JSP</title>\n" +
"        <meta name=\"viewport\" content=\"with=device-width, user-scalable=no,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0\">\n" +
"        <!-- Latest compiled and minified CSS -->\n" +
"        <link rel=\"stylesheet\" href=\"css/bootstrap.min.css\">\n" +
"        <link rel=\"stylesheet\" type=\"text/css\" href=\"estilos.css\">\n" +
"    </head>\n" +
"    \n" +
"    <body class=\"html\">\n" +
"        <div class=\"container\" >\n" +
"            \n" +
"            <div class=\"panel-body\" >\n" +
"        <form action=\"cerrar.jsp\">\n" +
"            <p align=\"right\">\n" +
"                <input type=\"submit\" value=\"cerrar sesion\" class=\"btn btn-success\">\n" +
"            </p>\n" +
"        </form>\n" +
"        </div>\n" +
"            <div class=\"panel-body\">\n" +
"        <h1 align=\"center\">Bienvenido al Sistema para Agregar Activos!"+concatenar+"</h1>\n" +
"        \n" +
"        <form action=\"Servlet3\" method=\"post\">\n" +
"            <table align=\"center\">\n" +
"                <tr>\n" +
"                    <td>NOMBRE DEL ACTIVO:</td>\n" +
"                    <td> <input type=\"text\" name=\"name\" class=\"form-control\"/></td>\n" +
"                </tr>\n" +
"                 <tr>\n" +
"                 \n" +
"                </tr>\n" +
"            </table>\n" +
"            <p align=\"center\">\n" +
"                <textarea cols=\"50\" rows=\"5\" name=\"area\" class=\"form-control\" placeholder=\"Descripción....\"></textarea><br>\n" +
"                <input type=\"submit\" value=\"Agregar\" class=\"btn btn-primary\" />\n" +
"                </p>\n" +
"        </form>\n" +
"        </div>\n" +
"        </div>\n" +
"        <script src=\"js/jquery.js\"></script>\n" +
"            <script src=\"js/bootstrap.min.js\"></script>\n" +
"    </body>\n" +
"</html>\n" +
"");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }
    
    private void response(HttpServletResponse resp, String msg)
        throws IOException {
  
            
            PrintWriter out = resp.getWriter();
            //out.println("<%@page contentType=\"text/html\" pageEncoding=\"UTF-8\" import=\"Objetos.Persona\" errorPage=\"\"%>");
            out.println("<!DOCTYPE html>");
            //out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet Servlet1</title>");            
            out.println("</head>");
            out.println("<body >");
            out.println("<h1 align=\"center\">REGISTRO DE USUARIOS</h1>");
            out.println("<img id=\"estirada\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%\" src=\"blurry-2.jpg\" />");
            out.println(" <form action=\"Servlet1\" method=\"post\" >\n" +
"<table align=\"center\">\n" +
"<tr>\n" +
"<td>Nombre de Usuario:</td>\n" +
"<td><input name=\"usuario\" /></td>\n" +
"</tr>\n" +
"<tr>\n" +
"<td>Contraseña:</td>\n" +
"<td><input name=\"clave\" /></td>\n" +
"</tr>\n" +
"<tr>\n" +
"<td>Nombre Completo:</td>\n" +
"<td><input name=\"completo\" /></td>\n" +
"</tr>\n" +
"<tr>\n" +
"<td>Empresa donde Trabaja:</td>\n" +
"<td><input name=\"empresa\" /></td>\n" +
"</tr>\n" +
"<tr>\n" +
"<td>Departamento en el que Trabaja:</td>\n" +
"<td><input name=\"departamento\" /></td>\n" +  
"</tr>\n" +
"</table>\n" +
"<p align=\"center\">"+
"<input  type=\"submit\" value=\"Registrar Usuario\" />\n" +
"</p>"+
"<a href=\"index.jsp\">Regresar a Login</a>"+
"<p align=\"center\"></p>"+
"</form>");
          out.println("<script src=\"js/jquery.js\"></script>\n" +
"            <script src=\"js/bootstrap.min.js\"></script>");
            out.println("</body>");
            out.println("</html>");
}

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
             LinkedList lin= new LinkedList();
lin.add(0,"a");
lin.add(1,"b");
lin.add(2,"c");
lin.add(3,"d");
lin.add(4,"e");
lin.add(5,"f");
lin.add(6,"g");
lin.add(7,"h");
lin.add(8,"i");
lin.add(9,"j");
lin.add(10,"k");
lin.add(11,"l");
lin.add(12,"m");
lin.add(13,"n");
lin.add(14,"o");
lin.add(15,"p");
lin.add(16,"q");
lin.add(17,"r");
lin.add(18,"s");
lin.add(19,"t");
lin.add(20,"u");
lin.add(21,"v");
lin.add(22,"w");
lin.add(23,"x");
lin.add(24,"y");
lin.add(25,"z");
Random r =new Random();
String alfanumerico="";
String numero="";
String numero2="";
int suma1=0;
int suma2=0;
for(int i=0;i<7;i++){
    
alfanumerico+=lin.get(r.nextInt(lin.size())).toString()+String.valueOf(r.nextInt(9));
}
alfanumerico+=lin.get(r.nextInt(lin.size())).toString();
//System.out.println(concatenar);

char vector[]=alfanumerico.toCharArray();

for(int i=0;i<vector.length;i++){

numero+=String.valueOf(lin.indexOf(String.valueOf(vector[i])));
}


String caracter[]=numero.split("-");

suma1+=Integer.parseInt(caracter[0]+caracter[1]);
suma2+=Integer.parseInt(caracter[2]+caracter[3])+suma1; 
numero2=String.valueOf(suma1);
//System.out.println(suma1);
//System.out.println(alfanumerico);
        
        
        
       String nombreactivo = request.getParameter("name");
        String descripcion=request.getParameter("area");
        String usuario=String.valueOf(request.getSession().getAttribute("sesionusuario"));
        String empresa=String.valueOf(request.getSession().getAttribute("sesionempresa"));
        String departamento=String.valueOf(request.getSession().getAttribute("sesiondepartamento"));
        String pass=String.valueOf(request.getSession().getAttribute("sesionpass"));
         
                   
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            
                            .add("usuario",usuario.trim())
                            .add("empresa",empresa.trim())
                            .add("departamento",departamento.trim())
                            .add("identificador",numero2.trim())
                            .add("contrasenia",pass.trim())
                            .build();
                          
              
               concatenar=getString("agregarAVL", formBody);
        
                           
        
        
        
        //response.sendRedirect("Activos.jsp");
       processRequest(request, response);
       // response(response,con);
    }

     public String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://192.168.43.56:5000/" + metodo);
            Request req = new Request.Builder().url(url).post(formBody).build();
            com.squareup.okhttp.Response resp = webClient.newCall(req).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = resp.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println(ex.getMessage());
        } catch (Exception ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        System.out.println(ex.getMessage());
        }
        return null;
    }
    
    
    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}

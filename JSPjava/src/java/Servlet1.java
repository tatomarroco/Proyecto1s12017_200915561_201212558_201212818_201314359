/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//import static Servlet2.webClient;
import static com.sun.xml.internal.ws.api.message.Packet.Status.Request;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.core.Response;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 *
 * @author Roberto
 */
@WebServlet(urlPatterns = {"/Servlet1"})
public class Servlet1 extends HttpServlet {

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
   String r="";
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            //out.println("<%@page contentType=\"text/html\" pageEncoding=\"UTF-8\" import=\"Objetos.Persona\" errorPage=\"\"%>\n");
            
           
            
            out.println("<!DOCTYPE html>");
            //out.println("<!DOCTYPE html>");
            out.println("<html>\n" +
"    \n" +
"    <head>\n" +
"        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n" +
"        \n" +
"\n" +
"\n" +
"        <title>Página JSP</title>\n" +
"        <meta name=\"viewport\" content=\"with=device-width, user-scalable=no,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0\">\n" +
"        <!-- Latest compiled and minified CSS -->\n" +
"        <link rel=\"stylesheet\" href=\"css/bootstrap.min.css\">\n" +
"        <link rel=\"stylesheet\" type=\"text/css\" href=\"estilos.css\">\n" +
"    </head>\n" +
"    <body >\n" +
"        \n" +
"        <br>\n" +
"        <br>\n" +
"        <div class=\"container\">\n" +
"            <img id=\"estirada\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%\" src=\"blurry-2.jpg\" />\n" +
"            \n" +
"            <div class=\"row\">\n" +
"                <div class=\"col-md-1\">  \n" +
"                    <img id=\"profile-img\" class=\"usaclogo\" src=\"usaclogo.png\" />\n" +
"                </div>\n" +
"                <div class=\"col-md-10\">\n" +
"                    <div class=\"panel panel-default\">\n" +
"                        <div class=\"panel-heading\">\n" +
"                           REGISTRO DE USUARIOS" +                 
"                         </div>\n" +
"                         <div class=\"panel-body\">\n" +
"                            <form action=\"Servlet1\" method=\"post\" class=\"form-horizontal\" role=\"form\">\n" +
"                                \n" +
"                                <div class=\"form-group\">\n" +
"                                       <label for=\"name\" class=\"col-sm-3 control-label\">\n" +
"                                     Nombre:</label>\n" +
"                                    <div class=\"col-sm-9\">\n" +
"                                        <input type=\"text\" name=\"usuario\" id=\"name\" class=\"form-control\" placeholder=\"Nombre\" required/>\n" +
"                                    </div>\n" +
"                                </div>\n" +
"                                <div class=\"form-group\">\n" +
"                                        <label for=\"pass\" class=\"col-sm-3 control-label\">\n" +
"                                         Contraseña:</label>\n" +
"                                    <div class=\"col-sm-9\">\n" +
"                                        <input type=\"password\" name=\"clave\" class=\"form-control\" placeholder=\"Contraseña\" required/>\n" +
"                                    </div>\n" +
"                                 </div>\n" +
"                    <div class=\"form-group\">\n" +
"                                       <label for=\"completo\" class=\"col-sm-3 control-label\">\n" +
"                                     Nombre Completo:</label>\n" +
"                                    <div class=\"col-sm-9\">\n" +
"                                        <input type=\"text\" name=\"completo\" id=\"name\" class=\"form-control\" placeholder=\"Nombre Completo\" required/>\n" +
"                                    </div>\n" +
"                                </div>\n" +
"                                <div class=\"form-group\">     \n" +
"                                        <label for=\"empresa\" class=\"col-sm-3 control-label\">\n" +
"                                         Empresa:</label>\n" +
"                                     <div class=\"col-sm-9\">\n" +
"                                        <input type=\"text\" name=\"empresa\" class=\"form-control\" placeholder=\"Empresa\" required/>\n" +
"                                    </div>  \n" +
"                                </div>\n" +
"                                <div class=\"form-group\">  \n" +
"                                    <label for=\"departamento\" class=\"col-sm-3 control-label\">\n" +
"                                    Departamento:</label>\n" +
"                                    <div class=\"col-sm-9\">\n" +
"                                       <input type=\"text\" name=\"departamento\" class=\"form-control\" placeholder=\"Departamento\" required />\n" +
"                                    </div>\n" +
"                                </div>\n" +
"                    <p align=\"center\">\n" +
"                        <input  class=\"btn btn-primary\" type=\"submit\" name=\"login\" value=\"Registrar\"/>   \n" +
"                    </p>\n" +
"                    \n" +
"                     " +r+
"\n" +
"                    </form>\n" +
"                    <div class=\"panel-footer\" style=\"background-color: black,color: white\">\n" +
"                    Necesita Regesar al Login? <a href=\"index.jsp\">Login here</a></div>\n" +
"                    </div>"+
"                </div>\n" +
"                </div>       \n" +
"            </div>\n" +
"       </div>\n" +
"            <script src=\"js/jquery.js\"></script>\n" +
"            <script src=\"js/bootstrap.min.js\"></script>\n" +
"    </body>\n" +
"    \n" +
"</html>");
    }
        r="";
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
            r="";
            
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
"<p align=\"center\">"+msg+"</p>"+
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
    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
         
        String usuario = request.getParameter("usuario"); 
        String pass = request.getParameter("clave");
        String nombre= request.getParameter("completo");
        String empresa= request.getParameter("empresa");
        String departamento=request.getParameter("departamento");
        
                    
   
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("usuario",usuario)
                            .add("contrasenia", pass)
                            .add("nombre",nombre)
                            .add("empresa",empresa)
                            .add("departamento",departamento)
                            
                            .build();
              
                    
                    r = getString("matrizAgregar", formBody);
                    //System.out.println(r + "---");


        //sponse(response,r);
        processRequest(request, response);
        
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
  
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}

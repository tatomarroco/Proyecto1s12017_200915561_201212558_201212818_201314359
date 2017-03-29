/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//import static Servlet3.webClient;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashSet;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author Roberto
 */
@WebServlet(urlPatterns = {"/Servlet2"})
public class Servlet2 extends HttpServlet {
public static OkHttpClient webClient = new OkHttpClient();
String r="HOla";
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

           
    if(request.getSession().getAttribute("sesionusuario")==null){
        response.sendRedirect("index.jsp");
        }
    
       
            
            
        }
    }
    
    protected void processRequest1(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>\n" +
"<html>\n" +
"    \n" +
"    <head>\n" +
"        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n" +
"        <title>Página JSP</title>\n" +
"        <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n" +
"    </head>\n" +
"    <body>\n" +
            "<% HttpSession objsesion=request.getSession();\n" +
      "String usuario = request.getParameter(\"name\"); \n"+
"     objsesion.setAttribute(\"sesionusuario\",usuario); %>"+
"        <br>\n" +
"        <br>\n" +
"        <form action=\"Servlet2\" method=\"post\" >\n" +
"        <table ALIGN=\"center\">\n" +
"            <tr>\n" +
"                <td> NOMBRE:</td>\n" +
"                <td> <input type=\"text\" name=\"name\" /></td>\n" +
"            </tr>\n" +
"            <tr>\n" +
"                <td> CONTRASEÑA:</td>\n" +
"                <td> <input type=\"password\" name=\"pass\" /></td>\n" +
"                \n" +
"            </tr>\n" +
"            <tr>\n" +
"                <td> EMPRESA:</td>\n" +
"                <td> <input type=\"text\" name=\"empresa\" /></td>\n" +
"                \n" +
"            </tr>\n" +
"            <tr>\n" +
"                <td>DEPARTAMENTO:</td>\n" +
"                \n" +
"                <td> <input type=\"text\" name=\"departamento\" /></td>\n" +
"                \n" +
"            </tr>\n" +
" \n" +
"        </table>\n" +
"            \n" +
"        <p align=\"center\">\n" +
"            <input type=\"submit\" name=\"login\" value=\"LOGIN\"/>   \n" +
"        </p>\n" +
"        <p align=\"center\">\n" +
"        \n" +
   "<p>Usuario o contrasenia Invalida</p>"+
"            <a href=\"Servlet1\" > Registrar Usuario</a>\n" +
"        \n" +
"        </p>\n" +
"        </form>\n" +
"    </body>\n" +
"    \n" +
"</html>");
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
        String usuario = request.getParameter("name"); 
        String pass = request.getParameter("pass");
        String empresa = request.getParameter("empresa");
        String departamento = request.getParameter("departamento");
                    
       
                   
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("usuario",usuario)
                            .add("contrasenia", pass)                            
                            .add("empresa",empresa)
                            .add("departamento",departamento)
                            //.add("dato3","Roberto")
                            .build();
                            r = getString("Login", formBody);
                            
                    if(r.equalsIgnoreCase("true")){
                       //boolean sesion=true;
                       
                       HttpSession sesion = request.getSession(true);
                       HttpSession sesion1 = request.getSession(true);
                       HttpSession sesion2 = request.getSession(true);
                       HttpSession sesion3 = request.getSession(true);
                       sesion.setAttribute("sesionusuario",usuario);
                       sesion1.setAttribute("sesionempresa",empresa);
                       sesion2.setAttribute("sesiondepartamento",departamento);
                       sesion3.setAttribute("sesionpass",pass);
                       response.sendRedirect("menu.jsp");
                       //processRequest(request, response);
                    }else{
                         HttpSession sesion2 = request.getSession(true);
                        sesion2.setAttribute("sesionError","Usuario o Contraseña Inválida");
                        response.sendRedirect("index.jsp");
                        
                    }
                    
                    //System.out.println(r + "---");
                    
                        
        
        
    
    }
    
     public String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://192.168.43.56:5000/" + metodo);
            Request req = new Request.Builder().url(url).post(formBody).build();
            Response resp = webClient.newCall(req).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
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

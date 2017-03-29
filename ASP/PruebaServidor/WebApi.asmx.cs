using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.Services;
using System.Web.Services.Protocols;

namespace PruebaServidor{

   
    [WebService(Namespace = "http://Proyecto1-EDD.com/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    [System.Web.Script.Services.ScriptService]
    public class WebApi : System.Web.Services.WebService
    {
        int g = 0;
        int idactivo = 0;        

        [WebMethod]
        public string insertarArbol(string idactivo, string nombreactivo, string descripcion, string nombreusuario, string departamento, string empresa, string fecha, string tiempo)
        {
            string retornado = "";
            int idtransaccion = 0;
            string idtranNom = "";
            string idactivo1 = idactivo;
            string nombreactivo1 = nombreactivo;
            string descripcion1 = descripcion;
            string nombreusuario1 = nombreusuario;
            string departamento1 = departamento;
            string empresa1 = empresa;
            string fecha1 = fecha;
            string tiempo1 = tiempo;
            
            retornado = general.generarCodigo();

            string[] caracter = retornado.Split(':');
            idtransaccion = int.Parse(caracter[0].ToString());
            idtranNom = caracter[1].ToString();

            general.insertarArbol(idtransaccion, idtranNom, idactivo1, nombreactivo1, descripcion1, nombreusuario1, departamento1, empresa1, fecha1, tiempo1);            
            return retornado;
        }

        [WebMethod]
        public string mostrarTransacciones(string nombreusuario)
        {
            string retornado = "";
            string nombreUsuario = nombreusuario;

            retornado = general.retornar(nombreUsuario);

            return retornado;
        }

        
    }
    
}

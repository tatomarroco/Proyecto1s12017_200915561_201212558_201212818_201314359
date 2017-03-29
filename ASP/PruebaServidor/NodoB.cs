using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace PruebaServidor
{
    public class NodoB
    {
        public int nofactura;
        public string fecha;
        public string idtransaccion;
        public string nombreactivo;
        public string idactivo;
        public string descripcion;
        public string tiempo;
        public string empresa;
        public string departamento;        
        public string nombreUsuario;

        public NodoB() { }

        public NodoB(int factura, string idtransaccion, string idactivo, string nombreactivo, string descripcion, 
            string nombreUsuario, string departamento, string empresa, string fecha, string tiempo)
        {
            this.nofactura = factura;
            this.idtransaccion = idtransaccion;
            this.nombreactivo = nombreactivo;
            this.idactivo = idactivo;
            this.descripcion = descripcion;
            this.tiempo = tiempo;
            this.fecha = fecha;
            this.empresa = empresa;
            this.departamento = departamento;
            this.nombreUsuario = nombreUsuario;           

        }

        public string getNombreActivo()
        {
            return nombreactivo;
        }

        public void setNombreActivo(string nombreactivo)
        {
            this.nombreactivo = nombreactivo;
        }

        public string getidActivo()
        {
            return nombreactivo;
        }

        public void setidactivo(string idactivo)
        {
            this.idactivo = idactivo;
        }

        public string getdescripcion()
        {
            return descripcion;
        }

        public void setdescripcion(string descripcion)
        {
            this.descripcion = descripcion;
        }

        public string gettiempo()
        {
            return tiempo;
        }

        public void settiempo(string tiempo)
        {
            this.tiempo = tiempo;
        }


        public string getempresa()
        {
            return empresa;
        }

        public void setempresa(string empresa)
        {
            this.empresa = empresa;
        }

        public string getdepartamento()
        {
            return departamento;
        }

        public void setdepartamento(string departamento)
        {
            this.departamento = departamento;
        }

        public string getnombreUsuario()
        {
            return nombreUsuario;
        }

        public void setnombreUsuario(string nombreUsuario)
        {
            this.nombreUsuario = nombreUsuario;
        }       


        public int getNofactura()
        {
            return nofactura;
        }

        public void setNofactura(int nofactura)
        {
            this.nofactura = nofactura;
        }

        public string getFecha()
        {
            return fecha;
        }

        public void setFecha(string fecha)
        {
            this.fecha = fecha;
        }

        
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;

namespace PruebaServidor
{
    public class general
    {
        static ArbolB5 ar = new ArbolB5();

        public static void insertarArbol(int idtransaccion, string idtranNom, string idactivo, string nombreactivo, string descripcion, string nombreusuario, string departamento, string empresa, string fecha, string tiempo)
        {
            ar.insertar(idtransaccion, idtranNom, idactivo, nombreactivo, descripcion, nombreusuario, departamento, empresa, fecha, tiempo);
        }

        public static void graficar()
        {
            ar.reporteVentas();

        }

        public static string retornar(string nombre)
        {
            return ar.retornarInf(nombre);

        }

        public static string generarCodigo()
        {
            string numero = "";
            int suma1 = 0;
            int suma2 = 0;

            Random obj = new Random();
            string posibles = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            int longitud = posibles.Length;
            char letra;
            int longitudnuevacadena = 15;
            string nuevacadena = "";
            string nuevacadena2 = "";
            for (int i = 0; i < longitudnuevacadena; i++)
            {
                letra = posibles[obj.Next(longitud)];                 
                nuevacadena += letra.ToString() + "-";
                nuevacadena2 += letra.ToString();
            }

            string [] caracter = nuevacadena.Split('-');
            suma1 += Encoding.ASCII.GetBytes(caracter[0])[0] + Encoding.ASCII.GetBytes(caracter[1])[0];
            suma2 += (Encoding.ASCII.GetBytes(caracter[2])[0] + Encoding.ASCII.GetBytes(caracter[3])[0]) + suma1;
            numero = Convert.ToString(suma1);

            return numero + ":" + nuevacadena2;
        }
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace PruebaServidor
{
    public class Pagina
    {
        public Pagina[] ramas = new Pagina[5];
        public NodoB[] claves = new NodoB[4];
        public int cuentas = 0;

        public Pagina(NodoB info)
        {
            claves[0] = info;
        }

        public Pagina() { }

    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Web;
using System.Text;
using System.Threading.Tasks;

namespace PruebaServidor
{
    public class ArbolB5
    {
        Pagina inicio = new Pagina();

        Pagina paginaIzq;
        Pagina paginaDer;

        NodoB inserta;               //nuevo nodo a insertar
        Pagina enlace;              // enlace del nodo padre al hijo
        string imprime = "";          // cadena a imprimir para dibujar
        bool pivote = false;       // para validar una accion
        bool existe = false;
        int cantidad;
        
        public string canciones, canciones2;
        bool pivote1 = false;       // para validar una accion
        bool existe1 = false;

        public string token = "";

        public int insertar(int idtransaccion, string idtranNom, string idactivo, string nombreactivo, string descripcion, string nombreusuario, string departamento, string empresa, string fecha, string tiempo)            
        {
            NodoB a = new NodoB(idtransaccion, idtranNom, idactivo, nombreactivo, descripcion, nombreusuario, departamento, empresa, fecha, tiempo);
            insertarr(a, inicio);
            return a.nofactura;
        }

        void insertarr(NodoB clave, Pagina raiz)
        {
            agregar(clave, raiz);
            if (pivote)
            {
                inicio = new Pagina();
                inicio.cuentas = 1;
                inicio.claves[0] = inserta;
                inicio.ramas[0] = raiz;
                inicio.ramas[1] = enlace;
            }            
        }

        void agregar(NodoB clave, Pagina raiz)
        {
            int pos = 0;                /// k=0;
            pivote = false;           // EmpA=false;

            if (vacio(raiz))  /// crea los nodos para insertar en la pagina
            {
                pivote = true;        //Emp=false;
                inserta = clave;      // X=clave
                enlace = null;        //Xr=null;
            }
            else
            {

                pos = existeNodo(clave, raiz);

                if (existe)
                {
                  pivote = false;
                }
                else
                {
                    agregar(clave, raiz.ramas[pos]);  // se vuelve a llamar para crear el nodo a insertar en la pagina

                    if (pivote)
                    {
                        if (raiz.cuentas < 4)
                        {
                            pivote = false;
                            insertarClave(inserta, raiz, pos);
                        }
                        else
                        {
                            pivote = true;
                            dividirPagina(inserta, raiz, pos);
                            Console.WriteLine("inserto");
                        }
                    }
                }
            }
        }

        void insertarClave(NodoB clave, Pagina raiz, int posicion)
        {
            int i = raiz.cuentas;
            while (i != posicion)
            {
                raiz.claves[i] = raiz.claves[i - 1];
                raiz.ramas[i + 1] = raiz.ramas[i];
                --i;
            }
            raiz.claves[posicion] = clave;
            raiz.ramas[posicion + 1] = enlace;
            raiz.cuentas = ++raiz.cuentas;

            Console.WriteLine("INSERTO");
        }


        void dividirPagina(NodoB clave, Pagina raiz, int posicion)
        {
            int pos = 0;
            int Posmda = 0;
            if (posicion <= 2)
                Posmda = 2;
            else
            {
                Posmda = 3;
            }
            Pagina Mder = new Pagina();
            pos = Posmda + 1;
            while (pos != 5)
            {
                Mder.claves[(pos - Posmda) - 1] = raiz.claves[pos - 1];
                Mder.ramas[pos - Posmda] = raiz.ramas[pos];
                ++pos;
            }
            Mder.cuentas = 4 - Posmda;
            raiz.cuentas = Posmda;
            if (posicion <= 2)
                insertarClave(clave, raiz, posicion);
            else
            {
                insertarClave(clave, Mder, (posicion - Posmda));
            }
            inserta = raiz.claves[raiz.cuentas - 1];
            Mder.ramas[0] = raiz.ramas[raiz.cuentas];
            raiz.cuentas = --raiz.cuentas;
            enlace = Mder;


        }

        public bool vacio(Pagina raiz)
        {
            return (raiz == null || raiz.cuentas == 0);
        }


        public int existeNodo(NodoB clave, Pagina raiz)
        {
            int valor = 0;

            if (clave.nofactura < raiz.claves[0].nofactura)
            {
                existe1 = false;
                valor = 0;
            }
            else
            {
                valor = raiz.cuentas;
                while (clave.nofactura < raiz.claves[valor - 1].nofactura && valor > 1)
                    --valor;

                existe = (clave.nofactura < raiz.claves[valor - 1].nofactura);                
                existe1 = (clave.nofactura == raiz.claves[valor - 1].nofactura);
            }

            return valor;
        }

        
        NodoB fuck;
        public NodoB nodoAB(int nofactura)
        {
            fuck = null;
            NodoB n = new NodoB(nofactura, "","","","","","","","","");
            retornarNodo(n, inicio);
            return fuck;

        }

        // WEB SERVICE NUEVO
        public NodoB retornarNodo(NodoB clave, Pagina raiz)
        {

            int pos = 0;    

            if (vacio(raiz))  /// crea los nodos para insertar en la pagina
            {
                Console.WriteLine("no existe");
                return null;
            }
            else
            {
                pos = existeNodo(clave, raiz);

                if (existe1)
                {
                    NodoB aux;
                    int n = raiz.claves[pos - 1].getNofactura();
                    aux = raiz.claves[pos - 1];                    
                    Console.WriteLine("Se encontro a " + n);
                    fuck = aux;
                    return aux;

                }
                else
                {
                    int n = clave.getNofactura();
                    retornarNodo(clave, raiz.ramas[pos]);  // se vuelve a llamar para crear el nodo a inertar en la pagina
                    Console.WriteLine("No existe" + n);
                    return null;

                }

            }

        }

        public void graficarPagina(StringBuilder n, Pagina raiz)
        {
            Pagina nodo = raiz;
            
            if (nodo == null)
            {

            }
            else
            {
                if (nodo.cuentas != 0)
                {

                    int k = 0;
                    n.Append("cancion_" + nodo.claves[0].nofactura + " [label= \"");

                    for (k = 1; k <= nodo.cuentas; k++)
                    {
                        n.Append("<r" + (k - 1) + ">" + " | " + "<cl" + k + ">" + "IdTransacción: " + nodo.claves[k - 1].nofactura + " &#92;" + "nFecha: " + nodo.claves[k - 1].fecha + " &#92;" + "nTotal: " + nodo.claves[k - 1].idtransaccion + " &#92;" + "nUsuario: " + nodo.claves[k - 1].nombreUsuario + " | ");
                    }
                    n.Append("<r" + (k - 1) + "> \"];\n");

                    for (k = 0; k <= nodo.cuentas; k++)
                    {
                        if (nodo.ramas[k] != null)
                        {
                            if (nodo.ramas[k].cuentas != 0)
                            {
                                n.Append("cancion_" + nodo.claves[0].nofactura + ":r" + k + " -> cancion_" + nodo.ramas[k].claves[0].nofactura + ";\n");
                                
                                Console.WriteLine(n.ToString());
                            }
                            else { 
                            }
                        }

                    }

                    for (k = 0; k <= nodo.cuentas; k++)
                    {

                        graficarPagina(n, nodo.ramas[k]);
                    }
                }
                else
                { }
            }            
        }

        public void graficarArbolB(Pagina raiz)
        {

            string ruta = "C:\\Users\\l_enr\\Desktop\\ArbolB.txt";
            FileStream stream = new FileStream(ruta, FileMode.OpenOrCreate, FileAccess.Write); ;
            StreamWriter reader = new StreamWriter(stream);

            if (File.Exists(ruta))
            {
                StringBuilder contenido = new StringBuilder();
                contenido.Append("digraph{\n");
                contenido.Append("node [shape = record];\n");
                contenido.Append("rankdir = TD;\n");
                graficarPagina(contenido, raiz);
                contenido.Append("}");
                reader.WriteLine(contenido.ToString());
                //aux.close();
            }
            else
            {
                StringBuilder contenido = new StringBuilder();
                contenido.Append("digraph{\n");
                contenido.Append("node [shape = record];\n");
                contenido.Append("rankdir = TD;\n");
                graficarPagina(contenido, raiz);
                contenido.Append("}");
                reader.WriteLine(contenido.ToString());
            }
            reader.Close();

        }
        public void generarImagen()
        {
            graficarArbolB(inicio);
        }

         public string retornarInf(string nombre)
         {
             token = "";
             graficarBuscar(inicio, nombre);
             return token;
         }
        
        string retornarParametrosDetalle(int nofactura, String usuario)
        {
            string enviar = "";
            string usuario2 = "";
            usuario2 = usuario;
            string nof = Convert.ToString(nofactura);
            enviar = nofactura + "," + usuario2;

            return enviar;
        }

        public void reporteVentas() 
         {
             generarImagen();             
         }

        public void Buscar(string nombre)
        {
            retornarInf(nombre);            
        }

        int contador;
        string fechas;
        public string reporteFechas(string fecha1, string fecha2)
        {
            contador = 0;
            fechas = "";
            recorrerArbol(inicio, fecha1, fecha2);
            Console.WriteLine("Fechas: " + fechas);
            Console.WriteLine("Cantidad" + contador);
            return fechas;
        }

        public void recorrerArbol(Pagina raiz, string fecha1, string fecha2)
        {
            try
            {

                DateTime f1 = Convert.ToDateTime(fecha1);
                DateTime f2 = Convert.ToDateTime(fecha2);
                Pagina nodo = raiz;

                if (nodo == null) { }
                else
                {
                    if (nodo.cuentas != 0)
                    {
                        int k = 0;

                        for (k = 1; k <= nodo.cuentas; k++)
                        {
                            string af = nodo.claves[k - 1].fecha;
                            DateTime f11 = Convert.ToDateTime(af);

                            if (f11.CompareTo(f1) >= 0 && f11.CompareTo(f2) <= 0)
                            {
                                fechas = fechas + nodo.claves[k - 1].nofactura + "," + nodo.claves[k - 1].fecha + "," + nodo.claves[k - 1].idtransaccion + "," + nodo.claves[k - 1].nombreUsuario + ";";
                                contador++;
                            }

                        }

                        for (k = 0; k <= nodo.cuentas; k++)
                        {

                            recorrerArbol(nodo.ramas[k], fecha1, fecha2);
                        }
                    }
                }
            }
            catch (Exception ee)
            { }
        }

        string totales;
        public string reporteVentasxValor(double valor, double valor2)
        {

            totales = "";
            contador = 0;
            Console.WriteLine(totales);
            Console.WriteLine("Cantidad: " + contador);
            return totales;
        }

      
        string repxusuarios;
        public string reporteVentasxUsuario(string valor, string valor2)
        {

            repxusuarios = "";
            contador = 0;            
            Console.WriteLine(repxusuarios);
            Console.WriteLine("Numero:" + contador);
            return repxusuarios;
        }      

        public void graficarBuscar(Pagina raiz, string nombre)
        {
            Pagina nodo = raiz;            

            if (nodo == null)
            {

            }
            else
            {
                if (nodo.cuentas != 0)
                {

                    int k = 0;
                   
                    for (k = 1; k <= nodo.cuentas; k++)
                    {

                        if (nombre.CompareTo(nodo.claves[k - 1].nombreUsuario) == 0)
                        {
                            token += nodo.claves[k - 1].nofactura + "->";
                        }                        
                    }                    

                    for (k = 0; k <= nodo.cuentas; k++)
                    {
                        if (nodo.ramas[k] != null)
                        {
                            if (nodo.ramas[k].cuentas != 0)
                            {
                               
                            }
                            else { }
                        }
                    }

                    for (k = 0; k <= nodo.cuentas; k++)
                    {
                        graficarBuscar(nodo.ramas[k], nombre);
                    }
                }
                else{ }
            }            
        }
    }
}
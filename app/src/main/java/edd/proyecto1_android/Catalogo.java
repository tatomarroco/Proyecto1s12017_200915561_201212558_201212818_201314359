package edd.proyecto1_android;

/**
 * Created by Estuardo on 24/03/2017.
 */

public class Catalogo {
    NodoCatalogo Primero;
    NodoCatalogo Ultimo;

    private int longitud=0;

    public static Catalogo getCatalogue() {
        return catalogue;
    }

    public static void setCatalogue(Catalogo catalogue) {
        Catalogo.catalogue = catalogue;
    }

    private static Catalogo catalogue;

    public Catalogo(){
        Primero = null;
        Ultimo = null;
    }

    public boolean estado(){
        if(Primero==null){
            return true;
        }
        else{
            return false;
        }
    }

    public void Add(String IdProducto, String Nombre, String Descripcion){
        longitud++;
        if(estado()){
            NodoCatalogo nuevo=new NodoCatalogo(IdProducto,Nombre,Descripcion,longitud);
            Primero=nuevo;
            Ultimo=nuevo;
        }
        else{
            Ultimo = Ultimo.Next = new NodoCatalogo(IdProducto,Nombre,Descripcion, longitud);
            Ultimo.Next = Primero;
        }
    }

    public String Search(String IdProducto) {
        NodoCatalogo aux = Primero;
        String respon="";
        if (Primero == null) {
            return "Lista Vacia";
        } else {
            while (aux != null) {
                if (aux.getIDProducto() == IdProducto) {
                    respon = aux.getIDProducto();
                    break;
                }
                aux = aux.Next;
            }
        }
        return respon;
    }

    public int getLongitud() {
        return longitud;
    }

    public String ObtenerID(int pos){
        NodoCatalogo aux = Primero;
        String respuesta="";
        if (Primero == null) {
            return "Lista Vacia";
        } else {
            while (aux != null) {
                if (aux.getPos() == pos) {
                    respuesta = aux.getIDProducto();
                    break;
                }
                aux = aux.Next;
            }
        }

        return respuesta;
    }


    public String ObtenerNombre(int pos){
        NodoCatalogo aux = Primero;
        String respuesta="";
        if (Primero == null) {
            return "Lista Vacia";
        } else {
            while (aux != null) {
                if (aux.getPos() == pos) {
                    respuesta = aux.getNombre();
                    break;
                }
                aux = aux.Next;
            }
        }

        return respuesta;
    }

    public String ObtenerDescrip(int pos){
        NodoCatalogo aux = Primero;
        String respuesta="";
        if (Primero == null) {
            return "Lista Vacia";
        } else {
            while (aux != null) {
                if (aux.getPos() == pos) {
                    respuesta = aux.getDescripcion();
                    break;
                }
                aux = aux.Next;
            }
        }

        return respuesta;
    }

}

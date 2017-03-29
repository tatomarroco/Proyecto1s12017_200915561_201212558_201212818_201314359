package edd.proyecto1_android;

/**
 * Created by Estuardo on 24/03/2017.
 */

public class NodoCatalogo {
    private String IDProducto;
    private String Nombre;
    private String Descripcion;

    public int getPos() {
        return pos;
    }

    public void setPos(int pos) {
        this.pos = pos;
    }

    private int pos;

    NodoCatalogo Next;

    public NodoCatalogo(String IdProducto, String Nombre, String Descripcion, int pos){
        this.IDProducto = IdProducto;
        this.Nombre = Nombre;
        this.Descripcion = Descripcion;
        this.pos = pos;
    }


    public String getIDProducto() {
        return IDProducto;
    }

    public void setIDProducto(String IDProducto) {
        this.IDProducto = IDProducto;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String nombre) {
        Nombre = nombre;
    }

    public String getDescripcion() {
        return Descripcion;
    }

    public void setDescripcion(String descripcion) {
        Descripcion = descripcion;
    }


}

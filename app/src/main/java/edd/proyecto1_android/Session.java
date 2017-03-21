package edd.proyecto1_android;

/**
 * Created by Estuardo on 18/3/2017.
 */

public class Session {
    private boolean sesion = false;
    private String User;

    public static Session ss;

    public Session(){}

    public Session(boolean sesion,String User){
           this.sesion = sesion;
           this.User = User;
    }

    public boolean isSesion() {
        return this.sesion;
    }

    public void setSesion(boolean sesion) {
        this.sesion = sesion;
    }

    public String getUser() {
        return this.User;
    }

    public void setUser(String user) {
        this.User = user;
    }

    /*OBTIENE SECCION ACTUAL Y ATRIBUTOS*/
    public static Session getSession(){
           return ss;
    }

    public void setSession(Session ss){
        this.ss = ss;
    }
}

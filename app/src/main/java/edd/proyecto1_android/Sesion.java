package edd.proyecto1_android;

/**
 * Created by Estuardo on 18/3/2017.
 */

public class Sesion {
    private boolean sesion = false;
    private String User;

    public Sesion(){}

    public Sesion(boolean sesion,String User){
           this.sesion = sesion;
           this.User = User;
    }

    public boolean isSesion() {
        return sesion;
    }

    public void setSesion(boolean sesion) {
        this.sesion = sesion;
    }

    public String getUser() {
        return User;
    }

    public void setUser(String user) {
        User = user;
    }
    
}

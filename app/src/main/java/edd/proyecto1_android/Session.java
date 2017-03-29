package edd.proyecto1_android;

/**
 * Created by Estuardo on 18/3/2017.
 */

public class Session {
    private boolean sesion = false;
    private String User;
    private String Department;
    private String Company;

    public static Session ss;

    //*************CONSTRUCTORES*******************************************************************//
    public Session(){}
    //---------------------------------------------------------------------------------------------//
    public Session(boolean sesion,String Usuario, String Empresa, String Departamento){
        this.sesion = sesion;
        this.User = Usuario;
        this.Company = Empresa;
        this.Department = Departamento;
    }
    //*********************************************************************************************//



    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String department) {
        Department = department;
    }

    public String getCompany() {
        return Company;
    }

    public void setCompany(String company) {
        Company = company;
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

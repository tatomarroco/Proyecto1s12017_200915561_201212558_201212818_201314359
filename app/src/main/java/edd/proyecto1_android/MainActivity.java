package edd.proyecto1_android;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.TargetApi;
import android.content.Entity;
import android.content.Intent;
import android.os.Build;
import android.support.annotation.MainThread;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AutoCompleteTextView;
import android.os.AsyncTask;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;

import android.widget.TextView;
import android.widget.Toast;
import android.util.Log;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;

public class MainActivity extends AppCompatActivity {

    public static OkHttpClient webClient = new OkHttpClient();
    public static String res = "";
    private Button btnLogin;
    private EditText txtUser;
    private EditText txtPassword;
    private EditText txtEmp;
    private EditText txtDeptom;
    protected ProgressBar barra;

    public static String st;
    public static String user;
    public static String password;
    public static String departamento;
    public static String empresa;

    protected static final int TIMER_RUNTIME = 2000;
    protected boolean barraAtiva;
    protected boolean barrallena;

    boolean conec = false;

    public boolean isElfalso() {
        return elfalso;
    }

    public void setElfalso(boolean elfalso) {
        this.elfalso = elfalso;
    }

    boolean elfalso = false;

    final Session sesionvar = new Session();

    public Intent getMenuP() {
        return MenuP;
    }

    public void setMenuP(Intent menuP) {
        MenuP = menuP;
    }

    Intent MenuP;
    private conexionTask d = null;//Hilo

    public static String getRes() {
        return res;
    }

    public static void setRes(String res) {
        MainActivity.res = res;
    }

    @Override
    public void onBackPressed() {
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnLogin = (Button) findViewById(R.id.btnLogin);
        txtUser = (EditText) findViewById(R.id.txtUsuario);
        txtPassword = (EditText) findViewById(R.id.txtPass);
        txtEmp = (EditText) findViewById(R.id.txtEmpresa);
        txtDeptom = (EditText) findViewById(R.id.txtDepto);
        barra = (ProgressBar) findViewById(R.id.Login_Progress);
        final Intent irAMenu = new Intent(MainActivity.this, menuPrincipalActivity.class);//Moverse entre Layout
        setMenuP(irAMenu);

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                setUser(txtUser.getText().toString());
                setPassword(txtPassword.getText().toString());
                setEmpresa(txtEmp.getText().toString());
                setDepartamento(txtDeptom.getText().toString());
                barra.setVisibility(View.VISIBLE);
                //showProgress(true);
                d = new conexionTask();
                d.execute((Void) null);







                //txtUsuario.setText(st);
                //Toast.makeText(MainActivity.this, "Hola " + st, Toast.LENGTH_LONG).show();
                //System.out.println(getRes());




            }
        });
    }


    //---------------------HILO ASINCRONICO---------------------------//
    public class conexionTask extends AsyncTask<Void,Void,Boolean>{
        @Override
        protected  Boolean doInBackground(Void... voids){


            try {
                Conexion(getUser(),getPassword(),getEmpresa(),getDepartamento());
                if (conec){
                    barraAtiva = true;
                    int waited = 0;
                    while (barraAtiva && (waited< TIMER_RUNTIME)){
                        Thread.sleep(100);
                        if(barraAtiva){
                            waited +=500;
                            updateProgress(waited);
                        }
                    }

                }else{
                    try{
                        System.out.println("No hay Conexíon");
                        return false;
                    }catch (Exception e){
                        System.out.println(e.getMessage());
                        return  false;
                    }

                }

                // Simulate network access.

            } catch (InterruptedException e) {
                System.out.println(e.getMessage()+"   "+e.getLocalizedMessage());
                return false;
            } finally {
                onContinue();
            }

            return true;
        }

        @Override
        protected void onPostExecute(final Boolean success) {
            if (success) {
                finish();
            } else {
                d = null;
                barra.setProgress(0);
                barra.setVisibility(false ? View.GONE : View.INVISIBLE);
                if(conec && isElfalso()){
                    txtUser.setError(getString(R.string.error_Login));
                    txtUser.requestFocus();
                }else if(conec==false){
                    Toast.makeText(MainActivity.this,"¡Hubo un problema de Conexión!",Toast.LENGTH_SHORT).show();
                }

            }
        }


        public void updateProgress(final int timePassed){
            if(null != barra){
                final int progress = barra.getMax() * timePassed / TIMER_RUNTIME;
                barra.setProgress(progress);
            }
        }

        public void onContinue(){
            Log.d("Mensaje Final: ","La Barra Ha Cargado");
            barrallena = true;
            if(conec == true){
                if (getRes().equalsIgnoreCase("true")) {
                    sesionvar.setSesion(true);
                    sesionvar.setUser(getUser());
                    sesionvar.setCompany(getEmpresa());
                    sesionvar.setDepartment(getDepartamento());
                    sesionvar.setSession(sesionvar);
                    if(sesionvar != null && barrallena && sesionvar.isSesion()==true){
                        startActivity(getMenuP());
                    }
                }else {
                    d = null;
                    setElfalso(true);
                    sesionvar.setUser("");
                    sesionvar.setCompany("");
                    sesionvar.setDepartment("");
                    sesionvar.setSesion(false);
                    sesionvar.setSession(sesionvar);
                }
            }else{
                /*if(isElfalso()){
                    try{
                        //EsFalso();
                    }catch (Exception e){
                        System.out.println(e.getMessage()+"   "+e.getLocalizedMessage());
                    }
                }*/
            }

        }




        public boolean Conexion(String user, String contrasenia, String empresa, String Depto) {
            RequestBody formBody = new FormEncodingBuilder()
                    .add("usuario", user)
                    .add("contrasenia", contrasenia)
                    .add("empresa", empresa)
                    .add("departamento", Depto)
                    .build();
            String r = "";
            setRes(getStr("Login", formBody));
            if(conec) {
                if (getRes() != null && getRes().equalsIgnoreCase("true")) {
                    System.out.println("LA MATRIZ RETORNÓ " + getRes());
                    setElfalso(false);
                    return true;
                } else {
                    setElfalso(true);
                    return false;
                }
            }
            return true;
        }




        public String getStr(String metodo, RequestBody formBody) {

            try {
                URL url = new URL("http://192.168.43.56:5000/" + metodo);
                Request request = new Request.Builder().url(url).post(formBody).build();
                Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
                String response_string = response.body().string();//y este seria el string de las respuesta
                conec = true;
                return response_string;
            } catch (MalformedURLException ex) {
                setRes("");
                conec = false;
                System.out.println(ex.getMessage());
                //java.util.logging.Logger.getLogger(edd.proyecto1_android.MainActivity.class.getName()).log(Level.SEVERE, null, ex);
               // Toast.makeText(MainActivity.this,ex.getMessage(),Toast.LENGTH_SHORT);
            } catch (Exception ex) {
               System.out.println(ex.getMessage());
                setRes("");
                conec = false;
                // java.util.logging.Logger.getLogger(edd.proyecto1_android.MainActivity.class.getName()).log(Level.SEVERE, null, ex);
            }
            return "";
        }

    }



    protected void EsFalso(){
        ;
       // txtPassword.setError(getString(R.string.error_Login));
        //txtPassword.requestFocus();
    }

  /*  @TargetApi(Build.VERSION_CODES.LOLLIPOP_MR1)
    private void showProgress(final boolean show) {
        // On Honeycomb MR2 we have the ViewPropertyAnimator APIs, which allow
        // for very easy animations. If available, use these APIs to fade-in
        // the progress spinner.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP_MR1) {
            int shortAnimTime = getResources().getInteger(android.R.integer.config_shortAnimTime);


            ProgressBar.setVisibility(show ? View.VISIBLE : View.GONE);
            ProgressBar.animate().setDuration(shortAnimTime).alpha(
                    show ? 1 : 0).setListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animation) {
                    ProgressBar.setVisibility(show ? View.VISIBLE : View.GONE);
                }
            });
        } else {
            // The ViewPropertyAnimator APIs are not available, so simply show
            // and hide the relevant UI components.
            ProgressBar.setVisibility(show ? View.VISIBLE : View.GONE);
        }
    }*/



    public static String getUser() {
        return user;
    }

    public static void setUser(String user) {
        MainActivity.user = user;
    }

    public static String getPassword() {
        return password;
    }

    public static void setPassword(String password) {
        MainActivity.password = password;
    }

    public static String getDepartamento() {
        return departamento;
    }

    public static void setDepartamento(String departamento) {
        MainActivity.departamento = departamento;
    }

    public static String getEmpresa() {
        return empresa;
    }

    public static void setEmpresa(String empresa) {
        MainActivity.empresa = empresa;
    }

}

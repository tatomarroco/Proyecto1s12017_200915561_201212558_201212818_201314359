package edd.proyecto1_android;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.TargetApi;
import android.content.Entity;
import android.content.Intent;
import android.os.Build;
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
    private AutoCompleteTextView txtUser;
    private EditText txtPassword;
    private AutoCompleteTextView txtEmp;
    private AutoCompleteTextView txtDeptom;
    protected ProgressBar barra;

    public static String st;
    public static String user;
    public static String password;
    public static String departamento;
    public static String empresa;

    protected static final int TIMER_RUNTIME = 2000;
    protected boolean barraAtiva;
    protected boolean barrallena;

    public Intent getMenuP() {
        return MenuP;
    }

    public void setMenuP(Intent menuP) {
        MenuP = menuP;
    }

    Intent MenuP;


    public static String getRes() {
        return res;
    }

    public static void setRes(String res) {
        MainActivity.res = res;
    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnLogin = (Button) findViewById(R.id.btnLogin);
        txtUser = (AutoCompleteTextView) findViewById(R.id.txtUsuario);
        txtPassword = (EditText) findViewById(R.id.txtPass);
        txtEmp = (AutoCompleteTextView) findViewById(R.id.txtEmpresa);
        txtDeptom = (AutoCompleteTextView) findViewById(R.id.txtDepto);
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
                conexionTask d = new conexionTask(); //Hilo
                d.execute();




                //txtUsuario.setText(st);
                //Toast.makeText(MainActivity.this, "Hola " + st, Toast.LENGTH_LONG).show();
                //System.out.println(getRes());




            }
        });
    }


    //---------------------HILO ASINCRONICO---------------------------//
    private class conexionTask extends AsyncTask<Void,Void,Void>{
        @Override
        protected  Void doInBackground(Void... voids){
            barraAtiva = true;
            try {
                int waited = 0;
                while (barraAtiva && (waited< TIMER_RUNTIME)){
                    Thread.sleep(100);
                    if(barraAtiva){
                        waited +=500;
                        updateProgress(waited);
                    }
                }
                Conexion(getUser(),getPassword(),getEmpresa(),getDepartamento());


                // Simulate network access.

            } catch (InterruptedException e) {
                return null;
            } finally {
                onContinue();
            }



            return null;
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
            if(getRes().equalsIgnoreCase("true")){
                boolean s = true;
                Sesion sesionvar = new Sesion(s,getUser());
                if(sesionvar != null && barrallena ){
                    startActivity(getMenuP());
                }
            }

        }

        public void Conexion(String user, String contrasenia, String empresa, String Depto) {
            RequestBody formBody = new FormEncodingBuilder()
                    .add("usuario", user)
                    .add("contrasenia", contrasenia)
                    .add("empresa", empresa)
                    .add("departamento", Depto)
                    .build();
            String r = "";
            setRes(getString("Login", formBody));
            System.out.println(getRes());
        }



        public String getString(String metodo, RequestBody formBody) {

            try {
                URL url = new URL("http://192.168.1.45:5000/" + metodo);
                Request request = new Request.Builder().url(url).post(formBody).build();
                Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
                String response_string = response.body().string();//y este seria el string de las respuesta
                return response_string;
            } catch (MalformedURLException ex) {
                java.util.logging.Logger.getLogger(edd.proyecto1_android.MainActivity.class.getName()).log(Level.SEVERE, null, ex);
            } catch (Exception ex) {
                java.util.logging.Logger.getLogger(edd.proyecto1_android.MainActivity.class.getName()).log(Level.SEVERE, null, ex);
            }
            return null;
        }

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

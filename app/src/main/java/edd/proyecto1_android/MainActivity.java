package edd.proyecto1_android;

import android.content.Entity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AutoCompleteTextView;
import android.os.AsyncTask;
import android.widget.Button;
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
    //Thread hiloImg = new Thread(new hPost());
    private Button btnLogin;
    private TextView txtName;
    private AutoCompleteTextView txtUsuario;
    public static String st;


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
        txtUsuario = (AutoCompleteTextView) findViewById(R.id.txtUsuario);



        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent irAMenu = new Intent(MainActivity.this, menuPrincipalActivity.class);//Moverse entre Layout
                conexionTask d = new conexionTask(); //Hilo
                d.execute();
                //st = getRes();

                //txtUsuario.setText(st);
                //Toast.makeText(MainActivity.this, "Hola " + st, Toast.LENGTH_LONG).show();
                //System.out.println(getRes());


                startActivity(irAMenu);//Se mueve a otro Layout

            }
        });
    }



  /*  private class hPost implements Runnable {

        @Override
        public void run() {
            while (true) {
                //pruebaConexion("hola", "Prro");

                METODOS

                try {
                    Thread.sleep(100);

                } catch (InterruptedException ex) {
                    Logger.getLogger(MainActivity.class.getName()).log(Level.SEVERE, null, ex);
                }
                //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
            }
        }

    }*/


    //---------------------HILO ASINCRONICO---------------------------//
    private class conexionTask extends AsyncTask<Void,Void,Void>{

        @Override
        protected  Void doInBackground(Void... voids){
            pruebaConexion("hola","prro");

            Log.d("Hola mundo","Se está ejecutando proceso en background");
            return null;
        }


        public void pruebaConexion(String opcion, String palabra) {
            RequestBody formBody = new FormEncodingBuilder()
                    .add("p", palabra)
                    //.add("opcion", opcion)
                    .build();
            String r = "";
            setRes(getString("meto", formBody));
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


}

package edd.proyecto1_android;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.widget.ImageView;
import android.widget.TextClock;
import android.widget.TextView;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

public class RentaActivos extends AppCompatActivity {


    private ImageView ImagenInicio;
    private TextView lblCarga;
    public int crono=4;
    public int control=0;
    public String controlbl;

    public Intent getElLogin() {
        return elLogin;
    }

    public void setElLogin(Intent elLogin) {
        this.elLogin = elLogin;
    }

    Intent elLogin;


    TextView lblalterno;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_renta_activos);
        ImagenInicio = (ImageView)findViewById(R.id.ImagenEDD);
        lblCarga = (TextView)findViewById(R.id.lblCarga);
        final Intent irLogin = new Intent(RentaActivos.this,MainActivity.class);
        setElLogin(irLogin);
        controlbl = "Iniciando";
        lblCarga.setText(controlbl);
        Cronometro d = new Cronometro(); //Hilo
        d.execute();

    }



    //---------------------HILO ASINCRONICO---------------------------//
    private class Cronometro extends AsyncTask<Void,Void,Void> {
        @Override
        protected  Void doInBackground(Void... voids){
            try {

                int waited = 0;
                while (waited< crono){
                    Thread.sleep(1000);
                        waited +=1;
                        control = waited;
                    controlbl =controlbl + ".";
                   // updateProgress(controlbl);
                }
                // Simulate network access.
            } catch (InterruptedException e) {
                return null;
            } finally {
              onContinue();
            }
            return null;
        }

        public void onContinue(){
            if (control == crono) {
                startActivity(getElLogin());
            }
        }



    }

    public void updateProgress(final String ctrl){
        if (control < crono){
            final String progreso = ctrl;
            lblalterno.setText(progreso);
        }else {

            lblalterno.setText("¡Listo!");
        }

    }


}

package edd.proyecto1_android;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.okhttp.OkHttpClient;

import org.ksoap2.SoapEnvelope;
import org.ksoap2.serialization.SoapObject;
import org.ksoap2.serialization.SoapPrimitive;
import org.ksoap2.serialization.SoapSerializationEnvelope;
import org.ksoap2.transport.HttpTransportSE;
import org.xmlpull.v1.XmlPullParserException;

import java.io.IOException;

public class DevolucionesActivity extends AppCompatActivity {

    private Spinner ComboBox1;
    private Spinner ComboBox2;
    private EditText txtUserName;
    private EditText txtDescrip;
    private Button btnDevolver;
    private Button btnRegresarMp;
    private TextView lblday;

    public static OkHttpClient webClient = new OkHttpClient();

    Catalogo catalogo = new Catalogo();

    public Session sesionactual = new Session();

    boolean conec = false;

    //----------Strings------------------
    String nombreActivo,idActivo,Descrip,usuario,Depto,Empresa,Fecha,Tiempo;

    //*******************Cadena de Respuesta de FLASK (Activos)************************************//
    String RespuestaASP;

    public String getRespuestaASP() {
        return RespuestaASP;
    }

    public void setRespuestaASP(String respuestaASP) {
        RespuestaASP = respuestaASP;
    }
    //*********************************************************************************************//





    @Override
    public void onBackPressed() {
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_devoluciones);

        sesionactual = sesionactual.getSession();
        catalogo = catalogo.getCatalogue();

        final Intent irAMp = new Intent(DevolucionesActivity.this, menuPrincipalActivity.class);//Moverse a Menu Principal

        btnDevolver = (Button) findViewById(R.id.btnDevolver);
        btnRegresarMp = (Button) findViewById(R.id.btnRegresarMp);
        lblday = (TextView) findViewById(R.id.lblday);
        ComboBox1 = (Spinner) findViewById(R.id.lactiv);

        ComboBox2 = (Spinner) findViewById(R.id.ComboBox2);
        txtUserName = (EditText) findViewById(R.id.txtNombreUser);
        txtUserName.setEnabled(false);

        txtDescrip = (EditText) findViewById(R.id.txtDescrip);
        txtDescrip.setEnabled(false);
        //ArrayAdapter adapter2 = ArrayAdapter.createFromResource(this, R.array.ListaPrueba2, android.R.layout.simple_spinner_item);

        btnDevolver.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        btnRegresarMp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(irAMp);
            }
        });

        ConsultarB();


    }


    //************************METODO PARA COMUNICAR Y ENVIAR A ASP*********************************//
    public void ConsultarB() {


        Thread nt = new Thread() {
            String res;

            @Override
            public void run() {
                String NAMESPACE = "http://Proyecto1-EDD.com/";
                String URL = "http://192.168.43.19/PruebaServidor/WebApi.asmx";
                String METHOD_NAME = "insertarArbol";
                String SOAP_ACTION = "http://Proyecto1-EDD.com/insertarArbol";

                SoapObject request = new SoapObject(NAMESPACE, METHOD_NAME);
                request.addProperty("valor1", idActivo);
                request.addProperty("valor2", nombreActivo);
                request.addProperty("valor3", Descrip);
                request.addProperty("valor4", usuario);
                request.addProperty("valor5", Depto);
                request.addProperty("valor6", Empresa);
                request.addProperty("valor7", Fecha);
                request.addProperty("valor8", Tiempo);

                SoapSerializationEnvelope envelope = new SoapSerializationEnvelope(SoapEnvelope.VER11);
                envelope.dotNet = true;

                envelope.setOutputSoapObject(request);

                HttpTransportSE transporte = new HttpTransportSE(URL);

                try {
                    transporte.call(SOAP_ACTION, envelope);
                    SoapPrimitive resultado_xml = (SoapPrimitive) envelope.getResponse();
                    res = resultado_xml.toString();
                    setRespuestaASP(res);
                    System.out.println(res);
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (XmlPullParserException e) {
                    e.printStackTrace();
                }

                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        CrearCatalogo();
                        Toast.makeText(DevolucionesActivity.this, "", Toast.LENGTH_LONG).show();
                        txtDescrip.setText("");
                    }
                });
            }
        };

        nt.start();
    }
    //*********************************************************************************************//


    public void CrearCatalogo(){
        String Catal[] = getRespuestaASP().split(":");
        for(int i=0; i < Catal.length-1;i++){
            String node[] = Catal[i].split(",");
            catalogo.Add(node[0],node[1],node[2]);
            lblday.setText(node[3]);
        }
    }




}

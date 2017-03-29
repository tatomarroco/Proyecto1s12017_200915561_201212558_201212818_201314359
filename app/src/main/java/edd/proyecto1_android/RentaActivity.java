package edd.proyecto1_android;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Adapter;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

//LIBRERIAS PARA CONEXION CON FLASK PYTHON---------------------------------------------------------//
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.IllegalFormatException;
import java.util.logging.Level;
import java.util.logging.Logger;

//LIBRERIAS PARA CONEXION EN API ASP---------------------------------------------------------------//
import org.ksoap2.SoapEnvelope;
import org.ksoap2.serialization.SoapObject;
import org.ksoap2.serialization.SoapPrimitive;
import org.ksoap2.serialization.SoapSerializationEnvelope;
import org.ksoap2.transport.HttpTransportSE;
import org.xmlpull.v1.XmlPullParserException;

import java.io.IOException;
import java.io.*;
//-------------------------------------------------------------------------------------------------//




public class RentaActivity extends AppCompatActivity {

    private Spinner ComboBox1;
    private Spinner ComboBox2;
    private EditText txtUserName;
    private EditText txtDescrip;
    private Button btnRentar;
    private Button btnRegresarMp;

    public static OkHttpClient webClient = new OkHttpClient();

    private conexionTask d = null;//Hilo

    Catalogo catalogo = new Catalogo();

    public Session sesionactual = new Session();

    boolean conec = false;

    //----------Strings------------------
    String nombreActivo,idActivo,Descrip,usuario,Depto,Empresa,Fecha,Tiempo;

    //*******************Cadena de Respuesta de FLASK (Activos)************************************//
    String RespuestaFlask;

    public String getRespuestaFlask() {
        return RespuestaFlask;
    }

    public void setRespuestaFlask(String respuestaFlask) {
        RespuestaFlask = respuestaFlask;
    }
    //*********************************************************************************************//


    @Override
    public void onBackPressed() {
    }

    //@Override
    //protected void onOpen(){}

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_renta);

        d= new conexionTask();
        d.execute((Void) null);

        sesionactual = sesionactual.getSession();

        btnRentar = (Button) findViewById(R.id.btnRentar);
        btnRegresarMp = (Button) findViewById(R.id.btnRegresarMp);
        final Intent irAMp = new Intent(RentaActivity.this, menuPrincipalActivity.class);//Moverse a Menu Principal

        ComboBox1 = (Spinner) findViewById(R.id.lactiv);


        ComboBox2 = (Spinner) findViewById(R.id.ComboBox2);
        ArrayAdapter adapter2 = ArrayAdapter.createFromResource(this, R.array.ListaPrueba2, android.R.layout.simple_spinner_item);

        txtUserName = (EditText) findViewById(R.id.txtNombreUser);
        txtUserName.setEnabled(false);

        txtDescrip = (EditText) findViewById(R.id.txtDescrip);
        txtDescrip.setEnabled(false);



        btnRentar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                usuario = sesionactual.getUser();
                Depto = sesionactual.getDepartment();
                Empresa = sesionactual.getCompany();
                Fecha = getDateTime();
                catalogo.setCatalogue(catalogo);
                Enviar();
            }
        });


        btnRegresarMp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(irAMp);
            }
        });

        //-------------------------------CUANDO SE SELECCIONA UNA OPCION DEL SPINNER----------------------------------------------//
        ComboBox1.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                // TODO Auto-generated method stub
                Object item = parent.getItemAtPosition(position);


                if (item != null && position != 0) {
                    MostrarInfoProducto(position);
                    idActivo = catalogo.ObtenerID(position);
                    nombreActivo = catalogo.ObtenerNombre(position);
                    Descrip = catalogo.ObtenerDescrip(position);
                }

            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }


        });
        //------------------------------------------------------------------------------------------------------------------------//

        ComboBox2.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                // TODO Auto-generated method stub
                Object item = parent.getItemAtPosition(position);


                if (item != null && position != 0) {
                    Tiempo = item.toString();
                }

            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }


        });



    }

    public void MostrarInfoProducto(int position){
        txtUserName.setText(catalogo.ObtenerNombre(position));
        txtDescrip.setText(catalogo.ObtenerDescrip(position));
    }


    private String getDateTime() {
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd");
        Date date = new Date();
        return dateFormat.format(date);
    }


    //************************METODO PARA COMUNICAR Y ENVIAR A ASP*********************************//
    public void Enviar() {


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
                    System.out.println(res);
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (XmlPullParserException e) {
                    e.printStackTrace();
                }

                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Toast.makeText(RentaActivity.this, res, Toast.LENGTH_LONG).show();
                        txtDescrip.setText(res);
                    }
                });
            }
        };

        nt.start();
    }
    //*********************************************************************************************//


    //---------------------HILO ASINCRONICO---------------------------//
    public class conexionTask extends AsyncTask<Void, Void, Boolean> {


        @Override
        protected Boolean doInBackground(Void... voids) {
            boolean conex;

            try {
                conex = Conexion();
                if (conex) {
                    CrearCatalogo();
                }
            }catch(IllegalStateException e){
                    System.out.println(e.getMessage());
            }

            finally {
                onContinue();
            }

            return true;
        }

        @Override
        protected void onPostExecute(final Boolean success) {
            if (success) {
                //------------------------------AGREGAR AL SPINNER------------------------------------------------------//
                ArrayAdapter <CharSequence> adapter = new ArrayAdapter <CharSequence> (RentaActivity.this, android.R.layout.simple_spinner_item);
                adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                adapter.add("Seleccionar...");
                for (int x = 1; x <= catalogo.getLongitud();x++){
                    adapter.add(catalogo.ObtenerID(x));
                }
                ComboBox1.setAdapter(adapter);
                //------------------------------------------------------------------------------------------------------//
                finish();
            } else {
                d = null;
                if(conec==false){
                    Toast.makeText(RentaActivity.this,"¡Hubo un problema de Conexión!",Toast.LENGTH_SHORT).show();
                }

            }
        }


        public void onContinue() {
            //if(conec == true){
               /* if (getRes().equalsIgnoreCase("true")) {
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
            }else{*/
                /*if(isElfalso()){
                    try{
                        //EsFalso();
                    }catch (Exception e){
                        System.out.println(e.getMessage()+"   "+e.getLocalizedMessage());
                    }
                }*/
        }




    public boolean Conexion() {
        RequestBody formBody = new FormEncodingBuilder()
                .add("parametro", "parametro")
                .build();
        String r = "";
        setRespuestaFlask(getStr("Catalogo", formBody));
        if (conec) {
            return true;
        } else {
            return false;
        }
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
            setRespuestaFlask("");
            conec = false;
            System.out.println(ex.getMessage());
            //java.util.logging.Logger.getLogger(edd.proyecto1_android.MainActivity.class.getName()).log(Level.SEVERE, null, ex);
            // Toast.makeText(MainActivity.this,ex.getMessage(),Toast.LENGTH_SHORT);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
            setRespuestaFlask("");
            conec = false;
            // java.util.logging.Logger.getLogger(edd.proyecto1_android.MainActivity.class.getName()).log(Level.SEVERE, null, ex);
        }
        return "";
    }

        public void CrearCatalogo(){
            String Catal[] = getRespuestaFlask().split(":");
            for(int i=0; i < Catal.length-1;i++){
                String node[] = Catal[i].split(",");
                catalogo.Add(node[0],node[1],node[2]);
            }
        }

   }




}

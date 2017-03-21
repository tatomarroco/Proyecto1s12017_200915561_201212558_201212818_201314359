package edd.proyecto1_android;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class menuPrincipalActivity extends AppCompatActivity {

    private Button btnIrRenta;
    private Button btnIrDevol;
    private Button btnCerrarSesion;
    private TextView lblMpUser;
    Session sesionactual = new Session();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu_principal);
        final Intent irALogin = new Intent(menuPrincipalActivity.this,MainActivity.class);//Moverse A Login

        sesionactual  = sesionactual.getSession();
        lblMpUser = (TextView)findViewById(R.id.lblmpuser);

        lblMpUser.setText("Hola "+ sesionactual.getUser());

        btnIrRenta = (Button) findViewById(R.id.btnMp_Rentar);
        btnIrDevol = (Button) findViewById(R.id.btnMp_RegDev);
        btnCerrarSesion = (Button) findViewById(R.id.btnMp_CloseS);
        final Intent irARentar = new Intent(menuPrincipalActivity.this,RentaActivity.class);//Moverse a Renta
        final Intent irADevoluciones = new Intent(menuPrincipalActivity.this,DevolucionesActivity.class);//Moverse a Devoluciones

        btnIrRenta.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(irARentar);
            }
        });

        btnIrDevol.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v){
                startActivity(irADevoluciones);
            }
        });


        btnCerrarSesion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(menuPrincipalActivity.this,"Cerrando Sesion de "+ sesionactual.getUser(), Toast.LENGTH_SHORT).show();
                sesionactual.setSesion(false);
                sesionactual.setUser(null);
                startActivity(irALogin);
            }
        });


    }
}

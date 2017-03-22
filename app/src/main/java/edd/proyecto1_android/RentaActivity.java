package edd.proyecto1_android;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Adapter;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

public class RentaActivity extends AppCompatActivity {

    private Spinner ComboBox1;
    private Spinner ComboBox2;
    private EditText txtUserName;
    private EditText txtDescrip;
    private Button btnRentar;
    private Button btnRegresarMp;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_renta);

        btnRentar = (Button) findViewById(R.id.btnRentar);
        btnRegresarMp = (Button)findViewById(R.id.btnRegresarMp);
        final Intent irAMp = new Intent(RentaActivity.this,menuPrincipalActivity.class);//Moverse a Renta

        ComboBox1 = (Spinner) findViewById(R.id.lactiv);
        ArrayAdapter adapter = ArrayAdapter.createFromResource(this, R.array.ListaPrueba, android.R.layout.simple_spinner_item);

        ComboBox2 = (Spinner) findViewById(R.id.ComboBox2);
        ArrayAdapter adapter2 = ArrayAdapter.createFromResource(this, R.array.ListaPrueba2, android.R.layout.simple_spinner_item);

        txtUserName = (EditText)findViewById(R.id.txtNombreUser);
        txtUserName.setEnabled(false);

        txtDescrip = (EditText)findViewById(R.id.txtDescrip);
        txtDescrip.setEnabled(false);

        btnRegresarMp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(irAMp);
            }
        });

    }
}

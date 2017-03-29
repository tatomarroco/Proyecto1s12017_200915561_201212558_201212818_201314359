from flask import Flask, request, Response
from NodoM import NodoM
from Matriz import Matriz

matriz = Matriz()

app = Flask("EDD_codigo_ejemplo")
class WebService():
    
    @app.route('/matrizAgregar',methods=['POST']) 
    def matrizAgregar(): 
        usuario = str(request.form['usuario'])
        contrasenia = str(request.form['contrasenia'])
        nombre = str(request.form['nombre'])
        empresa = str(request.form['empresa'])
        depto = str(request.form['departamento'])

        nuevoNodo = NodoM(empresa, depto, nombre, contrasenia, usuario)
        matriz.agregarCabecerasMatriz(nuevoNodo)
        if matriz.necesitaProfundidad(nuevoNodo) == True:
            matriz.agregarProfundidad(nuevoNodo)
        else:
            matriz.agregarMatriz(nuevoNodo)
        return "MARIO BROS... El nodo con los siguientes atriburos empresa: '" + str(empresa) + "' departamento: '" + str(depto) + "' nombre: '" + str(nombre) + "' fue agregado correctamente" 
    
    @app.route('/Login',methods=['POST']) #matriz Login este es el metodo para el login xDxdxDxd
    def Login(): 
        usuario = str(request.form['usuario'])
        contrasenia = str(request.form['contrasenia'])
        nombre = None
        empresa = str(request.form['empresa'])
        depto = str(request.form['departamento'])
        nuevoNodo = NodoM(empresa, depto, nombre, contrasenia, usuario)
        var = matriz.buscarUsuario(nuevoNodo)
        return str(var)
    
    if __name__ == "__main__":
        app.run(debug=True, host='192.168.43.56')    
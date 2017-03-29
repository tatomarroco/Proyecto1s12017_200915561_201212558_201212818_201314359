from flask import Flask, request, Response
from NodoM import NodoM
from Matriz import Matriz
from NodoAVL import NodoAVL
from AVL import Arbol

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
    
    @app.route('/Catalogo',methods=['POST']) #metodo que tato me pide, devolver todo el arbol de un nodo especificado
    def catalogo(): 
        valor = str(request.form['parametro'])
        datos = matriz.tato2()
        return str(datos)
    
    @app.route('/devolverArbol',methods=['POST']) #metodo que tato me pide, devolver todos los arboles
    def DevolverArbol():
        valor = str(request.form['mario'])
        datos = matriz.tato2()
        return str(datos)
    
    @app.route('/agregarAVL',methods=['POST']) #matriz Login este es el metodo para el login xDxdxDxd
    def Login1():
        usuario = str(request.form['usuario'])
        empresa = str(request.form['empresa'])
        depto = str(request.form['departamento'])
        idd = str(request.form['identificador'])
        contrasenia = str(request.form['contrasenia'])
        matriz.kelvin3(usuario, depto, empresa, idd, contrasenia) 
        valor = matriz.retornarDatos()
        return usuario + str(valor)             
        
    @app.route('/graficarAVL',methods=['POST']) #metodo para graficar un arbol de un nodo especifico
    def GraficarAVL(): 
        usuario = str(request.form['usuario'])
        empresa = str(request.form['empresa'])
        depto = str(request.form['departamento'])
        matriz.limpiarVariableGraficar()
        matriz.serviceGraficarArbol(depto, empresa, usuario)
        return "funciono Mario Bross"
        
    @app.route('/graficarMatriz',methods=['POST']) #metodo para graficar un arbol de un nodo especifico
    def GraficarMatriz():
        usuario = str(request.form['mario'])
        matriz.ArchivoMatriz()    
        
    @app.route('/mario',methods=['POST']) #metodo para graficar un arbol de un nodo especifico
    def raficarAVL(): 
        nombreActivo = str(request.form['activo'])
        descripcion = str(request.form['descripcion'])
        alfaNumerico = str(request.form['alfanumerico'])
        idd = str (request.form['identificador'])
        usuario = str(request.form['usuario'])
        empresa = str(request.form['empresa'])
        depto = str(request.form['departamento'])
        iddd = int(idd)
        variable = nombreActivo + " " + descripcion + " " + alfaNumerico + " " + " " + idd + " " + usuario + " " + empresa + " " + depto
        return variable
    
    arbol=Arbol(None,0);
    #arbol.raiz = arbol
    
    @app.route('/metodoWeb',methods=['POST'])
    def hello():
        parametro = str(request.form['dato'])
        indice=int(parametro)
        arbol.agregar(arbol,indice)
        variable = arbol.raiz.info
        return str(variable)    
    
    if __name__ == "__main__":
        app.run(debug=True, host='192.168.43.56')    
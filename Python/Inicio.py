from Matriz import Matriz
from NodoM import NodoM
from NodoAVL import NodoAVL

if __name__ == "__main__":
    print ("\n2012-12558 Julio Cesar Eduardo Flores Tubac")
    
    matriz = Matriz()
    raiz = matriz.raiz
    nwhile = 0
    while nwhile<3:
        print("\n---- MENU ----")
        print("1. Agregar")
        print("2. Mostrar Profundidad ")
        print("3. Eliminar Matriz")
        print("4. Busqueda")  
        print("5. Graficar Matriz")
        print("61. 62,63,64,65,66,67, llenar matriz")
        print("71. 72,73,74,75,76,77, llenar avl")
        print("8. Graficar arbol")  
        print("9. mostrar profundidad")
        num = input("Ingrese una opcion: ")
        if num == "1":
            empresa = str (input ("Ingrese un empresa: "))
            depto = str (input ("Ingrese un depto: "))
            nombre = str (input ("Ingrese un nombre: "))
            pas = str (input ("Ingrese un contrasenia: "))
            usuario = nombre + "1"
            print()
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)
        elif num == "2":
            empresa = str (input ("Ingrese un empresa: "))
            depto = str (input ("Ingrese un depto: "))
            nombre = "prueba"
            nuevoNodo = NodoM(empresa, depto, nombre)
            matriz.mostrarProfundidad(nuevoNodo)            
        elif num == "3":
            empresa = str (input ("Ingrese un empresa: "))
            depto = str (input ("Ingrese un depto: "))
            nombre = str (input ("Ingrese un nombre: "))
            pas = str(input ("Ingrese una contrasenia: "))
            nuevoNodo = NodoM(empresa, depto, nombre, pas)
            nodoEliminado = matriz.eliminarMatriz(nuevoNodo)
            if nodoEliminado != None:
                print("el nodo con los valores empresa: '" + str(nodoEliminado.empresa) + "' departamento: '"+ str(nodoEliminado.departamento) + "' nombre: '" + str(nodoEliminado.nombre) +"' fue eliminado")           
        elif num == "4":
            empresa = str (input ("Ingrese un empresa: "))
            depto = str (input ("Ingrese un depto: "))
            nombre = str (input ("Ingrese un nombre: "))
            pas = str(input ("Ingrese una contrasenia: "))
            nuevoNodo = NodoM(empresa, depto, nombre, pas)
            var = matriz.buscarUsuario(nuevoNodo)       
            print(str(var))            
        elif num == "5":
            print("Graficar Matriz")
            matriz.ArchivoMatriz()
        elif num == "61":
            empresa = "claro"
            depto = "otros"
            nombre = "cesar"
            pas = "123"
            usuario = "cesar1"
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)
        elif num == "62":
            empresa = "movistar"
            depto = "mercadeo"
            nombre = "sara"
            pas = "234"
            usuario = "sara1"
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo) 
        elif num == "63":
            empresa = "tigo"
            depto = "otros"
            nombre = "karla"
            pas = "345"
            usuario = "karla1"
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)        
        elif num == "64":
            empresa = "claro"
            depto = "mercadeo"
            nombre = "julio"
            pas = "456"
            usuario = "julio1"
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)        
        elif num == "65":
            empresa = "movistar"
            depto = "ventas"
            nombre = "ester"
            pas = "567"
            usuario = "ester1"
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)               
        elif num == "66":
            empresa = "movistar"
            depto = "ventas"
            nombre = "luis"
            pas = "678"
            usuario = "luis1"
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)        
        elif num == "67":
            empresa = "movistar"
            depto = "ventas"
            nombre = "tato"
            pas = "789"
            usuario = "tato1"
            nuevoNodo = NodoM(depto, empresa, nombre, pas, usuario)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)        
        elif num == "71":
            usuario = "cesar1"
            empresa = "claro"
            depto = "otros"
            contrasenia = "123"
            idd = str (input ("Ingrese un id para arbol: "))
            matriz.kelvin3(usuario, depto, empresa, idd, contrasenia)
            
            
        elif num == "72":
            usuario = "sara1"
            empresa = "movistar"
            depto = "mercadeo"
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)            
        elif num == "73":
            usuario = "karla1"
            empresa = "tigo"
            depto = "otros"
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)            
        elif num == "74":
            usuario = "julio1"
            empresa = "claro"
            depto = "mercadeo"
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)            
        elif num == "75":
            usuario = "ester1"
            empresa = "movistar"
            depto = "ventas"
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)            
        elif num == "76":
            usuario = "luis1"
            empresa = "movistar"
            depto = "ventas"
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)            
        elif num == "77":
            usuario = "tato1"
            empresa = "movistar"
            depto = "ventas"
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)
            idd = str (input ("Ingrese un id para arbol: "))
            nuevoNodo = NodoAVL(idd)
            nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
            matriz.agregarAVL1(nuevoNodo, nuevoNodoMat)            
        
        elif num == "8":
            print("Grafica")
            usuario = str (input ("Ingrese un usuario para graficar: "))
            empresa = str (input ("Ingrese una empresa para graficar: "))
            depto = str (input ("Ingrese un departametno para graficar: "))
            nuevoNodo = NodoM(depto, empresa, None, None, usuario)
            matriz.limpiarVariableGraficar()
            matriz.grabarArchivo(matriz.getRaiz(nuevoNodo))            
        elif num == "9":
            datos = matriz.tato2()
            print(datos)
  
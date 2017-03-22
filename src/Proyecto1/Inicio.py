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
        print("2. Mostrar por departamentos")
        print("3. Mostrar por Empresas")
        print("4. Mostrar Profundidad")  
        print("5. Eliminar Matriz")
        print("6. Agregrar Matriz")
        print("7. Mostrar cabeceras y laterales")
        print("8. mostrar todo el dominio y toda la letra")  
        print("9. mostrar profundidad de una letra y un dominio especifico")
        num = input("Ingrese una opcion: ")
        if num == "1":
            empresa = str (input ("Ingrese un empresa: "))
            depto = str (input ("Ingrese un depto: "))
            nombre = str (input ("Ingrese un nombre: "))
            pas = str (input ("Ingrese un contrasenia: "))
            nuevoNodo = NodoM(depto, empresa, nombre, pas, nombre)
            matriz.agregarCabecerasMatriz(nuevoNodo)
            print("Departamenos")
            matriz.mostrarCabeceraDepartamento()
            print("Empresas")
            matriz.mostrarCabeceraEmpresa()
            if matriz.necesitaProfundidad(nuevoNodo) == True:
                matriz.agregarProfundidad(nuevoNodo)
            else:
                matriz.agregarMatriz(nuevoNodo)
        elif num == "2":
            empresa = "prueba"
            depto = str (input ("Ingrese un depto: "))
            nombre = "prueba"
            nuevoNodo = NodoM(empresa, depto, nombre)
            matriz.mostrarTodoDepartamento(nuevoNodo)
        elif num == "3":
            depto = "prueba"
            empresa = str (input ("Ingrese una empresa: "))
            nombre = "prueba"
            nuevoNodo = NodoM(empresa, depto, nombre)
            matriz.mostrarTodoEmpresa(nuevoNodo)            
        elif num == "4":
            empresa = str (input ("Ingrese un empresa: "))
            depto = str (input ("Ingrese un depto: "))
            nombre = "prueba"
            nuevoNodo = NodoM(empresa, depto, nombre)
            matriz.mostrarProfundidad(nuevoNodo)
        elif num == "5":
            empresa = str (input ("Ingrese un empresa: "))
            depto = str (input ("Ingrese un depto: "))
            nombre = str (input ("Ingrese un nombre: "))
            pas = str(input ("Ingrese una contrasenia: "))
            nuevoNodo = NodoM(empresa, depto, nombre, pas)
            #nodoEliminado = matriz.eliminarMatriz(nuevoNodo)
            var = matriz.buscarUsuario(nuevoNodo)       
            print(str(var))
            #print("el nodo con los valores empresa: '" + str(nodoEliminado.empresa) + "' departamento: '"+ str(nodoEliminado.departamento) + "' nombre: '" + str(nodoEliminado.nombre) +"' fue eliminado")
        elif num == "6":
            nombre = str(input("Ingrese una nombre completo: "))
            usuario = str(input("Ingrese un usuario: "))
            contrasenia = str(input("Ingrese un contrasenia: "))
            nuevoNodo = NodoM(nombre, usuario, contrasenia)
            matriz.agregar(nuevoNodo)
        elif num == "7":
            matriz.mostrarCabecera()
            matriz.mostrarLateral()
        elif num == "8":
            dominio = str(input("Ingrese un Dominio: "))
            matriz.mostrarDominios(dominio)
            letra = str(input("Ingrese una Letra: "))
            matriz.mostrarLetras(letra)
        elif num == "9":
            dominio = str(input("Ingrese un Dominio: "))
            letra = str(input("Ingrese una Letra: "))
            matriz.mostrarProfundidad(letra, dominio)
        elif num == "10":
            nombre = str (input ("Ingrese un numero: "))
            nuevoNodo = NodoAVL(nombre)
            matriz.agregarAVL2(nuevoNodo)
        elif num == "11":
            print("PreOrden:")
            matriz.mostrarPreOrden(matriz.getRaiz())
        elif num == "12":
            print("InOrden:")
            matriz.mostrarInOrden(matriz.getRaiz())
        elif num == "13":
            print("PostOrden:")
            matriz.mostrarPostOrden(matriz.getRaiz())
        elif num == "14":
            print("Grafica")
            matriz.ArchivoMatriz()            
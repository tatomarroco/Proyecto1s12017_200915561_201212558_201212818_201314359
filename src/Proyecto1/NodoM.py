from NodoAVL import NodoAVL

class NodoM():
    def __init__ (self, empresa=None, departamento=None, nombre=None, contrasenia=None, usuario=None, arriba=None, abajo=None, derecha=None, izquierda=None, profundidad=None, nodoAVL=None):
        self.empresa = empresa
        self.departamento = departamento
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.usuario = usuario
        self.arriba = arriba
        self.abajo = abajo
        self.derecha = derecha
        self.izquierda = izquierda
        self.profundidad = profundidad
        self.raiz = None
        
    def agregarNodoAVL(self, nuevoNodo, ):
        if self.raiz == None:
            self.raiz = nuevoNodo
        elif nuevoNodo.identificador < self.raiz.identificador:
            self.raiz.izquierdo = agregarNodoAVL(nuevoNodo)
        elif nuevoNodo.identificador > self.raiz.identificador:
            self.raiz.derecho = agregarNodoAVL(nuevoNodo)
        else:
            print("nodo duplicado :( ")
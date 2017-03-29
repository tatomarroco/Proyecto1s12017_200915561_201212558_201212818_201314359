class NodoAVL():
        def __init__ (self, nombre=None, descripcion=None, nombreActivo=None, alfaNumerico=None, izquierda=None, derecha=None, padre=None):
                self.nombre = nombre
                self.descripcion = descripcion
                self.nombreActivo = nombreActivo
                self.alfaNumerico = alfaNumerico
                self.FE = 0
                self.izquierda = izquierda
                self.derecha = derecha
                self.padre = padre
                self.raiz = None
                self.encontro = None
                
        def getAVLraiz(self):
                return self.raiz
        
        def getAVLencontrado(self):
                return self.encontro
        
        def setAVLraiz(self, nuevoNodo):
                self.raiz = nuevoNodo
        
        def setAVLencontrado(self, valor):
                self.encontro = valor
                
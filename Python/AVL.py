class Arbol:

    def __init__(self,arbol,dato):
        self.derecha=None
        self.izquierda=None
        self.fe=0
        self.altura=0
        self.info=dato
        self.raiz=None
    def agregar(self,arbol,dato):
        if arbol.info < dato:
            self.agregaIzquierda(arbol,dato)
        elif arbol.info > dato:
            self.agregaDerecha(arbol,dato)

    def agregaIzquierda(self,arbol,dato):
        if arbol.izquierda==None:
            arbol.izquierda=Arbol(arbol,dato)
        else:
            self.agregar(arbol.izquierda,dato)

    def agregaDerecha(self,arbol,dato):
        if arbol.derecha==None:
            arbol.derecha=Arbol(arbol,dato)
        else:
            self.agregar(arbol.derecha,dato)

    def inOrIzquierda(self,arbol):
        self.InOrden(arbol.izquierda)

    def inOrDerecha(self,arbol):
        self.InOrden(arbol.derecha)

    def InOrden(self,arbol):
        if arbol.derecha!=None:
            self.inOrDerecha(arbol)

        print(arbol.info)

        if arbol.izquierda!=None:
            self.inOrIzquierda(arbol)


    def PosOrd(self,arbol):
        if arbol.derecha!=None:
            self.PosOrIzq(arbol.derecha)
            print(arbol.derecha.info)
        if arbol.izquierda!=None:
            print(arbol.izquierda.info)
            self.PosOrDer(arbol.izquierda)

    def PosOrIzq(self,arbol):
        self.PosOrd(arbol)


    def PosOrDer(self,arbol):
        self.PosOrd(arbol)









    def maximo(self,a,b):
        if a > b:
            return a
        elif b>a:
            return b
        else:
            return a




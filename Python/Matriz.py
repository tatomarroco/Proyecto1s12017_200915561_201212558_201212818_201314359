from NodoM import NodoM
from NodoAVL import NodoAVL
from logical import logical

class Matriz():
    def __init__ (self):
        self.inicio = None
        self.inicioDepartamento = None
        self.inicioEmpresa = None
        self.matrizVacia = "si"
        self.raiz = None
        #self.encontro = None
        self.digraf = "digraph G{\n"
        self.datosTato = ""
    
    def limpiarVariableGraficar(self):
        self.digraf = "digraph G{\n" 
        
    def existeDepartamento(self, nuevoNodo):
        temp = self.inicioDepartamento
        if temp != None:
            while temp != None:
                if temp.departamento == nuevoNodo.departamento:
                    return True
                temp = temp.derecha
        return False
        
    def existeEmpresa(self, nuevoNodo):
        temp = self.inicioEmpresa
        if temp != None:
            while temp != None:
                if temp.empresa == nuevoNodo.empresa:
                    return True
                temp = temp.abajo
        return False
        
    def agregarMatriz(self, nuevoNodo):
        print(":(")
        if self.matrizVacia == "no":
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo)
            nodoEmpresaTemp = self.obtenerEmpresa(nuevoNodo)
            nodoDepartamentoTemp.abajo = nuevoNodo
            nuevoNodo.arriba = nodoDepartamentoTemp
            nodoEmpresaTemp.derecha = nuevoNodo
            nuevoNodo.izquierda = nodoEmpresaTemp
            self.matrizVacia = "no"
        else:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo)
            nodoEmpresaTemp = self.obtenerEmpresa(nuevoNodo)            
            if nodoDepartamentoTemp.abajo == None:
                nodoDepartamentoTemp.abajo = nuevoNodo
                nuevoNodo.arriba = nodoDepartamentoTemp
                if nodoEmpresaTemp.derecha == None:
                    nodoEmpresaTemp.derecha = nuevoNodo
                    nuevoNodo.izquierda = nodoEmpresaTemp
                elif nodoEmpresaTemp.derecha != None:
                    departamentoNuevo = nuevoNodo.departamento
                    caracterNuevo = departamentoNuevo[0]
                    caracterNuevoASCII = ord(caracterNuevo)
                    temp1 = nodoEmpresaTemp.derecha #*************************************************
                    while temp1 != None:
                        departamento1 = temp1.departamento
                        caracter1 = departamento1[0]
                        caracter1ASCII = ord(caracter1)
                        if temp1.derecha != None:
                            temp2 = temp1.derecha
                            departamento2 = temp2.departamento
                            caracter2 = departamento2[0]
                            caracter2ASCII = ord(caracter2)
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizDepartamento(temp1, nuevoNodo)
                                break
                            elif caracterNuevoASCII > caracter1ASCII:
                                if caracterNuevoASCII < caracter2ASCII:
                                    self.agregarMedioMatrizDepartamento(temp1, nuevoNodo, temp2)
                                    break
                                else:
                                    print(":(")
                            elif caracterNuevoASCII == caracter1ASCII:
                                self.agregarMedioMatrizDepartamento(temp1, nuevoNodo, temp2)
                                break                                   
                        else:
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizDepartamento(temp1, nuevoNodo)
                                break
                            else:
                                self.agregarFinMatrizDepartamento(temp1, nuevoNodo)
                                break
                        temp1 = temp1.derecha                       
            elif nodoEmpresaTemp.derecha == None:#************************
                nodoEmpresaTemp.derecha = nuevoNodo
                nuevoNodo.izquierda = nodoEmpresaTemp
                if nodoDepartamentoTemp.abajo == None:
                    nodoDepartamentoTemp.abajo = nuevoNodo
                    nuevoNodo.arriba = nodoDepartamentoTemp
                elif nodoDepartamentoTemp.abajo != None:
                    empresaNuevo = nuevoNodo.empresa
                    caracterNuevo = empresaNuevo[0]
                    caracterNuevoASCII = ord(caracterNuevo)
                    temp1 = nodoDepartamentoTemp.abajo                    
                    while temp1 != None:
                        empresa1 = temp1.empresa
                        caracter1 = empresa1[0]
                        caracter1ASCII = ord(caracter1)
                        if temp1.abajo != None:
                            temp2 = temp1.abajo
                            empresa2 = temp2.empresa
                            caracter2 = empresa2[0]
                            caracter2ASCII = ord(caracter2)
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizEmpresa(temp1, nuevoNodo)
                                break
                            elif caracterNuevoASCII > caracter1ASCII:
                                if caracterNuevoASCII < caracter2ASCII:
                                    self.agregarMedioMatrizEmpresa(temp1, nuevoNodo, temp2)
                                    break
                            elif caracterNuevoASCII == caracter1ASCII:
                                self.agregarMedioMatrizEmpresa(temp1, nuevoNodo, temp2)
                                break                                   
                        else:
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizEmpresa(temp1, nuevoNodo)
                                break
                            else:
                                self.agregarFinMatrizEmpresa(temp1, nuevoNodo)
                                break        
                        temp1 = temp1.abajo                
            else:
                if nodoEmpresaTemp.derecha != None:
                    departamentoNuevo = nuevoNodo.departamento
                    caracterNuevo = departamentoNuevo[0]
                    caracterNuevoASCII = ord(caracterNuevo)
                    temp1 = nodoEmpresaTemp.derecha #*************************************************
                    while temp1 != None:
                        departamento1 = temp1.departamento
                        caracter1 = departamento1[0]
                        caracter1ASCII = ord(caracter1)
                        if temp1.derecha != None:
                            temp2 = temp1.derecha
                            departamento2 = temp2.departamento
                            caracter2 = departamento2[0]
                            caracter2ASCII = ord(caracter2)
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizDepartamento(temp1, nuevoNodo)
                                break
                            elif caracterNuevoASCII > caracter1ASCII:
                                if caracterNuevoASCII < caracter2ASCII:
                                    self.agregarMedioMatrizDepartamento(temp1, nuevoNodo, temp2)
                                    break
                                else:
                                    print(":(")
                            elif caracterNuevoASCII == caracter1ASCII:
                                self.agregarMedioMatrizDepartamento(temp1, nuevoNodo, temp2)
                                break                                   
                        else:
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizDepartamento(temp1, nuevoNodo)
                                break
                            else:
                                self.agregarFinMatrizDepartamento(temp1, nuevoNodo)
                                break
                        temp1 = temp1.derecha   
                if nodoDepartamentoTemp.abajo != None:
                    empresaNuevo = nuevoNodo.empresa
                    caracterNuevo = empresaNuevo[0]
                    caracterNuevoASCII = ord(caracterNuevo)
                    temp1 = nodoDepartamentoTemp.abajo                    
                    while temp1 != None:
                        empresa1 = temp1.empresa
                        caracter1 = empresa1[0]
                        caracter1ASCII = ord(caracter1)
                        if temp1.abajo != None:
                            temp2 = temp1.abajo
                            empresa2 = temp2.empresa
                            caracter2 = empresa2[0]
                            caracter2ASCII = ord(caracter2)
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizEmpresa(nuevoNodo)
                                break
                            elif caracterNuevoASCII > caracter1ASCII:
                                if caracterNuevoASCII < caracter2ASCII:
                                    self.agregarMedioMatrizEmpresa(temp1, nuevoNodo, temp2)
                                    break
                            elif caracterNuevoASCII == caracter1ASCII:
                                self.agregarMedioMatrizEmpresa(temp1, nuevoNodo, temp2)
                                break                                   
                        else:
                            if caracterNuevoASCII < caracter1ASCII:
                                self.agregarInicioMatrizEmpresa(temp1, nuevoNodo)
                                break
                            else:
                                self.agregarFinMatrizEmpresa(temp1, nuevoNodo)
                                break        
                        temp1 = temp1.abajo                    
               
    def agregarCabecerasMatriz(self, nuevoNodo):
        if self.existeDepartamento(nuevoNodo) == False:
            if self.inicioDepartamento == None:
                nuevoNodo1 = NodoM("", str(nuevoNodo.departamento))
                self.inicioDepartamento = nuevoNodo1
            elif self.inicioDepartamento != None:
                temp1 = self.inicioDepartamento
                departamentoNuevo = nuevoNodo.departamento
                caracterNuevo = departamentoNuevo[0]
                caracterNuevoASCII = ord(caracterNuevo)               
                while temp1 != None:
                    departamento1 = temp1.departamento
                    caracter1 = departamento1[0]
                    caracter1ASCII = ord(caracter1)
                    if temp1.derecha != None:
                        temp2 = temp1.derecha
                        departamento2 = temp2.departamento
                        caracter2 = departamento2[0]
                        caracter2ASCII = ord(caracter2)
                        if caracterNuevoASCII < caracter1ASCII:
                            self.agregarInicioDepartamento(nuevoNodo)
                            break
                        elif caracterNuevoASCII > caracter1ASCII:
                            if caracterNuevoASCII < caracter2ASCII:
                                self.agregarMedioDepartamento(temp1, nuevoNodo, temp2)
                                break
                            else:
                                print(":(")
                        #elif caracterNuevoASCII > caracter1ASCII:
                        elif caracterNuevoASCII == caracter1ASCII:
                            self.agregarMedioDepartamento(temp1, nuevoNodo, temp2)
                            break                                   
                    else:
                        if caracterNuevoASCII < caracter1ASCII:
                            self.agregarInicioDepartamento(nuevoNodo)
                            break
                        else:
                            self.agregarFinDepartamento(nuevoNodo)
                            break
                    temp1 = temp1.derecha

        if self.existeEmpresa(nuevoNodo) == False:
            if self.inicioEmpresa == None:
                nuevoNodo1 = NodoM(str(nuevoNodo.empresa), "")
                self.inicioEmpresa = nuevoNodo1
            elif self.inicioEmpresa != None:
                temp1 = self.inicioEmpresa
                empresaNuevo = nuevoNodo.empresa
                caracterNuevo = empresaNuevo[0]
                caracterNuevoASCII = ord(caracterNuevo)               
                while temp1 != None:
                    empresa1 = temp1.empresa
                    caracter1 = empresa1[0]
                    caracter1ASCII = ord(caracter1)
                    if temp1.abajo != None:
                        temp2 = temp1.abajo
                        empresa2 = temp2.empresa
                        caracter2 = empresa2[0]
                        caracter2ASCII = ord(caracter2)
                        if caracterNuevoASCII < caracter1ASCII:
                            self.agregarInicioEmpresa(nuevoNodo)
                            break
                        elif caracterNuevoASCII > caracter1ASCII:
                            if caracterNuevoASCII < caracter2ASCII:
                                self.agregarMedioEmpresa(temp1, nuevoNodo, temp2)
                                break
                        elif caracterNuevoASCII == caracter1ASCII:
                            self.agregarMedioEmpresa(temp1, nuevoNodo, temp2)
                            break                                   
                    else:
                        if caracterNuevoASCII < caracter1ASCII:
                            self.agregarInicioEmpresa(nuevoNodo)
                            break
                        else:
                            self.agregarFinEmpresa(nuevoNodo)
                            break        
                    temp1 = temp1.abajo
              
    def obtenerDepartamento(self, nuevoNodo):
        temp = self.inicioDepartamento
        while temp != None:
            if temp.departamento == nuevoNodo.departamento:
                return temp
            temp = temp.derecha
    
    def obtenerEmpresa(self, nuevoNodo):
        temp = self.inicioEmpresa
        while temp != None:
            if temp.empresa == nuevoNodo.empresa:
                return temp
            temp = temp.abajo
            
    def agregarInicioDepartamento(self, nuevoNodo):
        nuevoNodo1 = NodoM("", str(nuevoNodo.departamento))
        nuevoNodo1.derecha = self.inicioDepartamento
        self.inicioDepartamento.izquierda = nuevoNodo1
        self.inicioDepartamento = nuevoNodo1
        
    def agregarFinDepartamento(self, nuevoNodo):
        nuevoNodo1 = NodoM("", str(nuevoNodo.departamento))
        temp = self.inicioDepartamento
        while temp != None:
            aux = temp
            temp = temp.derecha
        aux.derecha = nuevoNodo1
        nuevoNodo1.izquierda = aux
    
    def agregarMedioDepartamento(self, nodo1, nuevoNodo, nodo2):
        nuevoNodo1 = NodoM("", str(nuevoNodo.departamento))
        nodo1.derecha = nuevoNodo1
        nuevoNodo1.izquierda = nodo1
        nuevoNodo1.derecha = nodo2
        nodo2.izquierda = nuevoNodo1
        
    def agregarInicioEmpresa(self, nuevoNodo):
        nuevoNodo1 = NodoM(str(nuevoNodo.empresa), "")
        nuevoNodo1.abajo = self.inicioEmpresa
        self.inicioEmpresa.arriba = nuevoNodo1
        self.inicioEmpresa = nuevoNodo1
        
    def agregarFinEmpresa(self, nuevoNodo):
        nuevoNodo1 = NodoM(str(nuevoNodo.empresa), "")
        temp = self.inicioEmpresa
        while temp != None:
            aux = temp
            temp = temp.abajo
        aux.abajo = nuevoNodo1
        nuevoNodo1.arriba = aux
    
    def agregarMedioEmpresa(self, nodo1, nuevoNodo, nodo2):
        nuevoNodo1 = NodoM(str(nuevoNodo.empresa), "")
        nodo1.abajo = nuevoNodo1
        nuevoNodo1.arriba = nodo1
        nuevoNodo1.abajo = nodo2
        nodo2.arriba = nuevoNodo1
        
    def mostrarCabeceraDepartamento(self):
        if self.inicioDepartamento != None:
            temp = self.inicioDepartamento
            while temp != None:
                print("->" + str(temp.departamento))
                temp = temp.derecha
    
    def mostrarCabeceraEmpresa(self):
        if self.inicioEmpresa != None:
            temp = self.inicioEmpresa
            while temp != None:
                print("->" + str(temp.empresa))
                temp = temp.abajo
           
    def agregarInicioMatrizDepartamento(self, nodoExistente, nuevoNodo):
        cabecera = nodoExistente.izquierda
        cabecera.derecha = nuevoNodo
        nuevoNodo.izquierda = cabecera
        nuevoNodo.derecha = nodoExistente
        nodoExistente.izquierda = nuevoNodo
        
    def agregarFinMatrizDepartamento(self, nodoExistente, nuevoNodo):
        nodoExistente.derecha = nuevoNodo
        nuevoNodo.izquierda = nodoExistente
        
    def agregarMedioMatrizDepartamento(self, nodo1, nuevoNodo, nodo2):
        nodo1.derecha = nuevoNodo
        nuevoNodo.izquierda = nodo1
        nuevoNodo.derecha = nodo2
        nodo2.izquierda = nuevoNodo        
    
    def agregarInicioMatrizEmpresa(self, nodoExistente, nuevoNodo):
        cabecera = nodoExistente.arriba
        cabecera.abajo = nuevoNodo
        nuevoNodo.arriba = cabecera
        nuevoNodo.abajo = nodoExistente
        nodoExistente.arriba = nuevoNodo
        
    def agregarMedioMatrizEmpresa(self, nodo1, nuevoNodo, nodo2):
        nodo1.abajo = nuevoNodo
        nuevoNodo.arriba = nodo1
        nuevoNodo.abajo = nodo2
        nodo2.arriba = nuevoNodo
        
    def agregarFinMatrizEmpresa(self, nodoExistente, nuevoNodo):
        nodoExistente.abajo = nuevoNodo
        nuevoNodo.arriba = nodoExistente
    
    def mostrarTodoDepartamento(self, nuevoNodo):
        if self.inicioDepartamento != None:
            temp = self.inicioDepartamento
            while temp != None:
                if temp.departamento == nuevoNodo.departamento:
                    temp2 = temp.abajo
                    while temp2 != None:
                        print("empresa: " + str(temp2.empresa) + " departamento: " + str(temp2.departamento) + " nombre: " + str(temp2.nombre))
                        temp2 = temp2.abajo       
                temp = temp.derecha
                
    def mostrarTodoEmpresa(self, nuevoNodo):
        temp = self.inicioEmpresa
        while temp != None:
            if temp.empresa == nuevoNodo.empresa:
                temp2 = temp.derecha
                while temp2 != None:
                    print("empresa: " + str(temp2.empresa) + " departamento: " + str(temp2.departamento) + " nombre: " + str(temp2.nombre))
                    temp2 = temp2.derecha
            temp = temp.abajo
    
    def agregarProfundidad(self, nuevoNodo):
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        temp2 = temp1
                        while temp2 != None:
                            aux = temp2
                            temp2 = temp2.profundidad
                        aux.profundidad = nuevoNodo
                    temp1 = temp1.abajo
                    
    def necesitaProfundidad(self, nuevoNodo):
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        return True
                    temp1 = temp1.abajo
        return False
    
    def mostrarProfundidad(self, nuevoNodo):
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        temp2 = temp1
                        while temp2 != None:
                            print("empresa: " + str(temp2.empresa) + " departamento: " + str(temp2.departamento) + " nombre: " + str(temp2.nombre))
                            temp2 = temp2.profundidad
                    temp1 = temp1.abajo
                    
    def eliminarMatriz(self, nuevoNodo):
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        temp2 = temp1
                        if temp2.nombre == nuevoNodo.nombre:
                            if temp2.profundidad != None:
                                tempNuevo = temp2.profundidad
                                tempArriba = temp2.arriba
                                tempAbajo = temp2.abajo
                                tempDerecha = temp2.derecha
                                tempIzquierda = temp2.izquierda
                                
                                tempNuevo.arriba = temp2.arriba
                                tempArriba.abajo = tempNuevo
                                tempNuevo.izquierda = temp2.izquierda
                                tempIzquierda.derecha = tempNuevo
                                if tempDerecha != None:
                                    tempNuevo.derecha = temp2.derecha
                                    tempDerecha.izquierda = tempNuevo
                                if tempAbajo != None:
                                    tempNuevo.abajo = temp2.abajo
                                    tempAbajo.arriba = tempNuevo
                                return temp2
                            else:
                                tempArriba = temp2.arriba
                                tempAbajo = temp2.abajo
                                tempDerecha = temp2.derecha
                                tempIzquierda = temp2.izquierda
                                
                                tempArriba.abajo = temp2.abajo
                                tempIzquierda.derecha = temp2.derecha
                                
                                if tempAbajo != None:
                                    tempAbajo.arriba = temp2.arriba
                                if tempDerecha != None:
                                    tempDerecha.izquierda = temp2.izquierda
                        else:
                            while temp2.profundidad != None:
                                temp3 = temp2.profundidad
                                if temp3.nombre == nuevoNodo.nombre:
                                    temp2.profundidad = temp3.profundidad
                                    return temp3
                                temp2 = temp2.profundidad
                    temp1 = temp1.abajo
                    
    def buscarUsuario(self, nuevoNodo):
        busqueda = False
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        if temp1.profundidad != None:
                            temp2 = temp1
                            while temp2 != None:
                                if temp2.usuario == nuevoNodo.usuario:
                                    if temp2.contrasenia == nuevoNodo.contrasenia:
                                        busqueda = True 
                                temp2 = temp2.profundidad
                        else:
                            if temp1.usuario == nuevoNodo.usuario:
                                if temp1.contrasenia == nuevoNodo.contrasenia:
                                    busqueda = True
                    temp1 = temp1.abajo
        return busqueda
    
    def buscarUsuario2(self, nuevoNodo):
        #busqueda = None
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        if temp1.profundidad != None:
                            temp2 = temp1
                            while temp2 != None:
                                if temp2.usuario == nuevoNodo.usuario:
                                    if temp2.contrasenia == nuevoNodo.contrasenia:
                                        return temp2 
                                temp2 = temp2.profundidad
                        else:
                            if temp1.usuario == nuevoNodo.usuario:
                                if temp1.contrasenia == nuevoNodo.contrasenia:
                                    return temp1
                    temp1 = temp1.abajo
        #return busqueda    
    
    def buscarUsuarioParaAVL(self, nuevoNodo):
        busqueda = None
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        if temp1.profundidad != None:
                            temp2 = temp1
                            while temp2 != None:
                                if temp2.usuario == nuevoNodo.usuario:
                                    busqueda = temp2
                                temp2 = temp2.profundidad
                        else:
                            if temp1.usuario == nuevoNodo.usuario:
                                busqueda = temp1
                    temp1 = temp1.abajo
        return busqueda
    
    def agregarAVL2(self, nuevoNodo):
        if self.raiz == None:
            self.raiz = nuevoNodo
        else:
            temp = self.raiz
            padre = None
            while temp != None:
                padre = temp
                if int(nuevoNodo.nombre) > int(temp.nombre):
                    temp = temp.derecha
                elif int(nuevoNodo.nombre) < int(temp.nombre):
                    temp = temp.izquierda
                else:
                    break
            if int(nuevoNodo.nombre) > int(padre.nombre):
                padre.derecha = nuevoNodo
            elif int(nuevoNodo.nombre) < int(padre.nombre):
                padre.izquierda = nuevoNodo
            else:
                print("valor repetido")
    
    def getRaiz(self, nuevoNodo):
        nodoMatriz = self.obtenerNodoMatriz(nuevoNodo)
        if nodoMatriz != None:
            if nodoMatriz.nodoAvl.getAVLraiz() != None:
                return nodoMatriz.nodoAvl.getAVLraiz()
    
    def mostrarPreOrden(self, nuevoNodo):
        if nuevoNodo != None:
            print(str(nuevoNodo.nombre))
            self.mostrarPreOrden(nuevoNodo.izquierda)
            self.mostrarPreOrden(nuevoNodo.derecha)
            
    def mostrarInOrden(self, nuevoNodo):
        if nuevoNodo != None:  
            self.mostrarInOrden(nuevoNodo.izquierda)
            print(str(nuevoNodo.nombre))
            self.mostrarInOrden(nuevoNodo.derecha)
            
    def mostrarPostOrden(self, nuevoNodo):
        if nuevoNodo != None:  
            self.mostrarPostOrden(nuevoNodo.izquierda)
            self.mostrarPostOrden(nuevoNodo.derecha)
            print(str(nuevoNodo.nombre))
            
    def ArchivoMatriz(self):
        texto="digraph G{"+"\n"+"rankdir=UD; \n"+"node [shape=box];"+"\n"
        texto+="{ \n rank=min; \n"
        texto+="m[label=""Matriz""]; \n"
        outfile = open("C:/archivo.txt", 'w')
        temp=self.inicioDepartamento
        while temp!=None:
            ident=""
            for letra in temp.departamento:
                ident+=str(ord(letra))
            texto+="x"+str(ident)+'[label="'+str(temp.departamento)+'"]; \n'
            temp=temp.derecha
        texto+="} \n"
    
        temp2=self.inicioEmpresa
        while temp2.abajo!=None:
            texto+="{ \n rank=same; \n"
            local=""
            for letra in temp2.empresa:
                local+=str(ord(letra))
            texto+="f"+local+'[label="'+str(temp2.empresa)+'"]; \n'
            if temp2.derecha!=None:
                temp21=temp2.derecha
                while temp21!=None:
                    contra=""
                    for letra in temp21.contrasenia:
                        contra+=str(ord(letra))
                    texto+="n"+str(contra)+'[label="'+str(temp21.usuario)+'"]; \n'
                    temp21=temp21.derecha
            temp2=temp2.abajo
            texto+="} \n"
    
        texto+="{ \n rank=max; \n"
        maximo=""
        for letra in temp2.empresa:
            maximo+=str(ord(letra))
        texto+="f"+maximo+'[label="'+str(temp2.empresa)+'"]; \n'
        if temp2.derecha!=None:
            temp21=temp2.derecha
            while temp21!=None:
                contra=""
                for letra in temp21.contrasenia:
                    contra+=str(ord(letra))
                texto+="n"+str(contra)+'[label="'+str(temp21.usuario)+'"]; \n'
                temp21=temp21.derecha
        texto+="} \n"
    
        temp3=self.inicioDepartamento
        while temp3.derecha!=None:
            concat=""
            concat2=""
            for letra in temp3.departamento:
                concat+=str(ord(letra))
            for letra2 in temp3.derecha.departamento:
                concat2+=str(ord(letra2))
            texto+="x"+str(concat)+" -> "+"x"+str(concat2)+"; \n"
            temp3=temp3.derecha
    
        temp4=self.inicioEmpresa
        while temp4.abajo!=None:
            emp1=""
            emp2=""
            for letra in temp4.empresa:
                emp1+=str(ord(letra))
            for letra2 in temp4.abajo.empresa:
                emp2+=str(ord(letra2))
    
            texto+="f"+emp1+" -> "+"f"+emp2+"[rankdir=UD]; \n"
            temp4=temp4.abajo
    
        temp5=self.inicioDepartamento
        while temp5!=None:
            if temp5.abajo!=None:
                cadena1=""
                cadena2=""
                for letra in temp5.departamento:
                    cadena1+=str(ord(letra))
                for letra1 in temp5.abajo.contrasenia:
                    cadena2+=str(ord(letra1))
                texto+="x"+str(cadena1)+" -> "+"n"+str(cadena2)+"; \n"
                aux=temp5.abajo
                while aux.abajo!=None:
                    text1=""
                    text2=""
                    for letra in aux.contrasenia:
                        text1+=str(ord(letra))
                    for letra2 in aux.abajo.contrasenia:
                        text2+=str(ord(letra2))
                    texto+="n"+str(text1)+" -> "+"n"+str(text2)+"; \n"
    
                    aux=aux.abajo
    
                    text3=""
                    text4=""
                    for letra in aux.contrasenia:
                        text3+=str(ord(letra))
                    for letra2 in aux.arriba.contrasenia:
                        text4+=str(ord(letra2))
                    texto+="n"+str(text3)+" -> "+"n"+str(text4)+"; \n"
            temp5=temp5.derecha
    
        temp6=self.inicioEmpresa
        while temp6!=None:
            if temp6.derecha!=None:
                cadena1=""
                cadena2=""
                for letra in temp6.empresa:
                    cadena1+=str(ord(letra))
                for letra2 in temp6.derecha.contrasenia:
                    cadena2+=str(ord(letra2))
                texto+="f"+cadena1+" -> "+"n"+str(cadena2)+"[constraint=false]; \n"
    
                temp61=temp6.derecha
                while temp61.derecha!=None:
                    text1=""
                    text2=""
                    for letra in temp61.contrasenia:
                        text1+=str(ord(letra))
                    for letra2 in temp61.derecha.contrasenia:
                        text2+=str(ord(letra2))
                    texto+="n"+str(text1)+" -> "+"n"+str(text2)+"[constraint=false]; \n"
    
                    temp61=temp61.derecha
    
                    text3=""
                    text4=""
                    for letra in temp61.contrasenia:
                        text3+=str(ord(letra))
                    for letra2 in temp61.izquierda.contrasenia:
                        text4+=str(ord(letra2))
                    texto+="n"+str(text3)+" -> "+"n"+str(text4)+"[constraint=false]; \n"
    
            temp6=temp6.abajo
    
        cadena1=""
        cadena2=""
        for letra in self.inicioDepartamento.departamento:
            cadena1+=str(ord(letra))
        for letra2 in self.inicioEmpresa.empresa:
            cadena2+=str(ord(letra2))
        texto+="m ->"+"x"+str(cadena1)+"; \n"
        texto+="m ->"+"f"+str(cadena2)+"; \n"
        texto+="}"
        outfile.write(texto)
        outfile.close()
        
    def rotacionID(self, nodo, nodo1):
        nodo2 = nodo1.derecha
        nodo1.derecha = nodo2.izquierda
        nodo2.izquierda = nodo1
        nodo.izquierda = nodo2.derecha
        nodo2.derecha = nodo
        #nodo = nodo2
        
        
        if nodo2.FE == 1:
            nodo1.FE = -1
        else:
            nodo1.FE = 0
        if nodo2.FE == -1:
            nodo.FE = 1
        else:
            nodo.FE = 0
        nodo2.FE = 0
        return nodo2
    
    def rotacionII(self, nodo, nodo1):
        nodo.izquierda = nodo1.derecha
        nodo1.derecha = nodo
        if nodo1.FE == -1:
            nodo.FE = 0
            nodo1.FE = 0
        else:
            nodo.FE = -1
            nodo1.FE = 1
        return nodo1
    
    def rotacionDD(self, nodo, nodo1):
        nodo.derecha = nodo1.izquierda
        nodo1.izquierda = nodo
        if nodo1.FE == 1:
            nodo.FE = 0
            nodo1.FE = 0
        else:
            nodo.FE = 1
            nodo1.FE = -1
        return nodo1
    
    def rotacionDI(self, nodo, nodo1):
        nodo2 = nodo1.izquierda
        nodo1.izquierda = nodo2.derecha
        nodo2.derecha = nodo1
        nodo.derecha = nodo2.izquierda
        nodo2.izquierda = nodo
          
        if nodo2.FE == 1:
            nodo.FE = -1
        else:
            nodo.FE = 0
        if nodo2.FE == -1:
            nodo1.FE = 1
        else:
            nodo1.FE = 0
        nodo2.FE = 0
        return nodo2
    
    def obtenerNodoMatriz(self, nuevoNodo):
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo  
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        temp2 = temp1
                        if temp2.usuario == nuevoNodo.usuario:
                            #retornar este nodo osea temp2
                            return temp2
                        else:
                            while temp2.profundidad != None:
                                temp3 = temp2.profundidad
                                if temp3.usuario == nuevoNodo.usuario:
                                    return temp3
                                temp2 = temp2.profundidad
                    temp1 = temp1.abajo                
        #nodoMatrizTemp = NodoM()
        #nodoAvl = nodoMatriz.retornarNodoAVL()
    
    def KelvinObtenerNodoMatriz(self, nuevoNodo):
        busqueda = None
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        if temp1.profundidad != None:
                            temp2 = temp1
                            while temp2 != None:
                                if temp2.usuario == nuevoNodo.usuario:
                                    busqueda = temp2 
                                temp2 = temp2.profundidad
                        else:
                            if temp1.usuario == nuevoNodo.usuario:
                                busqueda = temp1
                    temp1 = temp1.abajo
        return busqueda        
    
    def agregarAVL1(self, nuevoNodo, nodoMtemp): #nodo avl y nodo de matriz
        temp = self.retorarAVL(nuevoNodo, nodoMtemp) #temp = 
        #nodoMtemp = self.obtenerNodoMatriz(nodoMatriz)
        if temp == None:
            h = logical(False)
            nodoMtemp.nodoAvl.setAVLraiz(self.agregarAVL(nodoMtemp.nodoAvl.getAVLraiz(), nuevoNodo, h))
            #self.raiz = self.agregarAVL(self.raiz, nuevoNodo, h)
            print("nodo agregado correctamente")
        else:
            print("ya existe")
            
    def agregarAVL1BACKUP(self, nuevoNodo, nodoMatriz): #nodo avl y nodo de matriz
        temp = self.retorarAVLBACKUP(nuevoNodo, nodoMatriz) #temp = 
        nodoMtemp = self.obtenerNodoMatriz(nodoMatriz)
        if temp == None:
            h = logical(False)
            nodoMtemp.nodoAvl.setAVLraiz(self.agregarAVL(nodoMtemp.nodoAvl.getAVLraiz(), nuevoNodo, h))
            #self.raiz = self.agregarAVL(self.raiz, nuevoNodo, h)
            print("nodo agregado correctamente")
        else:
            print("ya existe")    
            
    def agregarAVL(self, raiz, nuevoNodo, h):
        if raiz == None:
            raiz = nuevoNodo
            self.datosTato = self.datosTato + " probando1 " + str(nuevoNodo.nombre) + "-"
            h.setLogical(True)
        elif int(nuevoNodo.nombre) < int(raiz.nombre):
            nodoIz = self.agregarAVL(raiz.izquierda, nuevoNodo, h)
            raiz.izquierda = nodoIz
            if h.getLogical() == True:
                op = raiz.FE
                if op == 1:
                    raiz.FE = 0
                    h.setLogical(False)
                elif op == 0:
                    raiz.FE = -1
                elif op == -1:
                    nodo1 = raiz.izquierda
                    if nodo1.FE == -1:
                        raiz = self.rotacionII(raiz, nodo1)
                    else:
                        raiz = self.rotacionID(raiz, nodo1)
                    h.setLogical(False)
        elif int(nuevoNodo.nombre) > int(raiz.nombre):
            nodoDr = self.agregarAVL(raiz.derecha, nuevoNodo, h)
            raiz.derecha = nodoDr
            if h.getLogical() == True:
                op = raiz.FE
                if op == 1:
                    nodo1 = raiz.derecha
                    if nodo1.FE == 1:
                        raiz = self.rotacionDD(raiz, nodo1)
                    else:
                        raiz = self.rotacionDI(raiz, nodo1)
                    h.setLogical(False)
                elif op == 0:
                    raiz.FE = 1
                elif op == -1:
                    raiz.FE = 0
                    h.setLogical(False)
        return raiz             
                        
        
    def retorarAVL(self, nuevoNodo, nuevoNodoM): # nodo avl y nodo matriz
        #nodoMtemp = self.obtenerNodoMatriz(nuevoNodoM) # nodoMtemp = nodo de la matriz, osea que lo encontro ESTO YA NO
        nuevoNodoM.nodoAvl.setAVLencontrado(None) # nodoMtemp , nodo avl, le doy valor NONE en encontrado ESTO YA NO
        self.buscarAVL(nuevoNodoM.nodoAvl.getAVLraiz(), nuevoNodo, nuevoNodoM)
        return nuevoNodoM.nodoAvl.getAVLencontrado()
    
    def retorarAVLBACKUP(self, nuevoNodo, nuevoNodoM): # nodo avl y nodo matriz
        nodoMtemp = self.obtenerNodoMatriz(nuevoNodoM) # nodoMtemp = nodo de la matriz, osea que lo encontro ESTO YA NO
        nodoMtemp.nodoAvl.setAVLencontrado(None) # nodoMtemp , nodo avl, le doy valor NONE en encontrado ESTO YA NO
        self.buscarAVL(nodoMtemp.nodoAvl.getAVLraiz(), nuevoNodo, nodoMtemp)
        return nodoMtemp.nodoAvl.getAVLencontrado()    
     
    def buscarAVL(self, raiz, nuevoNodo, nodoMat):  # raiz, nodo avl y nodo Matriz
        if raiz != None:
            if nuevoNodo.nombre == raiz.nombre:
                nodoMat.nodoAvl.setAVLencontrado(raiz)
                #self.encontro = raiz
            else:
                self.buscarAVL(raiz.izquierda, nuevoNodo, nodoMat)
                self.buscarAVL(raiz.derecha, nuevoNodo, nodoMat)
        
    
    def graficarPreOrden(self, nuevoNodo):
        if nuevoNodo != None:
            self.digraf += "nodo_" + str(nuevoNodo.nombre) + " [label=" +str(nuevoNodo.nombre)+"]\n"
            if nuevoNodo.izquierda != None:
                self.digraf += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.izquierda.nombre) + "\n"
                self.graficarPreOrden(nuevoNodo.izquierda)
            else:
                pass
            if nuevoNodo.derecha != None:
                self.digraf += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.derecha.nombre) + "\n"
                self.graficarPreOrden(nuevoNodo.derecha)                   
            else:
                pass
        else:
            pass
           
        
    def grabarArchivo(self, nuevoNodo):
        archivo = open("C:\\Users\\Lauro Tubac\\Desktop\\arbol.txt", 'w')
        self.graficarPreOrden(nuevoNodo)
        self.digraf += "\n}"
        archivo.write(self.digraf)
        archivo.close()   
        
    def tatoPreOrden(self, nuevoNodo):
        if nuevoNodo != None:
            self.datosTato += str(nuevoNodo.nombre) + "," + str(nuevoNodo.nombreActivo) + "," +  str(nuevoNodo.descripcion) + ":\n"
            if nuevoNodo.izquierda != None:
                #self.datosTato += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.izquierda.nombre) + "\n"
                self.tatoPreOrden(nuevoNodo.izquierda)
            else:
                pass
            if nuevoNodo.derecha != None:
                #self.datosTato += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.derecha.nombre) + "\n"
                self.tatoPreOrden(nuevoNodo.derecha)                   
            else:
                pass
        else:
            pass        
        
    def tato(self):
        if self.inicioDepartamento.abajo != None:
            temp1 = self.inicioDepartamento.abajo
            while temp1 != None:
                tempRaiz1 = self.getRaiz(temp1)
                self.tatoPreOrden(tempRaiz1)
                if temp1.profundidad != None:
                    temp2 = temp1.profundidad
                    while temp2 != None:
                        tempRaiz2 = self.getRaiz(temp2)
                        self.tatoPreOrden(tempRaiz2)
                        temp2 = temp2.profundidad
                temp1 = temp1.abajo
            if self.inicioDepartamento.derecha != None:    
                temp3 = self.inicioDepartamento.derecha
                if temp3.abajo != None:
                    temp3 = temp3.abajo
                    while temp3 != None:
                        tempRaiz3 = self.getRaiz(temp3)
                        self.tatoPreOrden(tempRaiz3)
                        if temp3.profundidad != None:
                            temp4 = temp3.profundidad
                            while temp4 != None:
                                tempRaiz4 = self.getRaiz(temp4)
                                self.tatoPreOrden(tempRaiz4)
                                temp4 = temp4.profundidad
                        temp3 = temp3.abajo
        return self.datosTato
    
    def tato2(self): #devuelve todos los arboles que existen
        if self.inicioDepartamento != None:
            tempPrincipal = self.inicioDepartamento
            while tempPrincipal != None:
                if tempPrincipal.abajo != None:
                    temp1 = tempPrincipal.abajo
                    while temp1 != None:
                        tempRaiz1 = self.getRaiz(temp1)
                        self.tatoPreOrden(tempRaiz1)
                        if temp1.profundidad != None:
                            temp2 = temp1.profundidad
                            while temp2 != None:
                                tempRaiz2 = self.getRaiz(temp2)
                                self.tatoPreOrden(tempRaiz2)
                                temp2 = temp2.profundidad
                        temp1 = temp1.abajo
                tempPrincipal = tempPrincipal.derecha
        return self.datosTato      
    
    def buscarParaAVL(self, nuevoNodo, nuevoNodoAvl):
        #busqueda = None
        if self.existeDepartamento(nuevoNodo) == True:
            nodoDepartamentoTemp = self.obtenerDepartamento(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoDepartamentoTemp.abajo != None:
                temp1 = nodoDepartamentoTemp.abajo
                while temp1 != None:
                    if temp1.empresa == nuevoNodo.empresa:
                        if temp1.profundidad != None:
                            temp2 = temp1
                            while temp2 != None:
                                if temp2.usuario == nuevoNodo.usuario:
                                    if temp2.contrasenia == nuevoNodo.contrasenia:  #encontro el nodo de la matriz 
                                        self.agregarAVL1(nuevoNodoAvl, temp2)
                                        #busqueda = temp2
                                temp2 = temp2.profundidad
                        else:
                            if temp1.usuario == nuevoNodo.usuario:
                                if temp1.contrasenia == nuevoNodo.contrasenia:  #encontro el nodo de la matriz 
                                    self.agregarAVL1(nuevoNodoAvl, temp1)
                                    #busqueda = temp1
                    temp1 = temp1.abajo
        #return busqueda
    
    def kelvin2(self, usuario, depto, empresa, idd):
        nuevoNodo = NodoAVL(idd)
        nuevoNodoMat = NodoM(depto, empresa, None, None, usuario)
        self.agregarAVL1BACKUP(nuevoNodo, nuevoNodoMat) 
        
    def kelvin3(self, usuario, depto, empresa, idd, contrasenia):
        nuevoNodoAvl = NodoAVL(idd)
        nuevoNodoMat = NodoM(depto, empresa, None, contrasenia, usuario)
        self.buscarParaAVL(nuevoNodoMat, nuevoNodoAvl)
        #self.agregarAVL1(nuevoNodo, nuevoNodoMat)
        
    def serviceGraficarArbol(self, depto, empresa, usuario):
        nuevoNodo = NodoM(depto, empresa, None, None, usuario)
        self.limpiarVariableGraficar()
        self.grabarArchivo(self.getRaiz(nuevoNodo))  
        
    def retornarDatos(self):
        return self.datosTato
       
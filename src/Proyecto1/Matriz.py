from NodoM import NodoM
from NodoAVL import NodoAVL

class Matriz():
    def __init__ (self):
        self.inicio = None
        self.inicioDepartamento = None
        self.inicioEmpresa = None
        self.matrizVacia = "si"
        self.raiz = None
        
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
    
    def getRaiz(self): 
        if self.raiz != None:
            return self.raiz
    
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
        texto="digraph{"+"\n"+"rankdir=UD; \n"+"node [shape=box];"+"\n"
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
    
                    temp61=tamp61.derecha
    
                    text3=""
                    text4=""
                    for letra in temp6.contrasenia:
                        text3+=str(ord(letra))
                    for letra2 in temp6.izquierda.contrasenia:
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
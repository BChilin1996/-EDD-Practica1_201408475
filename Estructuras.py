import os
from xml.dom import minidom



# NODO DE LA PILA
class nodo_pila:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def set_val(self, valor):
        self.valor = valor

    def get_val(self):
        return self.valor

    # NODO DE LA MATRIZ
class nodo_matriz:
    def __init__(self, x,y,valor):
            self.valor = valor
            self.x=x
            self.y=y
            self.derecha = None
            self.izquierda=None
            self.arriba=None
            self.abajo =None

    def set_val(self, valor):
            self.valor = valor

    def get_val(self):
            return self.valor

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y


# PILA DE OPERACIONES last in first out (LIFO)
class pila_operaciones:
    def __init__(self):
        self.inicio = None

    def vacia(self):
        if self.inicio == None:
            return True
        return False

    def ingresar(self, valor):
        nuevoNodo = nodo_pila(valor)
        if self.vacia() == False:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente

            aux.siguiente = nuevoNodo
        else:
            self.inicio = nuevoNodo

    def pop(self):
        if self.vacia() == False:
            aux = self.inicio
            aux2 = self.inicio
            if aux.siguiente != None:
                while aux.siguiente != None:
                    aux2 = aux
                    aux = aux.siguiente

                aux2.siguiente = None
            else:
                self.inicio = None

            valor = aux.get_val()
            aux = None
            return valor
        return "vacia"

    def recorre(self):
        if self.vacia() == False:
            aux = self.inicio
            datos = ""
            while aux!= None:
                if aux.siguiente != None:
                    datos = datos + str(aux.get_val()) + " -> "
                else:
                    datos = datos + str(aux.get_val())
                aux = aux.siguiente

            print ("PILA = "+ datos)

    def graficar(self):
        if self.vacia() == False:
            archivo = open("grafica_pila.dot", "w")
            archivo.write("Digraph G {\n")
            aux = self.inicio
            i = 0
            while aux != None:
                archivo.write("\"Nodo" + str(i) + "\"[label = \"" + str(aux.get_val()) + "\" style=filled]\n")
                i = i + 1
                aux = aux.siguiente
            aux = self.inicio
            i = 0
            while aux.siguiente != None:
                archivo.write("\"Nodo" + str(i) + "\" -> \"Nodo" + str(i + 1) + "\"[constraint=false];\n")
                i = i + 1
                aux = aux.siguiente

            archivo.write("}")
            archivo.close()
            os.system("dot -Tpng grafica_pila.dot -o grafica_pila.png")


# NODO DE LA COLA
class nodo_cola:
    def __init__(self, operacion):
        self.operacion = operacion
        self.siguiente = None

    def get_opera(self):
        return self.operacion




#COLA first in first out (FIFO)
class cola_operaciones:
    def __init__(self):
        self.inicio = None

    def vacia(self):
        if self.inicio == None:
            return True
        return False

    def ingresar(self, operacion):
        nuevoNodo = nodo_cola(operacion)
        if self.vacia() == False:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente

            aux.siguiente = nuevoNodo

        else:
            self.inicio = nuevoNodo

    def dequeue(self):
        if self.vacia() == False:
            aux = self.inicio
            self.inicio = self.inicio.siguiente
            return aux.get_opera()
        else:
            return "vacia"

    def recorre(self):
        if self.vacia() == False:
            aux = self.inicio
            i = 0
            while aux != None:
                print ("indice "+str(i)+": "+ aux.get_opera())
                aux = aux.siguiente
                i = i + 1

    def graficar(self):
        if self.vacia() == False:
            archivo = open("grafica_cola.dot", "w")
            archivo.write("Digraph G {\n")
            aux = self.inicio
            i = 0
            while aux != None:
                archivo.write("\"Nodo" + str(i) + "\"[label = \"" + aux.get_opera() + "\" style=filled]\n")
                i = i + 1
                aux = aux.siguiente
            aux = self.inicio
            i = 0
            while aux.siguiente != None:
                archivo.write("\"Nodo" + str(i) + "\" -> \"Nodo" + str(i + 1) + "\"[constraint=false];\n")
                i = i + 1
                aux = aux.siguiente

            archivo.write("}")
            archivo.close()
            os.system("dot -Tpng grafica_cola.dot -o grafica_cola.png")

class matriz_valores:
    def __init__(self):
        self.inicio = None
        self.ultimo = None

    def vacia(self):
        if self.inicio == None:
            return True
        return False

    def agregar_dato(self,x,y,dato):
        if self.vacia()== True:
            self.inicio==self.ultimo== nodo_matriz(x,y,dato)
        else:
            aux= self.ultimo
            self.ultimo==aux.siguiente==nodo_matrix(x,y,dato)



    def recorre(self):
         if self.vacia() == False:
            aux = self.inicio
            i = 0
            while aux != None:
             print("indice " + str(i) + ": " + aux.get_opera())
             aux = aux.siguiente
             i = i + 1




# NODO DE LA LISTA
class nodo_lista:
    def __init__(self, usuario, contrasena, cola,matriz):
        self.usuario = usuario
        self.contrasena = contrasena
        self.cola = cola
        self.matriz= matriz
        self.siguiente = None
        self.atras = None

    def get_user(self):
        return self.usuario

    def get_pass(self):
        return self.contrasena

    def set_cola(self, cola):
        self.cola = cola

    def get_cola(self):
        return self.cola

    def set_matriz(self, matriz):
        self.matriz = matriz

    def get_matriz(self):
        return self.matriz







# LISTA
class lista_usuarios:
    def __init__(self):
        self.inicio = None
        self.ultimo = None

    def vacia(self):
        if self.inicio == None:
            return True
        return False

    def insertar(self, usuario, contrasena):
        cola = cola_operaciones()
        matriz = matriz_valores()
        nuevoNodo = nodo_lista(usuario, contrasena, cola, matriz)
        if self.vacia()==True:
            self.inicio = self.ultimo = nuevoNodo
            self.inicio.siguiente = self.ultimo
            self.ultimo.atras = self.inicio
        else:
            self.ultimo.siguiente = nuevoNodo
            nuevoNodo.atras = self.ultimo
            self.ultimo = self.ultimo.siguiente
            self.ultimo.siguiente = self.inicio
            self.inicio.atras = self.ultimo

    def llena_cola(self, operacion, usu, contra):
        if self.vacia() == False:
            aux = self.inicio
            while aux != self.ultimo:
                if aux.get_user() == usu and aux.get_pass() == contra:
                    aux.get_cola().ingresar(operacion)
                    return True
                aux = aux.siguiente

            if aux.get_user() == usu and aux.get_pass() == contra:
                aux.get_cola().ingresar(operacion)
                return True
        return False

    def llena_matriz(self, x, y, valor, usu, contra):
        if self.vacia() == False:
            aux = self.inicio
            while aux != self.ultimo:
                if aux.get_user() == usu and aux.get_pass() == contra:
                    aux.get_matriz().ingresar(x,y,valor)
                    return True
                aux = aux.siguiente

            if aux.get_user() == usu and aux.get_pass() == contra:
                aux.get_matriz().ingresar(x,y,valor)
                return True
        return False

    def obtener_cola(self, usu, contra):
        if self.vacia() == False:
            aux = self.inicio
            while aux != self.ultimo:
                if aux.get_user() == usu and aux.get_pass() == contra:
                    return aux.get_cola()
                aux = aux.siguiente

            if aux.get_user() == usu and aux.get_pass() == contra:
                return aux.get_cola()
        return "sin cola"

    def mostrar(self):
        aux = self.inicio
        aux2 = self.ultimo
        cadena = ""
        cadena2 = ""
        while aux != self.ultimo:
            #print(aux.get_user())
            cadena = cadena + aux.get_user() + "->"
            aux = aux.siguiente

        while aux2 != self.inicio:
            #print(aux.get_user())
            cadena2 = cadena2 + aux2.get_user() + "->"
            aux2 = aux2.atras

        #print(aux.get_user())
        cadena = cadena + aux.get_user() + "->" + self.inicio.get_user()
        cadena2 = cadena2 + aux2.get_user() + "->" + self.ultimo.get_user()
        print(cadena)
        print(cadena2)

    def verificar(self, usu, contra):
        aux = self.inicio
        while aux != self.ultimo:
            if aux.get_user() == usu and aux.get_pass() == contra:
                return True
            aux = aux.siguiente

        if aux.get_user() == usu and aux.get_pass() == contra:
            return True
        return False

    def existe(self, usu):
        if self.vacia() == False:
            aux = self.inicio
            while aux != self.ultimo:
                if aux.get_user() == usu:
                    return True
                aux = aux.siguiente

            if aux.get_user() == usu:
                return True
        return False

    def graficar(self):
        if self.vacia()==False:
            archivo = open("grafica_lista.dot", "w")
            archivo.write("Digraph G {\n")
            aux = self.inicio
            i = 0
            while aux != self.ultimo:
                archivo.write("\"Nodo"+str(i)+"\"[label = \""+aux.get_user()+" "+aux.get_pass()+"\" style=filled]\n")
                archivo.write("\"Nodo"+str(i)+"\" -> \"Nodo"+str(i+1)+"\"[constraint=false];\n")
                archivo.write("\"Nodo"+str(i+1)+"\" -> \"Nodo"+str(i)+"\"[constraint=false];\n")
                i = i + 1
                aux = aux.siguiente

            archivo.write("\"Nodo" + str(i) + "\"[label = \"" + aux.get_user() + " " + aux.get_pass() + "\" style=filled]\n")
            archivo.write("\"Nodo"+str(i)+"\" -> \"Nodo"+str(0)+"\"[constraint=false];\n")
            archivo.write("\"Nodo"+str(0)+"\" -> \"Nodo"+str(i)+"\"[constraint=false];\n")

            archivo.write("}")
            archivo.close()
            os.system("dot -Tpng grafica_lista.dot -o grafica_lista.png")


####################################################################################
# hasta abajo esta el menu comentado



####################################################################################
lista = lista_usuarios()
menu = 0
lista.insertar("rafa", "morales")
lista.insertar("bryand", "chilin")
lista.insertar("jorge", "solarez")
lista.insertar("aura", "flores")
lista.insertar("maria", "la regalona")
lista.mostrar()
cadena=""
#lista.graficar()


while menu== 0:
    print("Seleccion una opcion")
    print("1. Crear usuario")
    print("2. Ingresar al sistema")
    print("3. Salir del programa")
    numero = input("Introduce una opcion: ")

    if numero == "1":
        usuario1= input("Ingrese el usuario")
        contraseña1=input("Ingrese la contraseña")
        lista.insertar(usuario1,contraseña1)
        menu==0


    if numero== "2":
        usuario2 = input("Ingrese el usuario")
        contraseña2 = input("Ingrese la contraseña")
        if lista.verificar(usuario2, contraseña2)== True:
            print("Seleccion una opcion")
            print("1. Leer archivo")
            print("2. Resolver operaciones")
            print("3. Operar la matriz")
            print("4. Mostrar usuarios")
            print("5. Mostrar cola")
            print("6.Cerrar sesión")
            print("7. Agregar Operacion")
            numero2 = input("Introduce una opcion: ")
            if numero2 == "7":
                operacion = input("ingrese una operacion")
                print(operacion, usuario2, contraseña2)
                lista.llena_cola(operacion, usuario2, contraseña2)

            if numero2=="2":
                print(" 1. Operar siguiente")
                print(" 2. Regresar")
                numero3 = input("Introduce una opcion: ")
                if numero3=="2":
                    menu=="0"
                if numero3=="1":
                    cola = lista.obtener_cola(usuario2, contraseña2)
                    #cola.graficar()
                    op = cola.dequeue()
                    datos = op.split(" ")
                    result = 0
                    pila = pila_operaciones()
                    for i in range(0, len(datos)):
                        pila.ingresar(datos[i])
                        if datos[i] == "+" or datos[i] == "-" or datos[i] == "*":
                            pila.recorre()
                            #pila.graficar()
                            signo = pila.pop()
                            dato2 = pila.pop()
                            dato1 = pila.pop()
                            if signo == "+":
                                result = int(dato1) + int(dato2)
                                print(str(dato1) + " + " + str(dato2) + " = " + str(result))
                                pila.ingresar(result)
                            elif signo == "-":
                                result = int(dato1) - int(dato2)
                                print(str(dato1) + " - " + str(dato2) + " = " + str(result))
                                pila.ingresar(result)
                            elif signo == "*":
                                result = int(dato1) * int(dato2)
                                print(str(dato1) + " * " + str(dato2) + " = " + str(result))
                                pila.ingresar(result)
                        pila.recorre()
            if numero2=="3":

                print("1. Ingresar dato")
                print("2. Operar transpuesta")
                print("3. Mostrar matriz original")
                print("4. Mostrar matriz transpuesta")
                print("5. Regresar")
                numero3 = input("Introduce una opcion: ")
                if numero3=="1":
                    x = input("ingresa la posicion en X")
                    y = input("ingresa la posicion en y")
                    valor = input("ingrese el valor")
                    matriz.insertarxy(x,y,valor)

            if numero2== "4":
                lista.mostrar()
                lista.graficar()

            if numero2=="5":

                print ("Mostra cola")
                cola = lista.obtener_cola(usuario2, contraseña2)
                cola.recorre()

            if numero2=="1":
                direccion = input("ingrese la direccion")
                archivo = open(direccion, "r")
                codigo = archivo.read()
                print(codigo)
                archivo.close()
                mixml = codigo
                xmldoc = minidom.parseString(mixml)

                # obtenemos el atributo de <X">
                print("X Columnas")
                print("----------------------")
                itemlist = xmldoc.getElementsByTagName("x")
                for i in itemlist:
                    print(i.firstChild.nodeValue)


                # obtenemos el atributo de <Y">
                print("Y Filas")
                print("----------------------")
                itemlist = xmldoc.getElementsByTagName("y")
                for i in itemlist:
                    print(i.firstChild.nodeValue)


                # obtenemos el atributo line de <operaciones...">
                print("Operaciones")
                print("----------------------")
                itemlist = xmldoc.getElementsByTagName("operacion")
                for i in itemlist:
                    operacion=""
                    operacion=i.firstChild.nodeValue
                    print(i.firstChild.nodeValue)
                    lista.llena_cola(operacion, usuario2, contraseña2)
            if numero2=="0" or numero=="6":
                menu==0

        else:
            print ("El usuario y la contraseña no existen")
            menu==0

    if numero=="3":
        sys.exit()
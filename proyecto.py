#Nombre: Evan Jesus Tejada Duarte
#Carné: 0907-21-7854
#nota: se supode que este es un proyecto de 5-6 integrantes pero devido a porblemas 
#eh terminado solo. Todo el codigo presente lo escribí yo.


#notas: la funcionalidad es escasas solo logra mostrar luego del menu principal
#al intentar agregar un producto dentro del documento xlsx no me dejaba guardar los cambios
#funciones de eliminar, editar y agregar no sirven (el de la 1.1 fue el primer intento) devido aque 
#fui porbando y haciendolo por orden funciones mas complejas como enviar un correo o crear un archivo 
#de guardado no se realizaron, podria haber copiado varias de las funciones en otras pero eso solo aria 
#que me salten muchos errores ya que no están completas. La ultima vez que lo edite (30/10/2021)
#las funciones de 'listar'(me refiero a productos, clientes, etc) si funcionaban hago enfasis en esto
#ya que pasaron un par de veces que estas me daban problemas siendo practicamente iguales

#coincidero logre hacer al rededor de un 20% o 15% o incluso menos, no se, califique según su criterio 
#si desea tomar en cuenta que lo trabaje solo y lo que hice hubiera sido un porcentual del trabajo que me 
#hubiece tocado si trabajaba en un grupo, o bien, califiquelo como si fuera un grupo solo.

#hay muchas notas que separan funciones para que se le sea mas entendible



#importo el documento inventario.xlsx
import openpyxl
libro = openpyxl.load_workbook("inventario.xlsx")
hoja_productos = libro["Productos"]
#libererias de productos 
productoslp =[] #productos -- lista de productos
diccionarioproductoslp = {}
productosap =[] #productos -- agregar producto
diccionarioproductosap = {}

hoja_clientes = libro["Clientes"]
#librerias de clientes 
clienteslc = [] #clientes -- lista de clientes 
diccionarioclienteslc = {}

hoja_pedidos = libro["Pedidos"]
#libreria de Pedidos
pedidoslp = [] #pedidos -- lista de pedidos
diccionariopedidoslp = {}

#def muestra un menu con las opciones principales
# 1. Productos
# 2. Clientes
# 3. Pedidos
# 4. Informes
# 5. Varios


def pricipal():
    print("1. Productos")
    print("2. Clientes")
    print("3. Pedidos")
    print("4. Informes")
    print("5. Varios")
    print("6. Cancelar \n")

pricipal()

print("Eliga una opción")
opcionElegida = int(input())

while opcionElegida != 6:

#1. Productos
    if opcionElegida == 1:
        def produc():
            print("1.1 Agregar producto")
            print("1.2 Editar producto")
            print("1.3 Eliminar producto")
            print("1.4 Listar productos")
            print("1.5 Enviar cotización por correo")
            print("1.6 Cancelar \n")
        produc()
        print("Eliga que acción realizar")
        productos =  float(input())
    #aqui comienza las funciones de las opciones 1.#

    #1.1 Agregar producto
        if productos == 1.1:
            hoja_productos['A1'].value = 'nombre'
            hoja_productos['B1'].value = 'precio'
            hoja_productos['C1'].value = 'existencia'
            
            nombrep = input("Introduce el nombre del producto: ")
            diccionarioproductosap['nombre'] = nombrep
            preciop = float(input("Introduce el precio del producto: "))
            diccionarioproductosap['precio'] = preciop
            existenciap = int(input("Introduce la existencia del producto: "))
            diccionarioproductosap['existencia'] = existenciap
            productosap.append(diccionarioproductosap)

            fila = hoja_productos.max_row + 1
            for producto in productosap:
                hoja_productos['A' + str(fila)].value = produc['nombre']#me salta un error justamente en esta linea de codigo diciendo que le falta un valor 
                hoja_productos['B' + str(fila)].value = produc['precio']
                hoja_productos['C' + str(fila)].value = produc['existencia']
                
        #guardar 
            libro.save("inventario.xlsx")
            

            for item in productosap:
                print("Nombre:" + item['nombre'])
                print("Precio:" + str(item['precio']))
                print("Existencia:" + str(item["existencia"]))
    
    # Esto me paso con todos, no logro hacer que vuelva a las opciones #.# asi que lo mando al menu principal
            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
            
    #1.2 Editar producto
        elif productos == 1.2:
            #esto simplemente no funciona además que no llegue hasta el. pero si imprime y hace lo que dice 
            nombrep = input("Introduce el nombre del producto : ")
            preciop = float(input("Introduce el precio del producto : "))
            existenciap = int(input("Introduce la existencia del producto : "))
            tuple_ed = {
            "El nombre del prodcuto es": nombrep,
            "su precio es de ": preciop,
            "y la existencia es": existenciap}
            print(tuple_ed)
            opcionElegida = 0
            produc()
            print("Eliga que acción realizar")
            productos =  float(input())

    #1.3 Eliminar producto
        elif productos == 1.3:
            #cuando haya diccionario remplazar variables
            nombrep = input("Introduce el nombre del producto a eliminar: ")
            preciop = float(input("Introduce el precio del producto a eliminar: "))
            existenciap = int(input("Introduce la existencia del producto a eliminar: "))
            tuple_el = {
            "El nombre del prodcuto es": nombrep,
            "su precio es de ": preciop,
            "y la existencia es": existenciap}
            print(tuple_el)
            opcionElegida = 0
            produc()
            print("Eliga que acción realizar")
            productos =  float(input())

    #1.4 Listar productos
        #la lista es completamente funcional
        elif productos == 1.4:
            for row in range(2, hoja_productos.max_row + 1):
                nombrep = hoja_productos["A" + str(row)].value
                preciop = hoja_productos["B" + str(row)].value
                existenciap = hoja_productos["C" + str(row)].value
                diccionarioproductoslp['nombre'] = nombrep
                diccionarioproductoslp['precio'] = preciop
                diccionarioproductoslp['existencia'] = existenciap
                productoslp.append(diccionarioproductoslp)
                diccionarioproductoslp = {}

            for item in productoslp:
                print("Nombre:" + item['nombre'])
                print("Precio:" + str(item['precio']))
                print("Existencia:" + str(item['existencia']))

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())

    #1.5 Enviar cotización por correo
        #cuando haya diccionario remplazar variables
        elif productos == 1.5:
            nombreac = input("Nombre del cliente: ")
            productoel = input("productos elegidos: ")
            correo = input("Correo electronico del cliente: ")
            tuple_cc = {
            "El nombre del cliente es": nombreac,
            "Los productos elegidos son": productoel,
            "El correo es": correo}
            print(tuple_cc)

            opcionElegida = 0
            print("saliendo \n")
            produc()
            print("Eliga una opción")
            opcionElegida = int(input())

    #1.6 Cancelar
        elif productos == 1.6:
            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())


# 2. Clientes
    elif opcionElegida == 2:
        def client():
            print("2.1 Agregar Cliente")
            print("2.2 Editar Cliente")
            print("2.3 Eliminar Cliente")
            print("2.4 Listar Clientes")
            print("2.5 Cancelar \n")
        client()
        print("Eliga que acción realizar")
        clientes =  float(input())
    #aqui comienza las funciones de las opciones 2.#

    #2.1 Agregar Cliente
        #cuando haya diccionario remplazar variables
        if clientes == 2.1:
            nombreac = input("Escriba el nombre del cliente:")
            print("A continuación se le pide el NIT, el nuestro es de 6 digitos y sin guiones")
            nitac = int(input("Ingrese el NIT del cliente:"))
            direccionac = input("Escriba la dirección del cliente:")
            tuple_ac = {
                "El nombre del cliente es": nombreac,
                "El nit del cliente es": nitac,
                "La dirección del cliente es": direccionac}
            print(tuple_ac)

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
    
    #2.2 Editar Cliente
        #cuando haya diccionario remplazar variables
        elif clientes == 2.2:
            nombreac = input("Escriba el nombre del cliente:")
            print("A continuación se le pide el NIT, el nuestro es de 6 digitos y sin guiones")
            nitac = int(input("Ingrese el NIT del cliente:"))
            direccionac = input("Escriba la dirección del cliente:")
            tuple_ec = {
                "El nombre del cliente es": nombreac,
                "El nit del cliente es": nitac,
                "La dirección del cliente es": direccionac}
            print(tuple_ec)

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())

    #2.3 Eliminar Cliente
        #cuando haya diccionario remplazar variables
        elif clientes == 2.3:
            nombrebc = input("Escriba el nombre del cliente:")
            #cuando haya diccionario cambiar variables
            tuple_bc = {
                "El nombre del cliente que elimino es": nombreac,
                "El nit del cliente que elimino es": nitac,
                "La dirección del cliente que elimino es": direccionac}
            print(tuple_bc)

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
    
    #2.4 Listar Clientes
        #A pesar de ser igual en el comando que el 1.4 este imprime al rededor de 8 caracteres (nombre, nit, dirreccion) bacios
        elif clientes == 2.4:
            for row in range(hoja_clientes.max_row + 1):
                nombrec = hoja_clientes["A" + str(row)].value
                nitc = hoja_clientes["B" + str(row)].value
                direccionac = hoja_clientes["C" + str(row)].value
                diccionarioclienteslc['cnombre'] = nombrec
                diccionarioclienteslc['nit'] = nitc
                diccionarioclienteslc['direccion'] = direccionac
                clienteslc.append(diccionarioclienteslc)
                diccionarioclienteslc = {}

            for item in clienteslc:
                print("Nombre:" + str(item['cnombre']))
                print("NIT:" + str(int['nit']))
                print("Dirección:" + str(item["direccion"]))

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
    
    #2.5 Cancelar
        if clientes == 2.5:
            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())


#3. Pedidos
    elif opcionElegida == 3:
        print("3.1 Agregar Pedido")
        print("3.2 Eliminar Pedido")
        print("3.3 Listar Pedidos")
        print("3.4 Cancelar \n")
        print("Eliga que acción realizar")
        pedidos =  float(input())
    #aqui comienza las funciones de las opciones 3.#

    #3.1 Agregar Pedido
        #cuando haya diccionario remplazar variables

        opcionElegida = 0
        print("saliendo \n")
        pricipal()
        print("Eliga una opción")
        opcionElegida = int(input())

    #3.2 Eliminar Pedido
        if pedidos == 3.2:
            nombrebp = input("Ingrese el nombre del pedido:")
        #cuando haya diccionario remplazar variables
        

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
    
    #3.3 Listar Pedidos
        #esta lista no pide el contenido del .xlsx pero si cambio 'hoja_pedidos' por 'hoja_productos' si es funcional, no lo comprendo
        elif pedidos == 3.3:
            for row in range(2, hoja_pedidos.max_row + 1):
                nombrecli = hoja_pedidos["A" + str(row)].value
                nombrelpp = hoja_pedidos["B" + str(row)].value
                cantidadplp = hoja_pedidos["C" + str(row)].value
                valorplp = hoja_pedidos["D" + str(row)].value
                diccionariopedidoslp['nombrecli'] =  nombrecli
                diccionariopedidoslp['nombrelp'] = nombrelpp
                diccionariopedidoslp['cantidad'] = cantidadplp
                diccionariopedidoslp['valor'] = valorplp
                pedidoslp.append(diccionariopedidoslp)
                diccionariopedidoslp = {}

            for item in pedidoslp:
                print("Nombre del Cliente:" + item[' nombrecli'])
                print("Nombre del Producto:" + item['nombrelp'])
                print("Cantidad de Producto:" + str(item['cantidad']))
                print("Valor de Prodcuto:" + float(item['valor']))

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
    
    #3.4 Cancelar
        elif pedidos == 3.4:
            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())


#4. Informes
    elif opcionElegida == 4:
        print("4.1 Total de Ventas por Cliente")
        print("4.2 Total de Ventas por Producto")
        print("4.3. Cancelar \n")
        print("Eliga que acción realizar")
        informes =  float(input())
    #aqui comienza las funciones de las opciones 4.#
    #4.1 Total de Ventas por Cliente
        if informes == 4.1:
        #cuando haya libreria reflejar lista de clientes + pedidos

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())

    #4.2 Total de Ventas por Cliente
        if informes == 4.2:
        #cuando haya libreria reflejar lista de productos + varible nueva

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())

    #4.3 Cancelar
        elif informes == 4.3:
            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())


#5. Varios
    elif opcionElegida == 5:
        print("5.1 Crear Copia de Seguridad de Datos")
        print("5.2. Cancelar \n")
        print("Eliga que acción realizar")
        varios =  float(input())
    #aqui comienza las funciones de las opciones 5.#
    #5.1 Crear Copia de Seguridad de Datos
        if varios == 5.1:
            print("Creando copia de seguridad")
            #conciste en un correo a mi correo .umg
            
        opcionElegida = 0
        print("saliendo \n")
        pricipal()
        print("Eliga una opción")
        opcionElegida = int(input())
    
    #5.2 Cancelar
        if varios == 5.2:
            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())

#no hay un numero 6 ya que es el que sale del codigo


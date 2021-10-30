# Muestra un menu con las opciones principales
# 1. Productos
# 2. Clientes
# 3. Pedidos
# 4. Informes
# 5. Varios

#NOTA: Cuando digo "#" en los comentarios me refiero a algun numero cualquiera


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

#Aquí coienzan las funciones de mis variables

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
            nombrep = input("Introduce el nombre del producto: ")
            preciop = float(input("Introduce el precio del producto: "))
            existenciap = int(input("Introduce la existencia del producto: "))
            tuple_agp = {
            "El nombre del prodcuto es": nombrep,
            "su precio es de ": preciop,
            "y la existencia es": existenciap }
            print(tuple_agp)

    # Esto me paso con todos, no logro hacer que vuelva a las opciones #.# si no que solo a las principales 
            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
            
    #1.2 Editar producto
        elif productos == 1.2:
            nombrep = input("Introduce el nombre del producto a cambiar: ")
            preciop = float(input("Introduce el precio del producto a cambiar: "))
            existenciap = int(input("Introduce la existencia del producto a cambiar: "))
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
        elif productos == 1.4:
            print(nombrep)

            opcionElegida = 0
            produc()
            print("Eliga que acción realizar")
            productos =  float(input())

    #1.5 Enviar cotización por correo
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
        elif clientes == 2.2:
            #cunaod haya el diccionario de clientes cambiar variables
            tuple_ac = {
                "El nombre del cliente es": nombreac,
                "El nit del cliente es": nitac,
                "La dirección del cliente es": direccionac
            }
            print(tuple_ac)

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
    
    #2.5 Cancelar
        elif clientes == 2.5:
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
        if pedidos == 3.1:
            nombrepa = input("Ingrese el nombre del pedido:")
            nombrepp = input("Ingrese el nombre del producto:")
            cantidadpp = int(input("Ingrese la cantidad del producto:"))
            valorpp = float(input("IIngrese el valor monetario del producto:"))
        tuple_pp = {
            "El nombre del pedido es:": nombrepa,
            "El nombre del producto es:": nombrepp,
            "La cantidad del producto es:": cantidadpp,
            "El valor monetario del producto es:": valorpp}
        print(tuple_pp)

        opcionElegida = 0
        print("saliendo \n")
        pricipal()
        print("Eliga una opción")
        opcionElegida = int(input())

    #3.2 Eliminar Pedido
        if pedidos == 3.2:
            nombrebp = input("Ingrese el nombre del pedido:")
        #cuando haya diccionario remplazar variables
            tuple_pp = {
                "El nombre del pedido que elimino es:": nombrepa,
                "El nombre del producto que elimino es:": nombrepp,
                "La cantidad del producto que elimino es:": cantidadpp,
                "El valor monetario del producto que elimino es:": valorpp}
            print(tuple_pp)

            opcionElegida = 0
            print("saliendo \n")
            pricipal()
            print("Eliga una opción")
            opcionElegida = int(input())
    
    #3.3 Listar Pedidos
        elif pedidos == 3.3:
        #cuando haya diccionario remplazar variables
            tuple_lp = {
                "El nombre del pedido es:": nombrepa,
                "El nombre del producto es:": nombrepp,
                "La cantidad del producto es:": cantidadpp,
                "El valor monetario del producto es:": valorpp}
            print(tuple_lp)

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
        #cuando haya libreria reflejar lista de productos

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



# ==========================================
# TRABAJO INTEGRADOR - GESTION SUPERMERCADOS
# Algoritmos y Estructuras de Datos
# ==========================================

# ==========================================
# Versión 1.1
# Se agregó documentación del proyecto.
# ==========================================

# -------------------------
# VARIABLES GLOBALES
# -------------------------

# Catálogo inicial de productos del supermercado
productos = {
    1: {"nombre": "Leche", "precio": 1800},
    2: {"nombre": "Pan", "precio": 1200},
    3: {"nombre": "Arroz", "precio": 2500},
    4: {"nombre": "Fideos", "precio": 2100},
    5: {"nombre": "Aceite", "precio": 5200},
    6: {"nombre": "Azúcar", "precio": 1900},
    7: {"nombre": "Harina", "precio": 1700},
    8: {"nombre": "Yerba", "precio": 4800},
    9: {"nombre": "Gaseosa", "precio": 3200},
    10: {"nombre": "Chocolate", "precio": 2900}
}

# Carrito donde se almacenan los productos seleccionados
carrito = []

# Variables utilizadas para registrar las ventas del supermercado
ventas_realizadas = 0
total_vendido = 0
productos_vendidos = {}


# -------------------------
# FUNCION MENU
# -------------------------

# Función encargada de mostrar el menú principal al usuario
def mostrar_menu():

    print("\n==============================")
    print("   GESTION DE SUPERMERCADOS")
    print("==============================")
    print("1 - Mostrar productos")
    print("2 - Agregar producto")
    print("3 - Ver carrito")
    print("4 - Modificar cantidad")
    print("5 - Eliminar producto")
    print("6 - Finalizar compra")
    print("7 - Estadisticas")
    print("8 - Salir")
    print("==============================")


# -------------------------
# MOSTRAR PRODUCTOS
# -------------------------

# Función que muestra el catálogo completo de productos disponibles
def mostrar_productos():

    print("\nLISTA DE PRODUCTOS\n")

    for codigo in productos:

        print(
            codigo,
            "-",
            productos[codigo]["nombre"],
            "$",
            productos[codigo]["precio"]
        )


# -------------------------
# BUSCAR PRODUCTO
# -------------------------

# Función que busca un producto por su código y devuelve sus datos
def buscar_producto(codigo):

    if codigo in productos:
        return productos[codigo]

    return None


# -------------------------
# AGREGAR PRODUCTO
# -------------------------

# Función que permite agregar productos al carrito de compras
def agregar_producto():

    mostrar_productos()

    try:

        codigo = int(input("\nIngrese codigo: "))

        producto = buscar_producto(codigo)

        if producto is None:
            print("Producto inexistente.")
            return

        cantidad = int(input("Cantidad: "))

        if cantidad <= 0:
            print("Cantidad invalida.")
            return

        encontrado = False

        for item in carrito:

            if item["codigo"] == codigo:

                item["cantidad"] += cantidad

                encontrado = True

                break

        if not encontrado:

            carrito.append({
                "codigo": codigo,
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad
            })

        print("Producto agregado correctamente.")

    except:

        print("Debe ingresar numeros.")
 # -------------------------
# VER CARRITO
# -------------------------

# Función que muestra los productos agregados al carrito de compras
def ver_carrito():

    if len(carrito) == 0:
        print("\nEl carrito esta vacio.")
        return

    print("\nCARRITO DE COMPRAS\n")

    subtotal = 0

    for item in carrito:

        total_item = item["precio"] * item["cantidad"]

        subtotal += total_item

        print(
            item["nombre"],
            "- Cantidad:",
            item["cantidad"],
            "- Precio:",
            item["precio"],
            "- Total:",
            total_item
        )

    print("\nSubtotal: $", subtotal)


# -------------------------
# MODIFICAR CANTIDAD
# -------------------------

def modificar_cantidad():

    if len(carrito) == 0:
        print("No hay productos en el carrito.")
        return

    try:

        codigo = int(input("Ingrese codigo del producto: "))

        for item in carrito:

            if item["codigo"] == codigo:

                nueva = int(input("Nueva cantidad: "))

                if nueva <= 0:
                    print("Cantidad invalida.")
                    return

                item["cantidad"] = nueva

                print("Cantidad modificada.")
                return

        print("Producto no encontrado.")

    except:

        print("Dato incorrecto.")


# -------------------------
# ELIMINAR PRODUCTO
# -------------------------

def eliminar_producto():

    if len(carrito) == 0:
        print("El carrito esta vacio.")
        return

    try:

        codigo = int(input("Codigo a eliminar: "))

        for item in carrito:

            if item["codigo"] == codigo:

                carrito.remove(item)

                print("Producto eliminado.")

                return

        print("Producto inexistente.")

    except:

        print("Debe ingresar un numero.")


# -------------------------
# CALCULAR TOTAL
# -------------------------

def calcular_total():

    subtotal = 0

    for item in carrito:

        subtotal += item["precio"] * item["cantidad"]

    descuento = 0

    if subtotal >= 50000:

        descuento = subtotal * 0.15

    elif subtotal >= 30000:

        descuento = subtotal * 0.10

    elif subtotal >= 15000:

        descuento = subtotal * 0.05

    total = subtotal - descuento

    return subtotal, descuento, total


# -------------------------
# PROMOCION
# -------------------------

def aplicar_promocion(total):

    respuesta = input(
        "¿Posee tarjeta de cliente? (S/N): "
    ).upper()

    if respuesta == "S":

        total = total * 0.95

        print("Promocion aplicada.")

    return total
# -------------------------
# FINALIZAR COMPRA
# -------------------------

def finalizar_compra():

    global ventas_realizadas
    global total_vendido
    global productos_vendidos

    if len(carrito) == 0:
        print("\nNo hay productos en el carrito.")
        return

    subtotal, descuento, total = calcular_total()

    total = aplicar_promocion(total)

    print("\nMEDIOS DE PAGO")
    print("1 - Efectivo")
    print("2 - Debito")
    print("3 - Credito")

    try:

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            medio = "Efectivo"

        elif opcion == 2:
            medio = "Debito"

        elif opcion == 3:
            medio = "Credito"

            recargo = total * 0.10
            total += recargo

        else:
            print("Opcion invalida.")
            return

    except:

        print("Debe ingresar un numero.")
        return

    print("\n===============================")
    print("         TICKET")
    print("===============================")

    for item in carrito:

        importe = item["precio"] * item["cantidad"]

        print(
            item["nombre"],
            "x",
            item["cantidad"],
            "- $",
            importe
        )

        nombre = item["nombre"]

        if nombre in productos_vendidos:

            productos_vendidos[nombre] += item["cantidad"]

        else:

            productos_vendidos[nombre] = item["cantidad"]

    print("-------------------------------")
    print("Subtotal: $", round(subtotal, 2))
    print("Descuento: $", round(descuento, 2))
    print("Total Final: $", round(total, 2))
    print("Pago:", medio)
    print("===============================\n")

    ventas_realizadas += 1
    total_vendido += total

    carrito.clear()

    print("Compra realizada correctamente.")


# -------------------------
# ESTADISTICAS
# -------------------------

def estadisticas():

    print("\n========== ESTADISTICAS ==========")

    print("Cantidad de ventas:", ventas_realizadas)

    print("Total vendido: $", round(total_vendido, 2))

    if ventas_realizadas > 0:

        promedio = total_vendido / ventas_realizadas

    else:

        promedio = 0

    print("Promedio por venta: $", round(promedio, 2))

    if len(productos_vendidos) > 0:

        mayor = ""

        cantidad = 0

        for producto in productos_vendidos:

            if productos_vendidos[producto] > cantidad:

                cantidad = productos_vendidos[producto]

                mayor = producto

        print("Producto mas vendido:", mayor)

        print("Cantidad vendida:", cantidad)

    else:

        print("Todavia no existen ventas.")

    print("=================================\n")
# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

def main():

    while True:

        mostrar_menu()

        try:

            opcion = int(input("Seleccione una opcion: "))

        except:

            print("Debe ingresar un numero.")
            continue

        if opcion == 1:

            mostrar_productos()

        elif opcion == 2:

            agregar_producto()

        elif opcion == 3:

            ver_carrito()

        elif opcion == 4:

            modificar_cantidad()

        elif opcion == 5:

            eliminar_producto()

        elif opcion == 6:

            finalizar_compra()

        elif opcion == 7:

            estadisticas()

        elif opcion == 8:

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("Opcion invalida.")


# -------------------------
# INICIO DEL PROGRAMA
# -------------------------

main()
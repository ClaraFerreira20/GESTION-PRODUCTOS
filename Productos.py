import os

# Lista para almacenar los productos
productos = []

def cargar_datos():
    """Carga los datos desde un archivo al inicio del programa."""
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(", ")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

def guardar_datos():
    """Guarda los datos de los productos en un archivo."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

def añadir_producto():
    """Añade un nuevo producto a la lista."""
    nombre = input("Introduce el nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para el precio.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para la cantidad.")
    
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido exitosamente.")

def ver_productos():
    """Muestra todos los productos en la lista."""
    if not productos:
        print("No hay productos en la lista.")
        return
    
    print("\nLista de Productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()  # Línea en blanco para mejor legibilidad

def actualizar_producto():
    """Actualiza los detalles de un producto existente."""
    nombre = input("Introduce el nombre del producto a actualizar: ")
    
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            while True:
                try:
                    nuevo_precio = float(input(f"Introduce el nuevo precio (actual: {producto['precio']}): "))
                    break
                except ValueError:
                    print("Por favor, introduce un valor numérico para el precio.")
            
            while True:
                try:
                    nueva_cantidad = int(input(f"Introduce la nueva cantidad (actual: {producto['cantidad']}): "))
                    break
                except ValueError:
                    print("Por favor, introduce un valor numérico para la cantidad.")
            
            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad
            print(f"Producto '{nombre}' actualizado exitosamente.")
            return
    
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    """Elimina un producto de la lista basado en su nombre."""
    nombre = input("Introduce el nombre del producto a eliminar: ")
    
    for i, producto in enumerate(productos):
        if producto["nombre"].lower() == nombre.lower():
            del productos[i]
            print(f"Producto '{nombre}' eliminado exitosamente.")
            return
    
    print(f"Producto '{nombre}' no encontrado.")

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        print("\nSistema de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del programa...")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    cargar_datos()  # Cargar datos al inicio
    menu()          # Mostrar menú principal
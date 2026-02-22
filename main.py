from servicios.inventario_service import InventarioService
from modelos.producto import Producto


def main():
    inventario = InventarioService()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_p = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

                print("✅ Producto agregado correctamente.")

            elif opcion == "2":
                id_p = input("ID del producto: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))

                inventario.actualizar_producto(id_p, cantidad, precio)
                print("✅ Producto actualizado correctamente.")

            elif opcion == "3":
                id_p = input("ID del producto: ")
                inventario.eliminar_producto(id_p)
                print("✅ Producto eliminado correctamente.")

            elif opcion == "4":
                productos = inventario.listar_productos()

                if not productos:
                    print("Inventario vacío.")
                else:
                    print("\n----- INVENTARIO -----")
                    for p in productos:
                        print(f"ID: {p.id_producto}")
                        print(f"Nombre: {p.nombre}")
                        print(f"Cantidad: {p.cantidad}")
                        print(f"Precio: ${p.precio}")
                        print("----------------------")

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    main()
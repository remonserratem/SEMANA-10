import os
from modelos.producto import Producto


class InventarioService:

    def __init__(self, file_path="data/inventario.txt"):
        self.file_path = file_path
        self.productos = {}

        self._asegurar_archivo()
        self._cargar()

    # -------------------------------------------------
    # Crear archivo si no existe
    # -------------------------------------------------
    def _asegurar_archivo(self):
        try:
            if not os.path.exists(self.file_path):
                open(self.file_path, "w").close()
        except PermissionError:
            print("❌ No tienes permisos para crear el archivo.")
        except Exception as e:
            print("❌ Error inesperado al verificar el archivo:", e)

    # -------------------------------------------------
    # Cargar productos desde archivo
    # -------------------------------------------------
    def _cargar(self):
        try:
            with open(self.file_path, "r") as archivo:
                for linea in archivo:
                    if not linea.strip():
                        continue  # Ignorar líneas vacías

                    try:
                        producto = Producto.from_line(linea)
                        self.productos[producto.id_producto] = producto
                    except ValueError:
                        print("⚠ Línea corrupta ignorada:", linea.strip())

        except FileNotFoundError:
            print("⚠ Archivo no encontrado. Se creará uno nuevo.")
            open(self.file_path, "w").close()

        except PermissionError:
            print("❌ No tienes permisos para leer el archivo.")

        except Exception as e:
            print("❌ Error inesperado al cargar el archivo:", e)

    # -------------------------------------------------
    # Guardar productos en archivo
    # -------------------------------------------------
    def _guardar(self):
        try:
            with open(self.file_path, "w") as archivo:
                for producto in self.productos.values():
                    archivo.write(producto.to_line() + "\n")

        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print("❌ Error inesperado al guardar:", e)

    # -------------------------------------------------
    # Agregar producto
    # -------------------------------------------------
    def agregar_producto(self, producto: Producto):
        if producto.id_producto in self.productos:
            raise ValueError("El producto ya existe.")

        self.productos[producto.id_producto] = producto
        self._guardar()

    # -------------------------------------------------
    # Actualizar producto
    # -------------------------------------------------
    def actualizar_producto(self, id_producto, cantidad, precio):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado.")

        self.productos[id_producto].cantidad = cantidad
        self.productos[id_producto].precio = precio
        self._guardar()

    # -------------------------------------------------
    # Eliminar producto
    # -------------------------------------------------
    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado.")

        del self.productos[id_producto]
        self._guardar()

    # -------------------------------------------------
    # Listar productos
    # -------------------------------------------------
    def listar_productos(self):
        return list(self.productos.values())
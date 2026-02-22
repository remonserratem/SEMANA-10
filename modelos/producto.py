class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_line(self) -> str:
        """
        Convierte el objeto en una línea de texto
        para guardarlo en el archivo.
        """
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_line(line: str):
        """
        Crea un objeto Producto a partir de
        una línea del archivo.
        """
        id_producto, nombre, cantidad, precio = line.strip().split(",")
        return Producto(id_producto, nombre, int(cantidad), float(precio))
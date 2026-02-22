#  Sistema de Gestión de Inventarios
## Nombre: Roxana Monserrate

## Descripción

Este proyecto implementa un Sistema de Gestión de Inventarios en Python que permite administrar productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

El sistema almacena la información en un archivo de texto (`inventario.txt`).



##  Objetivo

Aplicar conceptos fundamentales de programación en Python como:

- Programación orientada a objetos
- Arquitectura por capas (modelos, servicios, datos)
- Manipulación de archivos
- Manejo de excepciones
- Control de versiones con Git



## Estructura del Proyecto
SEMANA-10/
│
├── data/
│ └── inventario.txt
│
├── modelos/
│ └── producto.py
│
├── servicios/
│ └── inventario_service.py
│
├── main.py
└── README.md

---

## Funcionalidades

- Agregar productos
- Actualizar productos
- Eliminar productos
- Listar productos
- Persistencia automática en archivo
- Carga automática al iniciar el sistema
- Manejo de errores como:
  - FileNotFoundError
  - PermissionError
  - Líneas corruptas


##  Arquitectura

El proyecto está organizado en capas:

### modelos
Contiene la clase `Producto`, que representa la estructura de los datos.

### servicios
Contiene la clase `InventarioService`, que maneja:
- Lógica del negocio
- Lectura y escritura de archivos
- Manejo de excepciones

### data
Contiene el archivo `inventario.txt` donde se almacenan los productos.


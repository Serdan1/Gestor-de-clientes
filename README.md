# Gestor-de-clientes

https://github.com/Serdan1/Gestor-de-clientes.git


# Gestor de Clientes en Python

Un programa para gestionar clientes con opciones de listar, buscar, añadir, modificar y borrar registros. Incluye un modo terminal y una interfaz web interactiva con Gradio. Los datos se almacenan en un archivo CSV para persistencia.

## Requisitos
- Python 3.x
- Dependencias: `pytest` (para pruebas), `gradio` (para la interfaz web)

## Instalación
1. Clona el repositorio desde GitHub:
git clone <URL_del_repositorio>
   cd Gestor_Clientes

2. Crea y activa un entorno virtual:
python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. Instala las dependencias:
pip install -r requirements.txt


## Uso
- **Modo terminal**:
  python gestor/run.py -t


- **Modo web (Gradio)**:
python gestor/run.py
Esto abrirá una interfaz web en tu navegador (ej. `http://127.0.0.1:7860`). En entornos como Codespaces, también proporciona un enlace público.

- **Ejecutar pruebas**: 
pytest -v



## Estructura del Proyecto
Aquí tienes un diagrama de la estructura del proyecto:

Gestor_Clientes/
├── gestor/              # Módulos principales
│   ├── init.py     # Marca el directorio como paquete
│   ├── run.py         # Punto de entrada (elige modo terminal o Gradio)
│   ├── menu.py        # Interfaz de terminal
│   ├── database.py    # Gestión de datos (clientes y CSV)
│   ├── helpers.py     # Funciones auxiliares (validaciones, limpieza)
│   └── ui.py          # Interfaz web con Gradio
├── tests/              # Pruebas unitarias
│   ├── init.py    # Marca el directorio como paquete
│   └── test_database.py  # Tests para database.py
├── clientes.csv        # Archivo de datos persistentes
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación



## Funcionalidades
- **Listar clientes**: Muestra todos los clientes en una tabla.
- **Buscar cliente**: Busca un cliente por DNI.
- **Añadir cliente**: Agrega un nuevo cliente (DNI único, formato 2 números + 1 letra).
- **Modificar cliente**: Cambia nombre y apellido por DNI.
- **Borrar cliente**: Elimina un cliente por DNI.
- **Persistencia**: Los datos se guardan en `clientes.csv`.

## Notas
- El programa valida el DNI (2 números y 1 letra mayúscula) y asegura que no haya duplicados.
- Las pruebas unitarias verifican todas las operaciones de la base de datos.
- La interfaz Gradio es ideal para demostraciones web y funciona en entornos como Codespaces sin necesidad de un display gráfico.
- Desarrollado y probado en Python 3.12.

## Créditos
Creado por Daniel Serrano Martin.


graph TD
    A[Gestor_Clientes] --> B[gestor]
    A --> C[tests]
    A --> D[clientes.csv]
    A --> E[requirements.txt]
    A --> F[README.md]
    B --> G[__init__.py]
    B --> H[run.py]
    B --> I[menu.py]
    B --> J[database.py]
    B --> K[helpers.py]
    B --> L[ui.py]
    C --> M[__init__.py]
    C --> N[test_database.py]























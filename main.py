import sys
import os

# Agregar el directorio 'gestor' al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "gestor")))

from gestor import menu, ui

if __name__ == "__main__":
    if "-t" in sys.argv:
        menu.iniciar()
    else:
        ui.demo.launch()
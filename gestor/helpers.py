import os
import re
import platform

def limpiar_pantalla():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    if mensaje:
        print(mensaje)
    while True:
        texto = input("> ").strip()
        if longitud_min <= len(texto) <= longitud_max:
            return texto
        print(f"Error: El texto debe tener entre {longitud_min} y {longitud_max} caracteres.")

def dni_valido(dni, lista):
    if not re.match(r'^[0-9]{2}[A-Z]$', dni):  # 2 números + 1 letra mayúscula
        print("DNI incorrecto, debe ser 2 números y 1 letra (ej. 12A).")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI ya utilizado por otro cliente.")
            return False
    return True
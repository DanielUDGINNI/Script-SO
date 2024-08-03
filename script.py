# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:14:58 2023

@author: DanielVazquez
"""
import sys
import socket
import subprocess


def opc1():
    direccion_ip = socket.gethostbyname(socket.gethostname())
    print(f"Hola tu direccion IP en este equipo es: {direccion_ip}")

def opc2():

    interfaces()

    nombre_adaptador = input("Ingresa el nombre del adaptador (por ejemplo, Wi-Fi): ")
    nueva_ip = input("Ingresa la nueva dirección IP: ")
    mascara_subred = input("Ingresa la máscara de subred (por ejemplo, 255.255.255.0): ")

    try:
        # Comando para cambiar la dirección IP del adaptador de red WiFi en Windows
        comando = f"netsh interface ip set address name=\"{nombre_adaptador}\" static {nueva_ip} {mascara_subred}"
        resultado = subprocess.run(comando, shell=True, check=True, text=True)

        if resultado.returncode == 0:
            print(f"La dirección IP del adaptador {nombre_adaptador} ha sido cambiada a: {nueva_ip}")
    except Exception as e:
        print(f"Error al cambiar la dirección IP: {e}")
        
def opc3():
    interfaces()

    nombre_adaptador = input("Ingresa el nombre del adaptador (por ejemplo, Wi-Fi): ") 
    try:
        comando = f"netsh interface ip set address name=\"{nombre_adaptador}\" source=dhcp"
        resultado = subprocess.run(comando, shell=True, check=True, text=True)

        if resultado.returncode == 0:
            print(f"La configuración de red para el adaptador {nombre_adaptador} ha sido cambiada a DHCP.")
    except Exception as e:
        print(f"Error al cambiar la configuración de red a DHCP: {e}")


def opc4():
    #Deshabilitar adaptador de red
    interfaces()

    nombre_adaptador = input("Ingresa el nombre del adaptador (por ejemplo, Wi-Fi): ")

    try:
        comando = f"netsh interface set interface \"{nombre_adaptador}\" admin=disable"
        resultado = subprocess.run(comando, shell=True, check=True, text=True)

        if resultado.returncode == 0:
            print(f"El adaptador {nombre_adaptador} ha sido deshabilitado.")
    except Exception as e:
        print(f"Error al deshabilitar el adaptador: {e}")

    opc41()

def opc41(): #habilitar adaptador de red
    interfaces()
    nombre_adaptador = input("Ingresa el nombre del adaptador (por ejemplo, Wi-Fi): ")
    try:
        comando = f"netsh interface set interface \"{nombre_adaptador}\" admin=enable"
        resultado = subprocess.run(comando, shell=True, check=True, text=True)

        if resultado.returncode == 0:
            print(f"El adaptador {nombre_adaptador} ha sido habilitado.")
    except Exception as e:
        print(f"Error al habilitar el adaptador: {e}")

#---------------Activar Protocolo SMB----------------
def opc5():
    try:
        comando = 'sc config LanmanServer start=auto'
        resultado = subprocess.run(comando, shell=True, check=True, text=True)

        if resultado.returncode == 0:
            print("El protocolo SMB ha sido activado.")
    except Exception as e:
        print(f"Error al activar el protocolo SMB: {e}")


#------------Enlistar equipos en red-----------------
def opc6():
    direccion_ip = socket.gethostbyname(socket.gethostname())
    print(f"Hola tu direccion IP en este equipo es: {direccion_ip}")

    subred = input("Ingresa los primeros tres segmentos de la IP (por ejemplo, 192.168.1): ")
    print(f"Buscando equipos en la subred {subred}...")
    for i in range(1, 255):
        direccion = f"{subred}.{i}"
        try:
            nombre, _, _ = socket.gethostbyaddr(direccion)
            print(f"Equipo encontrado: {nombre} ({direccion})")
        except socket.herror:
            pass
        except socket.error:
            pass
#----------Respaldar tareas-------------
def opc7():
    print("hola")



def adaptadores():
    comando = 'ipconfig'
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)

    if resultado.returncode == 0:
        print(resultado.stdout)
    else:
        print(f"Error al mostrar la configuración de los adaptadores de red: {resultado.stderr}")

def interfaces():
    try:
        comando = 'netsh interface show interface'
        resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)

        if resultado.returncode == 0:
            print(resultado.stdout)
        else:
            print(f"Error al mostrar las interfaces de red: {resultado.stderr}")
    except Exception as e:
        print(f"Error: {e}")


def salir():
    print("Finalizado")
    sys.exit()
    
def menu():
    print("------Menu-------")
    print("1. Consultar direccion IP")
    print("2. Cambiar direccion IP estatica")
    print("3. Cambiar direccion IP Automatica DHCP")
    print("4. Reiniciar adaptador de red")
    print("5. Activar protocolo SMB")
    print("6. Equipos en red")
    print("7. Modo concentracion")


opcionesR = {
    '1': opc1,
    '2': opc2,
    '3': opc3,
    '4': opc4,
    '5': opc5,
    '6': opc6,
    '7': opc7,
    '9': salir
}   
    
i = 1
while (i == 1):
    menu()
    seleccion = input("Elige una opción: ")
    
    if seleccion in opcionesR:
        opcionesR[seleccion]()
    else:
        print("Opción no válida")
from persona import Persona, Archivo, Estudiante, TypeFile
import sys
import os

def limpiar_pantalla():
    
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("clear")



def registrar_persona(tipo_persona):
    os.system("clear")
    print(f"Registro de {tipo_persona.capitalize()}s")
    print()

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    dni = int(input("Ingrese su Dni: "))

    if tipo_persona == "docente":
        persona = Persona(nombre, edad, dni)
    else:
        notas = []
        print("\nRegistro de Notas - Ingresa tus 4 notas:")
        for i in range(1, 5):
            nota = int(input(f"Nota {i}: "))
            notas.append(nota)
        
        nmax = max(notas)
        nmin = min(notas)
        promedio = sum(notas) / 4

        persona = Estudiante(nombre, edad, dni, notas, nmax, nmin, promedio)
    
    archivo = TypeFile(f"{tipo_persona}s.txt", persona, f"{tipo_persona}s")
    archivo.save_file()
    
    print("✅ Datos agregados con éxito.")

    while True:
        selecc = input("Desea realizar otro registro? (S/N): ").strip().upper()
        if selecc == "S":
            registrar_persona(tipo_persona)
        elif selecc == "N":
            return seleccion()
        else:
            print("❌ Opción no válida. Inténtelo de nuevo.")

def seleccion():
    while True:
        os.system("clear")
        print("======= Bienvenido al sistema de Registros =======")
        print("Por favor, ingrese una opción:")

        try:
            opcion = int(input("\n1: Alumno.\n2: Docente.\n3: Salir.\n➡ Opción: "))

            if opcion == 1:
                registrar_persona("alumno")
            elif opcion == 2:
                registrar_persona("docente")
            elif opcion == 3:
                limpiar_pantalla()
                print("👋 Desconectado con éxito...")
                sys.exit()
            else:
                print("❌ Opción no válida.")
        except ValueError:
            print("❌ Ingrese un número válido.")
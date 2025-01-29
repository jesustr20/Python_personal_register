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





#profesor = "docente.txt"
#estudiante = "alumno.txt"
#reptotales = "reporteTotal.txt"
#
#def addDocentes():
#    os.system("cls")
#    print("Registro de Profesores: ")
#    print()
#    nomdoc = input("Ingrese su nombre: ")
#    ageDoc = int(input("Ingrese su edad: "))
#    dniDoc = int(input("Ingrese su Dni: "))
#    npro = 'Nombre: '+str(nomdoc)
#    edadpro = ' Edad: '+str(ageDoc)
#    dnipro = ' DNI: '+str(dniDoc)
#    doc = Persona(npro,edadpro,dnipro)
#    archivo = Archivo(profesor)
#    archivo.agregarDocente(doc)
#    print("Datos agregados...")
#    while True:
#        try:
#            selecc = input("Desea Realizar otro registro? S/N: ")
#            if selecc == 'S':
#                addDocentes()
#            if selecc == 'N':
#                selecciona()
#        except ValueError:
#            print("Selecciona correctamente")
#
#cont = 1
#def addAlumnos():
#    os.system("cls")
#    print("Registro de Alumnos: ")
#    print()
#    nomAlum = input("Ingrese su nombre: ")
#    ageAlum = int(input("Ingrese su edad: "))
#    dniAlum = int(input("Ingrese su Dni: "))
#    #---------------------#
#    nal = 'Nombre: '+str(nomAlum)
#    ealum = ' Edad: '+str(ageAlum)
#    dnial = ' DNI: '+str(dniAlum)
#    print()
#    notas = []
#    suma = 0
#    prome = 0
#    print("Registro de Notas")
#    print("Ingresa tus 4 notas")
#    for i in range(1,5):
#        nota = int(input(f"Nota Nr. {i}: "))
#        notas.append(nota)
#    for j in notas:
#        suma = suma + j
#        prome = suma/4
#    n1 = ' Nota1: '+str(notas[0])
#    n2 = ' Nota2: '+str(notas[1])
#    n3 = ' Nota3: '+str(notas[2])
#    n4 = ' Nota4: '+str(notas[3])
#    nmax= max(notas)
#    nmin= min(notas)
#    notaMaxi =' Nota Maxima: '+str(nmax)
#    notaMini =' Nota Maxima: '+str(nmin)
#    promeTotal =' Nota Maxima: '+str(prome)
#    #Agrego las notas Alumnos con su nombre en el archivo "alumno.txt"
#    alum = Estudiante(nal,ealum,dnial,n1,n2,n3,n4,notaMaxi,notaMini,promeTotal)
#    archivo = Archivo(estudiante)
#    archivo.agregarAlumno(alum)
#    print("Datos agregados...")
#    while True:
#        try:
#            selecc = input("Desea Realizar otro registro? S/N: ")
#            if selecc == 'S':
#                addAlumnos()
#            if selecc == 'N':
#                selecciona()
#        except ValueError:
#            print("Selecciona correctamente")
#
#
#def selecciona():
#    while True:
#        try:
#            os.system("cls")
#            print("======= Bienvenido al sistema de Registros, porfavor Ingrese una opcion... =======")
#            tipo = int(input("Ingrese tipo: \n1:Alumno.\n2:Docente.\n3:Salir.\nNro Opcion: "))
#            if tipo == 1 or tipo == "Alumno" or tipo == "alumno":
#                print("Registro del alumno")
#                addAlumnos()
#                break
#            if tipo == 2 or tipo == "Docente" or tipo == "docente":
#                print("Registro del Docente")
#                addDocentes()
#                break
#            if tipo == 3 or tipo == "Salir" or tipo == "salir":
#                os.system("cls")
#                print("###### Se ah desconectado con Exito... ######")
#                print()
#                sys.exit()
#        except ValueError:
#            print("Por favor ingresa una opcion correcta.")
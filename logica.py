from persona import Persona, Archivo, PersonaAlum, rGeneral
import sys,os

profesor = "docente.txt"
estudiante = "alumno.txt"
reptotales = "reporteTotal.txt"

def addDocentes():
    os.system("cls")
    print("Registro de Profesores: ")
    print()
    nomdoc = input("Ingrese su nombre: ")
    ageDoc = int(input("Ingrese su edad: "))
    dniDoc = int(input("Ingrese su Dni: "))
    npro = 'Nombre: '+str(nomdoc)
    edadpro = ' Edad: '+str(ageDoc)
    dnipro = ' DNI: '+str(dniDoc)
    doc = Persona(npro,edadpro,dnipro)
    archivo = Archivo(profesor)
    archivo.agregarDocente(doc)
    print("Datos agregados...")
    while True:
        try:
            selecc = input("Desea Realizar otro registro? S/N: ")
            if selecc == 'S':
                addDocentes()
            if selecc == 'N':
                selecciona()
        except ValueError:
            print("Selecciona correctamente")

cont = 1
def addAlumnos():
    os.system("cls")
    print("Registro de Alumnos: ")
    print()
    nomAlum = input("Ingrese su nombre: ")
    ageAlum = int(input("Ingrese su edad: "))
    dniAlum = int(input("Ingrese su Dni: "))
    #---------------------#
    nal = 'Nombre: '+str(nomAlum)
    ealum = ' Edad: '+str(ageAlum)
    dnial = ' DNI: '+str(dniAlum)
    print()
    notas = []
    suma = 0
    prome = 0
    print("Registro de Notas")
    print("Ingresa tus 4 notas")
    for i in range(1,5):
        nota = int(input(f"Nota Nr. {i}: "))
        notas.append(nota)
    for j in notas:
        suma = suma + j
        prome = suma/4
    n1 = ' Nota1: '+str(notas[0])
    n2 = ' Nota2: '+str(notas[1])
    n3 = ' Nota3: '+str(notas[2])
    n4 = ' Nota4: '+str(notas[3])
    nmax= max(notas)
    nmin= min(notas)
    notaMaxi =' Nota Maxima: '+str(nmax)
    notaMini =' Nota Maxima: '+str(nmin)
    promeTotal =' Nota Maxima: '+str(prome)
    #Agrego las notas Alumnos con su nombre en el archivo "alumno.txt"
    alum = PersonaAlum(nal,ealum,dnial,n1,n2,n3,n4,notaMaxi,notaMini,promeTotal)
    archivo = Archivo(estudiante)
    archivo.agregarAlumno(alum)
    print("Datos agregados...")
    while True:
        try:
            selecc = input("Desea Realizar otro registro? S/N: ")
            if selecc == 'S':
                addAlumnos()
            if selecc == 'N':
                selecciona()
        except ValueError:
            print("Selecciona correctamente")

retotal = rGeneral(estudiante,profesor)
retotal.rtotal(reptotales)


def selecciona():
    while True:
        try:
            os.system("cls")
            print("======= Bienvenido al sistema de Registros, porfavor Ingrese una opcion... =======")
            tipo = int(input("Ingrese tipo: \n1:Alumno.\n2:Docente.\n3:Salir.\nNro Opcion: "))
            if tipo == 1 or tipo == "Alumno" or tipo == "alumno":
                print("Registro del alumno")
                addAlumnos()
                break
            if tipo == 2 or tipo == "Docente" or tipo == "docente":
                print("Registro del Docente")
                addDocentes()
                break
            if tipo == 3 or tipo == "Salir" or tipo == "salir":
                os.system("cls")
                print("###### Se ah desconectado con Exito... ######")
                print()
                sys.exit()
        except ValueError:
            print("Por favor ingresa una opcion correcta.")
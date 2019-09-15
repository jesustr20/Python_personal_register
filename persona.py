class Persona():
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


class PersonaAlum(Persona):
    def __init__(self,nombre,edad,dni,n1,n2,n3,n4,nmaxi,nmini,prome):
        Persona.__init__(self,nombre,edad,dni)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.nmaxi = nmaxi
        self.nmini = nmini
        self.prome = prome


class rGeneral():
    def __init__(self,estudiante=None,profesor=None):
        self.estudiante = estudiante
        self.profesor = profesor

    def rtotal(self,rep):
        try:
            rtotal = open(rep,'w')
            estudiante = open(self.estudiante,'r')
            profesor = open(self.profesor,'r')
            rtotal.write("ESTUDIANTES...:\n")
            for lineaEst in estudiante.readlines():
                rtotal.write(f"{lineaEst}")
            rtotal.write("\n\nPROFESORES...:\n")
            for lineaProfe in profesor.readlines():
                rtotal.write(f"{lineaProfe}")
        except Exception as e:
            print("error: "+str(e))
        else:
            rtotal.close()
            #Me mostrara los reportes generales
        try:
            file = open(rep,'r')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print("error: "+str(e))
        else:
            file.close()

#Agregara datos del docente
class Archivo():
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    #Agregara datos del docente
    def agregarDocente(self,docente):
        try:
            file = open(self.nombre_archivo,'a')
            texto_agregar = "{},{},{}\n".format(docente.nombre,docente.edad,docente.dni)
            file.write(texto_agregar)
        except Exception as e:
            print("error: ",str(e))
        else:
            file.close()
            print(file)

    #Agregara datos y notas del alumno
    def agregarAlumno(self,alum):
        try:
            file = open(self.nombre_archivo,'a')
            texto_agregar = "{},{},{},{},{},{},{},{},{},{}\n".format(alum.nombre,alum.edad,alum.dni,alum.n1,alum.n2,alum.n3,alum.n4,alum.nmaxi,alum.nmini,alum.prome)
            file.write(texto_agregar)
        except Exception as e:
            print("error: ",str(e))
        else:
            file.close()
            print(file)

    def mostrar(self):
        try:
            file = open(self.nombre_archivo,'r')
            for linea in file.readlines():
                print(linea)
                file.readlines(linea)
        except Exception as e:
            print("error: ",str(e))
        else:
            file.close()
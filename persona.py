import os

class Persona():
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


class Estudiante(Persona):
    def __init__(self,nombre,edad,dni,notas, nmaxi,nmini,prome):
        Persona.__init__(self,nombre,edad,dni)
        self.notas = notas #Lista
        self.nmaxi = nmaxi
        self.nmini = nmini
        self.prome = prome

#Agregara datos del docente

class TypeFile:
    def __init__(self, name_file, objeto, tipo_persona, carpeta_principal = "registros"):
        self.name_file = name_file
        self.objeto = objeto
        self.tipo_persona = tipo_persona
        self.carpeta_principal = carpeta_principal
        
    def save_file(self):

        carpeta = os.path.join(self.carpeta_principal, self.tipo_persona)
        os.makedirs(carpeta, exist_ok=True)
        ruta_archivo = os.path.join(carpeta, self.name_file)
        
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            valores = list(vars(self.objeto).values())
            linea = ",".join(map(str, valores))+"\n"
            archivo.write(linea)
        

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
            texto_agregar = "{},{},{},{},{},{},{}\n".format(alum.nombre,alum.edad,alum.dni,alum.nota,alum.nmaxi,alum.nmini,alum.prome)
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
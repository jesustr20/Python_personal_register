import os

class Persona:
    def __init__(self,nombre: str,edad: int,dni: str):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


class Estudiante(Persona):
    def __init__(self,nombre: str, edad:int, dni:int, notas: list, nmaxi:int, nmini:int, prome:float):
        super().__init__(nombre,edad,dni)
        self.notas = notas #Lista de notas
        self.nmaxi = nmaxi
        self.nmini = nmini
        self.prome = prome

class Profesor(Persona):
    def __init__(self, nombre:str, edad:int, dni:int):
        super().__init__(nombre, edad, dni)            

#Agregara datos del docente

class TypeFile:
    def __init__(self, name_file: str, objeto, tipo_persona: str, carpeta_principal: str = "registros"):
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

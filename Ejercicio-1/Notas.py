from Estudiante import Estudiante 
from Materia import Materia 
from Materia import materia 
from Estudiante import alumno 

class Nota(Estudiante,Materia): 

    def __init__(self,laboratorio, parcial):
        self.laboratorio =  laboratorio
        self.parcial = parcial 
    
    def Revisar(self):
        return 'El estudiante {}, tuvo un {} en el laboratorio y tuvo un {} en la nota de parcial en la asignatura de {}'.format(alumno.nombre,self.laboratorio,self.parcial,materia.materia)
    
notas =  Nota(10,10)

print(notas.Revisar())


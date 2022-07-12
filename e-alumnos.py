class alumno():
  def __init__(self, nombre,nota):
            self.nombre=nombre
            self.nota=nota
        
class aprobacion(alumno):
  def aprobado(self):
      if self.nota > 3 and self.nota <= 5:
        return f'El alumno {self.nombre} con nota {self.nota} esta aprobado'
      elif self.nota == 3:
        return f'El alumno {self.nombre} con nota {self.nota} esta aprobado pero necesita refuerzo'
      elif self.nota > 3:
        return f'El alumno {self.nombre} con nota {self.nota} esta reprobado'    

ap=aprobacion("Ramiro",4)
print(ap.aprobado())

import pickle


class vehiculo():
  def __init__(self, color,ruedas,puertas):
            self.color=color
            self.ruedas=ruedas
            self.puertas=puertas

class coche(vehiculo):
  def carro(self, velocidad, cilindrada):
            self.velocidad=velocidad
            self.cilindrada=cilindrada
            return f'El carro es {self.color}, con {self.puertas} puertas,tiene {self.ruedas} llantas, con una velocidad de {self.velocidad} y un cilindraje de {self.cilindrada}'     

v=coche('azul',4,2)
c=v.carro('300 Km', '3000 cc')

f=open('prueba.bin', 'wb')
pickle.dump(c, f)
f.close()

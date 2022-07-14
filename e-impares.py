numeros=[]
n=int(input("ingrese cantidad de numeros: "))
for x in range(n):
  num= int(input("Ingrese numero: "))
  numeros.append(num)
  

def numerosImpares(num):
   if num %2:
    return True
   return False
impar=filter(numerosImpares,numeros)
print(f'Los numeros impares de la lista son: {list(impar)}')

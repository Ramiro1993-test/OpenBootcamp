paises=[]
n=int(input("ingrese cantidad de paises: "))
for x in range(n):
  pais=input("Ingrese pais: ")
  paises.append(pais)

orlist=set(paises)
orden=sorted(orlist)
print(orden)

class agenda:

    def __init__(self):
        self.contacto={}
    
    def menu(self):
        opc=0
        while opc != 5:
          print('Bienvenido al menu') 
          print('1. Cargar contacto ') 
          print('2. Listar contacto ') 
          print('3. Consultar contacto ') 
          print('4. Modificar contacto ') 
          print('5. Finalizar programa ') 
          opc=int(input(f'Ingrese una opcion: ') ) 
          if opc == 1:
            self.cargar()
          elif opc == 2:
            self.imprimir()
          elif opc == 3:
            self.consultar()
          elif opc == 4:
            self.modificar()
          elif opc == 5:
            break        

    def cargar(self):
       con='S'
       while con == 'S': 
        nombre=input("Ingrese nombre: ")
        telefono=int(input("Ingrese telefono: "))
        email=input('Ingrese email: ')
        self.contacto[nombre]=[telefono,email]
        con=input("Desea ingresar otro contacto? S/N: ")
       return self.contacto

    def imprimir(self):
        print('Lista cargada')
        for nombre in self.contacto:
         print (f' Nombre: {nombre} Tel: {self.contacto[nombre][0]} email: {self.contacto[nombre][1]} ')     
    
    def consultar(self):
        nombre=input("Ingrese nombre a consultar: ")
        if nombre in self.contacto:
            print(f'Contacto: \n {nombre} tel: {self.contacto[nombre][0]} correo: {self.contacto[nombre][1]}')

    def modificar(self):
        nombre=input("Ingrese nombre a modificar: ")
        if nombre in self.contacto: 
           opc=0
           while opc != 2: 
             opc=int(input(f'Que desea modificar \n 1. Telefono \n 2. Email \n Opcion: '))
             if opc == 1:
              telefono=int(input('Ingrese telefono nuevo: '))
              self.contacto[nombre]=telefono
             elif opc == 2: 
              email=input("Ingrese email nuevo: ")
              self.contacto[nombre]=email
             elif opc == 3:
                print('Opcion erronea') 
        else:
            print(f'El contacto no se encuentra registrado') 

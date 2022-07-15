def crear_usuario(identificador,nombre,apellido):
 n=int(input("Ingrese cantidad de alumnos a registrar: "))
 for x in range(n):
    identificador=int(input("Ingrese identicador: "))
    nombre=input("Ingrese nombre: ")
    apellido=input("Ingrese nombre: ")
    return (identificador, nombre, apellido)
 conn=sqlite3.connect('maplicacion.db')
 cursor=conn.cursor()
 
 query='INSERT INTO users(id,nombre,apellido)VALUES(?,?,?)'

 cursor.execute(query,(identificador,nombre,apellido))
 identificador+=1
 conn.commit()
 cursor.close()
 conn.close()

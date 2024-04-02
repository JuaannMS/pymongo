from pymongo import MongoClient
from datetime import datetime

# Conexión a la base de datos MongoDB (se conectará a localhost:27017)
client = MongoClient()
db = client['pythondatabase']
collection = db['usuarios']


def crear_usuario():
    nombre = input('Ingrese el nombre del usuario: ')
    edad = input('Ingrese la edad del usuario: ')
    telefono = input('Ingrese el número telefónico del usuario: ')
    ciudad = input('Ingrese la ciudad del usuario: ')
    

    fecha_ingreso = datetime.now().strftime('%Y-%m-%d')
    
    usuario = {'nombre': nombre, 'edad': edad, 'fecha_ingreso': fecha_ingreso, 'telefono': telefono, 'ciudad': ciudad}
    collection.insert_one(usuario)
    print('Usuario creado exitosamente')


def obtener_usuarios():
    usuarios = collection.find()
    for usuario in usuarios:
        print(usuario)


def actualizar_usuario(nombre, nueva_edad, nuevo_telefono, nueva_ciudad):
    # Obtener el usuario actual para mantener la fecha de ingreso
    usuario_actual = collection.find_one({'nombre': nombre})

    # Actualizar los campos excepto la fecha de ingreso
    nuevos_datos = {
        'edad': nueva_edad,
        'telefono': nuevo_telefono,
        'ciudad': nueva_ciudad
    }

    # Actualizar el usuario en la base de datos
    collection.update_one({'nombre': nombre}, {'$set': nuevos_datos})

    # Restaurar la fecha de ingreso original
    if usuario_actual:
        collection.update_one({'nombre': nombre}, {'$set': {'fecha_ingreso': usuario_actual['fecha_ingreso']}})

    print('Usuario actualizado exitosamente')



def eliminar_usuario(nombre):
    collection.delete_one({'nombre': nombre})
    print('Usuario eliminado exitosamente')

# Menú principal
def main():
    while True:
        print('1. Crear usuario')
        print('2. Obtener usuarios')
        print('3. Actualizar usuario')
        print('4. Eliminar usuario')
        print('5. Salir')
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            obtener_usuarios()
        elif opcion == '3':
            nombre = input('Ingrese el nombre del usuario a actualizar: ')
            nueva_edad = input('Ingrese la nueva edad del usuario: ')
            nuevo_telefono = input('Ingrese el nuevo telefono del usuario: ')
            nueva_ciudad = input('Ingrese la nueva ciudad del usuario: ')
            
            actualizar_usuario(nombre, nueva_edad, nuevo_telefono, nueva_ciudad)
        elif opcion == '4':
            nombre = input('Ingrese el nombre del usuario a eliminar: ')
            eliminar_usuario(nombre)
        elif opcion == '5':
            break
        else:
            print('Opción no válida')

if __name__ == '__main__':
    main()

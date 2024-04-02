from pymongo import MongoClient

# Conexión a la base de datos MongoDB (por defecto, se conectará a localhost:27017)
client = MongoClient()
db = client['mi_basededatos']
collection = db['usuarios']

# Función para crear un nuevo usuario
def crear_usuario(nombre, edad):
    usuario = {'nombre': nombre, 'edad': edad}
    collection.insert_one(usuario)
    print('Usuario creado exitosamente')

# Función para obtener todos los usuarios
def obtener_usuarios():
    usuarios = collection.find()
    for usuario in usuarios:
        print(usuario)

# Función para actualizar un usuario
def actualizar_usuario(nombre, nueva_edad):
    collection.update_one({'nombre': nombre}, {'$set': {'edad': nueva_edad}})
    print('Usuario actualizado exitosamente')

# Función para eliminar un usuario
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
            nombre = input('Ingrese el nombre del usuario: ')
            edad = input('Ingrese la edad del usuario: ')
            crear_usuario(nombre, edad)
        elif opcion == '2':
            obtener_usuarios()
        elif opcion == '3':
            nombre = input('Ingrese el nombre del usuario a actualizar: ')
            nueva_edad = input('Ingrese la nueva edad del usuario: ')
            actualizar_usuario(nombre, nueva_edad)
        elif opcion == '4':
            nombre = input('Ingrese el nombre del usuario a eliminar: ')
            eliminar_usuario(nombre)
        elif opcion == '5':
            break
        else:
            print('Opción no válida')

if __name__ == '__main__':
    main()

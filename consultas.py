from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
dataBase = cliente['CUCIENEGA']

coleccionDatos = dataBase.tablaContactos

def obtener_todos_contactos():
    cursor = coleccionDatos.find()
    return list(cursor)

def obtener_un_contacto(elContacto):
    resultadoConsulta = coleccionDatos.find_one({'nombre': elContacto})
    return resultadoConsulta

 def insertar_un_contacto(datosContacto):
    idContactoInsertado = coleccionDatos.insert_one(datosContacto)
    return idContactoInsertado  

def editar_un_contacto(nombreContacto, datosContacto):
    contactoModificado = coleccionDatos.update_one({'nombre': nombreContacto}, 
        {'$set': {'correo': datosContacto['correo']},
                 {'telefono': datosContacto['telefono']},
                 {'direccion': datosContacto['direccion']}})
    return str(contactoModificado.modified_count)


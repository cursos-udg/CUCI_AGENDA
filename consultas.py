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

#forma 1 de eliminar 
def eliminar_un_contacto(idContacto):

    resultado = coleccionDatos.delete_one(
        {
        '_id': ObjectId(idContacto)
        })
    return resultado.deleted_count

#forma 2 de eliminar 
def eliminar_un_contacto_secundario(contacto):

    resultado = coleccionDatos.delete_one(
        {
        'nombre': contacto
        })
    return resultado.deleted_count
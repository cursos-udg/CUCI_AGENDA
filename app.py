from flask import Flask, render_template, request, redirect, url_for
from consultas import *
import json
import os

app = Flask(__name__ ,static_url_path="")
port = os.getenv("PORT",8000)

@app.route('/')
def index():
    return redirect(url_for("obtener_contactos"))

@app.route('/contactos')
def obtener_contactos():
    contactos = obtener_todos_contactos()
    return render_template('listacontactos.html', contactos=contactos)

@app.route('/contactos/test')
def contactos_prueba():
    contactos = [{ "nombre" : "Pruebancio"}, {"nombre" : "Pruebantino"}]
    return render_template('listacontactos.html', contactos=contactos)

@app.route('/detalles/test')
def detalles_prueba():
    contacto = {
        "nombre" : "Pruebancio",
        "empresa" : "Test SA de CV",
        "correo" : "prueb4ncio@test.test",
        "telefono" : "01 800 123 TEST"
    }
    return render_template('detalles.html', contacto=contacto)

@app.route('/detalles/<nombre>')
def detalles_contacto(nombre):
    contacto = obtener_un_contacto(nombre)
    return render_template('detalles.html', contacto=contacto)

@app.route('/contacto', methods=["POST", "GET"])
def contacto_form():
    if request.method == "GET":
        return render_template('formContacto.html')
    else:
        insertar_un_contacto(request.form.to_dict())
        return redirect(url_for("obtener_contactos"))

@app.route('/contacto/<nombre>', methods=["POST", "GET"])
def contacto_form_editar(nombre):
    if request.method == "GET":
        contacto = obtener_un_contacto(nombre)
        return render_template('formContacto.html', contacto=contacto)
    else:
        editar_un_contacto(nombre,request.form.to_dict())
        return redirect(url_for("detalles_contacto", nombre=nombre))

if __name__ == "__main__":
    app.run(port=port,host="0.0.0.0",debug=True)  
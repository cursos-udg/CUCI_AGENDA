from flask import Flask, render_template, request, redirect, url_for
from consultas import *
import json

app = Flask(__name__)


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
def detalles_contacto():
    contacto = obtener_un_contacto(nombre)
    return render_template('detalles.html', contacto=contacto)

@app.route('/contacto', methods=["POST", "GET", "PUT"])
def contacto_form():
    if request.method == "GET":
        return render_template('formContacto.html')
    elif request.method == "POST":
        insertar_un_contacto(request.form)
        return redirect(url_for("obtener_contactos"))
    else:
        editar_un_contacto(resquest.form["nombre"],request.form)
        return redirect(url_for("obtener_contactos"))

@app.route('/contacto/<nombre>')
def contacto_form_editar():
    contacto = obtener_un_contacto(nombre)
    return render_template('formContacto.html', contacto=contacto)

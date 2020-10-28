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

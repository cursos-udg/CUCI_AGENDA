from flask import Flask, render_template, request, redirect, url_for
from consultas import *
import json

app = Flask(__name__)


@app.route('/contactos/todo')
def obtener_contactos():
    consulta = obtener_todos_contactos()
    return render_template('consultar_todo.html', consulta=consulta)


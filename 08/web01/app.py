#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import archivo_paises as ap
app = Flask(__name__)

import json

paises = ap.cargar()
print(json.dumps(paises, indent=2))

@app.route("/")
def index():
    # return "{} paises".format(len(paises))
    return render_template("index.html", num_paises=len(paises), paises=paises)

@app.route("/pais/<string:nombre>/")
def mostrar_pais(nombre):
    if nombre in paises :
        return render_template("pais.html", pais=nombre, capital=paises[nombre]["capital"], lider=paises[nombre]["lider"])
    return render_template("noexiste.html", pais=nombre)

if __name__ == '__main__':
    app.run(debug=True)

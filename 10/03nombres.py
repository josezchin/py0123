#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Ejemplo de conectar a base de datos y contar personas
import configparser
import os
import psycopg2

# Cargamos el archivo de configuración y las variables relevantes
PCONFIG=os.getenv('PCONFIG', './padron.ini')
config=configparser.ConfigParser()
config.read(PCONFIG)
USUARIO_BDD=os.getenv('USUARIO_BDD', config['BDD'].get('usuario'))
CLAVE_BDD=os.getenv('CLAVE_BDD', config['BDD'].get('clave'))
SERVIDOR_BDD=os.getenv('SERVIDOR_BDD', config['BDD'].get('servidor'))
NOMBRE_BDD=os.getenv('NOMBRE_BDD', config['BDD'].get('nombre'))

cnx=psycopg2.connect(dbname=NOMBRE_BDD, user=USUARIO_BDD, host=SERVIDOR_BDD, password=CLAVE_BDD)
cur=cnx.cursor()

cur.execute("SELECT count(1) FROM ciudadano WHERE nombre LIKE 'JOSE %' OR nombre LIKE '% JOSE' or nombre = 'JOSE';")
(count,)= cur.fetchone();
print("Hay {} personas con el nombre Jose en el padrón electoral.".format(count));
cnx.close()

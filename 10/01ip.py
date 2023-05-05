#!/usr/bin/env python3
# coding: utf-8
#
# Ejemplo para averiguar mi propia dirección ip

import requests

req=requests.get("https://icanhazip.com/")
print(req.content.decode().strip("\n"))

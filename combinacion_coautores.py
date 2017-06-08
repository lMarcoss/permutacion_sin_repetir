#!/usr/bin/env python
# -*- coding: 850 -*-
# Listar, crear directorios y archivos del sistema
# @utor: Leonardo Marcos Santiago

import os
import shutil

# funciones
def crear_archivo():
    archivo = open('datos.txt','w')
    archivo.close()

def escribir_en_archivo(lista_coautores):
    archivo = open('coautores1.txt','a')
    for coautoria in lista_coautores:
		archivo.write(coautoria[0].strip() + ", " + coautoria[1])
    archivo.close()

def leer_archivo(autores):
	archivo = open("coautores.txt", "r")
	for linea in archivo.readlines():
		autores.append(sustituir_caracteres(linea))

# Sustituir caracteres no deseados
def sustituir_caracteres(texto):
	texto_limpio = texto.lower()
	texto_limpio = texto_limpio.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
	texto_limpio = texto_limpio.replace('ñ', 'ni')
	texto_limpio = texto_limpio.replace(' ', '_').replace('-', '_').replace('ñ', 'ni')
	return texto_limpio

def existe_coautores(lista_coautores, autor, coautor):
	existe = False
	for coautores in lista_coautores:
		if((coautores[0] == autor and coautores[1] == coautor) or (coautores[0] == coautor and coautores[1] == autor)):
			existe = True
			break
	return existe


def agregar_combinacion(lista_coautores,autor, coautor):
	coautoria = [autor, coautor]
	if(autor != coautor):
		if(existe_coautores(lista_coautores,autor,coautor) == False):
			lista_coautores.append(coautoria)


def combinaciones(autores, coautores):
	for autor in autores:
		for coautor in autores:
			agregar_combinacion(lista_coautores,autor,coautor)

	
# os.system("reset")
lista_autores = []
lista_coautores = []
leer_archivo(lista_autores)
combinaciones(lista_autores, lista_coautores)
escribir_en_archivo(lista_coautores)

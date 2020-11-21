# importacion de librerias
import os
import subprocess
import sys
import getpass

# funcion de agregar usuarios
def add_user():

	# Preguntar el nombre de usuarios
	username = input("Enter Username ")

	# Preguntar por la contraseña
	password = getpass.getpass() 4

	try:
		# Ejecucion de la funcion
		subprocess.run(['useradd', '-p', password, username ])
	except:
  # Error :(
		print(f"Failed to add user.")
		sys.exit(1)

add_user() 

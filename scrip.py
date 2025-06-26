from usuario import Usuario
import datetime
import pytz
import json

import requests

#ruta = "usuario.txt"
tz_CL = pytz.timezone('America/Santiago')
datetime_CL = datetime.datetime.now(tz_CL)

instancias = []

with open("usuarios.txt") as users:
    linea = users.readline()
    while linea:
        try:
            usuario = json.loads(linea)
            instancias.append(Usuario(
                usuario.get("nombre"),
                usuario.get("apellido"),
                usuario.get("email"),
                usuario.get("genero")
            ))
        except Exception as e:  # error capturado en e y se guarda en archivo
            with open("error.log","a+") as log:
                log.write(f"{datetime_CL.strftime("%d/%m/%y %H:%M:")}, {e} \n")
        finally:
            linea = users.readline()
    

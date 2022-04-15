def niños(username):
    username=int(username)
    if username==75599279:
        print("Bienvenido Marcelo :)")
    elif username==75599278:
        print("Bienvenido Mariano :)")
    elif username==75599277:
        print("Bienvenida Alexandra")
    elif username==75599276:
        print("Bienvenido Gael :)")
#-------------------------------
def error_dni():
    inv_dni=input("""
El DNI consta de 8 caracteres
Por favor, escribalo de nuevo.
DNI: """)
    while not len(inv_dni)==8:
        inv_dni=input("""
El DNI consta de 8 caracteres
Por favor, escribalo de nuevo.
DNI: """)
    niños(inv_dni)

#-----------------------------------------
def iniciar_sesion():
    username=input(""""
Escriba el DNI de su menor hijo
DNI: """)
    if len(username)==8:
        niños(username)
    else:
        error_dni()

#-------------------------------------------------------
def error_loop():
    error=input("""
Opción inválida.
(I) Iniciar sesion
(R) Registrarse

Por favor, escriba una opción correcta : """)
    error=error.upper()
    while not (error=="I" or error=="R"):
        error=input("""
Opción inválida.
(I) Iniciar sesion
(R) Registrarse

Por favor, escriba una opción correcta: """)
        error=error.upper()
    in_rg(error)
#------------------------------------------------------
def in_rg(mssg_wllk):
    if mssg_wllk=="I":
        iniciar_sesion()
    elif mssg_wllk=="R":
        print("Registrarse")
    else:
        error_loop()
#---------------------------------------------------------
def inicio_app():
    mssg_wllk=input("""Sea bienvenido a la aplicación
de la movilidad número 11. #DeVueltaAlCole

(I) Iniciar sesión
(R) Registrarse

Escriba una de las opciones: """)
    mssg_wllk=mssg_wllk.upper()
    in_rg(mssg_wllk)

if __name__=="__main__":
    inicio_app()
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
        print("Iniciar sesion")
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
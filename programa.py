
def inicio_app():
    mssg_wllk=input("""Sea bienvenido a la aplicación
de la movilidad número 11. #DeVueltaAlCole

(I) Iniciar sesión
(R) Registrarse

Escriba una de las opciones: """)
    mssg_wllk=mssg_wllk.capitalize()
    if mssg_wllk=="I":
        print("Iniciar sesion")
    elif mssg_wllk=="R":
        print("Registrarse")
    else:
        error=input("""Opcion desconocida.
(I) Iniciar sesión
(R) Registrarse
Por favor, escoja alguna opcion: """)
        error=error.capitalize()   
        while not error=="R" and error=="I":
            error=input("""Opcion desconocida.
(I) Iniciar sesión
(R) Registrarse
Por favor, escoja alguna opcion: """)
        if error=="I":
            print("Iniciar sesion")
        elif error=="R":
            print("Registrarse")

if __name__=="__main__":
    inicio_app()
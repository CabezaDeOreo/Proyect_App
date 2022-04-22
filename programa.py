def niños(username):
    """Mensaje de bienvenida al
    usuario que inicio sesión"""
    username=int(username)
    dict_est={
        75599278:"Marcelo",
        75599277:"Mariano",
        75599276:"Alexandro",
        75599275:"Gael"
    }
    for estudiantes in dict_est.keys():
        if estudiantes==username:
            print(f'Bienvenid@ {dict_est[estudiantes]}')
            break
        else:
            print(f'El estudiante no existe')

#-------------------------------
def error_dni():
    """DNI erroneo, o posee
    menos de 8 caracteres o más
    que este."""
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
    """Relleno de datos
    para iniciar sesion"""
    username=input(""""
Escriba el DNI de su menor hijo
DNI: """)
    if len(username)==8:
        niños(username)
    else:
        error_dni()
#-------------------------------------------------------
def registrarse():
    dni_est=input("""Para registrarse correctamente escriba
el DNI de su menor hijo para poder guardarlo en nuestro sistema.
DNI: """)
    while not (len(dni_est)==8):
        dni_est=input("""El DNI consta de 8 caracteres.
Por favor, escribalo de nuevo.
DNI:  """)
    reg_corre=input("Registrado con éxito")
#-------------------------------------------------------
def error_loop():
    """Mensaje de error al
    seleccionar una opción inválida."""
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
    """Se ejecuta una
    función dependiendo de
    la opción que haya elegido
    el usuario. """
    if mssg_wllk=="I":
        iniciar_sesion()
    elif mssg_wllk=="R":
        registrarse()
    else:
        error_loop()
#---------------------------------------------------------
def inicio_app():
    """Mensaje de bienvenida
    de la app y las opciones
    correspondientes."""
    mssg_wllk=input("""Sea bienvenido a la aplicación
de la movilidad número 11. #DeVueltaAlCole

(I) Iniciar sesión
(R) Registrarse

Escriba una de las opciones: """)
    mssg_wllk=mssg_wllk.upper()
    in_rg(mssg_wllk)

if __name__=="__main__":
    inicio_app()

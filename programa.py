
def niños(name):
    """Mensaje de bienvenida al
    usuario que inicio sesión"""
    print(f'''
Bienvenido a la movilidad número 11, {name} :).''')

#--------------------------------------------------

def sign_in():
    print("""-----------------------------------------------
Para iniciar sesión, rellene lo siguiente.""")
    n_st=input("""
Nombre del estudiante: """)
    d_st=input("""DNI: """)
    print("""---------------------------------------------------
El estudiante que usted indica no existe en nuestro sistema.""")
    register=input("""
¿Desea registrarse? (Si/No): """)
    register=register.strip()
    register=register.capitalize()
    if register=="Si":
        sign_up()
    elif register=="No":
        print("""
Gracias por su visita :)""")
    else:
        print("""
Opción inválida""")

#------------------------------------------------

def error_gen(dic_est):
    """Error generado por haber
    puesto algun dato erroneo"""
    print("""--------------------------------------------------
El nombre del estudiante o el DNI que introdujo es incorrecto.
Por favor, rellene los datos correctamente.""")
    name_stn=input("""
Nombre del estudiante: """)
    dni_stn=input("DNI: ")
    dic_error_si=dic_est
    for d in dic_error_si:
        if (name_stn==dic_error_si[d]) and (dni_stn==d):
            niños(name_stn)
            break
        else:
            error_gen(dic_est)
            break
#-----------------------------------------

def sign_up_to_sign_in(dic_est):
    """Relleno de datos
    para iniciar sesion"""
    print("""------------------------------------
Incie sesión rellenando lo siguiente:""")
    name=input("""
Nombre del estudiante: """)
    dni_8=input("DNI: ")
    students_sp=dic_est
    for dni in students_sp:
        if (name==students_sp[dni]) and (dni==dni_8):
            niños(name)
            break
        elif (name==students_sp[dni]) and (len(dni_8)!=8):
            error_gen(dic_est)
        elif (name!=students_sp[dni]) and (dni==dni_8):
            error_gen(dic_est)

#---------------------------------------------------------

def database_students(name_student,dni_st):
    dic_est={}
    dic_est[dni_st]=name_student
    sign_up_to_sign_in(dic_est)

#-------------------------------------------------------

def sign_up():
    print("""------------------------------------------------
Para registrarse con éxito, rellene los siguientes datos""")
    name_student=input("""
Escriba el nombre del estudiante: """)
    while not (len(name_student)>0):
        name_student=input("""
Es obligatorio rellenar este dato.
Por favor, escribe el nombre del estudiante: """)
    dni_st=input("DNI: ")
    while not (len(dni_st)==8):
        dni_st=input("""
El DNI consta de 8 caracteres.
Por favor, escribelo de nuevo.
DNI:  """)
    print("""
Registrado con éxito""")
    database_students(name_student,dni_st)

#-------------------------------------------------------

def error_loop():
    """Mensaje de error al
    seleccionar una opción inválida."""
    print("""----------------------------------------
Opción inválida.

Por favor, escoja una de las opciones:
(I) Iniciar sesión
(R) Registrarse
""")
    error=input("(I/R): ")
    error=error.strip()
    error=error.upper()
    while not (error=="I" or error=="R"):
        print("""
Opción inválida.

Por favor, escoja una de las opciones:
(I) Iniciar sesión
(R) Registrarse""")
        error=input("""
(I/R): """)
        error=error.strip()
        error=error.upper()
    options(error)

#------------------------------------------------------

def options(option_bg):
    """Se ejecuta una
    función dependiendo de
    la opción que haya elegido
    el usuario. """
    if option_bg=="R":
        sign_up()
    elif option_bg=="I":
        sign_in()
    else:
        error_loop()

#---------------------------------------------------------

def my_app():
    """Mensaje de bienvenida
    de la app y las opciones
    correspondientes."""
    print("""Sea bienvenido a la aplicación
de la movilidad número 11. #DeVueltaAlCole

(I) Iniciar sesión
(R) Registrarse
 """)
    option_bg=input("""
Elija una opción: """)    
    option_bg=option_bg.strip()
    option_bg=option_bg.capitalize()
    options(option_bg)


if __name__=="__main__":
    my_app()

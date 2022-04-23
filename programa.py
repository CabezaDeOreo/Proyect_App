def niños(name):
    """Mensaje de bienvenida al
    usuario que inicio sesión"""
    print(f'Bienvenido {name} :)')

#------------------------------------------------

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

def sign_in(dic_est):
    """Relleno de datos
    para iniciar sesion"""
    print("""
Incie sesión rellenando lo siguiente:""")
    name=input("Nombre del estudiante: ")
    dni_8=input("DNI: ")
    students_sp=dic_est
    for dni in students_sp:
        if (name==students_sp[dni]) and (dni==dni_8):
            niños(name)
            break
        elif (name==students_sp[dni]) and (len(dni_8)!=8):
            error_dni()
        elif (name!=students_sp[dni]) and (dni==dni_8):
            print("""Disculpe, pero el nombre que usted indica
no se encuentra en nuestro sistema""")
#---------------------------------------------------------

def database_students(name_student,dni_st):
    dic_est={}
    dic_est[dni_st]=name_student
    sign_in(dic_est)

#-------------------------------------------------------

def sign_up():
    print("""
Para registrarse con éxito, rellene los siguientes datos""")
    name_student=input("""
Escriba el nombre del estudiante: """)
    while not (len(name_student)>0):
        name_student=input("""Es obligatorio rellenar este dato
Por favor, escribe el nombre del estudiante: """)
    dni_st=input("""Para terminar con el resgistro correctamente escribe
el DNI del estudiante: """)
    while not (len(dni_st)==8):
        dni_st=input("""El DNI consta de 8 caracteres.
Por favor, escribalo de nuevo.
DNI:  """)
    print("Registrado con éxito")
    database_students(name_student,dni_st)

#-------------------------------------------------------

def error_loop():
    """Mensaje de error al
    seleccionar una opción inválida."""
    error=input("""
Opción inválida.

Escribe una de las opciones (Si/No): """)
    error=error.strip()
    error=error.capitalize()
    while not (error=="Si" or error=="No"):
        error=input("""
Opción inválida.

Escrive una de las opciones (Si/No): """)
        error=error.upper()
    options(error)

#------------------------------------------------------

def options(mssg_wllk):
    """Se ejecuta una
    función dependiendo de
    la opción que haya elegido
    el usuario. """
    if mssg_wllk=="Si":
        sign_up()
    elif mssg_wllk=="No":
        print("Está bien, adiós :(")
    else:
        error_loop()

#---------------------------------------------------------

def my_app():
    """Mensaje de bienvenida
    de la app y las opciones
    correspondientes."""
    mssg_wllk=input("""Sea bienvenido a la aplicación
de la movilidad número 11. #DeVueltaAlCole

¿Desea registrarse? (Si/No): """)
    mssg_wllk=mssg_wllk.strip()
    mssg_wllk=mssg_wllk.capitalize()
    options(mssg_wllk)


if __name__=="__main__":
    my_app()

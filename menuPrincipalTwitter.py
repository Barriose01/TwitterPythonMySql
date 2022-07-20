from registroYLoginBD import Conexion
from menuLogin import MenuLogin
cn = Conexion()

while True:
    print("\nElige una opcion: ")
    print("(1): Registro")
    print("(2): Inicio de Sesion")
    print("(3): Salir")
    opcion = input().lower().strip()

    if opcion == "3":
        break
    elif opcion == "1":
        usuario = input("Nombre de usuario: ")
        clave = input("Clave: ")
        clave2 = input("Vuelva a introducir la clave: ")
        if clave == clave2:
            if len(usuario) > 20 or len(clave) > 20:
                print("El nombre de usuario y la clave deben tener un maximo de 20 caracteres")
            elif len(usuario) < 1 or len(clave) < 1:
                print("El nombre de usuario y la clave deben tener un minimo de 1 caracter")
            else:
                usuarioExiste = cn.verificarUsuario(usuario)
                if usuarioExiste == True:
                    print("El usuario ingresado ya existe")
                else:
                    cn.registrarUsuario(usuario,clave)
                    print("Usuario registrado con exito")
        else:
            print("Las claves no coinciden")

    elif opcion == "2":
        usuario = input("Nombre de usuario: ")
        clave = input("Clave: ")
        if len(usuario) > 20 or len(clave) > 20:
            print("El nombre de usuario y la clave deben tener un maximo de 20 caracteres")
        elif len(usuario) < 1 or len(clave) < 1:
            print("El nombre de usuario y la clave deben tener un minimo de 1 caracter")
        else:
            usuarioExiste = cn.verificarUsuarioYClave(usuario,clave)
            if usuarioExiste == True:
                id = cn.getId(usuario)
                menu = MenuLogin(id[0][0], usuario)
                menu.menu()
            else:
                print("Usuario o clave incorrecta. Intentelo de nuevo")

    else:
        print("Ingrese una opcion valida")
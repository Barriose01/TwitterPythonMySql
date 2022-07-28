from registroYLoginBD import Conexion
from menuLogin import MenuLogin
cn = Conexion()

class MenuPrincipal:
    def registro(self):
        while True:
            print("Presione (q) en cualquier momento para volver al menu principal")
            usuario = input("Nombre de usuario: ")
            if usuario.lower().strip() == "q":
                break
            clave = input("Clave: ")
            if clave.lower().strip() == "q":
                break
            clave2 = input("Vuelva a introducir la clave: ")
            if clave2.lower().strip() == "q":
                break
            if clave == clave2:
                if len(usuario) > 20 or len(clave) > 20:
                    print("El nombre de usuario y la clave deben tener un maximo de 20 caracteres")
                elif len(usuario) < 1 or len(clave) < 1:
                    print("El nombre de usuario y la clave deben tener un minimo de 1 caracter")
                else:
                    try:
                        usuarioExiste = cn.verificarUsuario(usuario)
                        if usuarioExiste == True:
                            print("El usuario ingresado ya existe")
                        else:
                            cn.registrarUsuario(usuario,clave)
                            print("Usuario registrado con exito")
                    except:
                        print("Error al registrar la cuenta")
            else:
                print("Las claves no coinciden")
            break

    def login(self):
        while True:
            print("Presione (q) en cualquier momento para volver al menu principal")
            usuario = input("Nombre de usuario: ")
            if usuario.lower().strip() == "q":
                break
            clave = input("Clave: ")
            if clave.lower().strip() == "q":
                break
            if len(usuario) > 20 or len(clave) > 20:
                print("El nombre de usuario y la clave deben tener un maximo de 20 caracteres")
            elif len(usuario) < 1 or len(clave) < 1:
                print("El nombre de usuario y la clave deben tener un minimo de 1 caracter")
            else:
                try:
                    usuarioExiste = cn.verificarUsuarioYClave(usuario,clave)
                    if usuarioExiste == True:
                        id = cn.getId(usuario)
                        menu = MenuLogin(id[0][0], usuario)
                        menu.menu()
                except:
                    print("Error al iniciar sesion")
                else:
                    print("Usuario o clave incorrecta. Intentelo de nuevo")
            break

while True:
    menu = MenuPrincipal()
    print("\nElige una opcion: ")
    print("(1): Registro")
    print("(2): Inicio de Sesion")
    print("(3): Salir")
    opcion = input().lower().strip()

    if opcion == "3":
        break
    elif opcion == "1":
        menu.registro()
    elif opcion == "2":
        menu.login()
    else:
        print("Ingrese una opcion valida")
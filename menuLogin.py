from registroYLoginBD import Conexion
from querysMenuBD import QuerysMenu

cn = Conexion()
q = QuerysMenu()

class MenuLogin:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
    
    def menu(self):
        while True:
            print("\nBienvenid@, " + self.nombre)
            print("(1): Escribir post")
            print("(2): Ver posts de otros usuarios")
            print("(3): Ver tus posts")
            print("(4): Ver tus posts (de mas antiguo a mas reciente)")
            print("(5): Borrar un determinado post")
            print("(6): Borrar todos los posts")
            print("(7): Cerrar sesion")

            opcion = input().lower().strip()
            if opcion == "7":
                break
            elif opcion == "1":
                self.escribirPost()
            elif opcion == "2":
                q.verPostsGlobales()
            elif opcion == "3":
                orden = "recientes"
                publicaciones = q.verTusPosts(self.nombre,orden)
                self.verTusPostsRecientes(publicaciones)
            elif opcion == "4":
                orden = "antiguos"
                publicaciones = q.verTusPosts(self.nombre,orden)
                self.verTusPostsAntiguos(publicaciones)
            elif opcion == "5":
                self.eliminarPost()
            elif opcion == "6":
                self.eliminarTodo()

    def escribirPost(self):
        post = input("Escriba su post: ")
        if(len(post) > 180 or len(post) < 1):
            print("Los posts deben tener un minimo de 1 caracter y un maximo de 180")
        else:
            q.escribirPost(self.id, post)
            print("La publicacion ha sido realizada con exito")

    def verTusPostsRecientes(self,publicaciones):
        if len(publicaciones) > 0:
            for i in range(len(publicaciones)):
                print( "-" +publicaciones[i][1] + ": " + publicaciones[i][2] + ". Publicado en: " + 
                str(publicaciones[i][3]))
        else:
            print("No hay posts para mostrar")

    def verTusPostsAntiguos(self,publicaciones):
        if(len(publicaciones) > 0):
            for i in range(len(publicaciones)):
                print( "-" +publicaciones[i][1] + ": " + publicaciones[i][2] + ". Publicado en: " + 
                str(publicaciones[i][3]))
        else:
            print("No hay posts para mostrar")

    def eliminarPost(self):
        while True:
            publicaciones = q.verTusPosts(self.nombre, "recientes")
            if len(publicaciones) > 0:
                print("Ingrese el indice de la publicacion que desea eliminar")
                for i in range(0,len(publicaciones)):
                    print("(" + str(i) + ") " + publicaciones[i][1] + ": " + publicaciones[i][2] + ". Publicado en: " + 
                    str(publicaciones[i][3]))
                print("(q): Volver")
                opcion = input().lower().strip()
                try:
                    if opcion == "q":
                        break
                    elif int(opcion) < 0 or int(opcion) > len(publicaciones) - 1:
                        print("Debe ingresar una opcion valida")
                    else:
                        idPubliEliminada = publicaciones[int(opcion)][0]
                        q.eliminarPost(idPubliEliminada)
                        print("La publicacion ha sido eliminada con exito")
                        break
                except:
                    print("Debe ingresar una opcion valida")
            else:
                print("No hay posts para eliminar")
                break
    
    def eliminarTodo(self):
        publicaciones = q.verTusPosts(self.nombre, "recientes")
        if len(publicaciones) > 0:
            while True:
                print("Esta seguro de que quiere eliminar todos los posts?")
                print("(1): Si")
                print("(2): No")
                
                opcion = input().lower().strip()
                if opcion == "2":
                    break
                elif opcion == "1":
                    q.eliminarTodosLosPosts(self.id)
                    print("Los registros han sido eliminados con exito")
                    break      
                else:
                    print("Ingrese una opcion valida")
        else:
            print("No hay registros para eliminar")

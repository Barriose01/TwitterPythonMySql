from querysMenuBD import QuerysMenu
q = QuerysMenu()

class MenuLogin:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
    
    def menu(self):
        while True:
            print("\nBienvenid@, " + self.nombre)
            print("(1): Escribir post")
            print("(2): Ver Hashtags mas populares")
            print("(3): Buscar posts por Hashtag")
            print("(4): Ver posts")
            print("(5): Buscar posts por usuario")
            print("(6): Ver tus posts")
            print("(7): Ver tus posts (de mas antiguo a mas reciente)")
            print("(8): Borrar un determinado post")
            print("(9): Borrar todos tus posts")
            print("(10): Cerrar sesion")

            opcion = input().lower().strip()
            if opcion == "10":
                break
            else:
                self.opcionesMenu(opcion)
            

    def opcionesMenu(self,opcion):
        if opcion == "1":
            self.escribirPost()
        elif opcion == "2":
            self.hashtagsPopulares()
        elif opcion == "3":
            print("Presione (q) para volver al menu principal")
            hashtag = input("Ingrese un hashtag para buscar publicaciones relacionadas: ")
            if hashtag.lower().strip() == "q":
                pass
            else:
                try:
                    q.buscarHashtag(hashtag)
                except:
                    print("Error al buscar la publicacion")
        elif opcion == "4":
            try:
                q.verPostsGlobales()
            except:
                print("Error al ver los posts globales")
        elif opcion == "5":
            print("Presione (q) para volver al menu principal")
            usuario = input("Ingrese el nombre del usuario que desea buscar: ")
            if usuario.lower().strip():
                pass
            else:
                try:
                    q.buscarUsuario(usuario)
                except:
                    print("Error al buscar al usuario")
        elif opcion == "6":
            orden = "recientes"
            try:
                publicaciones = q.verTusPosts(self.nombre,orden)
                self.verTusPostsRecientes(publicaciones)
            except:
                print("Error al mostrar los posts del usuario")
        elif opcion == "7":
            orden = "antiguos"
            try:
                publicaciones = q.verTusPosts(self.nombre,orden)
                self.verTusPostsAntiguos(publicaciones)
            except:
                print("Error al mostrar los posts del usuario")
        elif opcion == "8":
            self.eliminarPost()
        elif opcion == "9":
            self.eliminarTodo()

    def obtenerHashtag(self, post):
        hashtags = []
        for i in range(len(post)):
            if post[i] == "#":
                tag1 = post[i:]
                tag2 = tag1.split(" ")[0]
                hashtags.append(tag2)
        return hashtags

    def hashtagsPopulares(self):
        try:
            hashtags = q.verHashtagsPopulares()
            if len(hashtags) > 0:
                for i in range(len(hashtags)):
                    print("(" + str(i + 1) + "): " + hashtags[i][0])
            else:
                print("No hay hashtags para mostrar")
        except:
            print("Error al mostrar los hashtags")

    def escribirPost(self):
        print("Presione (q) para volver al menu principal ")
        post = input("Escriba su post: ")
        if post.lower().strip() == "q":
            pass
        elif(len(post) > 180 or len(post) < 1):
            print("Los posts deben tener un minimo de 1 caracter y un maximo de 180")
        else:
            hashtags = self.obtenerHashtag(post)
            if len(hashtags) < 1:
                try:
                    q.escribirPost(self.id, post)
                    print("La publicacion ha sido realizada con exito")
                except:
                    print("Error al escribir el post")
            else:
                try:
                    ultimoID = q.escribirPost(self.id, post)
                    q.insertarHashtag(ultimoID[0][0], self.id, hashtags)
                    print("La publicacion ha sido realizada con exito")
                except:
                    print("Error al escribir el post")


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
        try:
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
        except:
            print("Error al eliminar los posts")
    
    def eliminarTodo(self):
        try:
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
        except:
            print("Error al eliminar los posts")

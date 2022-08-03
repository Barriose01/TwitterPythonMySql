from registroYLoginBD import Conexion
cn = Conexion()

#Para que funcionen los metodos, debo hacer la conexion y luego cerrar el cursor
class QuerysMenu:
    def escribirPost(self,id, post):
        ultimoID = []
        cn.conectar()
        sql = "CALL escribirPost(%s,%s)"
        cn.cursor.execute(sql,(id,post))
        cn.db.commit()
        #Esto ultimo es para obtener el ultimo id registrado para utilizarlo mas adelante
        sql2 = "SELECT LAST_INSERT_ID()"
        cn.cursor.execute(sql2)
        for x in cn.cursor:
            ultimoID.append(x)
        cn.cursor.close()
        return ultimoID
        
    def insertarHashtag(self, idPost, idUsuario, listaHashtag):
        cn.conectar()
        for i in listaHashtag:
            sql = "CALL insertarHashtags(%s,%s,%s)"
            cn.cursor.execute(sql,(idPost, idUsuario, i))
        cn.db.commit()
        cn.cursor.close()

    def verHashtagsPopulares(self):
        cn.conectar()
        hashtags = []
        sql = "SELECT * FROM hashtagsPopulares"
        cn.cursor.execute(sql)
        for elemento in cn.cursor:
            hashtags.append(elemento)
        cn.cursor.close()
        return hashtags
        
    def buscarHashtag(self, hashtag):
        cn.conectar()
        publicaciones = []
        sql = "CALL buscarHashtag(%s)"
        cn.cursor.execute(sql,(hashtag,))
        for elemento in cn.cursor:
            publicaciones.append(elemento)
        cn.cursor.close()
        if len(publicaciones) > 0:
            publicaciones.reverse()
            print("Resultados para '" + hashtag + "'")
            print(str(len(publicaciones)))
            for i in range(len(publicaciones)):
                print( "-" +publicaciones[i][0] + ": " + publicaciones[i][1] + ". Publicado en: " + 
                str(publicaciones[i][2]))
        else:
            print("No se encontraron post que coincidan con el hashtag ingresado")


    def verPostsGlobales(self):
        cn.conectar()
        publicaciones = []
        sql = "SELECT * FROM vistaPublicacion"
        cn.cursor.execute(sql)
        for elemento in cn.cursor:
            publicaciones.append(elemento)
        if len(publicaciones) > 0:
            publicaciones.reverse()
            for i in range(len(publicaciones)):
                #[i] representa a la fila
                #[1] = nombre de usuario
                #[2] = publicacion
                #[3] = fecha
                print( "-" +publicaciones[i][1] + ": " + publicaciones[i][2] + ". Publicado en: " + 
                str(publicaciones[i][3]))
        else:
            print("No hay posts para mostrar")
        cn.cursor.close()

    def buscarUsuario(self, usuario):
        cn.conectar()
        publicaciones = []
        sql = "CALL buscarUsuario(%s)"
        cn.cursor.execute(sql,(usuario,))
        for elemento in cn.cursor:
            publicaciones.append(elemento)
        if len(publicaciones) > 0:
            publicaciones.reverse()
            print("Resultados para '" + usuario + "': ")
            for i in range(len(publicaciones)):
                print( "-" +publicaciones[i][0] + ": " + publicaciones[i][1] + ". Publicado en: " + 
                str(publicaciones[i][2]))
        else:
            print("No se encontraron post para el usuario '" + usuario + "'")
        cn.cursor.close()


    def verTusPosts(self,usuario,orden):
        cn.conectar()
        publicaciones = []
        sql = "SELECT * FROM vistaPublicacion WHERE nombre = %s"
        cn.cursor.execute(sql,(usuario,))
        for elemento in cn.cursor:
            publicaciones.append(elemento)
        if orden == "recientes":
            publicaciones.reverse()
        else:
            pass
        cn.cursor.close()
        return publicaciones
        

    def eliminarPost(self,id):
        cn.conectar()
        sql = "DELETE FROM publicacionesXhashtags WHERE idPublicacion = %s"
        cn.cursor.execute(sql,(id,))
        sql2 = "DELETE FROM publicaciones WHERE id = %s"
        cn.cursor.execute(sql2,(id,))
        cn.db.commit()
        cn.cursor.close()


    def eliminarTodosLosPosts(self, id):
        cn.conectar()
        sql = "DELETE FROM publicacionesXhashtags WHERE idUsuario = %s"
        cn.cursor.execute(sql,(id,))
        sql2 = "DELETE FROM publicaciones WHERE idUsuario = %s"
        cn.cursor.execute(sql2,(id,))
        cn.db.commit()
        cn.cursor.close()

        
        


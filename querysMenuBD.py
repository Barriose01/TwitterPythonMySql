from registroYLoginBD import Conexion
cn = Conexion()

class QuerysMenu:
    def escribirPost(self,id, post):
        cn.__init__()
        sql = "CALL escribirPost(%s,%s)"
        cn.cursor.execute(sql,(id,post))
        cn.db.commit()
        cn.cursor.close()

    def verPostsGlobales(self):
        cn.__init__()
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

    def verTusPosts(self,usuario,orden):
        cn.__init__()
        publicaciones = []
        sql = "SELECT * FROM vistaPublicacion WHERE nombre = %s"
        cn.cursor.execute(sql,(usuario,))
        for elemento in cn.cursor:
            publicaciones.append(elemento)
        if orden == "recientes":
            publicaciones.reverse()
        else:
            pass
        return publicaciones
        

    def eliminarPost(self,id):
        cn.__init__()
        sql = "DELETE FROM publicaciones WHERE id = %s"
        cn.cursor.execute(sql,(id,))
        cn.db.commit()
        cn.cursor.close()

    def eliminarTodosLosPosts(self, id):
        cn.__init__()
        sql = "DELETE FROM publicaciones WHERE idUsuario = %s"
        cn.cursor.execute(sql,(id,))
        cn.db.commit()
        cn.cursor.close()

        


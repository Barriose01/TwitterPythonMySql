import mysql.connector
class Conexion:
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "twitter"
    )
        self.cursor = self.db.cursor(buffered = True)

        
    def verificarUsuario(self,usuario):
        self.__init__() #Hago esto porque me da error en algunos metodos al usar el cursor no se por que
                        #Lo que hago aqui es abrir la conexion y obtener el cursor. Al terminar
                        #el metodo, cierro el cursor

        usuarios = []
        existeUsuario = False
        sql = "CALL verificarUsuario(%s)"
        self.cursor.execute(sql,(usuario,))

        for elemento in self.cursor:
            usuarios.append(elemento)
        if(len(usuarios) > 0):
            existeUsuario = True
        else:
            existeUsuario = False
        self.cursor.close()    
        return existeUsuario

    def verificarUsuarioYClave(self,usuario,clave):
        self.__init__()
        usuarios = []
        existeUsuario = False
        sql = "CALL verificarUsuarioYClave(%s,%s)"
        self.cursor.execute(sql,(usuario,clave))
        for elemento in self.cursor:
            usuarios.append(elemento)
        if(len(usuarios) > 0):
            existeUsuario = True
        else:
            existeUsuario = False
        self.cursor.close()
        return existeUsuario

    def registrarUsuario(self,usuario,clave):
        self.__init__()
        sql = "CALL registrarUsuario(%s,%s)"
        self.cursor.execute(sql,(usuario,clave))
        self.cursor.close()
        self.db.commit()

    def getId(self,usuario):
        self.__init__()
        usuarios = []
        sql = "SELECT id FROM usuario WHERE nombre = %s"
        self.cursor.execute(sql,(usuario,))
        for elemento in self.cursor:
            usuarios.append(elemento)
        self.cursor.close()
        return usuarios
        
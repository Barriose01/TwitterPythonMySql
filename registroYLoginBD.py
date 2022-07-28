import mysql.connector
class Conexion:
    def conectar(self): #Por alguna razon, tengo que crear este metodo para que me funcione la conexion
        try:
            self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "twitter"
            )
            self.cursor = self.db.cursor(buffered = True)
        except:
            print("Error al hacer la conexion a la base de datos")

        
    def verificarUsuario(self,usuario):
        self.conectar() #Necesito conectar primero y despues cerrar el cursor. No se la razon todavia
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
        self.cursor.close() #Se cierra la conexion. Si no se cierra, me aparece un error de sincronizacion
        return existeUsuario

    def verificarUsuarioYClave(self,usuario,clave):
        self.conectar()
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
        self.conectar()
        sql = "CALL registrarUsuario(%s,%s)"
        self.cursor.execute(sql,(usuario,clave))
        self.db.commit()
        self.cursor.close()

    def getId(self,usuario):
        self.conectar()
        usuarios = []
        sql = "SELECT id FROM usuario WHERE nombre = %s"
        self.cursor.execute(sql,(usuario,))
        for elemento in self.cursor:
            usuarios.append(elemento)
        self.cursor.close()
        return usuarios
        
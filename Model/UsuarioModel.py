
class UsuarioModel:
    def __init__(self, ID=None, NOME=None):
        self.id = ID
        self.nome = NOME
        
    def obter_usuario(self, conn, id):
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM USUARIOS WHERE ID = {id}")
            row = cursor.fetchone()
            cursor.close()
            obj = UsuarioModel(**row)
            
            return obj
        except:
            return None
        
    def criar_usuario(self, conn, nome):
        try:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO USUARIOS (NOME) VALUES ('{nome}')")
            conn.commit()
            cursor.close()
            return True
        except Exception as ex:
            print(ex)
            return False
        
    @staticmethod
    def usuario_existe(conn , nome):
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM USUARIOS WHERE NOME = '{nome}'")
            row = cursor.fetchone()
            cursor.close()
            if row:
                return True
            else:
                return False
        except Exception as ex:
            print(ex)
            return None
        
    @staticmethod
    def deletar_todos_usuarios(conn):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM USUARIOS")
            conn.commit()
            cursor.close()
            
            return True
        except Exception as ex:
            print(ex)
            return False


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
        except Exception as ex:
            print(ex)

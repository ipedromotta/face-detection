from Controller.ConnectionDBController import ConnectionDBController
from Model.UsuarioModel import UsuarioModel


class CadastroController:
    def __init__(self, INTERFACE_CADASTRO) -> None:
        self.conn = ConnectionDBController.getConnection()
        self.conn.row_factory = ConnectionDBController.dict_factory
        self.ui_cadastro = INTERFACE_CADASTRO
     

    def cadastrar_usuario(self):
        nome = self.ui_cadastro.ui.inptNome.text()
        if nome == '':
            self.ui_cadastro.set_message("Preencha seu nome")
        else:
            self.ui_cadastro.set_message("")
            cadastrou = UsuarioModel().criar_usuario(self.conn, nome)
            if cadastrou:
                self.ui_cadastro.success()
            else:
                self.ui_cadastro.set_message("Algo deu errado")
            

import os

from Controller.ConnectionDBController import ConnectionDBController
from Controller.ReconhecimentoFacialController import ReconhecimentoFacialController
from Model.UsuarioModel import UsuarioModel


class CadastroController:
    def __init__(self, INTERFACE_CADASTRO) -> None:
        self.conn = ConnectionDBController.getConnection()
        self.conn.row_factory = ConnectionDBController.dict_factory
        self.ui_cadastro = INTERFACE_CADASTRO

    def cadastrar_usuario(self):
        try:
            nome = self.ui_cadastro.ui.inptNome.text()
            if nome == '':
                self.ui_cadastro.set_message.emit("Preencha seu nome")
                
            elif UsuarioModel.usuario_existe(self.conn, nome):
                self.ui_cadastro.set_message.emit("Esse usuario já existe")
            else:
                self.ui_cadastro.set_message.emit("")
                self.ui_cadastro.ui.btnConfirmar.setEnabled(False)
                cadastrou = UsuarioModel().criar_usuario(self.conn, nome)
                if cadastrou:
                    self.ui_cadastro.set_message.emit("Aguarde, detectando seu rosto...")
                    ReconhecimentoFacialController().run_thread_cadastro(nome, self.ui_cadastro)
                    
                else:
                    self.ui_cadastro.set_message.emit("Algo deu errado")
                    self.ui_cadastro.ui.btnConfirmar.setEnabled(True)
        except Exception as ex:
            print(ex)
                
    def deletar_todos_usuarios(self, interface):
        try:
            bancoimagens = './Content/bancoimagens'
            deletou = UsuarioModel.deletar_todos_usuarios(self.conn)
            if deletou:
                imgs = tuple(imagem for imagem in os.listdir(bancoimagens) if '.png' in imagem)
                for img in imgs:
                    os.remove(f'{bancoimagens}/{img}')
                    
                interface.set_message.emit('Usuarios deletados com sucesso')
            else:
                interface.set_message.emit('Não foi possivel deletar os usuarios')
                
        except Exception as ex:
            interface.set_message.emit('Algo deu errado')
            print(ex)
            
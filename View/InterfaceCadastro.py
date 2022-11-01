from PyQt5 import QtWidgets

from View.Cadastro import Ui_Cadastro
from Content.Layout import Layout
from Controller.CadastroController import CadastroController


class InterfaceCadastro:
    def __init__(self) -> None:
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self.window)
        self.cadastro_controller = CadastroController(self)
        self.init_buttons()
        self.window.setModal(True)
        
    def show(self) -> None:
        Layout.show_modal_box(self)
        if not self.window.exec_():
            self.modal_box.close()
            
    def set_message(self, msg:str) -> None:
        self.ui.inptMsg.setStyleSheet("color:#df4759;")
        self.ui.inptMsg.setText(msg)
        
    def success(self) -> None:
        self.set_message("Usuario cadastrado com sucesso")
        self.ui.inptMsg.setStyleSheet("color: #198754;")
        
    def init_buttons(self) -> None:
        self.ui.btnConfirmar.clicked.connect(lambda: self.cadastro_controller.cadastrar_usuario())

from PyQt5 import QtWidgets, QtCore

from View.Cadastro import Ui_Cadastro
from Content.Layout import Layout
from Controller.CadastroController import CadastroController


class InterfaceCadastro(QtCore.QObject):
    set_message = QtCore.pyqtSignal(str)
    set_success = QtCore.pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self.window)
        self.cadastro_controller = CadastroController(self)
        
        self.set_message.connect(self.message)
        self.set_success.connect(self.success)
        
        self.init_buttons()
        self.window.setModal(True)
        
    def show(self) -> None:
        Layout.show_modal_box(self)
        if not self.window.exec_():
            self.modal_box.close()
            
    @QtCore.pyqtSlot(str)
    def message(self, msg:str) -> None:
        self.ui.inptMsg.setStyleSheet("color:#df4759;")
        self.ui.inptMsg.setText(msg)
        
    @QtCore.pyqtSlot()
    def success(self) -> None:
        self.ui.inptMsg.setText("Usuario cadastrado com sucesso")
        self.ui.inptMsg.setStyleSheet("color: #198754;")
        self.ui.btnConfirmar.setEnabled(True)
        
    def init_buttons(self) -> None:
        self.ui.btnConfirmar.clicked.connect(lambda: self.cadastro_controller.cadastrar_usuario())

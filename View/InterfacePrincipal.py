from PyQt5 import QtWidgets, QtCore

from View.TelaPrincipal import Ui_TelaPrincipal
from View.InterfaceCadastro import InterfaceCadastro

from Controller.ReconhecimentoFacialController import ReconhecimentoFacialController
from Controller.CadastroController import CadastroController


class InterfacePrincipal(QtCore.QObject):
    set_message = QtCore.pyqtSignal(str)
    
    def __init__(self) -> None:
        super().__init__()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TelaPrincipal()
        self.ui.setupUi(self.window)
        self.ui_cadastro = InterfaceCadastro()
        self.set_message.connect(self.message)
        self.init_buttons()
        
    def show(self):
        self.window.show()
        
    @QtCore.pyqtSlot(str)
    def message(self, msg:str) -> None:
        self.ui.inptResposta.setText(msg)
        
    def init_buttons(self):
        self.ui.btnCadastrar.clicked.connect(lambda: self.ui_cadastro.show())
        self.ui.btnReconhecer.clicked.connect(lambda: ReconhecimentoFacialController().reconhecer_rosto(self))
        self.ui.actionDeletar_todos_os_cadastros.triggered.connect(lambda: self.ui_cadastro.cadastro_controller.deletar_todos_usuarios(self))

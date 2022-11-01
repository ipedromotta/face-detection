from PyQt5 import QtWidgets

from View.TelaPrincipal import Ui_TelaPrincipal
from View.InterfaceCadastro import InterfaceCadastro


class InterfacePrincipal:
    def __init__(self) -> None:
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TelaPrincipal()
        self.ui.setupUi(self.window)
        self.ui_cadastro = InterfaceCadastro()
        self.init_buttons()
        
    def show(self):
        self.window.show()
        
    def init_buttons(self):
        self.ui.btnCadastrar.clicked.connect(lambda: self.ui_cadastro.show())
        self.ui.btnReconhecer.clicked.connect(lambda: print("Reconhecer"))

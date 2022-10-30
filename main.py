import sys

from PyQt5 import QtWidgets

from View.TelaPrincipal import Ui_TelaPrincipal


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        
        window = QtWidgets.QMainWindow()
        tela = Ui_TelaPrincipal()
        tela.setupUi(window)
        window.show()
        
        
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)
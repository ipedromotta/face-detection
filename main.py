import sys

from PyQt5 import QtWidgets

from View.InterfacePrincipal import InterfacePrincipal


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        
        interface = InterfacePrincipal()
        interface.show()
        
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)
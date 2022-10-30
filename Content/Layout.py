from PyQt5 import QtWidgets, QtCore

from View.ModalBox import Ui_ModalBox


class Layout:
    
    @staticmethod
    def show_modal_box(self):
        self.modal_box = QtWidgets.QDialog()
        Ui_ModalBox().setupUi(self.modal_box)
        self.modal_box.setWindowModality(QtCore.Qt.NonModal)
        self.modal_box.showFullScreen()

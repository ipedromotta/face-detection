# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/ModalBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore


class Ui_ModalBox(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setWindowOpacity(0.8)
        Dialog.setStyleSheet("background-color: #000")
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

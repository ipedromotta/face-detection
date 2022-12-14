# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cadastro(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(312, 303)
        Cadastro.setStyleSheet("QWidget{\n"
"background-color: #fff;\n"
"color: #000\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Cadastro)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblHeader = QtWidgets.QLabel(Cadastro)
        self.lblHeader.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeader.setFont(font)
        self.lblHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeader.setObjectName("lblHeader")
        self.verticalLayout.addWidget(self.lblHeader)
        self.inptNome = QtWidgets.QLineEdit(Cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inptNome.setFont(font)
        self.inptNome.setStyleSheet("*{border-radius: 5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: #DADADA;\n"
"padding:5px;\n"
"}\n"
":focus{\n"
"border-color: #5C7AEA;\n"
"}")
        self.inptNome.setMaxLength(15)
        self.inptNome.setCursorPosition(0)
        self.inptNome.setObjectName("inptNome")
        self.verticalLayout.addWidget(self.inptNome)
        self.inptMsg = QtWidgets.QLabel(Cadastro)
        self.inptMsg.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inptMsg.setFont(font)
        self.inptMsg.setStyleSheet("color:#df4759;")
        self.inptMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.inptMsg.setWordWrap(True)
        self.inptMsg.setObjectName("inptMsg")
        self.verticalLayout.addWidget(self.inptMsg)
        self.btnConfirmar = QtWidgets.QPushButton(Cadastro)
        self.btnConfirmar.setEnabled(True)
        self.btnConfirmar.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnConfirmar.setFont(font)
        self.btnConfirmar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirmar.setStyleSheet("*{border-radius: 5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: #DADADA;\n"
"background-color: #3D56B2;\n"
"color: white;\n"
"padding:5px;\n"
"}\n"
"::hover{\n"
"background-color: #5C7AEA;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: #A0A0A0;\n"
"color: #797979;\n"
"}\n"
"")
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.verticalLayout.addWidget(self.btnConfirmar)

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Cadastre-se"))
        self.lblHeader.setText(_translate("Cadastro", "Cadastre-se"))
        self.inptNome.setPlaceholderText(_translate("Cadastro", "Digite seu nome"))
        self.inptMsg.setText(_translate("Cadastro", ""))
        self.btnConfirmar.setText(_translate("Cadastro", "Cadastrar"))

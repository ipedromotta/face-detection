# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName("TelaPrincipal")
        TelaPrincipal.resize(650, 370)
        TelaPrincipal.setMinimumSize(QtCore.QSize(650, 370))
        TelaPrincipal.setMaximumSize(QtCore.QSize(650, 370))
        TelaPrincipal.setStyleSheet("QWidget{\n"
"background-color: #fff;\n"
"color: #000\n"
"}")
        self.bodyWidget = QtWidgets.QWidget(TelaPrincipal)
        self.bodyWidget.setObjectName("bodyWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bodyWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(self.bodyWidget)
        self.lblTitulo.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setTextFormat(QtCore.Qt.AutoText)
        self.lblTitulo.setScaledContents(False)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setWordWrap(True)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.lblSubTitulo = QtWidgets.QLabel(self.bodyWidget)
        self.lblSubTitulo.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        self.lblSubTitulo.setFont(font)
        self.lblSubTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSubTitulo.setObjectName("lblSubTitulo")
        self.verticalLayout.addWidget(self.lblSubTitulo)
        self.respostaWidget = QtWidgets.QWidget(self.bodyWidget)
        self.respostaWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.respostaWidget.setObjectName("respostaWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.respostaWidget)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(6, -1, 6, -1)
        self.formLayout_2.setHorizontalSpacing(12)
        self.formLayout_2.setObjectName("formLayout_2")
        self.iconResposta = QtWidgets.QLabel(self.respostaWidget)
        self.iconResposta.setMinimumSize(QtCore.QSize(30, 30))
        self.iconResposta.setStyleSheet("")
        self.iconResposta.setText("")
        self.iconResposta.setScaledContents(False)
        self.iconResposta.setAlignment(QtCore.Qt.AlignCenter)
        self.iconResposta.setObjectName("iconResposta")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iconResposta)
        self.inptResposta = QtWidgets.QLabel(self.respostaWidget)
        self.inptResposta.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.inptResposta.setFont(font)
        self.inptResposta.setText("")
        self.inptResposta.setScaledContents(False)
        self.inptResposta.setAlignment(QtCore.Qt.AlignCenter)
        self.inptResposta.setObjectName("inptResposta")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inptResposta)
        self.verticalLayout.addWidget(self.respostaWidget)
        self.btnWidget = QtWidgets.QWidget(self.bodyWidget)
        self.btnWidget.setObjectName("btnWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.btnWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnReconhecer = QtWidgets.QPushButton(self.btnWidget)
        self.btnReconhecer.setMinimumSize(QtCore.QSize(200, 80))
        self.btnReconhecer.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnReconhecer.setFont(font)
        self.btnReconhecer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnReconhecer.setStyleSheet("*{border-radius: 5px;\n"
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
"")
        self.btnReconhecer.setObjectName("btnReconhecer")
        self.horizontalLayout.addWidget(self.btnReconhecer)
        self.btnCadastrar = QtWidgets.QPushButton(self.btnWidget)
        self.btnCadastrar.setMinimumSize(QtCore.QSize(200, 80))
        self.btnCadastrar.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCadastrar.setStyleSheet("*{border-radius: 5px;\n"
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
"")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.horizontalLayout.addWidget(self.btnCadastrar)
        self.verticalLayout.addWidget(self.btnWidget)
        TelaPrincipal.setCentralWidget(self.bodyWidget)
        self.menuBar = QtWidgets.QMenuBar(TelaPrincipal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuConfiguracao = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguracao.setObjectName("menuConfiguracao")
        TelaPrincipal.setMenuBar(self.menuBar)
        self.actionDeletar_todos_os_cadastros = QtWidgets.QAction(TelaPrincipal)
        self.actionDeletar_todos_os_cadastros.setObjectName("actionDeletar_todos_os_cadastros")
        self.menuConfiguracao.addAction(self.actionDeletar_todos_os_cadastros)
        self.menuBar.addAction(self.menuConfiguracao.menuAction())

        self.retranslateUi(TelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

    def retranslateUi(self, TelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "Reconhecimento Facial"))
        self.lblTitulo.setText(_translate("TelaPrincipal", "Sistema de reconhecimento facial"))
        self.lblSubTitulo.setText(_translate("TelaPrincipal", "O que deseja fazer?"))
        self.btnReconhecer.setText(_translate("TelaPrincipal", "Reconhecer"))
        self.btnCadastrar.setText(_translate("TelaPrincipal", "Cadastrar"))
        self.menuConfiguracao.setTitle(_translate("TelaPrincipal", "Configuracao"))
        self.actionDeletar_todos_os_cadastros.setText(_translate("TelaPrincipal", "Deletar todos os cadastros"))

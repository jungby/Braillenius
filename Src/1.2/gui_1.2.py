from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser as web

import translator_info
import py_to_scad


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 440)
        MainWindow.setMinimumSize(QtCore.QSize(710, 440))
        MainWindow.setMaximumSize(QtCore.QSize(710, 440))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("libro_braille.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(72, 202, 228);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.traducir = QtWidgets.QPushButton(self.centralwidget)
        self.traducir.setGeometry(QtCore.QRect(490, 90, 111, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.traducir.sizePolicy().hasHeightForWidth())
        self.traducir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.traducir.setFont(font)
        self.traducir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.traducir.setAcceptDrops(False)
        self.traducir.setAutoFillBackground(False)
        self.traducir.setStyleSheet("QPushButton:hover {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(0, 180, 216);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 150, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.traducir.setDefault(False)
        self.traducir.setFlat(False)
        self.traducir.setObjectName("traducir")
        self.save_astxt = QtWidgets.QPushButton(self.centralwidget)
        self.save_astxt.setGeometry(QtCore.QRect(380, 360, 311, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_astxt.sizePolicy().hasHeightForWidth())
        self.save_astxt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.save_astxt.setFont(font)
        self.save_astxt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_astxt.setAcceptDrops(False)
        self.save_astxt.setAutoFillBackground(False)
        self.save_astxt.setStyleSheet("QPushButton:hover {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(0, 180, 216);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 150, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.save_astxt.setDefault(False)
        self.save_astxt.setFlat(False)
        self.save_astxt.setObjectName("save_astxt")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(500, 270, 91, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setAcceptDrops(False)
        self.reset.setAutoFillBackground(False)
        self.reset.setStyleSheet("QPushButton:hover {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(0, 180, 216);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 150, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.reset.setDefault(False)
        self.reset.setFlat(False)
        self.reset.setObjectName("reset")
        self.spanish_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.spanish_txt.setGeometry(QtCore.QRect(30, 50, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spanish_txt.setFont(font)
        self.spanish_txt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.spanish_txt.setStyleSheet("background-color: rgb(202, 240, 248);")
        self.spanish_txt.setObjectName("spanish_txt")
        self.braille_result = QtWidgets.QTextEdit(self.centralwidget)
        self.braille_result.setGeometry(QtCore.QRect(30, 200, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.braille_result.setFont(font)
        self.braille_result.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.braille_result.setStyleSheet("background-color: rgb(202, 240, 248);")
        self.braille_result.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.braille_result.setPlaceholderText("")
        self.braille_result.setObjectName("braille_result")
        self.save_as3d = QtWidgets.QPushButton(self.centralwidget)
        self.save_as3d.setGeometry(QtCore.QRect(460, 150, 171, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as3d.sizePolicy().hasHeightForWidth())
        self.save_as3d.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.save_as3d.setFont(font)
        self.save_as3d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_as3d.setAcceptDrops(False)
        self.save_as3d.setAutoFillBackground(False)
        self.save_as3d.setStyleSheet("QPushButton:hover {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(0, 180, 216);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 150, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.save_as3d.setDefault(False)
        self.save_as3d.setFlat(False)
        self.save_as3d.setObjectName("save_as3d")
        self.report = QtWidgets.QPushButton(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(470, 210, 151, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report.sizePolicy().hasHeightForWidth())
        self.report.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.report.setFont(font)
        self.report.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report.setAcceptDrops(False)
        self.report.setAutoFillBackground(False)
        self.report.setStyleSheet("QPushButton:hover {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(0, 180, 216);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 150, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.report.setDefault(False)
        self.report.setFlat(False)
        self.report.setObjectName("report")
        self.entry_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_filename.setGeometry(QtCore.QRect(30, 360, 331, 31))
        self.entry_filename.setStyleSheet("background-color: rgb(202, 240, 248);")
        self.entry_filename.setObjectName("entry_filename")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #------------ no tocar ------------#
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #------------ triggers ---------------#
        self.reset.released.connect(self.spanish_txt.clear)
        self.reset.released.connect(self.braille_result.clear)
        self.traducir.clicked.connect(self.traducir_clicked)
        self.save_astxt.clicked.connect(self.saveastxt_clicked)
        self.save_as3d.clicked.connect(self.saveas3d_clicked)
        self.report.clicked.connect(self.reportar)

    def traducir_clicked(self):

        original = self.spanish_txt.toPlainText()
        traducido = translator_info.tradBraille(original)
        self.braille_result.setText(traducido)


    def saveastxt_clicked(self):
        if self.entry_filename.text() != "" and " ":

            inputname = self.entry_filename.text()

            with open(f'{inputname}.txt', 'w', encoding='utf-8') as f:
                original = self.spanish_txt.toPlainText()   
                tradastxt = self.braille_result.toPlainText()

                f.write("Español:");f.write("\n\n");f.write(original);f.write("\n\n")
                f.write("Braille:");f.write("\n\n");f.write(tradastxt)

                self.show_popup("Guardado", "El documento ha sido guardado con éxito")
        else:
            self.show_popup("Atención", "Debe ingresar un nombre para el archivo")

        return inputname

    def saveas3d_clicked(self):
        if self.entry_filename.text() != "" and " ":
            py_to_scad.pytoscad(self.entry_filename.text(), self.spanish_txt.toPlainText())
            py_to_scad.conversion(self.entry_filename.text())        # UNCOMMENT TO HAVE THE STL FILE INSTEAD OF JUST .SCAD
            self.show_popup("Guardado", "El archivo 3D ha sido guardado con éxito")
        else:
            self.show_popup("Atención", "Debe ingresar un nombre para el archivo")

    def reportar(self):
        web.open("https://mail.google.com/mail/?view=cm&fs=1&to=lauraequisde@gmail.com&su=Bug%20Report") 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Braillenius"))
        self.traducir.setText(_translate("MainWindow", "Traducir"))
        self.save_astxt.setText(_translate("MainWindow", "Guardar como documento de texto"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.spanish_txt.setPlaceholderText(_translate("MainWindow", "Ingrese el texto que desea traducir. "))
        self.entry_filename.setPlaceholderText(_translate("MainWindow", "Ingrese un nombre para guardar/crear modelo 3D. "))
        self.save_as3d.setText(_translate("MainWindow", "Crear modelo 3D"))
        self.report.setText(_translate("MainWindow", "Reportar error"))

    def show_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import translator_info
import sys, datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 631)
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
        self.traducir.setGeometry(QtCore.QRect(90, 260, 251, 36))
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
        self.guardar = QtWidgets.QPushButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(240, 520, 221, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guardar.sizePolicy().hasHeightForWidth())
        self.guardar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.guardar.setFont(font)
        self.guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.guardar.setAcceptDrops(False)
        self.guardar.setAutoFillBackground(False)
        self.guardar.setStyleSheet("QPushButton:hover {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(0, 180, 216);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 150, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.guardar.setDefault(False)
        self.guardar.setFlat(False)
        self.guardar.setObjectName("guardar")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(300, 560, 101, 36))
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
        self.traducir_2 = QtWidgets.QPushButton(self.centralwidget)
        self.traducir_2.setGeometry(QtCore.QRect(370, 260, 251, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.traducir_2.sizePolicy().hasHeightForWidth())
        self.traducir_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.traducir_2.setFont(font)
        self.traducir_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.traducir_2.setAcceptDrops(False)
        self.traducir_2.setAutoFillBackground(False)
        self.traducir_2.setStyleSheet("QPushButton:hover {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(0, 180, 216);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 150, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.traducir_2.setDefault(False)
        self.traducir_2.setFlat(False)
        self.traducir_2.setObjectName("traducir_2")
        self.espbra = QtWidgets.QTextEdit(self.centralwidget)
        self.espbra.setGeometry(QtCore.QRect(40, 50, 621, 192))
        self.espbra.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.espbra.setStyleSheet("background-color: rgb(202, 240, 248);")
        self.espbra.setObjectName("espbra")
        self.braesp = QtWidgets.QTextEdit(self.centralwidget)
        self.braesp.setGeometry(QtCore.QRect(40, 320, 621, 192))
        self.braesp.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.braesp.setStyleSheet("background-color: rgb(202, 240, 248);")
        self.braesp.setObjectName("braesp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # --------------- triggers ----------------
        self.retranslateUi(MainWindow)
        self.reset.released.connect(self.espbra.clear)
        self.reset.released.connect(self.braesp.clear)
        self.traducir.clicked.connect(self.button_clicked1)
        self.traducir_2.clicked.connect(self.button_clicked2)
        self.guardar.clicked.connect(self.button_clicked3)

    def button_clicked1(self):
        espbra = self.espbra.toPlainText()
        yatraducido = translator_info.tradBraille(espbra)
        self.braesp.setText(yatraducido)

    def button_clicked2(self):
        braesp = self.braesp.toPlainText()
        yatraducido = translator_info.tradEsp(braesp)
        self.espbra.setText(yatraducido)        

    def button_clicked3(self):
        t = datetime.datetime.now()
        current_time = t.strftime("%H:%M:%S %d-%m-%Y")
        namefile = current_time.replace(":", "" )

        with open(f'traduccion{namefile}.txt', 'w', encoding='utf-8') as f:
            original = self.espbra.toPlainText()   
            tradastxt = self.braesp.toPlainText()

            f.write("Español:");f.write("\n");f.write(original);f.write("\n\n")
            f.write("Braille:");f.write("\n");f.write(tradastxt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Braillenius"))
        self.traducir.setText(_translate("MainWindow", "Traducir Español - Braille"))
        self.guardar.setText(_translate("MainWindow", "Guardar como .txt"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.traducir_2.setText(_translate("MainWindow", "Traducir Braille - Español"))
        self.espbra.setPlaceholderText(_translate("MainWindow", "Ingrese el texto que desea traducir. "))
        self.braesp.setPlaceholderText(_translate("MainWindow", "Ingrese el texto que desea traducir. "))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
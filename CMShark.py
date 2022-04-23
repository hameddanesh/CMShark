import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from Sniffer import Sniffer
from Worker import Worker


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.sniffer = Sniffer()
        self

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 640)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 640))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setToolTip("")
        MainWindow.setAccessibleName("")
        MainWindow.setStyleSheet("background-color:#1f1f29;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.help = QtWidgets.QScrollArea(self.centralwidget)
        self.help.setWidgetResizable(True)
        self.help.setObjectName("help")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 1018, 1224))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setMinimumSize(QtCore.QSize(0, 700))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./tulpar.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMinimumSize(QtCore.QSize(1000, 500))
        self.label_5.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./tulpar.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.help.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.help)
        self.start = QtWidgets.QFrame(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(0, 0, 1024, 610))
        self.start.setStyleSheet("border:none;")
        self.start.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.start.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start.setObjectName("start")
        self.label = QtWidgets.QLabel(self.start)
        self.label.setGeometry(QtCore.QRect(120, 60, 190, 31))
        self.label.setStyleSheet(
            "background-color:#8a8a8b; border-radius:3px;font-size:18px")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.interfaceList = QtWidgets.QListWidget(self.start)
        self.interfaceList.setGeometry(QtCore.QRect(120, 160, 780, 221))
        self.interfaceList.setStyleSheet("background-color:#24242f;")
        self.interfaceList.setUniformItemSizes(False)
        self.interfaceList.setObjectName("interfaceList")

        self.label_2 = QtWidgets.QLabel(self.start)
        self.label_2.setGeometry(QtCore.QRect(120, 130, 591, 19))
        self.label_2.setAccessibleDescription("")
        self.label_2.setStyleSheet("color:#8a8a8b;")
        self.label_2.setObjectName("label_2")
        self.beginBtn = QtWidgets.QPushButton(self.start)
        self.beginBtn.setGeometry(QtCore.QRect(790, 530, 101, 31))
        self.beginBtn.setStyleSheet(
            "background-color:#477a62;border-radius:3px;")
        self.beginBtn.setObjectName("beginBtn")
        self.beginBtn.clicked.connect(self.BeginBtnOnClick)
        self.label_3 = QtWidgets.QLabel(self.start)
        self.label_3.setGeometry(QtCore.QRect(120, 410, 591, 19))
        self.label_3.setAccessibleDescription("")
        self.label_3.setStyleSheet("color:#8a8a8b;")
        self.label_3.setObjectName("label_3")
        self.payloadScanner = QtWidgets.QCheckBox(self.start)
        self.payloadScanner.setGeometry(QtCore.QRect(130, 466, 500, 20))
        self.payloadScanner.setChecked(True)
        self.payloadScanner.setObjectName("payloadScanner")
        self.mlScanner = QtWidgets.QCheckBox(self.start)
        self.mlScanner.setGeometry(QtCore.QRect(130, 492, 500, 20))
        self.mlScanner.setChecked(True)
        self.mlScanner.setObjectName("mlScanner")
        self.urlScanner = QtWidgets.QCheckBox(self.start)
        self.urlScanner.setGeometry(QtCore.QRect(130, 440, 500, 20))
        self.urlScanner.setChecked(True)
        self.urlScanner.setObjectName("urlScanner")
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(0, 0, 1024, 610))
        self.main.setStyleSheet("border:none")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.label_6 = QtWidgets.QLabel(self.main)
        self.label_6.setGeometry(QtCore.QRect(120, 97, 591, 19))
        self.label_6.setAccessibleDescription("")
        self.label_6.setStyleSheet("color:#8a8a8b;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.main)
        self.label_7.setGeometry(QtCore.QRect(120, 50, 90, 21))
        self.label_7.setStyleSheet("color: #33ab74;font-size:25px;")
        self.label_7.setObjectName("label_7")
        self.statusLabel = QtWidgets.QLabel(self.main)
        self.statusLabel.setGeometry(QtCore.QRect(210, 50, 90, 26))
        self.statusLabel.setStyleSheet("")
        self.statusLabel.setObjectName("statusLabel")
        self.mlScanner_2 = QtWidgets.QCheckBox(self.main)
        self.mlScanner_2.setGeometry(QtCore.QRect(130, 180, 500, 20))
        self.mlScanner_2.setChecked(True)
        self.mlScanner_2.setObjectName("mlScanner_2")
        self.mlScanner_2.setDisabled(True);
        self.urlScanner_2 = QtWidgets.QCheckBox(self.main)
        self.urlScanner_2.setGeometry(QtCore.QRect(130, 128, 500, 20))
        self.urlScanner_2.setChecked(True)
        self.urlScanner_2.setObjectName("urlScanner_2")
        self.urlScanner_2.setDisabled(True);
        self.payloadScanner_2 = QtWidgets.QCheckBox(self.main)
        self.payloadScanner_2.setGeometry(QtCore.QRect(130, 154, 500, 20))
        self.payloadScanner_2.setChecked(True)
        self.payloadScanner_2.setObjectName("payloadScanner_2")
        self.payloadScanner_2.setDisabled(True);
        self.detectionTable = QtWidgets.QTableWidget(self.main)
        self.detectionTable.setGeometry(QtCore.QRect(120, 220, 784, 271))
        self.detectionTable.setStyleSheet(
            "background-color: rgba(138, 138, 139,50);")
        self.detectionTable.setShowGrid(True)
        self.detectionTable.setObjectName("detectionTable")
        self.detectionTable.setColumnCount(4)
        self.detectionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detectionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detectionTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detectionTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detectionTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detectionTable.horizontalHeader().setDefaultSectionSize(190)
        self.detectionTable.horizontalHeader().setSortIndicatorShown(False)
        self.help.raise_()
        self.start.raise_()
        self.main.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 24))
        self.menubar.setObjectName("menubar")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuhelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuhelp_2.setObjectName("menuhelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.start.show()
        self.main.hide()
        self.help.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CMShark"))
        self.label.setText(_translate("MainWindow", "Welcome to CMShark"))
        self.label_2.setText(_translate(
            "MainWindow", "please choose an interface from list below"))
        self.beginBtn.setText(_translate("MainWindow", "begin"))
        self.label_3.setText(_translate("MainWindow", "scan policy"))
        self.payloadScanner.setText(_translate(
            "MainWindow", "payload inspector"))
        self.mlScanner.setText(_translate("MainWindow", "ML detector"))
        self.urlScanner.setText(_translate("MainWindow", "url scanner"))
        self.label_6.setText(_translate("MainWindow", "scan policy"))
        self.label_7.setText(_translate("MainWindow", "status:"))
        self.statusLabel.setText(_translate("MainWindow", "running"))
        self.mlScanner_2.setText(_translate("MainWindow", "ML detector"))
        self.urlScanner_2.setText(_translate("MainWindow", "url scanner"))
        self.payloadScanner_2.setText(
            _translate("MainWindow", "payload inspector"))
        self.detectionTable.setSortingEnabled(False)
        item = self.detectionTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ip"))
        item.setBackground(QtGui.QColor(255,255,255))
        item = self.detectionTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "detected by"))
        item.setBackground(QtGui.QColor(255,255,255))
        item = self.detectionTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "curtainity"))
        item.setBackground(QtGui.QColor(255,255,255))
        item = self.detectionTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "info"))
        item.setBackground(QtGui.QColor(255,255,255))


        self.SetInterfaces(self.sniffer.GetInterfaces())

    def AddInterface(self, interface):
        self.interfaceList.addItem(interface)

    def SetInterfaces(self, interfaces):
        for interface in interfaces():
            self.AddInterface(interface)

    def BeginBtnOnClick(self):
        self.urlScanner_2.setChecked(self.urlScanner.isChecked())
        self.payloadScanner_2.setChecked(self.payloadScanner.isChecked())
        self.mlScanner_2.setChecked(self.mlScanner.isChecked())

        self.sniffer.SetInterface(self.interfaceList.currentItem().text())
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self.sniffer,self.detectionTable, self.urlScanner_2.isChecked(
        ), self.payloadScanner_2.isChecked(), self.mlScanner_2.isChecked())
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Step 6: Start the thread
        self.thread.start()
        self.start.hide()
        self.main.show()

    def BackBtnOnClick(self):
        self.worker.stop()
        self.thread.quit()

        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
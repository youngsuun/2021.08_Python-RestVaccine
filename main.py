# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\pythonProject\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 752)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/로고_아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.maintxt_2 = QtWidgets.QLabel(self.centralwidget)
        self.maintxt_2.setGeometry(QtCore.QRect(80, 410, 251, 21))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(8)
        self.maintxt_2.setFont(font)
        self.maintxt_2.setObjectName("maintxt_2")
        self.maintxt_4 = QtWidgets.QLabel(self.centralwidget)
        self.maintxt_4.setGeometry(QtCore.QRect(80, 450, 251, 16))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(8)
        self.maintxt_4.setFont(font)
        self.maintxt_4.setObjectName("maintxt_4")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(160, 170, 101, 91))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/background/로고_연한거 (1).png"))
        self.logo.setObjectName("logo")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 620, 331, 51))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.maintxt_1 = QtWidgets.QLabel(self.centralwidget)
        self.maintxt_1.setGeometry(QtCore.QRect(60, 370, 291, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        self.maintxt_1.setFont(font)
        self.maintxt_1.setObjectName("maintxt_1")
        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(50, 0, 411, 571))
        self.bg_2.setText("")
        self.bg_2.setPixmap(QtGui.QPixmap(":/background/bg.png"))
        self.bg_2.setObjectName("bg_2")
        self.bg_3 = QtWidgets.QLabel(self.centralwidget)
        self.bg_3.setGeometry(QtCore.QRect(90, 50, 241, 331))
        self.bg_3.setText("")
        self.bg_3.setPixmap(QtGui.QPixmap(":/background/bg_2.png"))
        self.bg_3.setObjectName("bg_3")
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setGeometry(QtCore.QRect(10, 0, 501, 551))
        self.bg_1.setText("")
        self.bg_1.setPixmap(QtGui.QPixmap(":/background/bg-Light Gray.png"))
        self.bg_1.setObjectName("bg_1")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 560, 331, 51))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_1.setAutoFillBackground(False)
        self.pushButton_1.setAutoDefault(False)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.maintxt_3 = QtWidgets.QLabel(self.centralwidget)
        self.maintxt_3.setGeometry(QtCore.QRect(80, 430, 251, 21))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(8)
        self.maintxt_3.setFont(font)
        self.maintxt_3.setObjectName("maintxt_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 680, 331, 51))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.bg_1.raise_()
        self.bg_2.raise_()
        self.maintxt_2.raise_()
        self.maintxt_4.raise_()
        self.pushButton_2.raise_()
        self.maintxt_1.raise_()
        self.bg_3.raise_()
        self.pushButton_1.raise_()
        self.maintxt_3.raise_()
        self.pushButton_3.raise_()
        self.logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_1.clicked.connect(MainWindow.must)
        self.pushButton_2.clicked.connect(MainWindow.collect)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "당신 곁의 잔여백신_백발백신"))
        self.maintxt_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">데이터 수집을 통해</p><p align=\"center\"><br/></p></body></html>"))
        self.maintxt_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">확인해보세요</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "데이터 수집하기"))
        self.maintxt_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">우리동네 잔여백신 발생 현황</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_1.setText(_translate("MainWindow", "사용 전 필독 사항"))
        self.maintxt_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">신청 성공 확률이 높은 병원과 시간대를</p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "수집 결과 확인 "))
import testResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

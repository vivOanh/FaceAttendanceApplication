# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_add_TKB.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self, maLHP):
        self.maLHP = maLHP

    def GetDataInput(self):
        ngayHoc = self.ip_ngayHoc.text()
        tietHoc = self.ip_tietHoc.text()
        phongHoc = self.ip_phongHoc.text()
        # print(self.maLHP, ngayHoc, tietHoc, phongHoc)
        return self.maLHP, ngayHoc, tietHoc, phongHoc

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_title = QtWidgets.QLabel(self.centralwidget)
        self.lb_title.setGeometry(QtCore.QRect(0, 0, 800, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lb_title.setFont(font)
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_title.setObjectName("lb_title")
        self.lb_maLHP = QtWidgets.QLabel(self.centralwidget)
        self.lb_maLHP.setGeometry(QtCore.QRect(40, 100, 150, 40))
        self.lb_maLHP.setObjectName("lb_maLHP")
        self.lb_ngayHoc = QtWidgets.QLabel(self.centralwidget)
        self.lb_ngayHoc.setGeometry(QtCore.QRect(40, 170, 150, 40))
        self.lb_ngayHoc.setObjectName("lb_ngayHoc")
        self.lb_tietHoc = QtWidgets.QLabel(self.centralwidget)
        self.lb_tietHoc.setGeometry(QtCore.QRect(40, 240, 150, 40))
        self.lb_tietHoc.setObjectName("lb_tietHoc")
        self.lb_phongHoc = QtWidgets.QLabel(self.centralwidget)
        self.lb_phongHoc.setGeometry(QtCore.QRect(40, 310, 150, 40))
        self.lb_phongHoc.setObjectName("lb_phongHoc")
        self.ip_maLHP = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_maLHP.setGeometry(QtCore.QRect(240, 100, 450, 40))
        self.ip_maLHP.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ip_maLHP.setObjectName("ip_maLHP")
        self.ip_ngayHoc = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_ngayHoc.setGeometry(QtCore.QRect(240, 170, 450, 40))
        self.ip_ngayHoc.setObjectName("ip_ngayHoc")
        self.ip_tietHoc = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_tietHoc.setGeometry(QtCore.QRect(240, 240, 450, 40))
        self.ip_tietHoc.setObjectName("ip_tietHoc")
        self.ip_phongHoc = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_phongHoc.setGeometry(QtCore.QRect(240, 310, 450, 40))
        self.ip_phongHoc.setObjectName("ip_phongHoc")
        self.btn_them = QtWidgets.QPushButton(self.centralwidget)
        self.btn_them.setGeometry(QtCore.QRect(270, 370, 291, 51))
        self.btn_them.setObjectName("btn_them")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.ip_maLHP.setText(self.maLHP)

        # self.btn_them.clicked.connect(self.GetDataInput)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ỨNG DỤNG ĐIỂM DANH BẰNG KHUÔN MẶT"))
        self.lb_title.setText(_translate("MainWindow", "THÊM THỜI KHÓA BIỂU LỚP HỌC PHẦN"))
        self.lb_maLHP.setText(_translate("MainWindow", "Mã lớp học phần"))
        self.lb_ngayHoc.setText(_translate("MainWindow", "Ngày học"))
        self.lb_tietHoc.setText(_translate("MainWindow", "Tiết học"))
        self.lb_phongHoc.setText(_translate("MainWindow", "Phòng học"))
        self.btn_them.setText(_translate("MainWindow", "Thêm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow('201920503127001')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

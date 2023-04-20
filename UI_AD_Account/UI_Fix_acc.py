# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fix_acc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lb_tengiaovien = QtWidgets.QLabel(self.centralwidget)
        self.lb_tengiaovien.setGeometry(QtCore.QRect(50, 60, 121, 21))
        self.lb_tengiaovien.setObjectName("lb_tengiaovien")
        self.lb_tendangnhap = QtWidgets.QLabel(self.centralwidget)
        self.lb_tendangnhap.setGeometry(QtCore.QRect(50, 140, 121, 21))
        self.lb_tendangnhap.setObjectName("lb_tendangnhap")
        self.lb_matkhau = QtWidgets.QLabel(self.centralwidget)
        self.lb_matkhau.setGeometry(QtCore.QRect(60, 230, 121, 21))
        self.lb_matkhau.setObjectName("lb_matkhau")
        self.ip_fullname = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_fullname.setGeometry(QtCore.QRect(70, 90, 400, 35))
        self.ip_fullname.setObjectName("ip_fullname")
        self.ip_username = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_username.setGeometry(QtCore.QRect(70, 180, 400, 35))
        self.ip_username.setObjectName("ip_username")
        self.ip_password = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_password.setGeometry(QtCore.QRect(70, 260, 400, 35))
        self.ip_password.setObjectName("ip_password")
        self.btn_fix = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fix.setGeometry(QtCore.QRect(210, 320, 150, 30))
        self.btn_fix.setObjectName("btn_fix")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ỨNG DỤNG ĐIỂM DANH BẰNG KHUÔN MẶT"))
        self.label.setText(_translate("MainWindow", "SỬA TÀI KHOẢN"))
        self.lb_tengiaovien.setText(_translate("MainWindow", "Tên giáo viên"))
        self.lb_tendangnhap.setText(_translate("MainWindow", "Tên đăng nhập"))
        self.lb_matkhau.setText(_translate("MainWindow", "Mật Khẩu"))
        self.btn_fix.setText(_translate("MainWindow", "Sửa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

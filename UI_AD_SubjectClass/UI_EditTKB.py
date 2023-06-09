# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_TKB.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self, id, maLHP, ngayHoc, tietHoc, phongHoc):
        self.id = id
        self.maLHP = maLHP
        self.ngayHoc = ngayHoc
        self.tietHoc = tietHoc
        self.phongHoc = phongHoc

    def GetDataInput(self):
        ngayHoc = self.ip_ngayHoc.text()
        tietHoc = self.ip_tietHoc.text()
        phongHoc = self.ip_phongHoc.text()

        # print(self.id, self.maLHP, ngayHoc, tietHoc, phongHoc)
        return self.id, self.maLHP, ngayHoc, tietHoc, phongHoc

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
        self.lb_id = QtWidgets.QLabel(self.centralwidget)
        self.lb_id.setGeometry(QtCore.QRect(40, 80, 150, 40))
        self.lb_id.setObjectName("lb_id")
        self.lb_maLHP = QtWidgets.QLabel(self.centralwidget)
        self.lb_maLHP.setGeometry(QtCore.QRect(40, 150, 150, 40))
        self.lb_maLHP.setObjectName("lb_maLHP")
        self.lb_ngayHoc = QtWidgets.QLabel(self.centralwidget)
        self.lb_ngayHoc.setGeometry(QtCore.QRect(40, 220, 150, 40))
        self.lb_ngayHoc.setObjectName("lb_ngayHoc")
        self.lb_tietHoc = QtWidgets.QLabel(self.centralwidget)
        self.lb_tietHoc.setGeometry(QtCore.QRect(40, 290, 150, 40))
        self.lb_tietHoc.setObjectName("lb_tietHoc")
        self.lb_phongHoc = QtWidgets.QLabel(self.centralwidget)
        self.lb_phongHoc.setGeometry(QtCore.QRect(40, 360, 150, 40))
        self.lb_phongHoc.setObjectName("lb_phongHoc")
        self.ip_id = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_id.setGeometry(QtCore.QRect(240, 80, 450, 40))
        self.ip_id.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ip_id.setObjectName("ip_id")
        self.ip_maLHP = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_maLHP.setGeometry(QtCore.QRect(240, 150, 450, 40))
        self.ip_maLHP.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ip_maLHP.setObjectName("ip_maLHP")
        self.ip_ngayHoc = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_ngayHoc.setGeometry(QtCore.QRect(240, 220, 450, 40))
        self.ip_ngayHoc.setObjectName("ip_ngayHoc")
        self.ip_tietHoc = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_tietHoc.setGeometry(QtCore.QRect(240, 290, 450, 40))
        self.ip_tietHoc.setObjectName("ip_tietHoc")
        self.ip_phongHoc = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_phongHoc.setGeometry(QtCore.QRect(240, 360, 450, 40))
        self.ip_phongHoc.setObjectName("ip_phongHoc")
        self.btn_sua = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sua.setGeometry(QtCore.QRect(270, 420, 291, 51))
        self.btn_sua.setObjectName("btn_sua")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.ip_id.setText(self.id)
        self.ip_maLHP.setText(self.maLHP)
        self.ip_ngayHoc.setText(self.ngayHoc)
        self.ip_tietHoc.setText(self.tietHoc)
        self.ip_phongHoc.setText(self.phongHoc)

        # self.btn_sua.clicked.connect(self.GetDataInput)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_title.setText(_translate("MainWindow", "CHỈNH SỬA THÔNG TIN THỜI KHÓA BIỂU"))
        self.lb_id.setText(_translate("MainWindow", "ID"))
        self.lb_maLHP.setText(_translate("MainWindow", "Mã lớp học phần"))
        self.lb_ngayHoc.setText(_translate("MainWindow", "Ngày học"))
        self.lb_tietHoc.setText(_translate("MainWindow", "Tiết học"))
        self.lb_phongHoc.setText(_translate("MainWindow", "Phòng học"))
        self.btn_sua.setText(_translate("MainWindow", "Sửa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow('1', '201920503127001', '14/3', '1,2,3', 'P404A9')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# Form implementation generated from reading ui file 'Main_s.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 538)
        MainWindow.setMaximumSize(QtCore.QSize(790, 538))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, -1, 771, 491))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.page_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-10, 230, 791, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(266, 172))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color: rgb(133, 114, 85);\n"
"border-top-left-radius: 30px;\n"
"border-bottom-right-radius: 30px;\n"
"}\n"
"#pushButton:hover {\n"
"background:#dabb8b;\n"
"}\n"
"#pushButton:pressed {\n"
"color: #FFFFFF;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(266, 172))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"background-color: rgb(133, 114, 85);\n"
"border-top-right-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"}\n"
"#pushButton_2:hover {\n"
"background:#dabb8b;\n"
"}\n"
"#pushButton_2:pressed {\n"
"color: #FFFFFF;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.page_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 771, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label.setStyleSheet("border-top-left-radius: 55px;\n"
"border-top-right-radius: 55px;\n"
"border-bottom-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"background-color: rgba(211, 76, 3, 155);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.page_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-10, 10, 791, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(760, 145))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-top-left-radius: 55px;\n"
"border-top-right-radius: 55px;\n"
"border-bottom-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"background-color: rgba(211, 76, 3, 155);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.page_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-10, 299, 791, 201))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.horizontalLayoutWidget_2)
        self.frame.setMaximumSize(QtCore.QSize(696, 227))
        self.frame.setStyleSheet("border-top-left-radius: 40px;\n"
"border-top-right-radius: 40px;\n"
"border-bottom-right-radius: 40px;\n"
"border-bottom-left-radius: 40px;\n"
"background-color:#BBB4B4;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 701, 192))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_4.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_4.setStyleSheet("border-image: url(:/krest_v_krugle/checkmarkcircle_111048.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_32.addWidget(self.pushButton_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_3.setMaximumSize(QtCore.QSize(90, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_31.addWidget(self.label_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_3.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_3.setStyleSheet("border-image: url(:/Krest_v_kvadre/pngwing.com.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_30.addWidget(self.pushButton_3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_4.setMaximumSize(QtCore.QSize(90, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_29.addWidget(self.label_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_7.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_7.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_7.setStyleSheet("border-image: url(:/Oblako/download-from-cloud_icon-icons.com_54289.png);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_28.addWidget(self.pushButton_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_5.setMaximumSize(QtCore.QSize(90, 30))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_27.addWidget(self.label_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_11.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_11.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_11.setStyleSheet("border-image: url(:/Tochka_v_kruge/target-black-sportive-circular-symbol_icon-icons.com_57904.png);")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_26.addWidget(self.pushButton_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_6.setMaximumSize(QtCore.QSize(90, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_25.addWidget(self.label_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_12.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_12.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_12.setStyleSheet("border-image: url(:/stroka/free-icon-menu-bar-7787481.png);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_24.addWidget(self.pushButton_12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_7.setMaximumSize(QtCore.QSize(90, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_23.addWidget(self.label_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_13.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_13.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_13.setStyleSheet("border-image: url(:/Tekst/lines_icon_178720.png);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_21.addWidget(self.pushButton_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_8.setMaximumSize(QtCore.QSize(90, 30))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_22.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_5.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_5.setStyleSheet("border-image: url(:/Data/3507764-appointment-calendar-date-iconoteka-month-range-schedule_107688.png);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_14.addWidget(self.pushButton_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_9.setMaximumSize(QtCore.QSize(90, 30))
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_6.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_6.setStyleSheet("border-image: url(:/Vremya/1492790841-18time_84210.png);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_12.addWidget(self.pushButton_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_10.setMaximumSize(QtCore.QSize(90, 30))
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_8.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_8.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_8.setStyleSheet("border-image: url(:/Shkala/three_dots_icon_159804.png);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_16.addWidget(self.pushButton_8)
        self.verticalLayout_14.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_11.setMaximumSize(QtCore.QSize(90, 30))
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.verticalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_10.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_10.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_10.setStyleSheet("border-image: url(:/Setka_mnogo/free-icon-circle-grid-11809163.png);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_18.addWidget(self.pushButton_10)
        self.verticalLayout_13.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_13.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        self.verticalLayout_13.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_9.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_9.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_9.setStyleSheet("border-image: url(:/Setka_odin/thumbnail_web_layout_grid_view_icon_260023.png);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_20.addWidget(self.pushButton_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_12 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_12.setMaximumSize(QtCore.QSize(90, 30))
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_19.addWidget(self.label_12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.page_4)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(-1, 169, 771, 131))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setSpacing(30)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.textEdit = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_3)
        self.textEdit.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_33.addWidget(self.textEdit)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.pushButton_14.setMaximumSize(QtCore.QSize(65, 63))
        self.pushButton_14.setStyleSheet("border-image: url(:/Kartinoka/Group 9.png);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_33.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.pushButton_15.setMaximumSize(QtCore.QSize(141, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("#pushButton_15{\n"
"background-color: rgb(187, 180, 180);\n"
"border-radius: 12px\n"
"}\n"
"#pushButton_15:hover {\n"
"background:#8d8888;\n"
"}\n"
"#pushButton_15:pressed {\n"
"color: #FFFFFF;\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_33.addWidget(self.pushButton_15)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_33)
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", " ЗАПОЛНИТЬ\n"
"ДОКУМЕНТ"))
        self.pushButton_2.setText(_translate("MainWindow", "ДОБАВИТЬ\n"
"ДОКУМЕНТ"))
        self.label.setText(_translate("MainWindow", "ГЛАВНАЯ"))
        self.label_2.setText(_translate("MainWindow", "ДОБАВОЧНОЕ ПОЛЕ"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Раскрывающийся<br/>список</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Несколько<br/>из списка</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Загрузка<br/>файла</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Один<br/>из списка</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Текст<br/>(строка)</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Текст<br/>(абзац)</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Дата"))
        self.label_10.setText(_translate("MainWindow", "Время"))
        self.label_11.setText(_translate("MainWindow", "Шкала"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>Сетка<br/>(множ. выбор)</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Сетка<br/>флажков</p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Вопрос</p></body></html>"))
        self.pushButton_15.setText(_translate("MainWindow", "ОДИН ИЗ\n"
"СПИСКА"))

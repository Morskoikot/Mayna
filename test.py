import sys
import math
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication
)
from Authorization import Ui_MainWindow as Register
from Main_Form import Ui_MainWindow as Form
KT = int(1)
import Pictures
from PyQt6.QtGui     import QFontDatabase, QFont
from PyQt6.QtCore    import Qt
from PyQt6 import QtCore, QtGui, QtWidgets

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        id = QFontDatabase.addApplicationFont('./Fonts/Gagarin Star Mix Cyrillic.ttf')
        id2 = QFontDatabase.addApplicationFont('./Fonts/NokiaKokia(RYS BY LYAJKA).ttf')
        # Если id равен -1, то шрифт не установлен
        if id == -1 or id2 == -1: 
            print('Ошибка подключения шрифтов')
        font = QFont('Gagarin Star Mix Cyrillic', 86)
        font2 = QFont('NokiaKokia(RYS BY LYAJKA)', 32)
        font3 = QFont('Gagarin Star Mix Cyrillic', 12)
        
        self.ui = Register()
        self.ui.setupUi(self)

        self.ui.label.setFont(font)
        self.ui.label_3.setFont(font2)
        self.ui.label_2.setFont(font2)
        self.ui.pushButton.setFont(font3)
        self.ui.pushButton.clicked.connect(self.transfer)
    def transfer(self):
        AppWindow_main.show()
        AppWindow.close()
#основное окно программы        
class AppWindow_main(QMainWindow):
    def __init__(self):
        super(AppWindow_main, self).__init__()
        id = QFontDatabase.addApplicationFont('./Fonts/Gagarin Star Mix Cyrillic.ttf')
        id2 = QFontDatabase.addApplicationFont('./Fonts/NokiaKokia(RYS BY LYAJKA).ttf')
        id3 = QFontDatabase.addApplicationFont('./Fonts/No Limits(FONT BY LYAJKA).ttf')
        # Если id равен -1, то шрифт не установлен
        if id == -1 or id2 == -1 or id3 == -1: 
            print('Ошибка подключения шрифтов')
        font = QFont('Gagarin Star Mix Cyrillic', 50)
        font2 = QFont('NokiaKokia(RYS BY LYAJKA)', 25)
        font3 = QFont('No Limits(FONT BY LYAJKA)', 20)
        font4 = QFont('NokiaKokia(RYS BY LYAJKA)', 30)
        font5 = QFont('No Limits(FONT BY LYAJKA)', 16)
        font6 = QFont('NokiaKokia(RYS BY LYAJKA)', 24)
        

        self.ui = Form()
        self.ui.setupUi(self)

        self.ui.Kratki_otvet.setFont(font6)
        self.ui.Vopros.setFont(font6)

        self.ui.Glavnaya.setFont(font)
        self.ui.Button_Zapolnit.setFont(font2)
        self.ui.Button_Spisok.setFont(font2)
        self.ui.Button_Save.setFont(font5)
        self.ui.Button_Back.setFont(font5)
        self.ui.Obyazatelny_vopros.setFont(font3)
        self.ui.Button_Dok.setFont(font3)
        self.ui.Button_Forma_plus.setFont(font3)
        self.ui.Dobavit_dokument_label.setFont(font5)
        self.ui.Dobavochnoe_pole.setFont(font)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        self.ui.Button_Spisok.clicked.connect(self.transfer_page_add)
        self.ui.Button_Zapolnit.clicked.connect(self.transfer_Fill)
    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_page)
        self.ui.Button_Back.clicked.connect(self.transfer_back)
        self.ui.Button_Forma_plus.clicked.connect(self.add_field)
    def add_field(self):
        global KT
        _translate = QtCore.QCoreApplication.translate
        self.stackedWidget_t = QtWidgets.QStackedWidget ()
        self.ui.verticalLayout_7.addWidget(self.stackedWidget_t)
        
        
        
        self.page_t_1 = QtWidgets.QWidget()
        self.verticalLayout_t_1 = QtWidgets.QVBoxLayout(self.page_t_1)
        self.horizontalLayout_t_1 = QtWidgets.QHBoxLayout()
        self.widget_t_1 = QtWidgets.QWidget()
        self.widget_t_1.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_1.setObjectName(f"widget_t_1_{KT}")
        self.widget_t_1.setStyleSheet(f"#{self.widget_t_1.objectName()}" "{\n"
"background-color: rgb(228, 228, 228); \n"
"}")
        self.verticalLayout_w_1 = QtWidgets.QVBoxLayout(self.widget_t_1)
        self.verticalLayout_t_1.addLayout(self.horizontalLayout_t_1)
        self.horizontalLayout_t_1.addWidget(self.widget_t_1)
        self.horizontalLayout_f_100 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_100)
        self.horizontalLayout_f_110 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_100.addLayout(self.horizontalLayout_f_110)
        self.textField_vp_10 = QtWidgets.QLineEdit()
        self.textField_vp_10.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_10.setFont(font)
        self.textField_vp_10.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_10.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_110.addWidget(self.textField_vp_10)

        self.horizontalLayout_f_120 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_120.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_110.addLayout(self.horizontalLayout_f_120)
        self.comboBox_f_1 = QtWidgets.QComboBox()
        self.comboBox_f_1.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_1.setFont(font)
        self.comboBox_f_1.setObjectName(f"comboBox_f_1_{KT}")
        self.comboBox_f_1.setStyleSheet(f"#{self.comboBox_f_1.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_1.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_1.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_1.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_1.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_1.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_1.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_1.addItem("РАСКР. СПИСОК")
        self.comboBox_f_1.addItem("ШКАЛА")
        self.comboBox_f_1.addItem("ДАТА")
        self.comboBox_f_1.addItem("ВРЕМЯ")
        self.horizontalLayout_f_120.addWidget(self.comboBox_f_1)
        # Среднее поле
        self.horizontalLayout_f_200 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_200)
        self.horizontalLayout_f_210 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_220 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_200.addLayout(self.horizontalLayout_f_210)
        self.horizontalLayout_f_200.addLayout(self.horizontalLayout_f_220)
        self.textField_low_1 = QtWidgets.QLineEdit()
        self.textField_low_1.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_1.setFont(font)
        self.textField_low_1.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_210.addWidget(self.textField_low_1)
        self.textField_low_1.setPlaceholderText(_translate("MainWindow", "Краткий ответ"))
        self.textField_tag_1 = QtWidgets.QLineEdit()
        self.textField_tag_1.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_tag_1.setFont(font)
        self.textField_tag_1.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_tag_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_220.addWidget(self.textField_tag_1)
        self.textField_tag_1.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_230 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_220.addLayout(self.vertcalLayout_230)
        spacer_1 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_230.addItem(spacer_1)
        self.Button_Question_1 = QtWidgets.QPushButton()
        self.Button_Question_1.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_1.setFont(font)
        self.Button_Question_1.setObjectName(f"Button_Question_1_{KT}")
        self.Button_Question_1.setStyleSheet(f"#{self.Button_Question_1.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_1.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_1.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_230.addWidget(self.Button_Question_1)

        # Нижнее поле
        self.horizontalLayout_f_300 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_300)
        self.horizontalLayout_f_310 = QtWidgets.QHBoxLayout()
        self.Button_Copy_01 = QtWidgets.QPushButton()
        self.Button_Copy_01.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_01.setObjectName(f"Button_Copy_0{KT}")
        self.Button_Copy_01.setStyleSheet(f"#{self.Button_Copy_01.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_01.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_01.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_01.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_01.setIcon(icon2)
        self.horizontalLayout_f_300.addWidget(self.Button_Copy_01)
        self.horizontalLayout_f_300.addLayout(self.horizontalLayout_f_310)
        self.Obyazatelny_vopros_f_01 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_01.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_01.setFont(font)
        self.Obyazatelny_vopros_f_01.setObjectName("Obyazatelny_vopros_f_01")
        self.Obyazatelny_vopros_f_01.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_310.addWidget(self.Obyazatelny_vopros_f_01)
        self.widget_f_01 = QtWidgets.QWidget()
        self.widget_f_01.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_01.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_01.setObjectName("widget_f_01")
        self.pushButton_f_01_on = QtWidgets.QPushButton(self.widget_f_01)
        self.pushButton_f_01_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_01_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_01_on.setText("")
        self.pushButton_f_01_on.setObjectName("pushButton_f_01_on")
        self.pushButton_f_01_off = QtWidgets.QPushButton(self.widget_f_01)
        self.pushButton_f_01_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_01_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_01_off.setText("")
        self.pushButton_f_01_off.setObjectName("pushButton_f_01_off")
        self.horizontalLayout_f_310.addWidget(self.widget_f_01)

        
        






























        
        self.page_t_2 = QtWidgets.QWidget()
        self.verticalLayout_t_2 = QtWidgets.QVBoxLayout(self.page_t_2)
        self.horizontalLayout_t_2 = QtWidgets.QHBoxLayout()
        self.widget_t_2 = QtWidgets.QWidget()
        self.widget_t_2.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_2.setObjectName(f"widget_t_2_{KT}")
        self.widget_t_2.setStyleSheet(f"#{self.widget_t_2.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_2 = QtWidgets.QVBoxLayout(self.widget_t_2)
        self.verticalLayout_t_2.addLayout(self.horizontalLayout_t_2)
        self.horizontalLayout_t_2.addWidget(self.widget_t_2)
        self.horizontalLayout_f_101 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_2.addLayout(self.horizontalLayout_f_101)
        self.horizontalLayout_f_111 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_101.addLayout(self.horizontalLayout_f_111)
        self.textField_vp_20 = QtWidgets.QLineEdit()
        self.textField_vp_20.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_20.setFont(font)
        self.textField_vp_20.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_20.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_111.addWidget(self.textField_vp_20)

        self.horizontalLayout_f_121 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_121.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_111.addLayout(self.horizontalLayout_f_121)
        self.comboBox_f_2_ = QtWidgets.QComboBox()
        self.comboBox_f_2_.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_2_.setFont(font)
        self.comboBox_f_2_.setObjectName(f"comboBox_f_2_{KT}")
        self.comboBox_f_2_.setStyleSheet(f"#{self.comboBox_f_2_.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_2_.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_2_.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_2_.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_2_.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_2_.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_2_.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_2_.addItem("РАСКР. СПИСОК")
        self.comboBox_f_2_.addItem("ШКАЛА")
        self.comboBox_f_2_.addItem("ДАТА")
        self.comboBox_f_2_.addItem("ВРЕМЯ")
        self.horizontalLayout_f_121.addWidget(self.comboBox_f_2_)
        # Среднее поле
        self.horizontalLayout_f_201 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_2.addLayout(self.horizontalLayout_f_201)
        self.horizontalLayout_f_211 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_221 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_201.addLayout(self.horizontalLayout_f_211)
        self.horizontalLayout_f_201.addLayout(self.horizontalLayout_f_221)
        self.textField_low_2 = QtWidgets.QLineEdit()
        self.textField_low_2.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_2.setFont(font)
        self.textField_low_2.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_211.addWidget(self.textField_low_2)
        self.textField_low_2.setPlaceholderText(_translate("MainWindow", "Развёрнутый ответ"))
        self.textField_low_2 = QtWidgets.QLineEdit()
        self.textField_low_2.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_2.setFont(font)
        self.textField_low_2.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_221.addWidget(self.textField_low_2)
        self.textField_low_2.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_231 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_221.addLayout(self.vertcalLayout_231)
        spacer_2 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_231.addItem(spacer_2)
        self.Button_Question_2 = QtWidgets.QPushButton()
        self.Button_Question_2.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_2.setFont(font)
        self.Button_Question_2.setObjectName(f"Button_Question_2_{KT}")
        self.Button_Question_2.setStyleSheet(f"#{self.Button_Question_2.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_2.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_2.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_231.addWidget(self.Button_Question_2)

        # Нижнее поле
        self.horizontalLayout_f_301 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_2.addLayout(self.horizontalLayout_f_301)
        self.horizontalLayout_f_311 = QtWidgets.QHBoxLayout()
        self.Button_Copy_02 = QtWidgets.QPushButton()
        self.Button_Copy_02.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_02.setObjectName(f"Button_Copy_1{KT}")
        self.Button_Copy_02.setStyleSheet(f"#{self.Button_Copy_02.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_02.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_02.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_02.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_02.setIcon(icon2)
        self.horizontalLayout_f_301.addWidget(self.Button_Copy_02)
        self.horizontalLayout_f_301.addLayout(self.horizontalLayout_f_311)
        self.Obyazatelny_vopros_f_02 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_02.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_02.setFont(font)
        self.Obyazatelny_vopros_f_02.setObjectName("Obyazatelny_vopros_f_02")
        self.Obyazatelny_vopros_f_02.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_311.addWidget(self.Obyazatelny_vopros_f_02)
        self.widget_f_02 = QtWidgets.QWidget()
        self.widget_f_02.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_02.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_02.setObjectName("widget_f_02")
        self.pushButton_f_02_on = QtWidgets.QPushButton(self.widget_f_02)
        self.pushButton_f_02_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_02_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_02_on.setText("")
        self.pushButton_f_02_on.setObjectName("pushButton_f_02_on")
        self.pushButton_f_02_off = QtWidgets.QPushButton(self.widget_f_02)
        self.pushButton_f_02_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_02_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_02_off.setText("")
        self.pushButton_f_02_off.setObjectName("pushButton_f_02_off")
        self.horizontalLayout_f_311.addWidget(self.widget_f_02)

        
        
        


















        self.page_t_3 = QtWidgets.QWidget()
        self.verticalLayout_t_3 = QtWidgets.QVBoxLayout(self.page_t_3)
        self.horizontalLayout_t_3 = QtWidgets.QHBoxLayout()
        self.widget_t_3 = QtWidgets.QWidget()
        self.widget_t_3.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_3.setObjectName(f"widget_t_3_{KT}")
        self.widget_t_3.setStyleSheet (f"#{self.widget_t_3.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_3 = QtWidgets.QVBoxLayout(self.widget_t_3)
        self.verticalLayout_t_3.addLayout(self.horizontalLayout_t_3)
        self.horizontalLayout_t_3.addWidget(self.widget_t_3)
        self.horizontalLayout_f_102 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_3.addLayout(self.horizontalLayout_f_102)
        self.horizontalLayout_f_112 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_102.addLayout(self.horizontalLayout_f_112)
        self.textField_vp_30 = QtWidgets.QLineEdit()
        self.textField_vp_30.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_30.setFont(font)
        self.textField_vp_30.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_30.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_30.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_112.addWidget(self.textField_vp_30)

        self.horizontalLayout_f_122 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_122.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_112.addLayout(self.horizontalLayout_f_122)
        self.comboBox_f_3_ = QtWidgets.QComboBox()
        self.comboBox_f_3_.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_3_.setFont(font)
        self.comboBox_f_3_.setObjectName(f"comboBox_f_3_{KT}")
        self.comboBox_f_3_.setStyleSheet(f"#{self.comboBox_f_3_.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_3_.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_3_.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_3_.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_3_.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_3_.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_3_.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_3_.addItem("РАСКР. СПИСОК")
        self.comboBox_f_3_.addItem("ШКАЛА")
        self.comboBox_f_3_.addItem("ДАТА")
        self.comboBox_f_3_.addItem("ВРЕМЯ")
        self.horizontalLayout_f_122.addWidget(self.comboBox_f_3_)
        # Среднее поле
        self.horizontalLayout_f_202 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_3.addLayout(self.horizontalLayout_f_202)
        self.horizontalLayout_f_212 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_222 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_202.addLayout(self.horizontalLayout_f_212)
        self.horizontalLayout_f_202.addLayout(self.horizontalLayout_f_222)
        self.textField_low_3 = QtWidgets.QLineEdit()
        self.textField_low_3.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_3.setFont(font)
        self.textField_low_3.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_212.addWidget(self.textField_low_3)
        self.textField_low_3.setPlaceholderText(_translate("MainWindow", "1 Вариант"))
        self.textField_low_3 = QtWidgets.QLineEdit()
        self.textField_low_3.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_3.setFont(font)
        self.textField_low_3.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_222.addWidget(self.textField_low_3)
        self.textField_low_3.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_232 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_222.addLayout(self.vertcalLayout_232)
        spacer_3 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_232.addItem(spacer_3)
        self.Button_Question_3 = QtWidgets.QPushButton()
        self.Button_Question_3.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_3.setFont(font)
        self.Button_Question_3.setObjectName(f"Button_Question_3_{KT}")
        self.Button_Question_3.setStyleSheet(f"#{self.Button_Question_3.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_3.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_3.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_232.addWidget(self.Button_Question_3)

        self.horizontalLayout_m_03 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_3.addLayout(self.horizontalLayout_m_03)
        self.button_var = QtWidgets.QPushButton()
        self.button_var.setObjectName(f"button_var_{KT}")
        self.button_var.setStyleSheet(f"#{self.button_var.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.button_var.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.button_var.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_m_03.addWidget(self.button_var)

        # Нижнее поле
        self.horizontalLayout_f_302 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_3.addLayout(self.horizontalLayout_f_302)
        self.horizontalLayout_f_312 = QtWidgets.QHBoxLayout()
        self.Button_Copy_03 = QtWidgets.QPushButton()
        self.Button_Copy_03.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_03.setObjectName(f"Button_Copy_3{KT}")
        self.Button_Copy_03.setStyleSheet(f"#{self.Button_Copy_03.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_03.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_03.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_03.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_03.setIcon(icon2)
        self.horizontalLayout_f_302.addWidget(self.Button_Copy_03)
        self.horizontalLayout_f_302.addLayout(self.horizontalLayout_f_312)
        self.Obyazatelny_vopros_f_03 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_03.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_03.setFont(font)
        self.Obyazatelny_vopros_f_03.setObjectName("Obyazatelny_vopros_f_03")
        self.Obyazatelny_vopros_f_03.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_312.addWidget(self.Obyazatelny_vopros_f_03)
        self.widget_f_03 = QtWidgets.QWidget()
        self.widget_f_03.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_03.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_03.setObjectName("widget_f_03")
        self.pushButton_f_03_on = QtWidgets.QPushButton(self.widget_f_03)
        self.pushButton_f_03_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_03_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_03_on.setText("")
        self.pushButton_f_03_on.setObjectName("pushButton_f_03_on")
        self.pushButton_f_03_off = QtWidgets.QPushButton(self.widget_f_03)
        self.pushButton_f_03_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_03_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_03_off.setText("")
        self.pushButton_f_03_off.setObjectName("pushButton_f_03_off")
        self.horizontalLayout_f_312.addWidget(self.widget_f_03)




















        
        
        self.page_t_4 = QtWidgets.QWidget()
        self.verticalLayout_t_4 = QtWidgets.QVBoxLayout(self.page_t_4)
        self.horizontalLayout_t_4 = QtWidgets.QHBoxLayout()
        self.widget_t_4 = QtWidgets.QWidget()
        self.widget_t_4.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_4.setObjectName(f"widget_t_4_{KT}")
        self.widget_t_4.setStyleSheet (f"#{self.widget_t_4.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_4 = QtWidgets.QVBoxLayout(self.widget_t_4)
        self.verticalLayout_t_4.addLayout(self.horizontalLayout_t_4)
        self.horizontalLayout_t_4.addWidget(self.widget_t_4)
        self.horizontalLayout_f_103 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_4.addLayout(self.horizontalLayout_f_103)
        self.horizontalLayout_f_113 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_103.addLayout(self.horizontalLayout_f_113)
        self.textField_vp_40 = QtWidgets.QLineEdit()
        self.textField_vp_40.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_40.setFont(font)
        self.textField_vp_40.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_40.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_40.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_113.addWidget(self.textField_vp_40)

        self.horizontalLayout_f_123 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_123.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_113.addLayout(self.horizontalLayout_f_123)
        self.comboBox_f_4_ = QtWidgets.QComboBox()
        self.comboBox_f_4_.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_4_.setFont(font)
        self.comboBox_f_4_.setObjectName(f"comboBox_f_4_{KT}")
        self.comboBox_f_4_.setStyleSheet(f"#{self.comboBox_f_4_.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_4_.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_4_.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_4_.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_4_.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_4_.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_4_.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_4_.addItem("РАСКР. СПИСОК")
        self.comboBox_f_4_.addItem("ШКАЛА")
        self.comboBox_f_4_.addItem("ДАТА")
        self.comboBox_f_4_.addItem("ВРЕМЯ")
        self.horizontalLayout_f_123.addWidget(self.comboBox_f_4_)
        # Среднее поле
        self.horizontalLayout_f_203 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_4.addLayout(self.horizontalLayout_f_203)
        self.horizontalLayout_f_213 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_223 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_203.addLayout(self.horizontalLayout_f_213)
        self.horizontalLayout_f_203.addLayout(self.horizontalLayout_f_223)
        self.textField_low_4 = QtWidgets.QLineEdit()
        self.textField_low_4.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_4.setFont(font)
        self.textField_low_4.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_213.addWidget(self.textField_low_4)
        self.textField_low_4.setPlaceholderText(_translate("MainWindow", "1 Вариант"))
        self.textField_low_4 = QtWidgets.QLineEdit()
        self.textField_low_4.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_4.setFont(font)
        self.textField_low_4.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_223.addWidget(self.textField_low_4)
        self.textField_low_4.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_233 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_223.addLayout(self.vertcalLayout_233)
        spacer_4 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_233.addItem(spacer_4)
        self.Button_Question_4 = QtWidgets.QPushButton()
        self.Button_Question_4.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_4.setFont(font)
        self.Button_Question_4.setObjectName(f"Button_Question_4_{KT}")
        self.Button_Question_4.setStyleSheet(f"#{self.Button_Question_4.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_4.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_4.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_233.addWidget(self.Button_Question_4)

        self.horizontalLayout_m_04 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_4.addLayout(self.horizontalLayout_m_04)
        self.button_var_1 = QtWidgets.QPushButton()
        self.button_var_1.setObjectName(f"button_var_1_{KT}")
        self.button_var_1.setStyleSheet(f"#{self.button_var_1.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.button_var_1.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.button_var_1.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.horizontalLayout_m_04.addWidget(self.button_var_1)

        # Нижнее поле
        self.horizontalLayout_f_303 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_4.addLayout(self.horizontalLayout_f_303)
        self.horizontalLayout_f_313 = QtWidgets.QHBoxLayout()
        self.Button_Copy_04 = QtWidgets.QPushButton()
        self.Button_Copy_04.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_04.setObjectName(f"Button_Copy_4{KT}")
        self.Button_Copy_04.setStyleSheet(f"#{self.Button_Copy_04.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_04.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_04.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_04.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_03.setIcon(icon2)
        self.horizontalLayout_f_303.addWidget(self.Button_Copy_04)
        self.horizontalLayout_f_303.addLayout(self.horizontalLayout_f_313)
        self.Obyazatelny_vopros_f_04 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_04.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_04.setFont(font)
        self.Obyazatelny_vopros_f_04.setObjectName("Obyazatelny_vopros_f_03")
        self.Obyazatelny_vopros_f_04.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_312.addWidget(self.Obyazatelny_vopros_f_04)
        self.widget_f_04 = QtWidgets.QWidget()
        self.widget_f_04.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_04.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_04.setObjectName("widget_f_04")
        self.pushButton_f_04_on = QtWidgets.QPushButton(self.widget_f_04)
        self.pushButton_f_04_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_04_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_04_on.setText("")
        self.pushButton_f_04_on.setObjectName("pushButton_f_04_on")
        self.pushButton_f_04_off = QtWidgets.QPushButton(self.widget_f_04)
        self.pushButton_f_04_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_04_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_04_off.setText("")
        self.pushButton_f_04_off.setObjectName("pushButton_f_04_off")
        self.horizontalLayout_f_313.addWidget(self.widget_f_04)






















        
        
        self.page_t_5 = QtWidgets.QWidget()
        self.verticalLayout_t_5 = QtWidgets.QVBoxLayout(self.page_t_5)
        self.horizontalLayout_t_5 = QtWidgets.QHBoxLayout()
        self.widget_t_5 = QtWidgets.QWidget()
        self.widget_t_5.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_5.setObjectName(f"widget_t_5_{KT}")
        self.widget_t_5.setStyleSheet (f"#{self.widget_t_5.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_5 = QtWidgets.QVBoxLayout(self.widget_t_5)
        self.verticalLayout_t_5.addLayout(self.horizontalLayout_t_5)
        self.horizontalLayout_t_5.addWidget(self.widget_t_5)
        self.horizontalLayout_f_104 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_5.addLayout(self.horizontalLayout_f_104)
        self.horizontalLayout_f_114 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_104.addLayout(self.horizontalLayout_f_114)
        self.comboBox_L_5 = QtWidgets.QComboBox()
        self.comboBox_L_5.setMaximumSize(QtCore.QSize(60, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_L_5.setFont(font)
        self.comboBox_L_5.setObjectName(f"comboBox_L_5{KT}")
        self.comboBox_L_5.setStyleSheet(f"#{self.comboBox_L_5.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
f"#{self.comboBox_L_5.objectName()}"":hover {\n"
"background-color: rgb(243, 243, 243);\n"
"}\n"
f"#{self.comboBox_L_5.objectName()}"":pressed { \n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
"")
        self.comboBox_L_5.setObjectName("comboBox_6")
        self.comboBox_L_5.addItem("0")
        self.comboBox_L_5.addItem("1")
        self.horizontalLayout_f_104.addWidget(self.comboBox_L_5)
        self.comboBox_R_5 = QtWidgets.QComboBox()
        self.comboBox_R_5.setMaximumSize(QtCore.QSize(60, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_R_5.setFont(font)
        self.comboBox_R_5.setObjectName(f"comboBox_R_5{KT}")
        self.comboBox_R_5.setStyleSheet(f"#{self.comboBox_R_5.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
f"#{self.comboBox_R_5.objectName()}"":hover {\n"
"background-color: rgb(243, 243, 243);\n"
"}\n"
f"#{self.comboBox_R_5.objectName()}"":pressed { \n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
"")
        self.comboBox_R_5.setObjectName("comboBox_7")
        self.comboBox_R_5.addItem("2")
        self.comboBox_R_5.addItem("3")
        self.comboBox_R_5.addItem("4")
        self.comboBox_R_5.addItem("5")
        self.comboBox_R_5.addItem("6")
        self.comboBox_R_5.addItem("7")
        self.comboBox_R_5.addItem("8")
        self.comboBox_R_5.addItem("9")
        self.comboBox_R_5.addItem("10")
        self.horizontalLayout_f_104.addWidget(self.comboBox_R_5)
        self.horizontalLayout_f_124 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_124.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_114.addLayout(self.horizontalLayout_f_124)
        self.comboBox_f_5_ = QtWidgets.QComboBox()
        self.comboBox_f_5_.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_5_.setFont(font)
        self.comboBox_f_5_.setObjectName(f"comboBox_f_5_{KT}")
        self.comboBox_f_5_.setStyleSheet(f"#{self.comboBox_f_5_.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_5_.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_5_.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_5_.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_5_.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_5_.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_5_.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_5_.addItem("РАСКР. СПИСОК")
        self.comboBox_f_5_.addItem("ШКАЛА")
        self.comboBox_f_5_.addItem("ДАТА")
        self.comboBox_f_5_.addItem("ВРЕМЯ")
        self.horizontalLayout_f_124.addWidget(self.comboBox_f_5_)
        # Среднее поле
        self.horizontalLayout_f_204 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_5.addLayout(self.horizontalLayout_f_204)
        self.horizontalLayout_f_214 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_224 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_204.addLayout(self.horizontalLayout_f_214)
        self.horizontalLayout_f_204.addLayout(self.horizontalLayout_f_224)
        self.horizontalLayout_264 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_264.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_264.setSpacing(6)
        spacerItem_L_up = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_264.addItem(spacerItem_L_up)
        self.horizontalLayout_274 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_274.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_274.setSpacing(6)
        self.label_Up = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Up.setFont(font)
        self.horizontalLayout_274.addWidget(self.label_Up)
        self.horizontalLayout_264.addLayout(self.horizontalLayout_274)
        self.Vopros_Up = QtWidgets.QLineEdit()
        self.Vopros_Up.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Vopros_Up.setFont(font)
        self.Vopros_Up.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.Vopros_Up.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_264.addWidget(self.Vopros_Up)
        spacerItem_R_up = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_264.addItem(spacerItem_R_up)
        self.horizontalLayout_f_214.addLayout(self.horizontalLayout_264)
        self.horizontalLayout_284 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_284.setContentsMargins(-1, 30, 0, -1)
        spacerItem_l_d = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_284.addItem(spacerItem_l_d)
        self.horizontalLayout_294 = QtWidgets.QHBoxLayout()
        self.label_down = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_down.setFont(font)
        self.horizontalLayout_294.addWidget(self.label_down)
        self.horizontalLayout_284.addLayout(self.horizontalLayout_294)
        self.Vopros_down = QtWidgets.QLineEdit()
        self.Vopros_down.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Vopros_down.setFont(font)
        self.Vopros_down.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.Vopros_down.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_284.addWidget(self.Vopros_down)
        spacerItem8 = QtWidgets.QSpacerItem(130, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_284.addItem(spacerItem8)
        self.horizontalLayout_f_214.addLayout(self.horizontalLayout_284)
        
        self.vertcalLayout_234 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_224.addLayout(self.vertcalLayout_234)
        spacer_5 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_234.addItem(spacer_5)
        self.Button_Question_5 = QtWidgets.QPushButton()
        self.Button_Question_5.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_5.setFont(font)
        self.Button_Question_5.setObjectName(f"Button_Question_5{KT}")
        self.Button_Question_5.setStyleSheet(f"#{self.Button_Question_5.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_5.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_5.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_234.addWidget(self.Button_Question_5)
        # Нижнее поле
        self.horizontalLayout_f_304 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_2.addLayout(self.horizontalLayout_f_304)
        self.horizontalLayout_f_314 = QtWidgets.QHBoxLayout()
        self.Button_Copy_05 = QtWidgets.QPushButton()
        self.Button_Copy_05.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_05.setObjectName(f"Button_Copy_05{KT}")
        self.Button_Copy_05.setStyleSheet(f"#{self.Button_Copy_05.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_05.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_05.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_05.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_05.setIcon(icon2)
        self.horizontalLayout_f_304.addWidget(self.Button_Copy_05)
        self.horizontalLayout_f_304.addLayout(self.horizontalLayout_f_314)
        self.Obyazatelny_vopros_f_05 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_05.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_05.setFont(font)
        self.Obyazatelny_vopros_f_05.setObjectName("Obyazatelny_vopros_f_05")
        self.Obyazatelny_vopros_f_05.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_314.addWidget(self.Obyazatelny_vopros_f_05)
        self.widget_f_05 = QtWidgets.QWidget()
        self.widget_f_05.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_05.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_05.setObjectName("widget_f_05")
        self.pushButton_f_05_on = QtWidgets.QPushButton(self.widget_f_05)
        self.pushButton_f_05_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_05_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_05_on.setText("")
        self.pushButton_f_05_on.setObjectName("pushButton_f_05_on")
        self.pushButton_f_05_off = QtWidgets.QPushButton(self.widget_f_05)
        self.pushButton_f_05_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_05_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_05_off.setText("")
        self.pushButton_f_05_off.setObjectName("pushButton_f_05_off")
        self.horizontalLayout_f_314.addWidget(self.widget_f_05)
        
        self.page_t_6 = QtWidgets.QWidget()
        self.verticalLayout_t_6 = QtWidgets.QVBoxLayout(self.page_t_6)
        self.horizontalLayout_t_6 = QtWidgets.QHBoxLayout()
        self.widget_t_6 = QtWidgets.QWidget()
        self.widget_t_6.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_6.setObjectName(f"widget_t_6_{KT}")
        self.widget_t_6.setStyleSheet (f"#{self.widget_t_6.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_6 = QtWidgets.QVBoxLayout(self.widget_t_6)
        self.verticalLayout_t_6.addLayout(self.horizontalLayout_t_6)
        self.horizontalLayout_t_6.addWidget(self.widget_t_6)
        self.horizontalLayout_f_105 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_6.addLayout(self.horizontalLayout_f_105)
        self.horizontalLayout_f_115 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_105.addLayout(self.horizontalLayout_f_115)
        self.textField_vp_60 = QtWidgets.QLineEdit()
        self.textField_vp_60.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_60.setFont(font)
        self.textField_vp_60.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_60.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_60.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_115.addWidget(self.textField_vp_60)
        self.horizontalLayout_f_125 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_125.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_115.addLayout(self.horizontalLayout_f_125)
        self.comboBox_f_6_ = QtWidgets.QComboBox()
        self.comboBox_f_6_.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_6_.setFont(font)
        self.comboBox_f_6_.setObjectName(f"comboBox_f_6_{KT}")
        self.comboBox_f_6_.setStyleSheet(f"#{self.comboBox_f_6_.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_6_.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_6_.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_6_.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_6_.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_6_.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_6_.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_6_.addItem("РАСКР. СПИСОК")
        self.comboBox_f_6_.addItem("ШКАЛА")
        self.comboBox_f_6_.addItem("ДАТА")
        self.comboBox_f_6_.addItem("ВРЕМЯ")
        self.horizontalLayout_f_125.addWidget(self.comboBox_f_6_)
        # Среднее поле
        self.horizontalLayout_f_205 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_6.addLayout(self.horizontalLayout_f_205)
        self.horizontalLayout_f_215 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_225 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_205.addLayout(self.horizontalLayout_f_215)
        self.horizontalLayout_f_205.addLayout(self.horizontalLayout_f_225)
        self.timeEdit_6 = QtWidgets.QTimeEdit()
        self.timeEdit_6.setMaximumSize(QtCore.QSize(90, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEdit_6.setFont(font)
        self.timeEdit_6.setObjectName(f"timeEdit_6_{KT}")
        self.timeEdit_6.setStyleSheet(f"#{self.timeEdit_6.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
f"#{self.timeEdit_6.objectName()}" ":hover {\n"
"background-color: rgb(243, 243, 243);\n"
"}\n"
f"#{self.timeEdit_6.objectName()}" ":pressed { \n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
"")
        self.horizontalLayout_f_215.addWidget(self.timeEdit_6)
        self.vertcalLayout_235 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_225.addLayout(self.vertcalLayout_235)
        spacer_6 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_235.addItem(spacer_6)
        self.Button_Question_6 = QtWidgets.QPushButton()
        self.Button_Question_6.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_6.setFont(font)
        self.Button_Question_6.setObjectName(f"Button_Question_6{KT}")
        self.Button_Question_6.setStyleSheet(f"#{self.Button_Question_6.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_6.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_6.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_235.addWidget(self.Button_Question_6)
        # Нижнее поле
        self.horizontalLayout_f_305 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_6.addLayout(self.horizontalLayout_f_305)
        self.horizontalLayout_f_315 = QtWidgets.QHBoxLayout()
        self.Button_Copy_06 = QtWidgets.QPushButton()
        self.Button_Copy_06.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_06.setObjectName(f"Button_Copy_06{KT}")
        self.Button_Copy_06.setStyleSheet(f"#{self.Button_Copy_06.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_06.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_06.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_06.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_06.setIcon(icon2)
        self.horizontalLayout_f_305.addWidget(self.Button_Copy_06)
        self.horizontalLayout_f_305.addLayout(self.horizontalLayout_f_315)
        self.Obyazatelny_vopros_f_06 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_06.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_06.setFont(font)
        self.Obyazatelny_vopros_f_06.setObjectName("Obyazatelny_vopros_f_06")
        self.Obyazatelny_vopros_f_06.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_315.addWidget(self.Obyazatelny_vopros_f_06)
        self.widget_f_06 = QtWidgets.QWidget()
        self.widget_f_06.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_06.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_06.setObjectName("widget_f_06")
        self.pushButton_f_06_on = QtWidgets.QPushButton(self.widget_f_06)
        self.pushButton_f_06_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_06_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_06_on.setText("")
        self.pushButton_f_06_on.setObjectName("pushButton_f_06_on")
        self.pushButton_f_06_off = QtWidgets.QPushButton(self.widget_f_06)
        self.pushButton_f_06_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_06_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_06_off.setText("")
        self.pushButton_f_06_off.setObjectName("pushButton_f_06_off")
        self.horizontalLayout_f_315.addWidget(self.widget_f_06)
        
        self.page_t_7 = QtWidgets.QWidget()
        self.verticalLayout_t_7 = QtWidgets.QVBoxLayout(self.page_t_7)
        self.horizontalLayout_t_7 = QtWidgets.QHBoxLayout()
        self.widget_t_7 = QtWidgets.QWidget()
        self.widget_t_7.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_7.setObjectName(f"widget_t_7_{KT}")
        self.widget_t_7.setStyleSheet (f"#{self.widget_t_7.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_7 = QtWidgets.QVBoxLayout(self.widget_t_7)
        self.verticalLayout_t_7.addLayout(self.horizontalLayout_t_7)
        self.horizontalLayout_t_7.addWidget(self.widget_t_7)
        self.horizontalLayout_f_106 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_7.addLayout(self.horizontalLayout_f_106)
        self.horizontalLayout_f_116 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_106.addLayout(self.horizontalLayout_f_116)
        self.textField_vp_70 = QtWidgets.QLineEdit()
        self.textField_vp_70.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_70.setFont(font)
        self.textField_vp_70.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_70.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_70.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_116.addWidget(self.textField_vp_70)
        self.horizontalLayout_f_126 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_126.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_116.addLayout(self.horizontalLayout_f_126)
        self.comboBox_f_7_ = QtWidgets.QComboBox()
        self.comboBox_f_7_.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_7_.setFont(font)
        self.comboBox_f_7_.setObjectName(f"comboBox_f_7_{KT}")
        self.comboBox_f_7_.setStyleSheet(f"#{self.comboBox_f_7_.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_7_.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_7_.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_7_.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_7_.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_7_.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_7_.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_7_.addItem("РАСКР. СПИСОК")
        self.comboBox_f_7_.addItem("ШКАЛА")
        self.comboBox_f_7_.addItem("ДАТА")
        self.comboBox_f_7_.addItem("ВРЕМЯ")
        self.horizontalLayout_f_126.addWidget(self.comboBox_f_7_)
        # Среднее поле
        self.horizontalLayout_f_206 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_7.addLayout(self.horizontalLayout_f_206)
        self.horizontalLayout_f_216 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_226 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_206.addLayout(self.horizontalLayout_f_216)
        self.horizontalLayout_f_206.addLayout(self.horizontalLayout_f_226)
        self.dateEdit_7 = QtWidgets.QDateEdit()
        self.dateEdit_7.setMaximumSize(QtCore.QSize(90, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit_7.setFont(font)
        self.dateEdit_7.setObjectName(f"dateEdit_7_{KT}")
        self.dateEdit_7.setStyleSheet(f"#{self.dateEdit_7.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
f"#{self.dateEdit_7.objectName()}" ":hover {\n"
"background-color: rgb(243, 243, 243);\n"
"}\n"
f"#{self.dateEdit_7.objectName()}" ":pressed { \n"
"background-color:rgb(243, 243, 243);\n"
"}\n"
"")
        self.horizontalLayout_f_216.addWidget(self.dateEdit_7)
        self.vertcalLayout_236 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_226.addLayout(self.vertcalLayout_236)
        spacer_7 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_236.addItem(spacer_7)
        self.Button_Question_7 = QtWidgets.QPushButton()
        self.Button_Question_7.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_7.setFont(font)
        self.Button_Question_7.setObjectName(f"Button_Question_7{KT}")
        self.Button_Question_7.setStyleSheet(f"#{self.Button_Question_7.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_7.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_7.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_236.addWidget(self.Button_Question_7)
        # Нижнее поле
        self.horizontalLayout_f_306 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_7.addLayout(self.horizontalLayout_f_306)
        self.horizontalLayout_f_316 = QtWidgets.QHBoxLayout()
        self.Button_Copy_07 = QtWidgets.QPushButton()
        self.Button_Copy_07.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_07.setObjectName(f"Button_Copy_07{KT}")
        self.Button_Copy_07.setStyleSheet(f"#{self.Button_Copy_07.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_07.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_07.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_07.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_07.setIcon(icon2)
        self.horizontalLayout_f_306.addWidget(self.Button_Copy_07)
        self.horizontalLayout_f_306.addLayout(self.horizontalLayout_f_316)
        self.Obyazatelny_vopros_f_07 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_07.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_07.setFont(font)
        self.Obyazatelny_vopros_f_07.setObjectName("Obyazatelny_vopros_f_07")
        self.Obyazatelny_vopros_f_07.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_316.addWidget(self.Obyazatelny_vopros_f_07)
        self.widget_f_07 = QtWidgets.QWidget()
        self.widget_f_07.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_07.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_07.setObjectName("widget_f_07")
        self.pushButton_f_07_on = QtWidgets.QPushButton(self.widget_f_07)
        self.pushButton_f_07_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_07_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_07_on.setText("")
        self.pushButton_f_07_on.setObjectName("pushButton_f_07_on")
        self.pushButton_f_07_off = QtWidgets.QPushButton(self.widget_f_07)
        self.pushButton_f_07_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_07_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_07_off.setText("")
        self.pushButton_f_07_off.setObjectName("pushButton_f_07_off")
        self.horizontalLayout_f_316.addWidget(self.widget_f_07)

        self.page_t_8 = QtWidgets.QWidget()
        self.verticalLayout_t_8 = QtWidgets.QVBoxLayout(self.page_t_8)
        self.horizontalLayout_t_8 = QtWidgets.QHBoxLayout()
        self.widget_t_8 = QtWidgets.QWidget()
        self.widget_t_8.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_8.setObjectName(f"widget_t_8_{KT}")
        self.widget_t_8.setStyleSheet (f"#{self.widget_t_8.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_8 = QtWidgets.QVBoxLayout(self.widget_t_8)
        self.verticalLayout_t_8.addLayout(self.horizontalLayout_t_8)
        self.horizontalLayout_t_8.addWidget(self.widget_t_8)
        self.horizontalLayout_f_107 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_8.addLayout(self.horizontalLayout_f_107)
        self.horizontalLayout_f_117 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_107.addLayout(self.horizontalLayout_f_117)
        self.textField_vp_80 = QtWidgets.QLineEdit()
        self.textField_vp_80.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_80.setFont(font)
        self.textField_vp_80.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_80.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_80.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_117.addWidget(self.textField_vp_80)
        self.horizontalLayout_f_127 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_127.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_117.addLayout(self.horizontalLayout_f_127)
        self.comboBox_f_8_ = QtWidgets.QComboBox()
        self.comboBox_f_8_.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_8_.setFont(font)
        self.comboBox_f_8_.setObjectName(f"comboBox_f_8_{KT}")
        self.comboBox_f_8_.setStyleSheet(f"#{self.comboBox_f_8_.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_8_.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_8_.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_8_.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_8_.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_8_.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_8_.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_8_.addItem("РАСКР. СПИСОК")
        self.comboBox_f_8_.addItem("ШКАЛА")
        self.comboBox_f_8_.addItem("ДАТА")
        self.comboBox_f_8_.addItem("ВРЕМЯ")
        self.horizontalLayout_f_127.addWidget(self.comboBox_f_8_)
        # Среднее поле
        self.horizontalLayout_f_207 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_8.addLayout(self.horizontalLayout_f_207)
        self.horizontalLayout_f_217 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_227 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_207.addLayout(self.horizontalLayout_f_217)
        self.horizontalLayout_f_207.addLayout(self.horizontalLayout_f_227)
        self.textField_low_8 = QtWidgets.QLineEdit()
        self.textField_low_8.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_8.setFont(font)
        self.textField_low_8.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_213.addWidget(self.textField_low_8)
        self.textField_low_8.setPlaceholderText(_translate("MainWindow", "1 Вариант"))
        self.textField_low_8 = QtWidgets.QLineEdit()
        self.textField_low_8.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_8.setFont(font)
        self.textField_low_8.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_227.addWidget(self.textField_low_8)
        self.textField_low_8.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_237 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_227.addLayout(self.vertcalLayout_237)
        spacer_8 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_237.addItem(spacer_8)
        self.Button_Question_8 = QtWidgets.QPushButton()
        self.Button_Question_8.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_8.setFont(font)
        self.Button_Question_8.setObjectName(f"Button_Question_8_{KT}")
        self.Button_Question_8.setStyleSheet(f"#{self.Button_Question_8.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_8.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_8.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_237.addWidget(self.Button_Question_8)

        self.horizontalLayout_m_08 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_8.addLayout(self.horizontalLayout_m_08)
        self.button_var_8 = QtWidgets.QPushButton()
        self.button_var_8.setObjectName(f"button_var_8_{KT}")
        self.button_var_8.setStyleSheet(f"#{self.button_var_8.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.button_var_8.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.button_var_8.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.horizontalLayout_m_08.addWidget(self.button_var_8)

        # Нижнее поле
        self.horizontalLayout_f_307 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_8.addLayout(self.horizontalLayout_f_307)
        self.horizontalLayout_f_317 = QtWidgets.QHBoxLayout()
        self.Button_Copy_08 = QtWidgets.QPushButton()
        self.Button_Copy_08.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_08.setObjectName(f"Button_Copy_8{KT}")
        self.Button_Copy_08.setStyleSheet(f"#{self.Button_Copy_08.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_08.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_08.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_08.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_08.setIcon(icon2)
        self.horizontalLayout_f_307.addWidget(self.Button_Copy_08)
        self.horizontalLayout_f_307.addLayout(self.horizontalLayout_f_317)
        self.Obyazatelny_vopros_f_08 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_08.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_08.setFont(font)
        self.Obyazatelny_vopros_f_08.setObjectName("Obyazatelny_vopros_f_08")
        self.Obyazatelny_vopros_f_08.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_317.addWidget(self.Obyazatelny_vopros_f_08)
        self.widget_f_08 = QtWidgets.QWidget()
        self.widget_f_08.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_08.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_08.setObjectName("widget_f_08")
        self.pushButton_f_08_on = QtWidgets.QPushButton(self.widget_f_08)
        self.pushButton_f_08_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_08_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_08_on.setText("")
        self.pushButton_f_08_on.setObjectName("pushButton_f_08_on")
        self.pushButton_f_08_off = QtWidgets.QPushButton(self.widget_f_08)
        self.pushButton_f_08_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_08_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_08_off.setText("")
        self.pushButton_f_08_off.setObjectName("pushButton_f_08_off")
        self.horizontalLayout_f_317.addWidget(self.widget_f_08)

        KT += 1
        self.stackedWidget_t.addWidget(self.page_t_1)
        self.stackedWidget_t.addWidget(self.page_t_2)
        self.stackedWidget_t.addWidget(self.page_t_3)
        self.stackedWidget_t.addWidget(self.page_t_4)
        self.stackedWidget_t.addWidget(self.page_t_5)
        self.stackedWidget_t.addWidget(self.page_t_6)
        self.stackedWidget_t.addWidget(self.page_t_7)
        self.stackedWidget_t.addWidget(self.page_t_8)
    def transfer_back(self):
        global KT
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        KT = 1
    def transfer_Fill(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.Button_Back_Fill.clicked.connect(self.transfer_back)

app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())

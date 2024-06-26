import os, ast, sys, tkinter.messagebox
from tkinter.messagebox import showinfo, askyesno
from os import listdir
from os.path import isfile, join
from functools import partial
from tkinter import filedialog
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication,
    QFileDialog
)
import sys
import math
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication
)
from Main_Form import Ui_MainWindow as Form
# from delete import Ui_MainWindow as DDD
import Pictures, copy_delete
from PyQt6.QtGui     import QFontDatabase, QFont
from PyQt6.QtCore    import Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from docxtpl import DocxTemplate

# import delete, copy
KT = int(1)
DT = int(8)
Ammount = int()
Armagedon = []
class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        #загрузка шрифтов в приложение
        id = QFontDatabase.addApplicationFont('./Fonts/ofont.ru_Noah.ttf')
        # Если id равен -1, то шрифт не установлен
        if id == -1: 
            print('Ошибка подключения шрифтов')
        font = QFont('ofont.ru_Noah', 70)
        font2 = QFont('ofont.ru_Noah', 28)
        font3 = QFont('ofont.ru_Noah', 20)
        
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
        #добовление шрифтов
        global font,font2,font3,font4,font9,font6,font7,Collective, Collectiv_1, fool_name, Collectable
        fool_name = ''
        font = QFont('ofont.ru_Noah', 80)
        font2 = QFont('ofont.ru_Noah', 30)
        font3 = QFont('ofont.ru_Noah', 20)
        font4 = QFont('ofont.ru_Noah', 70)
        font6 = QFont('ofont.ru_Noah', 30)
        font7 = QFont('ofont.ru_Noah', 22)
        font8 = QFont('ofont.ru_Noah', 60)
        font9 = QFont('ofont.ru_Noah', 14)
        self.ui = Form()
        self.ui.setupUi(self)
        Collectable = []
        Collective = []
        Collectiv_1 = []
        Collectiv_1.append([self.ui.stackedWidget_2,
        [[self.ui.comboBox_2, self.ui.page_4,self.ui.Vopros_2,self.ui.Obyazatelny_vopros_2,self.ui.Tag_2],
        [self.ui.comboBox_5, self.ui.page_7,self.ui.Vopros_5,self.ui.Obyazatelny_vopros_5,self.ui.Tag_5],
        [self.ui.comboBox_9, self.ui.page_9,self.ui.Vopros_7,self.ui.Obyazatelny_vopros_7,self.ui.Tag_7,[]],
        [self.ui.comboBox_4, self.ui.page_6,self.ui.Vopros_4,self.ui.Obyazatelny_vopros_4,self.ui.Tag_4,[]],
        [self.ui.comboBox_3, self.ui.page_5,self.ui.Vopros_3,self.ui.Obyazatelny_vopros_3,self.ui.Tag_3,[]],
        [self.ui.comboBox_8, self.ui.page_8,"pool",self.ui.Obyazatelny_vopros_6,self.ui.Tag_6,[]],
        [ self.ui.comboBox, self.ui.page_2,self.ui.Vopros,self.ui.Obyazatelny_vopros,self.ui.Tag],
        [self.ui.comboBox_10, self.ui.page_3,self.ui.Vopros_8,self.ui.Obyazatelny_vopros_8,self.ui.Tag_8]]])

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)

        #Делаем не активными поля на формах
        self.ui.dateEdit.setDisabled(True)
        self.ui.timeEdit.setDisabled(True)
        self.ui.Kratki_otvet.setDisabled(True)
        self.ui.Kratki_otvet_4.setDisabled(True)

        #присвоение шрифтов объектам
        self.ui.Kratki_otvet.setFont(font3)

        self.ui.Vopros_2.setFont(font3)
        self.ui.Glavnaya.setFont(font4)
        self.ui.Button_Zapolnit.setFont(font6)
        self.ui.Button_Spisok.setFont(font6)
        self.ui.Button_Save.setFont(font3)
        self.ui.Button_Back.setFont(font3)

        self.ui.Obyazatelny_vopros_2.setFont(font7)
        self.ui.Button_Dok.setFont(font3)
        self.ui.Button_Forma_plus.setFont(font3)
        self.ui.Dobavit_dokument_label.setFont(font3)
        self.ui.Dobavochnoe_pole.setFont(font8)
        self.ui.Button_Dok.setFont(font3)
        self.ui.Button_Forma_plus.setFont(font3)
        self.ui.Dobavit_dokument_label.setFont(font3)
        self.ui.Tag_2.setFont(font3)
        self.ui.Vopros_5.setFont(font3)
        self.ui.Kratki_otvet_4.setFont(font3)
        self.ui.comboBox_5.setFont(font9)
        self.ui.comboBox_2.setFont(font9)
        self.ui.Tag_5.setFont(font3)
        self.ui.Obyazatelny_vopros_5.setFont(font7)
        self.ui.Button_Question.setFont(font3)
        self.ui.Button_Trash.setFont(font3)

        self.ui.Button_Question_5.setFont(font3)
        self.ui.label_3.setFont(font7)
        self.ui.Poisk_2.setFont(font3)
        self.ui.tableWidget.setFont(font9)
        self.ui.Button_Back_Fill.setFont(font3)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        self.ui.Button_Spisok.clicked.connect(self.transfer_page_add)
        self.ui.Button_Zapolnit.clicked.connect(self.transfer_Fill)
        self.ui.Button_Dok.clicked.connect(self.Open_main_file_btn)
        self.ui.Button_Save.clicked.connect(self.save_form)
        self.ui.Button_Back.clicked.connect(self.transfer_back)
        self.ui.Button_Forma_plus.clicked.connect(self.add_field)
        self.ui.Button_Back_Fill.clicked.connect(self.transfer_back)
        self.ui.Button_Save_2.clicked.connect(self.save_document) 
        
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        
        self.ui.comboBox_2.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_2))

        self.newDocument()
        
    def opt(self,index):
        index.currentIndexChanged.disconnect()
        self.ui.comboBox_10.setCurrentIndex(index.currentIndex())
        self.ui.comboBox_9.setCurrentIndex(index.currentIndex())
        self.ui.comboBox_8.setCurrentIndex(index.currentIndex())
        self.ui.comboBox_5.setCurrentIndex(index.currentIndex())
        self.ui.comboBox_4.setCurrentIndex(index.currentIndex())
        self.ui.comboBox_3.setCurrentIndex(index.currentIndex())
        self.ui.comboBox_2.setCurrentIndex(index.currentIndex())
        self.ui.comboBox.setCurrentIndex(index.currentIndex())
        if (index.currentIndex() == 0):
            self.ui.comboBox_2.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_2))
        elif (index.currentIndex() == 1):
            self.ui.comboBox_5.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_5))
        elif (index.currentIndex() == 2):
            self.ui.comboBox_9.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_9))
        elif (index.currentIndex() == 3):
            self.ui.comboBox_4.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_4))
        elif (index.currentIndex() == 4):
            self.ui.comboBox_3.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_3))
        elif (index.currentIndex() == 5):
            self.ui.comboBox_8.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_8))
        elif (index.currentIndex() == 6):
            self.ui.comboBox.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox))
        elif (index.currentIndex() == 7):
            self.ui.comboBox_10.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_10))
        # elif (index.currentIndex() == 8):
        #     self.ui.comboBox_2.currentIndexChanged.connect(partial(self.opt,self.ui.comboBox_2))

        if index.currentIndex() == 6:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_2)
        elif index.currentIndex() == 7:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3)
        elif index.currentIndex() == 5:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_8)
        elif index.currentIndex() == 4:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)   
        elif index.currentIndex() == 3:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)     
        elif index.currentIndex() == 2:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_9)
        elif index.currentIndex() == 1:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_7)     
        elif index.currentIndex() == 0:
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)
        index_page = index.currentIndex() 
         
                     
    #постороение пути к документу
    def Open_main_file_btn(self):
        res =QFileDialog.getOpenFileName(self, 'Open File', ".",'DOC file (*.doc*)')
        res = os.path.basename(res[0])
        self.ui.Dobavit_dokument_label.setText(res)
        global fool_name, name,filename
    #разделение названия файла от его расширения  
        fool_name = res
        filename = fool_name
        name, extension = os.path.splitext(filename)
        
    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_page)
        
    def add_field(self):
        global KT, Collective, Armagedon, Collectiv_1,font,font2,font3,font4,font9,font6,font7
        global name
        

        
        _translate = QtCore.QCoreApplication.translate
        self.stackedWidget_t_ = QtWidgets.QStackedWidget()
        self.ui.verticalLayout_7.addWidget(self.stackedWidget_t_)
        
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
        self.textField_vp_10.setFont(font3)
        self.horizontalLayout_f_110.addWidget(self.textField_vp_10)
        self.horizontalLayout_f_120 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_120.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_110.addLayout(self.horizontalLayout_f_120)
        self.comboBox_f_1 = QtWidgets.QComboBox()
        self.comboBox_f_1.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_1.setFont(font9)
        self.comboBox_f_1.setObjectName(f"comboBox_f_1_{KT}")
        self.comboBox_f_1.setStyleSheet(f"#{self.comboBox_f_1.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_1.objectName()}"":hover {\n"
"background: rgb(188, 188, 188);\n"
"}\n"
f"#{self.comboBox_f_1.objectName()}"":pressed { \n"
"background: rgb(171, 171, 171);\n"
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
        self.horizontalLayout_f_200.setSpacing(6)
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_200)
        self.horizontalLayout_f_210 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_210.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_f_220 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_220.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_f_200.addLayout(self.horizontalLayout_f_210)
        self.horizontalLayout_f_200.addLayout(self.horizontalLayout_f_220)
        self.textField_low_1 = QtWidgets.QLineEdit()
        self.textField_low_1.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_1.setFont(font3)
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
        self.textField_tag_1.setFont(font3)
        self.textField_tag_1.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_tag_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_220.addWidget(self.textField_tag_1)
        self.textField_tag_1.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_230 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_f_220.addLayout(self.vertcalLayout_230)
        spacer_1 = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
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
        self.Button_Question_1.setText(_translate("MainWindow", "?"))
        self.vertcalLayout_230.addItem(spacer_1)
        self.vertcalLayout_230.addWidget(self.Button_Question_1)
        self.Button_Question_1.setFont(font3)
        # Нижнее поле
        self.horizontalLayout_f_300 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_300)
        self.horizontalLayout_f_310 = QtWidgets.QHBoxLayout()
        self.Button_Delete_01 = QtWidgets.QPushButton()
        self.Button_Delete_01.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_01.setObjectName(f"Button_Delete_0{KT}")
        self.Button_Delete_01.setStyleSheet(f"#{self.Button_Delete_01.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_01.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_01.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_01.setText("")
        # self.Button_Delete_01.setIcon(QIcon("delete.png"))
        self.Button_Copy_01 = QtWidgets.QPushButton()
        self.Button_Copy_01.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_01.setObjectName(f"Button_Copy_0{KT}")
        self.Button_Copy_01.setStyleSheet(f"#{self.Button_Copy_01.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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
        icon2.addPixmap(QtGui.QPixmap("../../../../../copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_01.setIcon(icon2)
        self.horizontalLayout_f_300.addWidget(self.Button_Delete_01)
        self.horizontalLayout_f_300.addWidget(self.Button_Copy_01)
        self.horizontalLayout_f_300.addLayout(self.horizontalLayout_f_310)
        self.Obyazatelny_vopros_f_01 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_01.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_01.setFont(font7)
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
"background-color: rgb(228, 228, 228); \n"
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
        self.textField_vp_20.setFont(font3)
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
        self.comboBox_f_2_.setFont(font9)
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
        self.horizontalLayout_f_211.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_f_221 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_201.addLayout(self.horizontalLayout_f_211)
        self.horizontalLayout_f_201.addLayout(self.horizontalLayout_f_221)
        self.textField_low_2 = QtWidgets.QLineEdit()
        self.textField_low_2.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_2.setFont(font3)
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
        self.textField_low_2.setFont(font3)
        self.textField_low_2.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_221.addWidget(self.textField_low_2)
        self.textField_low_2.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_231 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_f_221.addLayout(self.vertcalLayout_231)
        spacer_2 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_231.addItem(spacer_2)
        self.Button_Question_2 = QtWidgets.QPushButton()
        self.Button_Question_2.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_2.setFont(font3)
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
        self.Button_Question_2.setText(_translate("MainWindow", "?"))
        # Нижнее поле
        self.horizontalLayout_f_301 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_2.addLayout(self.horizontalLayout_f_301)
        self.horizontalLayout_f_311 = QtWidgets.QHBoxLayout()
        self.Button_Delete_02 = QtWidgets.QPushButton()
        self.Button_Delete_02.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_02.setObjectName(f"Button_Delete_1{KT}")
        self.Button_Delete_02.setStyleSheet(f"#{self.Button_Delete_02.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_02.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_02.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_02.setText("")
        self.horizontalLayout_f_301.addWidget(self.Button_Delete_02)
        self.Button_Copy_02 = QtWidgets.QPushButton()
        self.Button_Copy_02.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_02.setObjectName(f"Button_Copy_1{KT}")
        self.Button_Copy_02.setStyleSheet(f"#{self.Button_Copy_02.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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
        self.Obyazatelny_vopros_f_02.setFont(font7)
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
"background-color: rgb(228, 228, 228); \n"
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
        self.horizontalLayout_f_212.setContentsMargins(0, 0, 5, 0)
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
        self.vertcalLayout_232 = QtWidgets.QVBoxLayout()
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
        self.button_var.setMaximumSize(300, 40)
        self.button_var.setObjectName(f"button_var_{KT}")
        self.button_var.setStyleSheet(f"#{self.button_var.objectName()}""{\n"
"border-top: 2px solid;"
"border-top-color: rgb(255, 76, 0);"
"border-bottom: 2px solid;"
"border-bottom-color: rgb(255, 76, 0);"
"}\n"
f"#{self.button_var.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.button_var.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.button_var.setText("ДОБАВИТЬ ВАРИАНТ")
        self.button_var.setFont(font)
        self.horizontalLayout_m_03.addWidget(self.button_var)
        self.label_or = QtWidgets.QLabel()
        self.label_or.setText('ИЛИ')
        self.label_or.setMaximumSize(55, 35)
        self.horizontalLayout_m_03.addWidget(self.label_or)
        self.button_difvar = QtWidgets.QPushButton()
        self.button_difvar.setMaximumSize(380, 35)
        self.button_difvar.setText('ДОБАВИТЬ ВАРИАНТ "Другое"')
        self.button_difvar.setObjectName(f"button_difvar_{KT}")
        self.button_difvar.setStyleSheet(f"#{self.button_difvar.objectName()}""{\n"
"border-top: 2px solid;"
"border-top-color: rgb(255, 76, 0);"
"border-bottom: 2px solid;"
"border-bottom-color: rgb(255, 76, 0);"
"}\n"
f"#{self.button_difvar.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.button_difvar.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.horizontalLayout_m_03.addWidget(self.button_difvar)
        # Нижнее поле
        self.horizontalLayout_f_302 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_3.addLayout(self.horizontalLayout_f_302)
        self.horizontalLayout_f_312 = QtWidgets.QHBoxLayout()
        self.Button_Delete_03 = QtWidgets.QPushButton()
        self.Button_Delete_03.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_03.setObjectName(f"Button_Delete_2{KT}")
        self.Button_Delete_03.setStyleSheet(f"#{self.Button_Delete_03.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_03.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_03.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_03.setText("")
        self.horizontalLayout_f_302.addWidget(self.Button_Delete_03)
        self.Button_Copy_03 = QtWidgets.QPushButton()
        self.Button_Copy_03.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_03.setObjectName(f"Button_Copy_3{KT}")
        self.Button_Copy_03.setStyleSheet(f"#{self.Button_Copy_03.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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
"background-color: rgb(228, 228, 228); \n"
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
        self.horizontalLayout_f_213.setContentsMargins(0, 0, 5, 0)
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
        self.vertcalLayout_233 = QtWidgets.QVBoxLayout()
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
        self.button_var_1.setMaximumSize(300, 40)
        self.button_var_1.setObjectName(f"button_var_1_{KT}")
        self.button_var_1.setStyleSheet(f"#{self.button_var_1.objectName()}""{\n"
"border-top: 2px solid;"
"border-top-color: rgb(255, 76, 0);"
"border-bottom: 2px solid;"
"border-bottom-color: rgb(255, 76, 0);"
"}\n"
f"#{self.button_var_1.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.button_var_1.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.button_var_1.setText("ДОБАВИТЬ ВАРИАНТ")
        self.button_var_1.setFont(font)
        self.horizontalLayout_m_04.addWidget(self.button_var_1)

        # Нижнее поле
        self.horizontalLayout_f_303 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_4.addLayout(self.horizontalLayout_f_303)
        self.horizontalLayout_f_313 = QtWidgets.QHBoxLayout()
        self.Button_Delete_04 = QtWidgets.QPushButton()
        self.Button_Delete_04.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_04.setObjectName(f"Button_Delete_3{KT}")
        self.Button_Delete_04.setStyleSheet(f"#{self.Button_Delete_04.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_04.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_04.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_04.setText("")
        self.horizontalLayout_f_303.addWidget(self.Button_Delete_04)
        self.Button_Copy_04 = QtWidgets.QPushButton()
        self.Button_Copy_04.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_04.setObjectName(f"Button_Copy_4{KT}")
        self.Button_Copy_04.setStyleSheet(f"#{self.Button_Copy_04.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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
        self.horizontalLayout_f_313.addWidget(self.Obyazatelny_vopros_f_04)
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
"background-color: rgb(228, 228, 228); \n"
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
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_L_5.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_L_5.objectName()}"":pressed { \n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"")
        self.comboBox_L_5.setObjectName("comboBox_6")
        self.comboBox_L_5.addItem("0")
        self.comboBox_L_5.addItem("1")
        self.horizontalLayout_f_114.addWidget(self.comboBox_L_5)
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
        self.horizontalLayout_f_114.addWidget(self.comboBox_R_5)
        self.horizontalLayout_f_114.setSpacing(50)
        self.horizontalLayout_f_124 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_124.setContentsMargins(200, 0, 0, 0)
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
        self.horizontalLayout_f_214.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_f_224 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_224.setContentsMargins(0, 0, 80, 0)
        self.horizontalLayout_f_204.addLayout(self.horizontalLayout_f_214)
        self.horizontalLayout_f_204.addLayout(self.horizontalLayout_f_224)
        self.verticalLayout_f_234 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_f_234 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_224.addLayout(self.horizontalLayout_f_234)
        self.horizontalLayout_f_214.addLayout(self.verticalLayout_f_234)
        self.horizontalLayout_f_244 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_254 = QtWidgets.QHBoxLayout()
        self.verticalLayout_f_234.addLayout(self.horizontalLayout_f_244)
        self.verticalLayout_f_234.addLayout(self.horizontalLayout_f_254)
        spacer_up_l = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_f_244.addSpacerItem(spacer_up_l)
        self.horizontalLayout_n_204 = QtWidgets.QHBoxLayout()
        self.Label_up = QtWidgets.QLabel()
        self.Label_up.setFont(font)
        self.Label_up.setText("0")
        self.horizontalLayout_n_204.addWidget(self.Label_up)
        self.horizontalLayout_f_244.addLayout(self.horizontalLayout_n_204)
        self.vopros_up = QtWidgets.QLineEdit()
        self.vopros_up.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vopros_up.setFont(font)
        self.vopros_up.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.vopros_up.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.vopros_up.setPlaceholderText('Подпись (Необязательно)')
        self.horizontalLayout_f_244.addWidget(self.vopros_up)
        spacer_up_r = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_f_244.addSpacerItem(spacer_up_r)
        self.horizontalLayout_n_214 = QtWidgets.QHBoxLayout()
        self.Label_Down = QtWidgets.QLabel()
        self.Label_Down.setFont(font)
        self.Label_Down.setText("2")
        spacer_down_l = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_f_254.addSpacerItem(spacer_down_l)
        self.horizontalLayout_n_214.addWidget(self.Label_Down)
        self.horizontalLayout_f_254.addLayout(self.horizontalLayout_n_214)
        self.vopros_down = QtWidgets.QLineEdit()
        self.vopros_down.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vopros_down.setFont(font)
        self.vopros_down.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.vopros_down.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.vopros_down.setPlaceholderText('Подпись (Необязательно)')
        self.horizontalLayout_f_254.addWidget(self.vopros_down)
        spacer_down_r = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_f_254.addSpacerItem(spacer_down_r)
        self.textField_Tag_5 = QtWidgets.QLineEdit()
        self.textField_Tag_5.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_Tag_5.setFont(font)
        self.textField_Tag_5.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_Tag_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_224.addWidget(self.textField_Tag_5)
        self.textField_Tag_5.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_234 = QtWidgets.QVBoxLayout()
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
        self.verticalLayout_w_5.addLayout(self.horizontalLayout_f_304)
        self.horizontalLayout_f_314 = QtWidgets.QHBoxLayout()
        self.Button_Delete_05 = QtWidgets.QPushButton()
        self.Button_Delete_05.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_05.setObjectName(f"Button_Delete_4{KT}")
        self.Button_Delete_05.setStyleSheet(f"#{self.Button_Delete_05.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_05.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_05.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_05.setText("")
        self.horizontalLayout_f_304.addWidget(self.Button_Delete_05)
        self.Button_Copy_05 = QtWidgets.QPushButton()
        self.Button_Copy_05.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_05.setObjectName(f"Button_Copy_05{KT}")
        self.Button_Copy_05.setStyleSheet(f"#{self.Button_Copy_05.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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
"background-color: rgb(228, 228, 228); \n"
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
        self.horizontalLayout_f_215.setContentsMargins(0, 0, 300, 0)
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
        self.textField_Tag_6 = QtWidgets.QLineEdit()
        self.textField_Tag_6.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_Tag_6.setFont(font)
        self.textField_Tag_6.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_Tag_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_225.addWidget(self.textField_Tag_6)
        self.textField_Tag_6.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_235 = QtWidgets.QVBoxLayout()
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
        self.Button_Delete_06 = QtWidgets.QPushButton()
        self.Button_Delete_06.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_06.setObjectName(f"Button_Delete_5{KT}")
        self.Button_Delete_06.setStyleSheet(f"#{self.Button_Delete_06.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_06.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_06.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_06.setText("")
        self.horizontalLayout_f_305.addWidget(self.Button_Delete_06)
        self.Button_Copy_06 = QtWidgets.QPushButton()
        self.Button_Copy_06.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_06.setObjectName(f"Button_Copy_06{KT}")
        self.Button_Copy_06.setStyleSheet(f"#{self.Button_Copy_06.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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
"background-color: rgb(228, 228, 228); \n"
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
        self.horizontalLayout_f_216.setContentsMargins(0, 0, 300, 0)
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
        self.textField_Tag_7 = QtWidgets.QLineEdit()
        self.textField_Tag_7.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_Tag_7.setFont(font)
        self.textField_Tag_7.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_Tag_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_226.addWidget(self.textField_Tag_7)
        self.textField_Tag_7.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_236 = QtWidgets.QVBoxLayout()
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
        self.Button_Delete_07 = QtWidgets.QPushButton()
        self.Button_Delete_07.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_07.setObjectName(f"Button_Delete_6{KT}")
        self.Button_Delete_07.setStyleSheet(f"#{self.Button_Delete_07.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_07.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_07.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_07.setText("")
        self.horizontalLayout_f_306.addWidget(self.Button_Delete_07)
        self.Button_Copy_07 = QtWidgets.QPushButton()
        self.Button_Copy_07.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_07.setObjectName(f"Button_Copy_07{KT}")
        self.Button_Copy_07.setStyleSheet(f"#{self.Button_Copy_07.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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
"background-color: rgb(228, 228, 228); \n"
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
        self.horizontalLayout_f_217.setContentsMargins(0, 0, 5, 0)
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
        self.horizontalLayout_f_217.addWidget(self.textField_low_8)     
        self.textField_low_8.setPlaceholderText(_translate("MainWindow", "1 Вариант"))
        self.textField_Tag_8 = QtWidgets.QLineEdit()
        self.textField_Tag_8.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_Tag_8.setFont(font)
        self.textField_Tag_8.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_Tag_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_227.addWidget(self.textField_Tag_8)
        self.textField_Tag_8.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_237 = QtWidgets.QVBoxLayout()
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
        self.button_var_8.setMaximumSize(300, 40)
        self.button_var_8.setObjectName(f"button_var_8_{KT}")
        self.button_var_8.setStyleSheet(f"#{self.button_var_8.objectName()}""{\n"
"border-top: 2px solid;"
"border-top-color: rgb(255, 76, 0);"
"border-bottom: 2px solid;"
"border-bottom-color: rgb(255, 76, 0);"
"}\n"
f"#{self.button_var_8.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.button_var_8.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.button_var_8.setText("ДОБАВИТЬ ВАРИАНТ")
        self.button_var_8.setFont(font)
        self.horizontalLayout_m_08.addWidget(self.button_var_8)
        # Нижнее поле
        self.horizontalLayout_f_307 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_8.addLayout(self.horizontalLayout_f_307)
        self.horizontalLayout_f_317 = QtWidgets.QHBoxLayout()
        self.Button_Delete_08 = QtWidgets.QPushButton()
        self.Button_Delete_08.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Delete_08.setObjectName(f"Button_Delete_7{KT}")
        self.Button_Delete_08.setStyleSheet(f"#{self.Button_Delete_08.objectName()}""{\n"
"image: url(:/delete/Rectangle_32.png);\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Delete_08.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Delete_08.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Delete_08.setText("")
        self.horizontalLayout_f_307.addWidget(self.Button_Delete_08)
        self.Button_Copy_08 = QtWidgets.QPushButton()
        self.Button_Copy_08.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_08.setObjectName(f"Button_Copy_8{KT}")
        self.Button_Copy_08.setStyleSheet(f"#{self.Button_Copy_08.objectName()}""{\n"
"image: url(:/copy/1621635.png);\n"
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

        self.stackedWidget_t_.addWidget(self.page_t_1)
        self.stackedWidget_t_.addWidget(self.page_t_2)
        self.stackedWidget_t_.addWidget(self.page_t_3)
        self.stackedWidget_t_.addWidget(self.page_t_4)
        self.stackedWidget_t_.addWidget(self.page_t_5)
        self.stackedWidget_t_.addWidget(self.page_t_6)
        self.stackedWidget_t_.addWidget(self.page_t_7)
        self.stackedWidget_t_.addWidget(self.page_t_8)
        self.stackedWidget_t_.setCurrentWidget(self.page_t_1)
        Armagedon.append(self.stackedWidget_t_) 
        KT += 1
        # Пятая
        Collective.append([self.stackedWidget_t_,
        [[self.comboBox_f_1,self.page_t_1,self.textField_vp_10,self.Obyazatelny_vopros_f_01,self.textField_tag_1],
        [self.comboBox_f_2_,self.page_t_2,self.textField_vp_20,self.Obyazatelny_vopros_f_02,self.textField_low_2],
        [self.comboBox_f_3_,self.page_t_3,self.textField_vp_30,self.Obyazatelny_vopros_f_03,self.textField_low_3],
        [self.comboBox_f_4_,self.page_t_4,self.textField_vp_40,self.Obyazatelny_vopros_f_04,self.textField_low_4],
        [self.comboBox_f_5_,self.page_t_8,"fool",self.Obyazatelny_vopros_f_05,self.textField_Tag_5,[]],
        [self.comboBox_f_6_,self.page_t_5,self.textField_vp_60,self.Obyazatelny_vopros_f_06,self.textField_Tag_6,[]],
        [self.comboBox_f_7_,self.page_t_7,self.textField_vp_70,self.Obyazatelny_vopros_f_07,self.textField_Tag_7,[]],
        [self.comboBox_f_8_,self.page_t_6,self.textField_vp_80,self.Obyazatelny_vopros_f_08,self.textField_Tag_8,[]]]])

        self.comboBox_f_1.currentIndexChanged.connect(partial(self.opt_2,self.comboBox_f_1))
    def opt_2(self,index):
        index.currentIndexChanged.disconnect()
        global number_form
        result = False 
        number_form = 0
        number_list = 0  
        for forms in Collective:
                for lists in forms[1]:
                        if index == lists[0]:
                                result = True
                                break
                        else:
                                number_list +=1
                if result == True:
                        break
                else:                        
                        number_form +=1   
        Collective[number_form][1][0][0].setCurrentIndex(index.currentIndex())
        Collective[number_form][1][1][0].setCurrentIndex(index.currentIndex())
        Collective[number_form][1][2][0].setCurrentIndex(index.currentIndex())
        Collective[number_form][1][3][0].setCurrentIndex(index.currentIndex())
        Collective[number_form][1][4][0].setCurrentIndex(index.currentIndex())
        Collective[number_form][1][5][0].setCurrentIndex(index.currentIndex())
        Collective[number_form][1][6][0].setCurrentIndex(index.currentIndex())
        Collective[number_form][1][7][0].setCurrentIndex(index.currentIndex())         

        if (index.currentIndex() == 0):
            Collective[number_form][1][0][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][0][0]))
        elif (index.currentIndex() == 1):
            Collective[number_form][1][1][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][1][0]))
        elif (index.currentIndex() == 2):
            Collective[number_form][1][2][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][2][0]))
        elif (index.currentIndex() == 3):
            Collective[number_form][1][3][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][3][0]))
        elif (index.currentIndex() == 4):
            Collective[number_form][1][7][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][7][0]))
        elif (index.currentIndex() == 5):
            Collective[number_form][1][4][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][4][0]))
        elif (index.currentIndex() == 6):
            Collective[number_form][1][6][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][6][0]))
        elif (index.currentIndex() == 7):
            Collective[number_form][1][5][0].currentIndexChanged.connect(partial(self.opt_2,Collective[number_form][1][5][0]))
        # elif (index.currentIndex() == 8):
        #     self.comboBox_f_1.currentIndexChanged.connect(partial(self.opt_2,self.comboBox_f_1))

        if index.currentIndex() == 6:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][6][1])
        elif index.currentIndex() == 7:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][7][1])
        elif index.currentIndex() == 5:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][5][1])
        elif index.currentIndex() == 4:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][4][1])   
        elif index.currentIndex() == 3:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][3][1])     
        elif index.currentIndex() == 2:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][2][1])
        elif index.currentIndex() == 1:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][1][1])     
        elif index.currentIndex() == 0:
           Collective[number_form][0].setCurrentWidget(Collective[number_form][1][0][1])
        index_page = index.currentIndex()

    def Questioning(self):
        global Collectable, Ammount
        Ammount = ((len(Collectable))-1)
        with open("/Danno/Test.txt") as textFile:
                lines = [line.split() for line in textFile]


    def delete(self,stackedWidget_t_):
        pages = stackedWidget_t_.count()
        for i in range(pages):
                widget = stackedWidget_t_.widget(0)
                stackedWidget_t_.removeWidget(widget)
        stackedWidget_t_.deleteLater()
    def save_form(self, index):
        global name, fool_name, Collective, number_form, Collectiv_1
        if fool_name == '':
            tkinter.messagebox.showwarning(title="Внимание!",message="Выберите документ для формы!")
        else:
                forma_1 = [] 
                vse = []
                forma = [] 
                vse.append(fool_name)
                for forms_1 in Collectiv_1:
                        forma_1 = [] 
                        Box_1 = forms_1[1][0][0].currentIndex() 
                        text_1 = forms_1[1][Box_1][2].text()
                        ob_vopros_1 = False
                        Teg_1 = forms_1[1][Box_1][4].text() 
                        forma_1.append(Box_1)
                        forma_1.append(text_1)
                        forma_1.append(Teg_1)
                        vse.append(forma_1) 

                for forms in Collective:
                        forma = []
                        Box = forms[1][0][0].currentIndex()
                        text = forms[1][Box][2].text()
                        ob_vopros = False
                        Teg = forms[1][Box][4].text()
                        forma.append(Box)
                        forma.append(text)
                        forma.append(Teg)
                        vse.append(forma) 
               

                my_file = open('Danno/' + name+".txt", "w+")
                my_file.write(str(vse))
                my_file.close()
                with open('Danno/' + name+'.txt', 'r') as f:
                        mylist = ast.literal_eval(f.read())
                self.newDocument()
                self.ui.stackedWidget.setCurrentWidget(self.ui.page)
                self.transfer_back_save()

    def newDocument(self):
        global font9
        while (self.ui.tableWidget.rowCount() > 0):
            self.ui.tableWidget.setRowCount(0)
        onlyfiles = [os.path.join('Danno', f) for f in os.listdir('Danno') if 
        os.path.isfile(os.path.join('Danno', f))]


        global button
        for i, b in enumerate(onlyfiles):
            file_name = os.path.basename(b).split('.')[0]
            row_index = self.ui.tableWidget.rowCount() 
            button = QtWidgets.QPushButton("Заполнить")
            button.setFont(font9)  
            button.clicked.connect(self.test)
            self.ui.tableWidget.insertRow(row_index)  
            self.ui.tableWidget.setItem(row_index, 0, QtWidgets.QTableWidgetItem(file_name))
            self.ui.tableWidget.setCellWidget(row_index, 1,button)
            button.clicked.connect(self.per)
        
    def test (self):
        global Collectable, Ammount, KT, galavni_collective, mylist, font3, font6
        button = self.sender()
        if button:
                row = self.ui.tableWidget.indexAt(button.pos()).row()
                name_file = self.ui.tableWidget.item(row,0).text()
                name_file = 'Danno/' + name_file +".txt"
                name_file = open( name_file)
                print(row, name_file.read())
                self.ui.Button_Back_2.clicked.connect(self.transfer_back_2)
                Ammount = ((len(Collectable))-1)
            
                any =  open("./Danno/test.txt", 'r')
                mylist = ast.literal_eval(any.read())
                # print(mylist)
                galavni_collective = []

                for f in mylist:
                        if f != mylist[0]:
                                form_id = f[0]
                                form_question = f[1]
                                form_tag = f[2]
                                # print (form_id, form_question, form_tag)
                                if form_id == 0:
                                        self.verticalLayout_q_01 = QtWidgets.QVBoxLayout()
                                        self.horizontalLayout_q_01 = QtWidgets.QHBoxLayout()
                                        font = QtGui.QFont()
                                        font.setPointSize(20)
                                        self.widget_q_01 = QtWidgets.QWidget()
                                        self.widget_q_01.setMaximumSize(QtCore.QSize(600, 400))
                                        self.widget_q_01.setObjectName(f"widget_q_01_{KT}")
                                        self.widget_q_01.setStyleSheet(f"#{self.widget_q_01.objectName()}""{\n"
"background-color: rgb(228, 228, 228)\n"
"}")
                                        self.verticalLayout_q_02 = QtWidgets.QVBoxLayout(self.widget_q_01)
                                        self.horizontalLayout_q_02 = QtWidgets.QHBoxLayout()
                                        self.horizontalLayout_q_03 = QtWidgets.QHBoxLayout()
                                        self.Question_Sentence = QtWidgets.QLabel()
                                        self.Question_Sentence.setMaximumSize(QtCore.QSize(500, 150))
                                        self.Question_Sentence.setFont(font)
                                        self.Question_Sentence.setWordWrap(True)
                                        # self.Question_Sentence.setTextFormat(Qt.RichText)
                                        # self.Question_Sentence.setAlignment(QtCore.Qt.AlignJustify)
                                        self.Question_Sentence.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
                                        self.Question_Sentence.setObjectName("Question_Sentence")
                                        self.Question_Sentence.setFont(font3)
                                        self.horizontalLayout_q_03.addWidget(self.Question_Sentence)
                                        self.horizontalLayout_q_02.addLayout(self.horizontalLayout_q_03)
                                        self.verticalLayout_q_02.addLayout(self.horizontalLayout_q_02)
                                        self.horizontalLayout_q_04 = QtWidgets.QHBoxLayout()
                                        self.horizontalLayout_q_05 = QtWidgets.QHBoxLayout()
                                        self.Line_Answer = QtWidgets.QLineEdit()
                                        self.Line_Answer.setMaximumSize(QtCore.QSize(500, 60))
                                        font = QtGui.QFont()
                                        font.setPointSize(20)
                                        self.Line_Answer.setFont(font9)
                                        self.Line_Answer.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"border-color: rgb(100, 100, 100);\n"
"background-color: rgb(220, 220, 220);")
                                        self.Line_Answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
                                        self.horizontalLayout_q_05.addWidget(self.Line_Answer)
                                        self.Line_Answer.setPlaceholderText("Ответ")
                                        self.horizontalLayout_q_04.addLayout(self.horizontalLayout_q_05)
                                        self.verticalLayout_q_02.addLayout(self.horizontalLayout_q_04)
                                        self.horizontalLayout_q_01.addWidget(self.widget_q_01)
                                        self.verticalLayout_q_01.addLayout(self.horizontalLayout_q_01)
                                        self.verticalLayout_q_03 = QtWidgets.QVBoxLayout()
                                        self.verticalLayout_q_03.addLayout(self.verticalLayout_q_01)
                                        self.ui.verticalLayout_29.addLayout(self.verticalLayout_q_03)
                                        self.Question_Sentence.setText(form_question)
                                        KT += 1
                                        galavni_collective.append([self.Line_Answer,form_tag])
                                if form_id == 1: #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                        self.verticalLayout_q_11 = QtWidgets.QVBoxLayout()
                                        self.horizontalLayout_q_11 = QtWidgets.QHBoxLayout()
                                        font = QtGui.QFont()
                                        font.setPointSize(20)
                                        self.widget_q_11 = QtWidgets.QWidget()
                                        self.widget_q_11.setMaximumSize(QtCore.QSize(600, 400))
                                        self.widget_q_11.setObjectName(f"widget_q_11_{KT}")
                                        self.widget_q_11.setStyleSheet(f"#{self.widget_q_11.objectName()}""{\n"
"background-color: rgb(228, 228, 228)\n"
"}")
                                        self.verticalLayout_q_12 = QtWidgets.QVBoxLayout(self.widget_q_11)
                                        self.horizontalLayout_q_12 = QtWidgets.QHBoxLayout()
                                        self.horizontalLayout_q_13 = QtWidgets.QHBoxLayout()
                                        self.Question_Text = QtWidgets.QLabel()
                                        self.Question_Text.setMaximumSize(QtCore.QSize(500, 150))
                                        self.Question_Text.setFont(font)
                                        # self.Question_Text.setTextFormat(Qt.RichText)
                                        self.Question_Text.setWordWrap(True)
                                        # self.Question_Text.setStyleSheet("text-align: justify;")
                                        self.Question_Text.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
                                        self.Question_Text.setObjectName("Question_Text")
                                        self.Question_Text.setFont(font3)
                                        self.horizontalLayout_q_13.addWidget(self.Question_Text)
                                        self.horizontalLayout_q_12.addLayout(self.horizontalLayout_q_13)
                                        self.verticalLayout_q_12.addLayout(self.horizontalLayout_q_12)
                                        self.horizontalLayout_q_14 = QtWidgets.QHBoxLayout()
                                        self.horizontalLayout_q_15 = QtWidgets.QHBoxLayout()
                                        self.Text_Answer = QtWidgets.QTextEdit()
                                        self.Text_Answer.setMaximumSize(QtCore.QSize(500, 150))
                                        font = QtGui.QFont()
                                        font.setPointSize(20)
                                        self.Text_Answer.setFont(font9)
                                        self.Text_Answer.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"border-color: rgb(100, 100, 100);\n"
"background-color: rgb(220, 220, 220);")
                                        self.Text_Answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
                                        self.horizontalLayout_q_15.addWidget(self.Text_Answer)
                                        self.Text_Answer.setPlaceholderText("Ответ")
                                        self.horizontalLayout_q_14.addLayout(self.horizontalLayout_q_15)
                                        self.verticalLayout_q_12.addLayout(self.horizontalLayout_q_14)
                                        self.horizontalLayout_q_11.addWidget(self.widget_q_11)
                                        self.verticalLayout_q_11.addLayout(self.horizontalLayout_q_11)
                                        self.verticalLayout_q_13 = QtWidgets.QVBoxLayout()
                                        self.verticalLayout_q_13.addLayout(self.verticalLayout_q_11)
                                        self.ui.verticalLayout_29.addLayout(self.verticalLayout_q_13)
                                        self.Question_Text.setText(form_question)
                                        KT += 1
                                        galavni_collective.append([self.Text_Answer,form_tag])
                name_file.close()
                any.close()
           
    def save_document(self):
        global filename, galavni_collective, mylist
        forma = {}
        for danni in galavni_collective:
                try:
                        text = danni[0].toPlainText()
                        forma[danni[1]] = text
                except:
                        text = danni[0].text()
                        forma[danni[1]] = text

        doc = DocxTemplate("shablon/"+ str(mylist[0]))
        try:
                doc.render(forma)
                doc.save("gotovo/" + str(mylist[0]))
        except:
            print("Закройте документ - шаблон-final.docx")
    def transfer_back_2(self):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)          
           
    def per(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Fill_page)

    def Annihilation (self, Armagedon):
        # /////////////////////////////////////////////////////////////////////
        pages_all = Armagedon.count()
        for i in range(pages_all):
                widget = Armagedon.widget(0)
                Armagedon.removeWidget(widget)
        Armagedon.deleteLater()
        # /////////////////////////////////////////////////////////////////////
        
    def transfer_back(self):
        global KT, Armagedon
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        for i in Armagedon:
            self.Annihilation(i)
        Armagedon = []
        KT = 1

    def transfer_back_save(self):
            global KT, Armagedon
            for i in Armagedon:
                self.Annihilation(i)
            Armagedon = []
            KT = 1

    def transfer_Fill(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow_main.show()
sys.exit(app.exec())
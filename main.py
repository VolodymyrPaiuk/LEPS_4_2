# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LEPS_4_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import module.Harness_to_Internal
import module.Choose_file
import module.read_record_csv
import module.Check_modular_V2

class Ui_LEPS_4_2(object):

    def __init__(self):
        #Ініціалізація всіх змінних
        self.Read_harnesses = []
        self.uniq_har = []
        self.Read_Int = []
        self.Readed_Int_and_number_of_virt = []
        self.Read_Virt = []
        self.Rezult = []
        self.Mistakes_harn = []
        self.only_index_virt = []
        self.Wirelist = []
        self.wires_in_prod_mod = []
        self.Rezult_of_check = []

    def setupUi(self, LEPS_4_2):
        LEPS_4_2.setObjectName("LEPS_4_2")
        LEPS_4_2.setWindowModality(QtCore.Qt.ApplicationModal)
        LEPS_4_2.resize(817, 420)
        self.pushButton = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 201, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 130, 271, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 271, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 210, 271, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 250, 201, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 290, 201, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 330, 271, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 370, 271, 31))
        self.pushButton_10.setObjectName("pushButton_10")

        self.label = QtWidgets.QLabel(LEPS_4_2)
        self.label.setGeometry(QtCore.QRect(220, 10, 521, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LEPS_4_2)
        self.label_2.setGeometry(QtCore.QRect(220, 50, 521, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LEPS_4_2)
        self.label_3.setGeometry(QtCore.QRect(220, 90, 521, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(LEPS_4_2)
        self.label_4.setGeometry(QtCore.QRect(500, 130, 100, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(LEPS_4_2)
        self.label_5.setGeometry(QtCore.QRect(220, 250, 100, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(LEPS_4_2)
        self.label_6.setGeometry(QtCore.QRect(220, 290, 100, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(LEPS_4_2)
        self.label_7.setGeometry(QtCore.QRect(500, 330, 100, 21))
        self.label_7.setObjectName("label_7")


        self.progressBar = QtWidgets.QProgressBar(LEPS_4_2)
        self.progressBar.setGeometry(QtCore.QRect(290, 130, 200, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(LEPS_4_2)
        self.progressBar_2.setGeometry(QtCore.QRect(290, 330, 200, 31))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")


        self.retranslateUi(LEPS_4_2)
        QtCore.QMetaObject.connectSlotsByName(LEPS_4_2)

    def retranslateUi(self, LEPS_4_2):
        _translate = QtCore.QCoreApplication.translate
        LEPS_4_2.setWindowTitle(_translate("LEPS_4_2", "LEPS_4_Harnesses_to_Internal"))
        self.pushButton.setText(_translate("LEPS_4_2", "Download harnesses"))
        self.pushButton.clicked.connect(self.clicer_pushButton)
        self.pushButton_2.setText(_translate("LEPS_4_2", "Download Virtual"))
        self.pushButton_2.clicked.connect(self.clicer_pushButton_2)
        self.pushButton_3.setText(_translate("LEPS_4_2", "Download Internal"))
        self.pushButton_3.clicked.connect(self.clicer_pushButton_3)
        self.pushButton_4.setText(_translate("LEPS_4_2", "Generate Internal for harnesses"))
        self.pushButton_4.clicked.connect(self.clicer_pushButton_4)
        self.pushButton_5.setText(_translate("LEPS_4_2", "SAVE Internal"))
        self.pushButton_5.clicked.connect(self.clicer_pushButton_5)
        self.pushButton_6.setText(_translate("LEPS_4_2", "SAVE Mistakes"))
        self.pushButton_6.clicked.connect(self.clicer_pushButton_6)
        self.pushButton_7.setText(_translate("LEPS_4_2", "Download Wirelist"))
        self.pushButton_7.clicked.connect(self.clicer_pushButton_7)
        self.pushButton_8.setText(_translate("LEPS_4_2", "Download wires in prod_mod"))
        self.pushButton_8.clicked.connect(self.clicer_pushButton_8)
        self.pushButton_9.setText(_translate("LEPS_4_2", "Generate a check"))
        self.pushButton_9.clicked.connect(self.clicer_pushButton_9)
        self.pushButton_10.setText(_translate("LEPS_4_2", "SAVE result of check"))
        self.pushButton_10.clicked.connect(self.clicer_pushButton_10)

        self.label.setText(_translate("LEPS_4_2", "NOT"))
        self.label_2.setText(_translate("LEPS_4_2", "NOT"))
        self.label_3.setText(_translate("LEPS_4_2", "NOT"))
        self.label_4.setText(_translate("LEPS_4_2", "NOT"))
        self.label_5.setText(_translate("LEPS_4_2", "NOT"))
        self.label_6.setText(_translate("LEPS_4_2", "NOT"))
        self.label_7.setText(_translate("LEPS_4_2", "NOT"))

    def clicer_pushButton(self):
        Open_Read_harnesses = QFileDialog.getExistingDirectory()
        if Open_Read_harnesses:
            self.Read_harnesses = module.Choose_file.choose_harnesses_in_folder(Open_Read_harnesses)
            # визначення списку унікальних вязок
            for i in self.Read_harnesses:
                if i[0] not in self.uniq_har:
                    self.uniq_har.append(i[0])
            self.label.setText(Open_Read_harnesses)

    def clicer_pushButton_2(self):
        Open_Read_Virtual = QFileDialog.getOpenFileName()
        if Open_Read_Virtual:
            self.Read_Virt = module.Choose_file.choose_Virt(Open_Read_Virtual[0])
            #Роблю масив тільки з індексів віртуала для перевірки чи є всі індекси в вязці
            for i in self.Read_Virt:
                if i[1] not in self.only_index_virt:
                    self.only_index_virt.append(i[1])

            name_open_file = Open_Read_Virtual[0].split("/")
            self.label_2.setText(name_open_file[len(name_open_file) - 1])


    def clicer_pushButton_3(self):
        Open_Read_Int = QFileDialog.getOpenFileName()
        if Open_Read_Int:
            self.Read_Int = module.read_record_csv.read(Open_Read_Int[0])
            # Роблю список інтернал і кількість віртуалів(умов) під інтернал, щоб в кінці відсіяти умови які виконались але це умови які не виконались під більші конфігурації
            internal_withaut_harn = []
            internal_withaut_harn_mas = []
            for i in self.Read_Int:
                if i[0] not in internal_withaut_harn:
                    internal_withaut_harn.append(i[0])
            for i in self.Read_Int:
                internal_withaut_harn_mas.append(i[0])
            for i in internal_withaut_harn:
                add_in_mass = []
                add_in_mass.append(i)
                add_in_mass.append(internal_withaut_harn_mas.count(i))
                self.Readed_Int_and_number_of_virt.append(add_in_mass)

            name_open_file = Open_Read_Int[0].split("/")
            self.label_3.setText(name_open_file[len(name_open_file) - 1])

    def clicer_pushButton_4(self):
        for i in range(len(self.uniq_har)):
            # Проходжу циклом для відбору окремої вязки в масив
            one_separ_harn_prev = []
            for k in self.Read_harnesses:
                if self.uniq_har[i] == k[0]:
                    one_separ_harn_prev.append(k)
            # Видаляю дублікати щоб не було помилки при закиданні однакових вязок
            one_separ_harn = []
            for k in one_separ_harn_prev:
                if k not in one_separ_harn:
                    one_separ_harn.append(k)
            rez_prev = module.Harness_to_Internal.Harness_to_Internal(self.uniq_har[i], one_separ_harn, self.Read_Virt, self.Read_Int, self.Readed_Int_and_number_of_virt, self.only_index_virt)
            self.Rezult.extend(rez_prev[0])
            self.Mistakes_harn.extend(rez_prev[1])

            self.progressBar.setProperty("value", (i+1)/len(self.uniq_har)*100)
        self.label_4.setText("GENERATED")

    def clicer_pushButton_5(self):
        save_Rezult = QFileDialog.getSaveFileName(filter='Data File (*.csv)')
        if save_Rezult:
            module.read_record_csv.record(self.Rezult, save_Rezult[0])

    def clicer_pushButton_6(self):
        save_Rezult = QFileDialog.getSaveFileName(filter='Data File (*.csv)')
        if save_Rezult:
            module.read_record_csv.record(self.Mistakes_harn, save_Rezult[0])

    def clicer_pushButton_7(self):
        Open_Wirelist = QFileDialog.getOpenFileName()
        if Open_Wirelist:
            self.Wirelist = module.Choose_file.choose_Virt(Open_Wirelist[0])

            name_open_file = Open_Wirelist[0].split("/")
            self.label_5.setText(name_open_file[len(name_open_file) - 1])


    def clicer_pushButton_8(self):
        Open_wires_in_prod_mod = QFileDialog.getOpenFileName()
        if Open_wires_in_prod_mod:
            self.wires_in_prod_mod = module.Choose_file.choose_Virt(Open_wires_in_prod_mod[0])

            name_open_file = Open_wires_in_prod_mod[0].split("/")
            self.label_6.setText(name_open_file[len(name_open_file) - 1])


    def clicer_pushButton_9(self):
        #Проходжу циклом по вязках
        for i in range(len(self.uniq_har)):
            # Проходжу циклом для відбору індексів під вязку
            one_separ_harn_inndex_prev = []
            for k in self.Read_harnesses:
                if self.uniq_har[i] == k[0]:
                    one_separ_harn_inndex_prev.append(k[4])
            # Видаляю дублікати щоб не було помилки при закиданні однакових вязок
            one_separ_harn_index = []
            for k in one_separ_harn_inndex_prev:
                if k not in one_separ_harn_index:
                    one_separ_harn_index.append(k)
            #Проходжу циклом для відбору інтерналів під вязку
            one_separ_harn_intern = []
            for k in self.Rezult:
                if self.uniq_har[i] == k[0]:
                    one_separ_harn_intern.append(k[1])

            rez_prev = module.Check_modular_V2.Check_modular(self.uniq_har[i], one_separ_harn_intern, self.wires_in_prod_mod, one_separ_harn_index, self.Wirelist)
            self.Rezult_of_check.extend(rez_prev)

            self.progressBar_2.setProperty("value", (i+1)/len(self.uniq_har)*100)
        self.label_7.setText("GENERATED")

    def clicer_pushButton_10(self):
        save_Rezult_of_check = QFileDialog.getSaveFileName(filter='Data File (*.csv)')
        if save_Rezult_of_check:
            module.read_record_csv.record(self.Rezult_of_check, save_Rezult_of_check[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LEPS_4_2 = QtWidgets.QWidget()
    ui = Ui_LEPS_4_2()
    ui.setupUi(LEPS_4_2)
    LEPS_4_2.show()
    sys.exit(app.exec_())

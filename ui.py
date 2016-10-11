# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warjammer.ui'
#
# Created: Fri Oct  7 13:54:20 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(234, 430)
        MainWindow.setMinimumSize(QtCore.QSize(234, 430))
        MainWindow.setMaximumSize(QtCore.QSize(234, 430))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/warjammer-images/archer.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(234, 430))
        self.centralwidget.setMaximumSize(QtCore.QSize(234, 430))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.img_banner = QtGui.QLabel(self.centralwidget)
        self.img_banner.setGeometry(QtCore.QRect(0, 0, 241, 61))
        self.img_banner.setText(_fromUtf8(""))
        self.img_banner.setPixmap(QtGui.QPixmap(_fromUtf8(":/warjammer-images/warjammer.png")))
        self.img_banner.setObjectName(_fromUtf8("img_banner"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 211, 351))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.input_username = QtGui.QLineEdit(self.layoutWidget)
        self.input_username.setObjectName(_fromUtf8("input_username"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.input_username)
        self.input_password = QtGui.QLineEdit(self.layoutWidget)
        self.input_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.input_password)
        self.input_server = QtGui.QComboBox(self.layoutWidget)
        self.input_server.setObjectName(_fromUtf8("input_server"))
        self.input_server.addItem(_fromUtf8(""))
        self.input_server.addItem(_fromUtf8(""))
        self.input_server.addItem(_fromUtf8(""))
        self.input_server.addItem(_fromUtf8(""))
        self.input_server.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.input_server)
        self.label_spambot_login = QtGui.QLabel(self.layoutWidget)
        self.label_spambot_login.setObjectName(_fromUtf8("label_spambot_login"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_spambot_login)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(203, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_attack_settings = QtGui.QLabel(self.layoutWidget)
        self.label_attack_settings.setObjectName(_fromUtf8("label_attack_settings"))
        self.verticalLayout_2.addWidget(self.label_attack_settings)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.input_victim = QtGui.QLineEdit(self.layoutWidget)
        self.input_victim.setObjectName(_fromUtf8("input_victim"))
        self.verticalLayout.addWidget(self.input_victim)
        self.input_clan_name = QtGui.QLineEdit(self.layoutWidget)
        self.input_clan_name.setObjectName(_fromUtf8("input_clan_name"))
        self.verticalLayout.addWidget(self.input_clan_name)
        self.radio_friend_list = QtGui.QRadioButton(self.layoutWidget)
        self.radio_friend_list.setObjectName(_fromUtf8("radio_friend_list"))
        self.verticalLayout.addWidget(self.radio_friend_list)
        self.radio_clan_invite = QtGui.QRadioButton(self.layoutWidget)
        self.radio_clan_invite.setObjectName(_fromUtf8("radio_clan_invite"))
        self.verticalLayout.addWidget(self.radio_clan_invite)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(203, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_status_msg_2 = QtGui.QLabel(self.layoutWidget)
        self.label_status_msg_2.setText(_fromUtf8(""))
        self.label_status_msg_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_msg_2.setObjectName(_fromUtf8("label_status_msg_2"))
        self.verticalLayout_2.addWidget(self.label_status_msg_2)
        self.label_status_msg = QtGui.QLabel(self.layoutWidget)
        self.label_status_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_msg.setObjectName(_fromUtf8("label_status_msg"))
        self.verticalLayout_2.addWidget(self.label_status_msg)
        spacerItem2 = QtGui.QSpacerItem(203, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.button_attack = QtGui.QPushButton(self.layoutWidget)
        self.button_attack.setAutoDefault(True)
        self.button_attack.setObjectName(_fromUtf8("button_attack"))
        self.verticalLayout_3.addWidget(self.button_attack)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.input_username, self.input_password)
        MainWindow.setTabOrder(self.input_password, self.input_server)
        MainWindow.setTabOrder(self.input_server, self.input_victim)
        MainWindow.setTabOrder(self.input_victim, self.input_clan_name)
        MainWindow.setTabOrder(self.input_clan_name, self.radio_friend_list)
        MainWindow.setTabOrder(self.radio_friend_list, self.radio_clan_invite)
        MainWindow.setTabOrder(self.radio_clan_invite, self.button_attack)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "WarJammer 3.0", None))
        self.input_username.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.input_server.setItemText(0, _translate("MainWindow", "pvpgn.valpohacks.com", None))
        self.input_server.setItemText(1, _translate("MainWindow", "server.war2.ru", None))
        self.input_server.setItemText(2, _translate("MainWindow", "backup.war2.ru", None))
        self.input_server.setItemText(3, _translate("MainWindow", "server.war2.me", None))
        self.input_server.setItemText(4, _translate("MainWindow", "backup.war2.me", None))
        self.label_spambot_login.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Spambot Login</span></p></body></html>", None))
        self.label_attack_settings.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Attack Settings</span></p></body></html>", None))
        self.input_victim.setPlaceholderText(_translate("MainWindow", "Victim Username", None))
        self.input_clan_name.setPlaceholderText(_translate("MainWindow", "Clan Name", None))
        self.radio_friend_list.setText(_translate("MainWindow", "Friend List Attack", None))
        self.radio_clan_invite.setText(_translate("MainWindow", "Clan Invite Attack", None))
        self.label_status_msg.setText(_translate("MainWindow", "Not Connected", None))
        self.button_attack.setText(_translate("MainWindow", "Attack", None))

import resources_rc

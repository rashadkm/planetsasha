# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/preferenceswindow.ui'
#
# Created: Sat Jul  6 19:54:04 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.resize(399, 462)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/tools.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Preferences.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Preferences)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBox = QtGui.QToolBox(Preferences)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 381, 291))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.page_5)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ossimpreference = QtGui.QLineEdit(self.groupBox_2)
        self.ossimpreference.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.ossimpreference.setText(_fromUtf8(""))
        self.ossimpreference.setObjectName(_fromUtf8("ossimpreference"))
        self.gridLayout.addWidget(self.ossimpreference, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.selectpref = QtGui.QToolButton(self.groupBox_2)
        self.selectpref.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.selectpref.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/page22_1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectpref.setIcon(icon1)
        self.selectpref.setObjectName(_fromUtf8("selectpref"))
        self.gridLayout.addWidget(self.selectpref, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.selectgeonamesdb = QtGui.QToolButton(self.groupBox_2)
        self.selectgeonamesdb.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.selectgeonamesdb.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/db.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectgeonamesdb.setIcon(icon2)
        self.selectgeonamesdb.setObjectName(_fromUtf8("selectgeonamesdb"))
        self.gridLayout.addWidget(self.selectgeonamesdb, 2, 1, 1, 1)
        self.geonames = QtGui.QLineEdit(self.groupBox_2)
        self.geonames.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.geonames.setText(_fromUtf8(""))
        self.geonames.setObjectName(_fromUtf8("geonames"))
        self.gridLayout.addWidget(self.geonames, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.selectgpsdevice = QtGui.QToolButton(self.groupBox_2)
        self.selectgpsdevice.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.selectgpsdevice.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/satellite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectgpsdevice.setIcon(icon3)
        self.selectgpsdevice.setObjectName(_fromUtf8("selectgpsdevice"))
        self.gridLayout.addWidget(self.selectgpsdevice, 3, 1, 1, 1)
        self.gpsdevice = QtGui.QLineEdit(self.groupBox_2)
        self.gpsdevice.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.gpsdevice.setObjectName(_fromUtf8("gpsdevice"))
        self.gridLayout.addWidget(self.gpsdevice, 3, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.selectVrt = QtGui.QToolButton(self.groupBox_2)
        self.selectVrt.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.selectVrt.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gdal-logo-1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectVrt.setIcon(icon4)
        self.selectVrt.setObjectName(_fromUtf8("selectVrt"))
        self.gridLayout.addWidget(self.selectVrt, 4, 1, 1, 1)
        self.VrtDir = QtGui.QLineEdit(self.groupBox_2)
        self.VrtDir.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.VrtDir.setText(_fromUtf8(""))
        self.VrtDir.setObjectName(_fromUtf8("VrtDir"))
        self.gridLayout.addWidget(self.VrtDir, 4, 2, 1, 1)
        self.selectKml = QtGui.QToolButton(self.groupBox_2)
        self.selectKml.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.selectKml.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/saveinfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectKml.setIcon(icon5)
        self.selectKml.setObjectName(_fromUtf8("selectKml"))
        self.gridLayout.addWidget(self.selectKml, 5, 1, 1, 1)
        self.KmlDir = QtGui.QLineEdit(self.groupBox_2)
        self.KmlDir.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.KmlDir.setText(_fromUtf8(""))
        self.KmlDir.setObjectName(_fromUtf8("KmlDir"))
        self.gridLayout.addWidget(self.KmlDir, 5, 2, 1, 1)
        self.filemanager = QtGui.QLineEdit(self.groupBox_2)
        self.filemanager.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.filemanager.setText(_fromUtf8(""))
        self.filemanager.setObjectName(_fromUtf8("filemanager"))
        self.gridLayout.addWidget(self.filemanager, 6, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mpi = QtGui.QCheckBox(self.groupBox_2)
        self.mpi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mpi.setAutoFillBackground(False)
        self.mpi.setText(_fromUtf8(""))
        self.mpi.setObjectName(_fromUtf8("mpi"))
        self.horizontalLayout.addWidget(self.mpi)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.np = QtGui.QSpinBox(self.groupBox_2)
        self.np.setProperty("value", 0)
        self.np.setObjectName(_fromUtf8("np"))
        self.horizontalLayout.addWidget(self.np)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 2)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/epi.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_5, icon6, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 381, 291))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_12 = QtGui.QLabel(self.page_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.PointSize = QtGui.QLineEdit(self.page_3)
        self.PointSize.setObjectName(_fromUtf8("PointSize"))
        self.gridLayout_2.addWidget(self.PointSize, 0, 1, 1, 1)
        self.LineWidth = QtGui.QLineEdit(self.page_3)
        self.LineWidth.setObjectName(_fromUtf8("LineWidth"))
        self.gridLayout_2.addWidget(self.LineWidth, 1, 1, 1, 1)
        self.PenColor = QtGui.QLineEdit(self.page_3)
        self.PenColor.setObjectName(_fromUtf8("PenColor"))
        self.gridLayout_2.addWidget(self.PenColor, 2, 1, 1, 1)
        self.BrushColor = QtGui.QLineEdit(self.page_3)
        self.BrushColor.setObjectName(_fromUtf8("BrushColor"))
        self.gridLayout_2.addWidget(self.BrushColor, 3, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.page_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.page_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.page_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.page_3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)
        self.Thickness = QtGui.QLineEdit(self.page_3)
        self.Thickness.setObjectName(_fromUtf8("Thickness"))
        self.gridLayout_2.addWidget(self.Thickness, 4, 1, 1, 1)
        self.Fill = QtGui.QLineEdit(self.page_3)
        self.Fill.setObjectName(_fromUtf8("Fill"))
        self.gridLayout_2.addWidget(self.Fill, 5, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.page_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/grass_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_3, icon7, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 381, 291))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.page_2)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.dataport = QtGui.QLineEdit(self.groupBox)
        self.dataport.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.dataport.setObjectName(_fromUtf8("dataport"))
        self.gridLayout_4.addWidget(self.dataport, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        self.navport = QtGui.QLineEdit(self.groupBox)
        self.navport.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.navport.setObjectName(_fromUtf8("navport"))
        self.gridLayout_4.addWidget(self.navport, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 1)
        self.hostname = QtGui.QLineEdit(self.groupBox)
        self.hostname.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.hostname.setObjectName(_fromUtf8("hostname"))
        self.gridLayout_4.addWidget(self.hostname, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.groupBox)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/keyser-tux-wifi-logo-2300.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon8, _fromUtf8(""))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 381, 291))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ConnectionGroupBox = QtGui.QGroupBox(self.page)
        self.ConnectionGroupBox.setTitle(_fromUtf8(""))
        self.ConnectionGroupBox.setObjectName(_fromUtf8("ConnectionGroupBox"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.ConnectionGroupBox)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.Database = QtGui.QHBoxLayout()
        self.Database.setObjectName(_fromUtf8("Database"))
        self.dbVerticalLayout = QtGui.QVBoxLayout()
        self.dbVerticalLayout.setObjectName(_fromUtf8("dbVerticalLayout"))
        self.label_name = QtGui.QLabel(self.ConnectionGroupBox)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.dbVerticalLayout.addWidget(self.label_name)
        self.label_host = QtGui.QLabel(self.ConnectionGroupBox)
        self.label_host.setObjectName(_fromUtf8("label_host"))
        self.dbVerticalLayout.addWidget(self.label_host)
        self.label_dbname = QtGui.QLabel(self.ConnectionGroupBox)
        self.label_dbname.setObjectName(_fromUtf8("label_dbname"))
        self.dbVerticalLayout.addWidget(self.label_dbname)
        self.label_port = QtGui.QLabel(self.ConnectionGroupBox)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.dbVerticalLayout.addWidget(self.label_port)
        self.label_username = QtGui.QLabel(self.ConnectionGroupBox)
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.dbVerticalLayout.addWidget(self.label_username)
        self.label_password = QtGui.QLabel(self.ConnectionGroupBox)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.dbVerticalLayout.addWidget(self.label_password)
        self.Database.addLayout(self.dbVerticalLayout)
        self.DBLayout = QtGui.QVBoxLayout()
        self.DBLayout.setObjectName(_fromUtf8("DBLayout"))
        self.ConnectionName = QtGui.QLineEdit(self.ConnectionGroupBox)
        self.ConnectionName.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.ConnectionName.setText(_fromUtf8(""))
        self.ConnectionName.setObjectName(_fromUtf8("ConnectionName"))
        self.DBLayout.addWidget(self.ConnectionName)
        self.DbHost = QtGui.QLineEdit(self.ConnectionGroupBox)
        self.DbHost.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.DbHost.setObjectName(_fromUtf8("DbHost"))
        self.DBLayout.addWidget(self.DbHost)
        self.DbName = QtGui.QLineEdit(self.ConnectionGroupBox)
        self.DbName.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.DbName.setText(_fromUtf8(""))
        self.DbName.setObjectName(_fromUtf8("DbName"))
        self.DBLayout.addWidget(self.DbName)
        self.DbPort = QtGui.QLineEdit(self.ConnectionGroupBox)
        self.DbPort.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.DbPort.setObjectName(_fromUtf8("DbPort"))
        self.DBLayout.addWidget(self.DbPort)
        self.DbUser = QtGui.QLineEdit(self.ConnectionGroupBox)
        self.DbUser.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.DbUser.setText(_fromUtf8(""))
        self.DbUser.setObjectName(_fromUtf8("DbUser"))
        self.DBLayout.addWidget(self.DbUser)
        self.DbPassword = QtGui.QLineEdit(self.ConnectionGroupBox)
        self.DbPassword.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.DbPassword.setText(_fromUtf8(""))
        self.DbPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.DbPassword.setObjectName(_fromUtf8("DbPassword"))
        self.DBLayout.addWidget(self.DbPassword)
        self.Database.addLayout(self.DBLayout)
        self.verticalLayout_21.addLayout(self.Database)
        self.ConnectionGroupBoxhorizontalLayout = QtGui.QHBoxLayout()
        self.ConnectionGroupBoxhorizontalLayout.setObjectName(_fromUtf8("ConnectionGroupBoxhorizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ConnectionGroupBoxhorizontalLayout.addItem(spacerItem4)
        self.pushButton = QtGui.QPushButton(self.ConnectionGroupBox)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 44px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.ConnectionGroupBoxhorizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_21.addLayout(self.ConnectionGroupBoxhorizontalLayout)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.ConnectionGroupBox)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/spit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon9, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.SaveSettings = QtGui.QPushButton(Preferences)
        self.SaveSettings.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 44px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }"))
        self.SaveSettings.setObjectName(_fromUtf8("SaveSettings"))
        self.gridLayout_5.addWidget(self.SaveSettings, 1, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)

        self.retranslateUi(Preferences)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_translate("Preferences", "Preferences", None))
        self.label_6.setText(_translate("Preferences", "Ossim preference", None))
        self.label_4.setText(_translate("Preferences", "Geonames - db", None))
        self.label_5.setText(_translate("Preferences", "GPS Device", None))
        self.gpsdevice.setText(_translate("Preferences", "/dev/tty.GarminGPS10-Gps10 ", None))
        self.label_8.setText(_translate("Preferences", "VRT - Directory", None))
        self.label_9.setText(_translate("Preferences", "KML - Directory", None))
        self.label_7.setText(_translate("Preferences", "File manager", None))
        self.label_11.setText(_translate("Preferences", "NP", None))
        self.label_10.setText(_translate("Preferences", "Enable MPI", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Preferences", "General", None))
        self.label_12.setText(_translate("Preferences", "Point Size", None))
        self.PointSize.setText(_translate("Preferences", "1,1", None))
        self.LineWidth.setText(_translate("Preferences", "1,1", None))
        self.PenColor.setText(_translate("Preferences", "111,111,111", None))
        self.BrushColor.setText(_translate("Preferences", "111,111,111", None))
        self.label_13.setText(_translate("Preferences", "Line Width", None))
        self.label_14.setText(_translate("Preferences", "Pen Color", None))
        self.label_15.setText(_translate("Preferences", "Brush Color", None))
        self.label_16.setText(_translate("Preferences", "Thickness", None))
        self.Thickness.setText(_translate("Preferences", "1", None))
        self.Fill.setText(_translate("Preferences", "0", None))
        self.label_17.setText(_translate("Preferences", "Fill", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Preferences", "Grass", None))
        self.dataport.setText(_translate("Preferences", "8000", None))
        self.label_3.setText(_translate("Preferences", "Data-Port", None))
        self.navport.setText(_translate("Preferences", "7000", None))
        self.label_2.setText(_translate("Preferences", "Nav-Port", None))
        self.hostname.setText(_translate("Preferences", "localhost", None))
        self.label.setText(_translate("Preferences", "Host", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Preferences", "TCP", None))
        self.label_name.setText(_translate("Preferences", "Name", None))
        self.label_host.setText(_translate("Preferences", "Host", None))
        self.label_dbname.setText(_translate("Preferences", "Database", None))
        self.label_port.setText(_translate("Preferences", "Port", None))
        self.label_username.setText(_translate("Preferences", "Username", None))
        self.label_password.setText(_translate("Preferences", "Password", None))
        self.DbHost.setText(_translate("Preferences", "localhost", None))
        self.DbPort.setText(_translate("Preferences", "5432", None))
        self.pushButton.setText(_translate("Preferences", "Test", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Preferences", "Postgis", None))
        self.SaveSettings.setText(_translate("Preferences", "OK", None))

import resources_rc

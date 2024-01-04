# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1236, 754)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border:"
                        " 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	image: url(:/images/images/images/sora_logo3.png);\n"
"	background-color: rgb(33, 37, 43);\n"
"	position: centered;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	back"
                        "ground-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
""
                        "\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushBu"
                        "tton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb("
                        "23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////"
                        "////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-ri"
                        "ght-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
""
                        " }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
""
                        "    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    b"
                        "ackground: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color"
                        ": rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider"
                        "::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	colo"
                        "r: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.gridLayout_7 = QGridLayout(self.styleSheet)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_calculate = QPushButton(self.topMenu)
        self.btn_calculate.setObjectName(u"btn_calculate")
        sizePolicy.setHeightForWidth(self.btn_calculate.sizePolicy().hasHeightForWidth())
        self.btn_calculate.setSizePolicy(sizePolicy)
        self.btn_calculate.setMinimumSize(QSize(0, 45))
        self.btn_calculate.setFont(font)
        self.btn_calculate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calculate.setLayoutDirection(Qt.LeftToRight)
        self.btn_calculate.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-terminal.png);")

        self.verticalLayout_8.addWidget(self.btn_calculate)

        self.btn_figure = QPushButton(self.topMenu)
        self.btn_figure.setObjectName(u"btn_figure")
        sizePolicy.setHeightForWidth(self.btn_figure.sizePolicy().hasHeightForWidth())
        self.btn_figure.setSizePolicy(sizePolicy)
        self.btn_figure.setMinimumSize(QSize(0, 45))
        self.btn_figure.setFont(font)
        self.btn_figure.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_figure.setLayoutDirection(Qt.LeftToRight)
        self.btn_figure.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_8.addWidget(self.btn_figure)

        self.btn_export = QPushButton(self.topMenu)
        self.btn_export.setObjectName(u"btn_export")
        sizePolicy.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy)
        self.btn_export.setMinimumSize(QSize(0, 45))
        self.btn_export.setFont(font)
        self.btn_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export.setLayoutDirection(Qt.LeftToRight)
        self.btn_export.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_8.addWidget(self.btn_export)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-options-horizontal.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.Home_page.setMinimumSize(QSize(1100, 0))
        self.verticalLayout_20 = QVBoxLayout(self.Home_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_3 = QLabel(self.Home_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 80))
        font4 = QFont()
        font4.setFamilies([u"Segoe Script"])
        font4.setPointSize(32)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"font: 700 32pt \"Segoe Script\";")
        self.label_3.setTextFormat(Qt.PlainText)

        self.gridLayout_10.addWidget(self.label_3, 0, 0, 1, 1)

        self.label = QLabel(self.Home_page)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 600 28pt \"Segoe UI\";\n"
"")

        self.gridLayout_10.addWidget(self.label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_6 = QLabel(self.Home_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(100, 16777215))
        self.label_6.setStyleSheet(u"background-image: url(:/images/python-logo_small.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right top;\n"
"")

        self.gridLayout_10.addWidget(self.label_6, 1, 1, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_10)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_3 = QFrame(self.Home_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 100))
        self.frame_3.setStyleSheet(u"image: url(:/images/images/images/Space_panda.png);\n"
"image-position: bottom;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_3, 0, 2, 1, 1, Qt.AlignRight)

        self.label_2 = QLabel(self.Home_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(900, 0))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(True)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"font: 600 italic 16pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.gridLayout_11.addWidget(self.label_2, 0, 1, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_11)


        self.verticalLayout_20.addLayout(self.verticalLayout_24)

        self.stackedWidget.addWidget(self.Home_page)
        self.Calculation_page = QWidget()
        self.Calculation_page.setObjectName(u"Calculation_page")
        self.Calculation_page.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.Calculation_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.Input_zone = QFrame(self.Calculation_page)
        self.Input_zone.setObjectName(u"Input_zone")
        self.Input_zone.setFrameShape(QFrame.StyledPanel)
        self.Input_zone.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Input_zone)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.FileBox = QFrame(self.Input_zone)
        self.FileBox.setObjectName(u"FileBox")
        self.FileBox.setMinimumSize(QSize(0, 110))
        self.FileBox.setMaximumSize(QSize(16777215, 110))
        self.FileBox.setFrameShape(QFrame.NoFrame)
        self.FileBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.FileBox)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.FileBox)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.Input_label_2 = QLabel(self.frame_title_wid_1)
        self.Input_label_2.setObjectName(u"Input_label_2")
        self.Input_label_2.setFont(font)
        self.Input_label_2.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.Input_label_2)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.FileBox)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.Input_btn = QPushButton(self.frame_content_wid_1)
        self.Input_btn.setObjectName(u"Input_btn")
        self.Input_btn.setMinimumSize(QSize(150, 30))
        self.Input_btn.setFont(font)
        self.Input_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Input_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Input_btn.setIcon(icon4)

        self.gridLayout.addWidget(self.Input_btn, 0, 1, 1, 1)

        self.Input_label = QLabel(self.frame_content_wid_1)
        self.Input_label.setObjectName(u"Input_label")
        self.Input_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.Input_label.setLineWidth(1)
        self.Input_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Input_label, 1, 0, 1, 2)

        self.Input_line = QLineEdit(self.frame_content_wid_1)
        self.Input_line.setObjectName(u"Input_line")
        self.Input_line.setMinimumSize(QSize(0, 30))
        self.Input_line.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.Input_line, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.FileBox)

        self.MeshBox = QFrame(self.Input_zone)
        self.MeshBox.setObjectName(u"MeshBox")
        self.MeshBox.setMinimumSize(QSize(0, 110))
        self.MeshBox.setMaximumSize(QSize(16777215, 110))
        self.MeshBox.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_19 = QVBoxLayout(self.MeshBox)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Mesh_frame = QFrame(self.MeshBox)
        self.Mesh_frame.setObjectName(u"Mesh_frame")
        self.Mesh_frame.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_21 = QVBoxLayout(self.Mesh_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Mesh_label_2 = QLabel(self.Mesh_frame)
        self.Mesh_label_2.setObjectName(u"Mesh_label_2")
        self.Mesh_label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_21.addWidget(self.Mesh_label_2)


        self.verticalLayout_19.addWidget(self.Mesh_frame)

        self.horizontalFrame = QFrame(self.MeshBox)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Calculate_btn = QPushButton(self.horizontalFrame)
        self.Calculate_btn.setObjectName(u"Calculate_btn")
        self.Calculate_btn.setMinimumSize(QSize(150, 30))
        self.Calculate_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Calculate_btn.setIcon(icon5)

        self.gridLayout_2.addWidget(self.Calculate_btn, 1, 1, 1, 1)

        self.Mesh_line = QLineEdit(self.horizontalFrame)
        self.Mesh_line.setObjectName(u"Mesh_line")
        self.Mesh_line.setMinimumSize(QSize(0, 30))
        self.Mesh_line.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.Mesh_line, 1, 0, 1, 1)

        self.Mesh_label = QLabel(self.horizontalFrame)
        self.Mesh_label.setObjectName(u"Mesh_label")
        self.Mesh_label.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_2.addWidget(self.Mesh_label, 2, 0, 1, 2)


        self.horizontalLayout_7.addLayout(self.gridLayout_2)


        self.verticalLayout_19.addWidget(self.horizontalFrame)


        self.verticalLayout_16.addWidget(self.MeshBox)


        self.verticalLayout.addWidget(self.Input_zone)

        self.Display_zone = QFrame(self.Calculation_page)
        self.Display_zone.setObjectName(u"Display_zone")
        self.Display_zone.setMinimumSize(QSize(0, 330))
        self.verticalLayout_22 = QVBoxLayout(self.Display_zone)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.Display_browser = QTextBrowser(self.Display_zone)
        self.Display_browser.setObjectName(u"Display_browser")
        self.Display_browser.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.Display_browser.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.Display_browser, 0, 0, 3, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 2, 1, 1)

        self.Display_btnbox = QFrame(self.Display_zone)
        self.Display_btnbox.setObjectName(u"Display_btnbox")
        self.Display_btnbox.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(33, 37, 43);")
        self.verticalLayout_23 = QVBoxLayout(self.Display_btnbox)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 10, -1, 10)
        self.Display_clear_btn = QPushButton(self.Display_btnbox)
        self.Display_clear_btn.setObjectName(u"Display_clear_btn")
        self.Display_clear_btn.setMinimumSize(QSize(60, 80))
        self.Display_clear_btn.setStyleSheet(u"image: url(:/icons/images/icons/cil-x-circle.png);\n"
"background-color: rgb(52, 59, 72);\n"
"text-align: bottom;\n"
"")

        self.verticalLayout_23.addWidget(self.Display_clear_btn)

        self.Display_save_btn = QPushButton(self.Display_btnbox)
        self.Display_save_btn.setObjectName(u"Display_save_btn")
        self.Display_save_btn.setMinimumSize(QSize(60, 80))
        self.Display_save_btn.setAutoFillBackground(False)
        self.Display_save_btn.setStyleSheet(u"image: url(:/icons/images/icons/cil-align-center.png);\n"
"background-color: rgb(52, 59, 72);\n"
"text-align: bottom;\n"
"")
        self.Display_save_btn.setIconSize(QSize(50, 50))
        self.Display_save_btn.setCheckable(False)
        self.Display_save_btn.setAutoExclusive(False)

        self.verticalLayout_23.addWidget(self.Display_save_btn)

        self.Display_next_btn = QPushButton(self.Display_btnbox)
        self.Display_next_btn.setObjectName(u"Display_next_btn")
        self.Display_next_btn.setMinimumSize(QSize(60, 80))
        self.Display_next_btn.setStyleSheet(u"image: url(:/icons/images/icons/cil-arrow-circle-right.png);\n"
"background-color: rgb(52, 59, 72);\n"
"text-align: bottom;\n"
"")

        self.verticalLayout_23.addWidget(self.Display_next_btn)


        self.gridLayout_3.addWidget(self.Display_btnbox, 1, 2, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.Display_zone)

        self.stackedWidget.addWidget(self.Calculation_page)
        self.Figure_page = QWidget()
        self.Figure_page.setObjectName(u"Figure_page")
        self.horizontalLayout_11 = QHBoxLayout(self.Figure_page)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalFrame_2 = QFrame(self.Figure_page)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy3)
        self.horizontalFrame_2.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout_34 = QVBoxLayout(self.horizontalFrame_2)
        self.verticalLayout_34.setSpacing(20)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame_4 = QFrame(self.horizontalFrame_2)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalFrame_4.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 20px")
        self.verticalLayout_36 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_36.setSpacing(20)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(9, 9, 9, 9)
        self.Fig_IFM_btn = QRadioButton(self.verticalFrame_4)
        self.Fig_IFM_btn.setObjectName(u"Fig_IFM_btn")
        self.Fig_IFM_btn.setMinimumSize(QSize(200, 50))
        self.Fig_IFM_btn.setFont(font)
        self.Fig_IFM_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Fig_IFM_btn.setStyleSheet(u"\n"
"QRadioButton {\n"
"	background-color: rgb(33, 37, 43);\n"
"	    border: 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"	border: 0px\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-3d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Fig_IFM_btn.setIcon(icon6)
        self.Fig_IFM_btn.setIconSize(QSize(16, 16))
        self.Fig_IFM_btn.setCheckable(True)
        self.Fig_IFM_btn.setChecked(True)

        self.verticalLayout_36.addWidget(self.Fig_IFM_btn)

        self.Fig_SD_btn = QRadioButton(self.verticalFrame_4)
        self.Fig_SD_btn.setObjectName(u"Fig_SD_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Fig_SD_btn.sizePolicy().hasHeightForWidth())
        self.Fig_SD_btn.setSizePolicy(sizePolicy4)
        self.Fig_SD_btn.setMinimumSize(QSize(200, 50))
        self.Fig_SD_btn.setFont(font)
        self.Fig_SD_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Fig_SD_btn.setStyleSheet(u"\n"
"QRadioButton {\n"
"	background-color: rgb(33, 37, 43);\n"
"	    border: 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"	border: 0px\n"
"}")
        self.Fig_SD_btn.setIcon(icon6)
        self.Fig_SD_btn.setCheckable(True)
        self.Fig_SD_btn.setChecked(False)

        self.verticalLayout_36.addWidget(self.Fig_SD_btn)

        self.Fig_Gap_btn = QRadioButton(self.verticalFrame_4)
        self.Fig_Gap_btn.setObjectName(u"Fig_Gap_btn")
        self.Fig_Gap_btn.setMinimumSize(QSize(200, 50))
        self.Fig_Gap_btn.setFont(font)
        self.Fig_Gap_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Fig_Gap_btn.setStyleSheet(u"\n"
"QRadioButton {\n"
"	background-color: rgb(33, 37, 43);\n"
"	    border: 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"	border: 0px\n"
"}")
        self.Fig_Gap_btn.setIcon(icon6)
        self.Fig_Gap_btn.setCheckable(True)
        self.Fig_Gap_btn.setChecked(False)

        self.verticalLayout_36.addWidget(self.Fig_Gap_btn)


        self.verticalLayout_34.addWidget(self.verticalFrame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Fig_save_btn = QPushButton(self.horizontalFrame_2)
        self.Fig_save_btn.setObjectName(u"Fig_save_btn")
        self.Fig_save_btn.setMinimumSize(QSize(200, 50))
        self.Fig_save_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.Fig_save_btn)


        self.verticalLayout_34.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_12.addWidget(self.horizontalFrame_2)

        self.Fig_Widget = QWidget(self.Figure_page)
        self.Fig_Widget.setObjectName(u"Fig_Widget")

        self.horizontalLayout_12.addWidget(self.Fig_Widget)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.Figure_page)
        self.Export_page = QWidget()
        self.Export_page.setObjectName(u"Export_page")
        self.verticalLayout_28 = QVBoxLayout(self.Export_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.ExportFrame = QFrame(self.Export_page)
        self.ExportFrame.setObjectName(u"ExportFrame")
        self.verticalLayout_27 = QVBoxLayout(self.ExportFrame)
        self.verticalLayout_27.setSpacing(2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 0, 9, 0)
        self.frame = QFrame(self.ExportFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.row_2 = QFrame(self.frame)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.row_2)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.frame_div_content_2 = QFrame(self.row_2)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.labelBoxBlenderInstalation_2)


        self.verticalLayout_30.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.Export_name_line = QLineEdit(self.frame_content_wid_2)
        self.Export_name_line.setObjectName(u"Export_name_line")
        self.Export_name_line.setMinimumSize(QSize(0, 30))
        self.Export_name_line.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Export_name_line, 0, 0, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelVersion_4, 1, 0, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_4)


        self.verticalLayout_30.addWidget(self.frame_content_wid_2)


        self.verticalLayout_29.addWidget(self.frame_div_content_2)

        self.verticalFrame_3 = QFrame(self.row_2)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalFrame_3.setMinimumSize(QSize(0, 110))
        self.verticalFrame_3.setMaximumSize(QSize(16777215, 110))
        self.verticalFrame_3.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_32 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame_5 = QFrame(self.verticalFrame_3)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        self.verticalFrame_5.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_33 = QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_4 = QLabel(self.verticalFrame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_33.addWidget(self.label_4)


        self.verticalLayout_32.addWidget(self.verticalFrame_5)

        self.horizontalFrame_12 = QFrame(self.verticalFrame_3)
        self.horizontalFrame_12.setObjectName(u"horizontalFrame_12")
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_7 = QPushButton(self.horizontalFrame_12)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(150, 30))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-options-horizontal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon7)

        self.gridLayout_5.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.Export_folder_line = QLineEdit(self.horizontalFrame_12)
        self.Export_folder_line.setObjectName(u"Export_folder_line")
        self.Export_folder_line.setMinimumSize(QSize(0, 30))
        self.Export_folder_line.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.Export_folder_line, 1, 0, 1, 1)

        self.label_5 = QLabel(self.horizontalFrame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 2)


        self.horizontalLayout_8.addLayout(self.gridLayout_5)


        self.verticalLayout_32.addWidget(self.horizontalFrame_12)


        self.verticalLayout_29.addWidget(self.verticalFrame_3)

        self.frame_2 = QFrame(self.row_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 373))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(30)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.node_sum = QLabel(self.frame_2)
        self.node_sum.setObjectName(u"node_sum")
        self.node_sum.setMinimumSize(QSize(100, 30))
        self.node_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_25.addWidget(self.node_sum)

        self.IFM_sum = QLabel(self.frame_2)
        self.IFM_sum.setObjectName(u"IFM_sum")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(100)
        sizePolicy5.setVerticalStretch(30)
        sizePolicy5.setHeightForWidth(self.IFM_sum.sizePolicy().hasHeightForWidth())
        self.IFM_sum.setSizePolicy(sizePolicy5)
        self.IFM_sum.setMinimumSize(QSize(100, 30))
        self.IFM_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_25.addWidget(self.IFM_sum)

        self.gap_sum = QLabel(self.frame_2)
        self.gap_sum.setObjectName(u"gap_sum")
        sizePolicy5.setHeightForWidth(self.gap_sum.sizePolicy().hasHeightForWidth())
        self.gap_sum.setSizePolicy(sizePolicy5)
        self.gap_sum.setMinimumSize(QSize(100, 30))
        self.gap_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_25.addWidget(self.gap_sum)

        self.sd_sum = QLabel(self.frame_2)
        self.sd_sum.setObjectName(u"sd_sum")
        sizePolicy5.setHeightForWidth(self.sd_sum.sizePolicy().hasHeightForWidth())
        self.sd_sum.setSizePolicy(sizePolicy5)
        self.sd_sum.setMinimumSize(QSize(100, 30))
        self.sd_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_25.addWidget(self.sd_sum)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_5)


        self.gridLayout_6.addLayout(self.verticalLayout_25, 1, 0, 2, 1)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(30)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.x_sum = QLabel(self.frame_2)
        self.x_sum.setObjectName(u"x_sum")
        sizePolicy5.setHeightForWidth(self.x_sum.sizePolicy().hasHeightForWidth())
        self.x_sum.setSizePolicy(sizePolicy5)
        self.x_sum.setMinimumSize(QSize(100, 30))
        self.x_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_35.addWidget(self.x_sum)

        self.y_sum = QLabel(self.frame_2)
        self.y_sum.setObjectName(u"y_sum")
        sizePolicy5.setHeightForWidth(self.y_sum.sizePolicy().hasHeightForWidth())
        self.y_sum.setSizePolicy(sizePolicy5)
        self.y_sum.setMinimumSize(QSize(100, 30))
        self.y_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_35.addWidget(self.y_sum)

        self.z_sum = QLabel(self.frame_2)
        self.z_sum.setObjectName(u"z_sum")
        sizePolicy5.setHeightForWidth(self.z_sum.sizePolicy().hasHeightForWidth())
        self.z_sum.setSizePolicy(sizePolicy5)
        self.z_sum.setMinimumSize(QSize(100, 30))
        self.z_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_35.addWidget(self.z_sum)

        self.theta_sum = QLabel(self.frame_2)
        self.theta_sum.setObjectName(u"theta_sum")
        sizePolicy5.setHeightForWidth(self.theta_sum.sizePolicy().hasHeightForWidth())
        self.theta_sum.setSizePolicy(sizePolicy5)
        self.theta_sum.setMinimumSize(QSize(100, 30))
        self.theta_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_35.addWidget(self.theta_sum)

        self.euler_sum = QLabel(self.frame_2)
        self.euler_sum.setObjectName(u"euler_sum")
        sizePolicy5.setHeightForWidth(self.euler_sum.sizePolicy().hasHeightForWidth())
        self.euler_sum.setSizePolicy(sizePolicy5)
        self.euler_sum.setMinimumSize(QSize(100, 30))
        self.euler_sum.setMaximumSize(QSize(100, 30))

        self.verticalLayout_35.addWidget(self.euler_sum)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_6)


        self.gridLayout_6.addLayout(self.verticalLayout_35, 1, 3, 2, 1)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_41.addItem(self.horizontalSpacer_3)


        self.gridLayout_6.addLayout(self.verticalLayout_41, 1, 5, 1, 1)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(30)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.x_sum_text = QTextBrowser(self.frame_2)
        self.x_sum_text.setObjectName(u"x_sum_text")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(30)
        sizePolicy6.setHeightForWidth(self.x_sum_text.sizePolicy().hasHeightForWidth())
        self.x_sum_text.setSizePolicy(sizePolicy6)
        self.x_sum_text.setMinimumSize(QSize(200, 30))
        self.x_sum_text.setMaximumSize(QSize(16777215, 30))
        self.x_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.x_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_38.addWidget(self.x_sum_text)

        self.y_sum_text = QTextBrowser(self.frame_2)
        self.y_sum_text.setObjectName(u"y_sum_text")
        sizePolicy6.setHeightForWidth(self.y_sum_text.sizePolicy().hasHeightForWidth())
        self.y_sum_text.setSizePolicy(sizePolicy6)
        self.y_sum_text.setMinimumSize(QSize(200, 30))
        self.y_sum_text.setMaximumSize(QSize(16777215, 30))
        self.y_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.y_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_38.addWidget(self.y_sum_text)

        self.z_sum_text = QTextBrowser(self.frame_2)
        self.z_sum_text.setObjectName(u"z_sum_text")
        sizePolicy6.setHeightForWidth(self.z_sum_text.sizePolicy().hasHeightForWidth())
        self.z_sum_text.setSizePolicy(sizePolicy6)
        self.z_sum_text.setMinimumSize(QSize(200, 30))
        self.z_sum_text.setMaximumSize(QSize(16777215, 30))
        self.z_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.z_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_38.addWidget(self.z_sum_text)

        self.theta_sum_text = QTextBrowser(self.frame_2)
        self.theta_sum_text.setObjectName(u"theta_sum_text")
        sizePolicy6.setHeightForWidth(self.theta_sum_text.sizePolicy().hasHeightForWidth())
        self.theta_sum_text.setSizePolicy(sizePolicy6)
        self.theta_sum_text.setMinimumSize(QSize(200, 30))
        self.theta_sum_text.setMaximumSize(QSize(16777215, 30))
        self.theta_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.theta_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_38.addWidget(self.theta_sum_text)

        self.euler_sum_text = QTextBrowser(self.frame_2)
        self.euler_sum_text.setObjectName(u"euler_sum_text")
        sizePolicy6.setHeightForWidth(self.euler_sum_text.sizePolicy().hasHeightForWidth())
        self.euler_sum_text.setSizePolicy(sizePolicy6)
        self.euler_sum_text.setMinimumSize(QSize(200, 30))
        self.euler_sum_text.setMaximumSize(QSize(16777215, 30))
        self.euler_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.euler_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_38.addWidget(self.euler_sum_text)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_7)


        self.gridLayout_6.addLayout(self.verticalLayout_38, 1, 4, 2, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(30)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.node_sum_text = QTextBrowser(self.frame_2)
        self.node_sum_text.setObjectName(u"node_sum_text")
        sizePolicy6.setHeightForWidth(self.node_sum_text.sizePolicy().hasHeightForWidth())
        self.node_sum_text.setSizePolicy(sizePolicy6)
        self.node_sum_text.setMinimumSize(QSize(200, 30))
        self.node_sum_text.setMaximumSize(QSize(16777215, 30))
        self.node_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.node_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_26.addWidget(self.node_sum_text)

        self.IFM_sum_text = QTextBrowser(self.frame_2)
        self.IFM_sum_text.setObjectName(u"IFM_sum_text")
        sizePolicy6.setHeightForWidth(self.IFM_sum_text.sizePolicy().hasHeightForWidth())
        self.IFM_sum_text.setSizePolicy(sizePolicy6)
        self.IFM_sum_text.setMinimumSize(QSize(200, 30))
        self.IFM_sum_text.setMaximumSize(QSize(16777215, 30))
        self.IFM_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.IFM_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_26.addWidget(self.IFM_sum_text)

        self.gap_sum_text = QTextBrowser(self.frame_2)
        self.gap_sum_text.setObjectName(u"gap_sum_text")
        sizePolicy6.setHeightForWidth(self.gap_sum_text.sizePolicy().hasHeightForWidth())
        self.gap_sum_text.setSizePolicy(sizePolicy6)
        self.gap_sum_text.setMinimumSize(QSize(200, 30))
        self.gap_sum_text.setMaximumSize(QSize(16777215, 30))
        self.gap_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.gap_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_26.addWidget(self.gap_sum_text)

        self.SD_sum_text = QTextBrowser(self.frame_2)
        self.SD_sum_text.setObjectName(u"SD_sum_text")
        sizePolicy6.setHeightForWidth(self.SD_sum_text.sizePolicy().hasHeightForWidth())
        self.SD_sum_text.setSizePolicy(sizePolicy6)
        self.SD_sum_text.setMinimumSize(QSize(200, 30))
        self.SD_sum_text.setMaximumSize(QSize(16777215, 30))
        self.SD_sum_text.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.SD_sum_text.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_26.addWidget(self.SD_sum_text)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_4)


        self.gridLayout_6.addLayout(self.verticalLayout_26, 1, 1, 2, 1)

        self.Export_label = QLabel(self.frame_2)
        self.Export_label.setObjectName(u"Export_label")
        self.Export_label.setMinimumSize(QSize(0, 30))
        self.Export_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.Export_label, 0, 0, 1, 6)


        self.horizontalLayout_6.addLayout(self.gridLayout_6)


        self.verticalLayout_29.addWidget(self.frame_2)


        self.verticalLayout_37.addWidget(self.row_2)


        self.verticalLayout_27.addWidget(self.frame)


        self.verticalLayout_28.addWidget(self.ExportFrame)

        self.stackedWidget.addWidget(self.Export_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout_7.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"IFM Calculator", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Designed by Sun Jun", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.btn_figure.setText(QCoreApplication.translate("MainWindow", u"Figure", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Ansys Interfragmentary Motion Calculator</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">A Interfragmentary Motion Calculator for orthopedic, and core algorithm created by Sun Jun."
                        "</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Sun Jun</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Based on PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Interfragmentary Motion </span><span style=\" font-size:16pt; font-weight:700; color:#00aaff;\">Calculator</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffaa00;\">Interfragmentary Motion </span><span style=\" color:#00aaff;\">Calculator</span></p><p align=\"center\"><span style=\" font-size:20pt;\">A </span><span style=\" font-size:20pt; color:#ffaa00;\">GUI</span><span style=\" font-size:20pt;\"> application based on </span><span style=\" font-size:20pt; color:#0055ff;\">Python</span><span style=\" font-size:20pt;\">.</span></p></body></html>", None))
        self.label_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">This software is designed to improve the deficiencies of Ansys in the field of orthopedic applications, please read the instructions before using it. </span></p><p><span style=\" font-size:14pt;\">The data folder used by this software needs to include the exported data of</span></p><p><span style=\" font-size:14pt;\"> [</span><span style=\" font-size:14pt; color:#0055ff;\">data_series_1.csv and data_series_2.csv</span><span style=\" font-size:14pt;\">]. </span></p><p><span style=\" font-size:14pt;\">The software can be used with </span><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Ansys_export_ACT.py</span><span style=\" font-size:14pt;\">.The </span><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Ansys_export_ACT.py</span><span style=\" font-size:14pt;\"> script can easily help you export the data you need.</span></p></body></html>", None))
        self.Input_label_2.setText(QCoreApplication.translate("MainWindow", u"File input", None))
        self.Input_btn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.Input_label.setText(QCoreApplication.translate("MainWindow", u"Select the working directory", None))
        self.Input_line.setText("")
        self.Input_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.Mesh_label_2.setText(QCoreApplication.translate("MainWindow", u"Mesh Accuracy", None))
        self.Calculate_btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.Mesh_line.setText("")
        self.Mesh_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.Mesh_label.setText(QCoreApplication.translate("MainWindow", u"Mesh size is the preferred choice", None))
        self.Display_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Display_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Display_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.Fig_IFM_btn.setText(QCoreApplication.translate("MainWindow", u"IFM distance", None))
        self.Fig_SD_btn.setText(QCoreApplication.translate("MainWindow", u"Sliding Distance", None))
        self.Fig_Gap_btn.setText(QCoreApplication.translate("MainWindow", u"Gap distance", None))
        self.Fig_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"Export Name", None))
        self.Export_name_line.setText("")
        self.Export_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Input the file name you want", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Export Folder", None))
        self.pushButton_7.setText("")
        self.Export_folder_line.setText("")
        self.Export_folder_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Choose the export folder", None))
        self.node_sum.setText(QCoreApplication.translate("MainWindow", u"Nodes count", None))
        self.IFM_sum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>IFM distance</p></body></html>", None))
        self.gap_sum.setText(QCoreApplication.translate("MainWindow", u"Gap distance", None))
        self.sd_sum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sliding distance</p></body></html>", None))
        self.x_sum.setText(QCoreApplication.translate("MainWindow", u"X axis angle", None))
        self.y_sum.setText(QCoreApplication.translate("MainWindow", u"Y axis angle", None))
        self.z_sum.setText(QCoreApplication.translate("MainWindow", u"Z axis angle", None))
        self.theta_sum.setText(QCoreApplication.translate("MainWindow", u"Theta", None))
        self.euler_sum.setText(QCoreApplication.translate("MainWindow", u"Euler angle (XYZ)", None))
        self.Export_label.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Sun Jun", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.2.1", None))
    # retranslateUi


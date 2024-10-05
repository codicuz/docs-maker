# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'docs-maker-main-window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import docs_maker_gui.resources.resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(548, 406)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_btn = QPushButton(self.centralwidget)
        self.main_btn.setObjectName(u"main_btn")
        self.main_btn.setStyleSheet(u"QPushButton {\n"
"	margin-left: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home-64-blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.main_btn.setIcon(icon)
        self.main_btn.setIconSize(QSize(36, 36))

        self.horizontalLayout.addWidget(self.main_btn)

        self.menu_btn = QPushButton(self.centralwidget)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setStyleSheet(u"QPushButton {\n"
"	margin-right: 10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/more-horiz-64-blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setIconSize(QSize(36, 36))

        self.horizontalLayout.addWidget(self.menu_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 112, 336))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout.addWidget(self.pushButton_12)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.mainStacked_sw = QStackedWidget(self.centralwidget)
        self.mainStacked_sw.setObjectName(u"mainStacked_sw")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainStacked_sw.sizePolicy().hasHeightForWidth())
        self.mainStacked_sw.setSizePolicy(sizePolicy1)
        self.mainPage_stPage = QWidget()
        self.mainPage_stPage.setObjectName(u"mainPage_stPage")
        self.verticalLayout_4 = QVBoxLayout(self.mainPage_stPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mainWindow_lbl = QLabel(self.mainPage_stPage)
        self.mainWindow_lbl.setObjectName(u"mainWindow_lbl")
        font = QFont()
        font.setPointSize(24)
        self.mainWindow_lbl.setFont(font)
        self.mainWindow_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.mainWindow_lbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.mainStacked_sw.addWidget(self.mainPage_stPage)
        self.menuPage_stPage = QWidget()
        self.menuPage_stPage.setObjectName(u"menuPage_stPage")
        self.verticalLayout_5 = QVBoxLayout(self.menuPage_stPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.menu_lbl = QLabel(self.menuPage_stPage)
        self.menu_lbl.setObjectName(u"menu_lbl")
        self.menu_lbl.setFont(font)
        self.menu_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.menu_lbl)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.mainStacked_sw.addWidget(self.menuPage_stPage)

        self.horizontalLayout_2.addWidget(self.mainStacked_sw)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainStacked_sw.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Docs Maker", None))
        self.main_btn.setText("")
        self.menu_btn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.mainWindow_lbl.setText(QCoreApplication.translate("MainWindow", u"main", None))
        self.menu_lbl.setText(QCoreApplication.translate("MainWindow", u"menu_lbl", None))
    # retranslateUi


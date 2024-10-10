# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db-indicator.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(237, 82)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.database_lbl = QLabel(Form)
        self.database_lbl.setObjectName(u"database_lbl")

        self.verticalLayout.addWidget(self.database_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.db_type = QLabel(Form)
        self.db_type.setObjectName(u"db_type")

        self.horizontalLayout.addWidget(self.db_type)

        self.db_status = QLabel(Form)
        self.db_status.setObjectName(u"db_status")

        self.horizontalLayout.addWidget(self.db_status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.information = QLabel(Form)
        self.information.setObjectName(u"information")

        self.verticalLayout.addWidget(self.information)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.database_lbl.setText(QCoreApplication.translate("Form", u"database", None))
        self.db_type.setText(QCoreApplication.translate("Form", u"db_type", None))
        self.db_status.setText("")
        self.information.setText(QCoreApplication.translate("Form", u"information", None))
    # retranslateUi


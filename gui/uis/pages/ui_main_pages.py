# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesUdItdr.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName("MainPages")
        MainPages.resize(876, 639)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName("main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName("pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.page_1.setStyleSheet("font-size: 14pt; background:lightgreen")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName("page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName("page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.text_edit = QPlainTextEdit(self.page_2)
        self.text_edit.setObjectName("text_edit")
        self.text_edit.setStyleSheet("background:#343b48;color:#f5f6f9")

        self.page_2_layout.addWidget(self.text_edit)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.page_3.setStyleSheet("background:orange")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName("page_3_layout")
        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainPages)

    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", "Form", None))

    # retranslateUi

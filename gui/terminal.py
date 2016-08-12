# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/qt\terminal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TerminalDialog(object):
    def setupUi(self, TerminalDialog):
        TerminalDialog.setObjectName("TerminalDialog")
        TerminalDialog.resize(1196, 394)
        TerminalDialog.setModal(False)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(TerminalDialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(TerminalDialog)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.outputTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputTextEdit.sizePolicy().hasHeightForWidth())
        self.outputTextEdit.setSizePolicy(sizePolicy)
        self.outputTextEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.outputTextEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.outputTextEdit.setCursorWidth(0)
        self.outputTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.verticalLayout_4.addWidget(self.outputTextEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.autoscrollCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.autoscrollCheckBox.setObjectName("autoscrollCheckBox")
        self.horizontalLayout_2.addWidget(self.autoscrollCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clearButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.horizontalLayoutWidget.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputTextBox = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTextBox.sizePolicy().hasHeightForWidth())
        self.inputTextBox.setSizePolicy(sizePolicy)
        self.inputTextBox.setMinimumSize(QtCore.QSize(0, 10))
        self.inputTextBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.inputTextBox.setObjectName("inputTextBox")
        self.horizontalLayout.addWidget(self.inputTextBox)
        self.sendButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addWidget(self.splitter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(TerminalDialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(TerminalDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ctrlaButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrlaButton.sizePolicy().hasHeightForWidth())
        self.ctrlaButton.setSizePolicy(sizePolicy)
        self.ctrlaButton.setMaximumSize(QtCore.QSize(40, 40))
        self.ctrlaButton.setObjectName("ctrlaButton")
        self.gridLayout_2.addWidget(self.ctrlaButton, 0, 0, 1, 1)
        self.ctrlbButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrlbButton.sizePolicy().hasHeightForWidth())
        self.ctrlbButton.setSizePolicy(sizePolicy)
        self.ctrlbButton.setMinimumSize(QtCore.QSize(10, 0))
        self.ctrlbButton.setMaximumSize(QtCore.QSize(40, 40))
        self.ctrlbButton.setObjectName("ctrlbButton")
        self.gridLayout_2.addWidget(self.ctrlbButton, 0, 1, 1, 1)
        self.ctrleButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrleButton.sizePolicy().hasHeightForWidth())
        self.ctrleButton.setSizePolicy(sizePolicy)
        self.ctrleButton.setMaximumSize(QtCore.QSize(40, 40))
        self.ctrleButton.setObjectName("ctrleButton")
        self.gridLayout_2.addWidget(self.ctrleButton, 1, 1, 1, 1)
        self.ctrlcButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrlcButton.sizePolicy().hasHeightForWidth())
        self.ctrlcButton.setSizePolicy(sizePolicy)
        self.ctrlcButton.setMaximumSize(QtCore.QSize(40, 40))
        self.ctrlcButton.setObjectName("ctrlcButton")
        self.gridLayout_2.addWidget(self.ctrlcButton, 0, 2, 1, 1)
        self.ctrldButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrldButton.sizePolicy().hasHeightForWidth())
        self.ctrldButton.setSizePolicy(sizePolicy)
        self.ctrldButton.setMaximumSize(QtCore.QSize(40, 40))
        self.ctrldButton.setObjectName("ctrldButton")
        self.gridLayout_2.addWidget(self.ctrldButton, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(TerminalDialog)
        QtCore.QMetaObject.connectSlotsByName(TerminalDialog)

    def retranslateUi(self, TerminalDialog):
        _translate = QtCore.QCoreApplication.translate
        TerminalDialog.setWindowTitle(_translate("TerminalDialog", "Terminal"))
        self.autoscrollCheckBox.setText(_translate("TerminalDialog", "Autoscroll"))
        self.clearButton.setText(_translate("TerminalDialog", "Clear"))
        self.sendButton.setText(_translate("TerminalDialog", "Send"))
        self.groupBox.setTitle(_translate("TerminalDialog", "Control"))
        self.ctrlaButton.setText(_translate("TerminalDialog", "-A"))
        self.ctrlbButton.setText(_translate("TerminalDialog", "-B"))
        self.ctrleButton.setText(_translate("TerminalDialog", "-E"))
        self.ctrlcButton.setText(_translate("TerminalDialog", "-C"))
        self.ctrldButton.setText(_translate("TerminalDialog", "-D"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crayfish_colormap_dialog.ui'
#
# Created: Fri Oct 25 17:16:41 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_CrayfishColorMapDialog(object):
    def setupUi(self, CrayfishColorMapDialog):
        CrayfishColorMapDialog.setObjectName(_fromUtf8("CrayfishColorMapDialog"))
        CrayfishColorMapDialog.resize(554, 416)
        self.gridLayout = QtGui.QGridLayout(CrayfishColorMapDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(CrayfishColorMapDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.radIntLinear = QtGui.QRadioButton(CrayfishColorMapDialog)
        self.radIntLinear.setChecked(True)
        self.radIntLinear.setObjectName(_fromUtf8("radIntLinear"))
        self.horizontalLayout.addWidget(self.radIntLinear)
        self.radIntDiscrete = QtGui.QRadioButton(CrayfishColorMapDialog)
        self.radIntDiscrete.setObjectName(_fromUtf8("radIntDiscrete"))
        self.horizontalLayout.addWidget(self.radIntDiscrete)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAdd = QtGui.QToolButton(CrayfishColorMapDialog)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.horizontalLayout_2.addWidget(self.btnAdd)
        self.btnRemove = QtGui.QToolButton(CrayfishColorMapDialog)
        self.btnRemove.setObjectName(_fromUtf8("btnRemove"))
        self.horizontalLayout_2.addWidget(self.btnRemove)
        self.btnLoad = QtGui.QToolButton(CrayfishColorMapDialog)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.horizontalLayout_2.addWidget(self.btnLoad)
        self.btnSave = QtGui.QToolButton(CrayfishColorMapDialog)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout_2.addWidget(self.btnSave)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.viewColorMap = QtGui.QTreeView(CrayfishColorMapDialog)
        self.viewColorMap.setRootIsDecorated(False)
        self.viewColorMap.setObjectName(_fromUtf8("viewColorMap"))
        self.verticalLayout_2.addWidget(self.viewColorMap)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 2, 1)
        self.groupBox = QtGui.QGroupBox(CrayfishColorMapDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.chkInvert = QtGui.QCheckBox(self.groupBox)
        self.chkInvert.setObjectName(_fromUtf8("chkInvert"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.chkInvert)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_2)
        self.editMin = QtGui.QLineEdit(self.groupBox)
        self.editMin.setObjectName(_fromUtf8("editMin"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.editMin)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinClasses = QtGui.QSpinBox(self.groupBox)
        self.spinClasses.setMinimum(2)
        self.spinClasses.setMaximum(9999)
        self.spinClasses.setProperty("value", 5)
        self.spinClasses.setObjectName(_fromUtf8("spinClasses"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinClasses)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.editMax = QtGui.QLineEdit(self.groupBox)
        self.editMax.setObjectName(_fromUtf8("editMax"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.editMax)
        self.cboColorRamp = QgsColorRampComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboColorRamp.sizePolicy().hasHeightForWidth())
        self.cboColorRamp.setSizePolicy(sizePolicy)
        self.cboColorRamp.setObjectName(_fromUtf8("cboColorRamp"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboColorRamp)
        self.btnClassify = QtGui.QPushButton(self.groupBox)
        self.btnClassify.setObjectName(_fromUtf8("btnClassify"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.btnClassify)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(CrayfishColorMapDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblPreview = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPreview.sizePolicy().hasHeightForWidth())
        self.lblPreview.setSizePolicy(sizePolicy)
        self.lblPreview.setMinimumSize(QtCore.QSize(250, 80))
        self.lblPreview.setText(_fromUtf8(""))
        self.lblPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPreview.setObjectName(_fromUtf8("lblPreview"))
        self.verticalLayout.addWidget(self.lblPreview)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CrayfishColorMapDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(CrayfishColorMapDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CrayfishColorMapDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CrayfishColorMapDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CrayfishColorMapDialog)
        CrayfishColorMapDialog.setTabOrder(self.radIntLinear, self.radIntDiscrete)
        CrayfishColorMapDialog.setTabOrder(self.radIntDiscrete, self.btnAdd)
        CrayfishColorMapDialog.setTabOrder(self.btnAdd, self.btnRemove)
        CrayfishColorMapDialog.setTabOrder(self.btnRemove, self.btnLoad)
        CrayfishColorMapDialog.setTabOrder(self.btnLoad, self.btnSave)
        CrayfishColorMapDialog.setTabOrder(self.btnSave, self.viewColorMap)
        CrayfishColorMapDialog.setTabOrder(self.viewColorMap, self.cboColorRamp)
        CrayfishColorMapDialog.setTabOrder(self.cboColorRamp, self.chkInvert)
        CrayfishColorMapDialog.setTabOrder(self.chkInvert, self.spinClasses)
        CrayfishColorMapDialog.setTabOrder(self.spinClasses, self.editMin)
        CrayfishColorMapDialog.setTabOrder(self.editMin, self.editMax)
        CrayfishColorMapDialog.setTabOrder(self.editMax, self.btnClassify)
        CrayfishColorMapDialog.setTabOrder(self.btnClassify, self.buttonBox)

    def retranslateUi(self, CrayfishColorMapDialog):
        CrayfishColorMapDialog.setWindowTitle(_translate("CrayfishColorMapDialog", "Color map properties", None))
        self.label_4.setText(_translate("CrayfishColorMapDialog", "Interpolation", None))
        self.radIntLinear.setText(_translate("CrayfishColorMapDialog", "Linear", None))
        self.radIntDiscrete.setText(_translate("CrayfishColorMapDialog", "Discrete", None))
        self.btnAdd.setText(_translate("CrayfishColorMapDialog", "...", None))
        self.btnRemove.setText(_translate("CrayfishColorMapDialog", "...", None))
        self.btnLoad.setText(_translate("CrayfishColorMapDialog", "...", None))
        self.btnSave.setText(_translate("CrayfishColorMapDialog", "...", None))
        self.groupBox.setTitle(_translate("CrayfishColorMapDialog", "Generate new color map", None))
        self.chkInvert.setText(_translate("CrayfishColorMapDialog", "Invert", None))
        self.label_2.setText(_translate("CrayfishColorMapDialog", "Min", None))
        self.label_3.setText(_translate("CrayfishColorMapDialog", "Max", None))
        self.label.setText(_translate("CrayfishColorMapDialog", "Classes", None))
        self.btnClassify.setText(_translate("CrayfishColorMapDialog", "Classify", None))
        self.label_6.setText(_translate("CrayfishColorMapDialog", "Source", None))
        self.groupBox_2.setTitle(_translate("CrayfishColorMapDialog", "Preview", None))

from qgis.gui import QgsColorRampComboBox

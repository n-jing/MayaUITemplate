# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(25, 25, 250, 350))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.nnz = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.nnz.setMinimum(1)
        self.nnz.setMaximum(100)
        self.nnz.setSingleStep(1)
        self.nnz.setProperty("value", 6)
        self.nnz.setObjectName("nnz")
        self.gridLayout.addWidget(self.nnz, 0, 1, 1, 1)
        
        self.laplacianStep = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.laplacianStep.setMinimum(0)
        self.laplacianStep.setMaximum(10)
        self.laplacianStep.setDecimals(5)
        self.laplacianStep.setSingleStep(0.0001)
        self.laplacianStep.setProperty("value", 0.01)
        self.laplacianStep.setObjectName("LaplacianStep")
        self.gridLayout.addWidget(self.laplacianStep, 1, 1, 1, 1)

        self.iterations = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.iterations.setMinimum(0)
        self.iterations.setMaximum(100)
        self.iterations.setProperty("value", 2)
        self.iterations.setObjectName("Iterations")
        self.gridLayout.addWidget(self.iterations, 2, 1, 1, 1)

        self.laplacianIterationNum = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.laplacianIterationNum.setMinimum(0)
        self.laplacianIterationNum.setMaximum(1000)
        self.laplacianIterationNum.setProperty("value", 180)
        self.laplacianIterationNum.setObjectName("LaplacianIterationNum")
        self.gridLayout.addWidget(self.laplacianIterationNum, 3, 1, 1, 1)

        self.clusterRing = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.clusterRing.setMinimum(1)
        self.clusterRing.setMaximum(20)
        self.clusterRing.setProperty("value", 2)
        self.clusterRing.setObjectName("ClusterRing")
        self.gridLayout.addWidget(self.clusterRing, 4, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBuild = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonBuild.setObjectName("buttonBuild")
        self.verticalLayout.addWidget(self.buttonBuild)

        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())

        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBuild, QtCore.SIGNAL("clicked()"), Dialog.invokeBuild)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "SkinDecomp", None, -1))
        self.label_1.setText(QtWidgets.QApplication.translate("Dialog", "nnz", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "LaplacianStep", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Iterations", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "LaplacianIterNum", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "clusterRing", None, -1))
        self.buttonBuild.setText(QtWidgets.QApplication.translate("Dialog", "Build", None, -1))


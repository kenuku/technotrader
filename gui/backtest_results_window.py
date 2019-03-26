# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backtest_results_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormPlot(object):
    def setupUi(self, FormPlot):
        FormPlot.setObjectName("FormPlot")
        FormPlot.resize(1149, 786)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormPlot)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidgetBacktestResults = QtWidgets.QTabWidget(FormPlot)
        self.tabWidgetBacktestResults.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidgetBacktestResults.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidgetBacktestResults.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidgetBacktestResults.setUsesScrollButtons(False)
        self.tabWidgetBacktestResults.setDocumentMode(True)
        self.tabWidgetBacktestResults.setTabsClosable(False)
        self.tabWidgetBacktestResults.setMovable(False)
        self.tabWidgetBacktestResults.setTabBarAutoHide(False)
        self.tabWidgetBacktestResults.setObjectName("tabWidgetBacktestResults")
        self.tabMainResults = QtWidgets.QWidget()
        self.tabMainResults.setObjectName("tabMainResults")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabMainResults)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.tabMainResults)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBoxPlotParameters = QtWidgets.QGroupBox(self.splitter)
        self.groupBoxPlotParameters.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBoxPlotParameters.setObjectName("groupBoxPlotParameters")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBoxPlotParameters)
        self.formLayout_2.setContentsMargins(4, 6, 4, 2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelPlotAgents = QtWidgets.QLabel(self.groupBoxPlotParameters)
        self.labelPlotAgents.setObjectName("labelPlotAgents")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelPlotAgents)
        self.labelPlotFee = QtWidgets.QLabel(self.groupBoxPlotParameters)
        self.labelPlotFee.setObjectName("labelPlotFee")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPlotFee)
        self.doubleSpinBoxPlotFee = QtWidgets.QDoubleSpinBox(self.groupBoxPlotParameters)
        self.doubleSpinBoxPlotFee.setMinimumSize(QtCore.QSize(0, 20))
        self.doubleSpinBoxPlotFee.setDecimals(4)
        self.doubleSpinBoxPlotFee.setSingleStep(0.0001)
        self.doubleSpinBoxPlotFee.setObjectName("doubleSpinBoxPlotFee")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxPlotFee)
        self.labelPlotType = QtWidgets.QLabel(self.groupBoxPlotParameters)
        self.labelPlotType.setObjectName("labelPlotType")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelPlotType)
        self.comboBoxPlotType = QtWidgets.QComboBox(self.groupBoxPlotParameters)
        self.comboBoxPlotType.setObjectName("comboBoxPlotType")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxPlotType)
        self.labelPlotNoFee = QtWidgets.QLabel(self.groupBoxPlotParameters)
        self.labelPlotNoFee.setObjectName("labelPlotNoFee")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelPlotNoFee)
        self.checkBoxPlotWithNoFee = QtWidgets.QCheckBox(self.groupBoxPlotParameters)
        self.checkBoxPlotWithNoFee.setText("")
        self.checkBoxPlotWithNoFee.setObjectName("checkBoxPlotWithNoFee")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBoxPlotWithNoFee)
        self.labelLegend = QtWidgets.QLabel(self.groupBoxPlotParameters)
        self.labelLegend.setObjectName("labelLegend")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelLegend)
        self.comboBoxLegend = QtWidgets.QComboBox(self.groupBoxPlotParameters)
        self.comboBoxLegend.setObjectName("comboBoxLegend")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxLegend)
        self.pushButtonPlot = QtWidgets.QPushButton(self.groupBoxPlotParameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPlot.sizePolicy().hasHeightForWidth())
        self.pushButtonPlot.setSizePolicy(sizePolicy)
        self.pushButtonPlot.setObjectName("pushButtonPlot")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButtonPlot)
        self.pushButtonComputeMetrics = QtWidgets.QPushButton(self.groupBoxPlotParameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonComputeMetrics.sizePolicy().hasHeightForWidth())
        self.pushButtonComputeMetrics.setSizePolicy(sizePolicy)
        self.pushButtonComputeMetrics.setObjectName("pushButtonComputeMetrics")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.pushButtonComputeMetrics)
        self.labelMainInstruments = QtWidgets.QLabel(self.groupBoxPlotParameters)
        self.labelMainInstruments.setObjectName("labelMainInstruments")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelMainInstruments)
        self.pushButtonPlotInstruments = QtWidgets.QPushButton(self.groupBoxPlotParameters)
        self.pushButtonPlotInstruments.setObjectName("pushButtonPlotInstruments")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButtonPlotInstruments)
        self.checkBoxNormalized = QtWidgets.QCheckBox(self.groupBoxPlotParameters)
        self.checkBoxNormalized.setChecked(True)
        self.checkBoxNormalized.setObjectName("checkBoxNormalized")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.checkBoxNormalized)
        self.pushButtonClearPlot = QtWidgets.QPushButton(self.groupBoxPlotParameters)
        self.pushButtonClearPlot.setObjectName("pushButtonClearPlot")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.pushButtonClearPlot)
        self.groupBoxMetrics = QtWidgets.QGroupBox(self.splitter)
        self.groupBoxMetrics.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBoxMetrics.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBoxMetrics.setObjectName("groupBoxMetrics")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxMetrics)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidgetMetrics = QtWidgets.QTableWidget(self.groupBoxMetrics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tableWidgetMetrics.setFont(font)
        self.tableWidgetMetrics.setObjectName("tableWidgetMetrics")
        self.tableWidgetMetrics.setColumnCount(8)
        self.tableWidgetMetrics.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMetrics.setHorizontalHeaderItem(7, item)
        self.tableWidgetMetrics.horizontalHeader().setDefaultSectionSize(90)
        self.verticalLayout_3.addWidget(self.tableWidgetMetrics)
        self.groupBoxPlot = QtWidgets.QGroupBox(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPlot.sizePolicy().hasHeightForWidth())
        self.groupBoxPlot.setSizePolicy(sizePolicy)
        self.groupBoxPlot.setMinimumSize(QtCore.QSize(700, 0))
        self.groupBoxPlot.setObjectName("groupBoxPlot")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxPlot)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.tabWidgetBacktestResults.addTab(self.tabMainResults, "")
        self.tabOtherResults = QtWidgets.QWidget()
        self.tabOtherResults.setObjectName("tabOtherResults")
        self.tabWidgetBacktestResults.addTab(self.tabOtherResults, "")
        self.tabBacktestInfo = QtWidgets.QWidget()
        self.tabBacktestInfo.setObjectName("tabBacktestInfo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabBacktestInfo)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_4 = QtWidgets.QSplitter(self.tabBacktestInfo)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.groupBoxGeneralInfo = QtWidgets.QGroupBox(self.splitter_3)
        self.groupBoxGeneralInfo.setObjectName("groupBoxGeneralInfo")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxGeneralInfo)
        self.formLayout.setObjectName("formLayout")
        self.labelRunId = QtWidgets.QLabel(self.groupBoxGeneralInfo)
        self.labelRunId.setObjectName("labelRunId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelRunId)
        self.lineEditRunId = QtWidgets.QLineEdit(self.groupBoxGeneralInfo)
        self.lineEditRunId.setEnabled(False)
        self.lineEditRunId.setObjectName("lineEditRunId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditRunId)
        self.labelRunTime = QtWidgets.QLabel(self.groupBoxGeneralInfo)
        self.labelRunTime.setObjectName("labelRunTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelRunTime)
        self.lineEditRunTime = QtWidgets.QLineEdit(self.groupBoxGeneralInfo)
        self.lineEditRunTime.setEnabled(False)
        self.lineEditRunTime.setObjectName("lineEditRunTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditRunTime)
        self.groupBoxBacktestInfo = QtWidgets.QGroupBox(self.splitter_3)
        self.groupBoxBacktestInfo.setObjectName("groupBoxBacktestInfo")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBoxBacktestInfo)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelDataset = QtWidgets.QLabel(self.groupBoxBacktestInfo)
        self.labelDataset.setObjectName("labelDataset")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDataset)
        self.lineEditDataset = QtWidgets.QLineEdit(self.groupBoxBacktestInfo)
        self.lineEditDataset.setEnabled(False)
        self.lineEditDataset.setObjectName("lineEditDataset")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditDataset)
        self.labelInstruments = QtWidgets.QLabel(self.groupBoxBacktestInfo)
        self.labelInstruments.setObjectName("labelInstruments")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelInstruments)
        self.textEditInstruments = QtWidgets.QTextEdit(self.groupBoxBacktestInfo)
        self.textEditInstruments.setEnabled(False)
        self.textEditInstruments.setObjectName("textEditInstruments")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEditInstruments)
        self.labelResolution = QtWidgets.QLabel(self.groupBoxBacktestInfo)
        self.labelResolution.setEnabled(True)
        self.labelResolution.setObjectName("labelResolution")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelResolution)
        self.lineEditResolution = QtWidgets.QLineEdit(self.groupBoxBacktestInfo)
        self.lineEditResolution.setEnabled(False)
        self.lineEditResolution.setObjectName("lineEditResolution")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditResolution)
        self.labelStep = QtWidgets.QLabel(self.groupBoxBacktestInfo)
        self.labelStep.setObjectName("labelStep")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelStep)
        self.lineEditStep = QtWidgets.QLineEdit(self.groupBoxBacktestInfo)
        self.lineEditStep.setEnabled(False)
        self.lineEditStep.setObjectName("lineEditStep")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditStep)
        self.labelFee = QtWidgets.QLabel(self.groupBoxBacktestInfo)
        self.labelFee.setObjectName("labelFee")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelFee)
        self.lineEditFee = QtWidgets.QLineEdit(self.groupBoxBacktestInfo)
        self.lineEditFee.setEnabled(False)
        self.lineEditFee.setObjectName("lineEditFee")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditFee)
        self.labelBacktestStart = QtWidgets.QLabel(self.groupBoxBacktestInfo)
        self.labelBacktestStart.setObjectName("labelBacktestStart")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelBacktestStart)
        self.lineEditBacktestStart = QtWidgets.QLineEdit(self.groupBoxBacktestInfo)
        self.lineEditBacktestStart.setEnabled(False)
        self.lineEditBacktestStart.setObjectName("lineEditBacktestStart")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditBacktestStart)
        self.labelBacktestEnd = QtWidgets.QLabel(self.groupBoxBacktestInfo)
        self.labelBacktestEnd.setObjectName("labelBacktestEnd")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelBacktestEnd)
        self.lineEditBacktestEnd = QtWidgets.QLineEdit(self.groupBoxBacktestInfo)
        self.lineEditBacktestEnd.setEnabled(False)
        self.lineEditBacktestEnd.setObjectName("lineEditBacktestEnd")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditBacktestEnd)
        self.groupBoxAgentsInfo = QtWidgets.QGroupBox(self.splitter_4)
        self.groupBoxAgentsInfo.setObjectName("groupBoxAgentsInfo")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxAgentsInfo)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidgetAgentsInfo = QtWidgets.QTableWidget(self.groupBoxAgentsInfo)
        self.tableWidgetAgentsInfo.setObjectName("tableWidgetAgentsInfo")
        self.tableWidgetAgentsInfo.setColumnCount(2)
        self.tableWidgetAgentsInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAgentsInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAgentsInfo.setHorizontalHeaderItem(1, item)
        self.tableWidgetAgentsInfo.horizontalHeader().setDefaultSectionSize(500)
        self.verticalLayout_6.addWidget(self.tableWidgetAgentsInfo)
        self.verticalLayout_5.addWidget(self.splitter_4)
        self.tabWidgetBacktestResults.addTab(self.tabBacktestInfo, "")
        self.verticalLayout.addWidget(self.tabWidgetBacktestResults)

        self.retranslateUi(FormPlot)
        self.tabWidgetBacktestResults.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormPlot)

    def retranslateUi(self, FormPlot):
        _translate = QtCore.QCoreApplication.translate
        FormPlot.setWindowTitle(_translate("FormPlot", "Backtest Results"))
        self.groupBoxPlotParameters.setTitle(_translate("FormPlot", "Parameters"))
        self.labelPlotAgents.setText(_translate("FormPlot", "Agents:"))
        self.labelPlotFee.setText(_translate("FormPlot", "Fee (%):"))
        self.labelPlotType.setText(_translate("FormPlot", "Plot Type:"))
        self.labelPlotNoFee.setText(_translate("FormPlot", "Plot No Fee"))
        self.labelLegend.setText(_translate("FormPlot", "Legend:"))
        self.pushButtonPlot.setText(_translate("FormPlot", "Plot"))
        self.pushButtonComputeMetrics.setText(_translate("FormPlot", "Compute Metrics"))
        self.labelMainInstruments.setText(_translate("FormPlot", "Instruments:"))
        self.pushButtonPlotInstruments.setText(_translate("FormPlot", "Plot Instruments"))
        self.checkBoxNormalized.setText(_translate("FormPlot", "Normalized"))
        self.pushButtonClearPlot.setText(_translate("FormPlot", "Clear Plot"))
        self.groupBoxMetrics.setTitle(_translate("FormPlot", "Metrics"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(0)
        item.setText(_translate("FormPlot", "Agent"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(1)
        item.setText(_translate("FormPlot", "Return (Sum)"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(2)
        item.setText(_translate("FormPlot", "Return (Prod)"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(3)
        item.setText(_translate("FormPlot", "APY"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(4)
        item.setText(_translate("FormPlot", "Sharpe"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(5)
        item.setText(_translate("FormPlot", "MDD"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(6)
        item.setText(_translate("FormPlot", "Turnover"))
        item = self.tableWidgetMetrics.horizontalHeaderItem(7)
        item.setText(_translate("FormPlot", "Volatility"))
        self.groupBoxPlot.setTitle(_translate("FormPlot", "Plot"))
        self.tabWidgetBacktestResults.setTabText(self.tabWidgetBacktestResults.indexOf(self.tabMainResults), _translate("FormPlot", "Main"))
        self.tabWidgetBacktestResults.setTabText(self.tabWidgetBacktestResults.indexOf(self.tabOtherResults), _translate("FormPlot", "Other"))
        self.groupBoxGeneralInfo.setTitle(_translate("FormPlot", "General Info"))
        self.labelRunId.setText(_translate("FormPlot", "Run ID:"))
        self.labelRunTime.setText(_translate("FormPlot", "Run Time:"))
        self.groupBoxBacktestInfo.setTitle(_translate("FormPlot", "Backtest Info"))
        self.labelDataset.setText(_translate("FormPlot", "Exchange or Dataset:"))
        self.labelInstruments.setText(_translate("FormPlot", "Instruments:"))
        self.labelResolution.setText(_translate("FormPlot", "Resolution:"))
        self.labelStep.setText(_translate("FormPlot", "Step:"))
        self.labelFee.setText(_translate("FormPlot", "Fee (%):"))
        self.labelBacktestStart.setText(_translate("FormPlot", "Backtest Start:"))
        self.labelBacktestEnd.setText(_translate("FormPlot", "Backtest End:"))
        self.groupBoxAgentsInfo.setTitle(_translate("FormPlot", "Agents Info"))
        item = self.tableWidgetAgentsInfo.horizontalHeaderItem(0)
        item.setText(_translate("FormPlot", "Agent"))
        item = self.tableWidgetAgentsInfo.horizontalHeaderItem(1)
        item.setText(_translate("FormPlot", "Parameters"))
        self.tabWidgetBacktestResults.setTabText(self.tabWidgetBacktestResults.indexOf(self.tabBacktestInfo), _translate("FormPlot", "Backtest Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormPlot = QtWidgets.QWidget()
    ui = Ui_FormPlot()
    ui.setupUi(FormPlot)
    FormPlot.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 822)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabRunBacktest = QtWidgets.QWidget()
        self.tabRunBacktest.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabRunBacktest.setAcceptDrops(False)
        self.tabRunBacktest.setObjectName("tabRunBacktest")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabRunBacktest)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBoxAgentsParameters = QtWidgets.QGroupBox(self.tabRunBacktest)
        self.groupBoxAgentsParameters.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBoxAgentsParameters.setFont(font)
        self.groupBoxAgentsParameters.setObjectName("groupBoxAgentsParameters")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxAgentsParameters)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelChooseAgent = QtWidgets.QLabel(self.groupBoxAgentsParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelChooseAgent.setFont(font)
        self.labelChooseAgent.setObjectName("labelChooseAgent")
        self.verticalLayout.addWidget(self.labelChooseAgent)
        self.comboBoxChooseAgent = QtWidgets.QComboBox(self.groupBoxAgentsParameters)
        self.comboBoxChooseAgent.setObjectName("comboBoxChooseAgent")
        self.verticalLayout.addWidget(self.comboBoxChooseAgent)
        self.groupBoxMainParameters = QtWidgets.QGroupBox(self.groupBoxAgentsParameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMainParameters.sizePolicy().hasHeightForWidth())
        self.groupBoxMainParameters.setSizePolicy(sizePolicy)
        self.groupBoxMainParameters.setObjectName("groupBoxMainParameters")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxMainParameters)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetMainParameters = QtWidgets.QTableWidget(self.groupBoxMainParameters)
        self.tableWidgetMainParameters.setObjectName("tableWidgetMainParameters")
        self.tableWidgetMainParameters.setColumnCount(2)
        self.tableWidgetMainParameters.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMainParameters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMainParameters.setHorizontalHeaderItem(1, item)
        self.tableWidgetMainParameters.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetMainParameters.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidgetMainParameters.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetMainParameters.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetMainParameters.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.tableWidgetMainParameters, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxMainParameters)
        self.groupBoxOtherParameters = QtWidgets.QGroupBox(self.groupBoxAgentsParameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxOtherParameters.sizePolicy().hasHeightForWidth())
        self.groupBoxOtherParameters.setSizePolicy(sizePolicy)
        self.groupBoxOtherParameters.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBoxOtherParameters.setMaximumSize(QtCore.QSize(16777215, 205))
        self.groupBoxOtherParameters.setObjectName("groupBoxOtherParameters")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBoxOtherParameters)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelPriceLabel = QtWidgets.QLabel(self.groupBoxOtherParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelPriceLabel.setFont(font)
        self.labelPriceLabel.setObjectName("labelPriceLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPriceLabel)
        self.comboBoxPriceLabel = QtWidgets.QComboBox(self.groupBoxOtherParameters)
        self.comboBoxPriceLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxPriceLabel.setObjectName("comboBoxPriceLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxPriceLabel)
        self.labelUseRiskFree = QtWidgets.QLabel(self.groupBoxOtherParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelUseRiskFree.setFont(font)
        self.labelUseRiskFree.setObjectName("labelUseRiskFree")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelUseRiskFree)
        self.checkBoxUseRiskFree = QtWidgets.QCheckBox(self.groupBoxOtherParameters)
        self.checkBoxUseRiskFree.setText("")
        self.checkBoxUseRiskFree.setChecked(True)
        self.checkBoxUseRiskFree.setObjectName("checkBoxUseRiskFree")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBoxUseRiskFree)
        self.labelUseShorts = QtWidgets.QLabel(self.groupBoxOtherParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelUseShorts.setFont(font)
        self.labelUseShorts.setObjectName("labelUseShorts")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelUseShorts)
        self.checkBoxUseShorts = QtWidgets.QCheckBox(self.groupBoxOtherParameters)
        self.checkBoxUseShorts.setText("")
        self.checkBoxUseShorts.setObjectName("checkBoxUseShorts")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBoxUseShorts)
        self.labelUseNeutralization = QtWidgets.QLabel(self.groupBoxOtherParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelUseNeutralization.setFont(font)
        self.labelUseNeutralization.setObjectName("labelUseNeutralization")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelUseNeutralization)
        self.checkUseNeutralization = QtWidgets.QCheckBox(self.groupBoxOtherParameters)
        self.checkUseNeutralization.setText("")
        self.checkUseNeutralization.setObjectName("checkUseNeutralization")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkUseNeutralization)
        self.labelProjectMethod = QtWidgets.QLabel(self.groupBoxOtherParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelProjectMethod.setFont(font)
        self.labelProjectMethod.setObjectName("labelProjectMethod")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelProjectMethod)
        self.comboBoxProjectMethod = QtWidgets.QComboBox(self.groupBoxOtherParameters)
        self.comboBoxProjectMethod.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxProjectMethod.setObjectName("comboBoxProjectMethod")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxProjectMethod)
        self.labelTopAmount = QtWidgets.QLabel(self.groupBoxOtherParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelTopAmount.setFont(font)
        self.labelTopAmount.setObjectName("labelTopAmount")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelTopAmount)
        self.spinBoxTopAmount = QtWidgets.QSpinBox(self.groupBoxOtherParameters)
        self.spinBoxTopAmount.setMinimumSize(QtCore.QSize(150, 0))
        self.spinBoxTopAmount.setMaximum(16777215)
        self.spinBoxTopAmount.setProperty("value", 1)
        self.spinBoxTopAmount.setObjectName("spinBoxTopAmount")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinBoxTopAmount)
        self.labelAgentsName = QtWidgets.QLabel(self.groupBoxOtherParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelAgentsName.setFont(font)
        self.labelAgentsName.setObjectName("labelAgentsName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelAgentsName)
        self.lineEditAgentsName = QtWidgets.QLineEdit(self.groupBoxOtherParameters)
        self.lineEditAgentsName.setObjectName("lineEditAgentsName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditAgentsName)
        self.verticalLayout.addWidget(self.groupBoxOtherParameters)
        self.pushButtonAddAgent = QtWidgets.QPushButton(self.groupBoxAgentsParameters)
        self.pushButtonAddAgent.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonAddAgent.setObjectName("pushButtonAddAgent")
        self.verticalLayout.addWidget(self.pushButtonAddAgent)
        self.horizontalLayout_2.addWidget(self.groupBoxAgentsParameters)
        self.groupBoxAddedAgents = QtWidgets.QGroupBox(self.tabRunBacktest)
        self.groupBoxAddedAgents.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBoxAddedAgents.setFont(font)
        self.groupBoxAddedAgents.setObjectName("groupBoxAddedAgents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxAddedAgents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxAddedActions = QtWidgets.QGroupBox(self.groupBoxAddedAgents)
        self.groupBoxAddedActions.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBoxAddedActions.setTitle("")
        self.groupBoxAddedActions.setObjectName("groupBoxAddedActions")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBoxAddedActions)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonAddedEdit = QtWidgets.QPushButton(self.groupBoxAddedActions)
        self.pushButtonAddedEdit.setObjectName("pushButtonAddedEdit")
        self.horizontalLayout_4.addWidget(self.pushButtonAddedEdit)
        self.pushButtonAddedDelete = QtWidgets.QPushButton(self.groupBoxAddedActions)
        self.pushButtonAddedDelete.setObjectName("pushButtonAddedDelete")
        self.horizontalLayout_4.addWidget(self.pushButtonAddedDelete)
        self.gridLayout_2.addWidget(self.groupBoxAddedActions, 1, 0, 1, 1)
        self.tableWidgetAddedAgents = QtWidgets.QTableWidget(self.groupBoxAddedAgents)
        self.tableWidgetAddedAgents.setObjectName("tableWidgetAddedAgents")
        self.tableWidgetAddedAgents.setColumnCount(3)
        self.tableWidgetAddedAgents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAddedAgents.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAddedAgents.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAddedAgents.setHorizontalHeaderItem(2, item)
        self.tableWidgetAddedAgents.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidgetAddedAgents.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_2.addWidget(self.tableWidgetAddedAgents, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBoxAddedAgents)
        self.groupBoxBacktestParameters = QtWidgets.QGroupBox(self.tabRunBacktest)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBoxBacktestParameters.setFont(font)
        self.groupBoxBacktestParameters.setObjectName("groupBoxBacktestParameters")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxBacktestParameters)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.comboBoxDataset = QtWidgets.QComboBox(self.groupBoxBacktestParameters)
        self.comboBoxDataset.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxDataset.setObjectName("comboBoxDataset")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxDataset)
        self.labelInstruments = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelInstruments.setFont(font)
        self.labelInstruments.setObjectName("labelInstruments")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelInstruments)
        self.textEditInstruments = QtWidgets.QTextEdit(self.groupBoxBacktestParameters)
        self.textEditInstruments.setMaximumSize(QtCore.QSize(190, 16777215))
        self.textEditInstruments.setObjectName("textEditInstruments")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEditInstruments)
        self.labelCandlesResolution = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelCandlesResolution.setFont(font)
        self.labelCandlesResolution.setObjectName("labelCandlesResolution")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelCandlesResolution)
        self.comboBoxCandlesResolution = QtWidgets.QComboBox(self.groupBoxBacktestParameters)
        self.comboBoxCandlesResolution.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxCandlesResolution.setObjectName("comboBoxCandlesResolution")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxCandlesResolution)
        self.spinBoxStep = QtWidgets.QSpinBox(self.groupBoxBacktestParameters)
        self.spinBoxStep.setMaximum(16777215)
        self.spinBoxStep.setObjectName("spinBoxStep")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxStep)
        self.labelFee = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelFee.setFont(font)
        self.labelFee.setObjectName("labelFee")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelFee)
        self.doubleSpinBoxFee = QtWidgets.QDoubleSpinBox(self.groupBoxBacktestParameters)
        self.doubleSpinBoxFee.setDecimals(4)
        self.doubleSpinBoxFee.setSingleStep(0.0001)
        self.doubleSpinBoxFee.setObjectName("doubleSpinBoxFee")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxFee)
        self.labelDumpPath = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelDumpPath.setFont(font)
        self.labelDumpPath.setObjectName("labelDumpPath")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelDumpPath)
        self.lineEditDumpPath = QtWidgets.QLineEdit(self.groupBoxBacktestParameters)
        self.lineEditDumpPath.setObjectName("lineEditDumpPath")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditDumpPath)
        self.labelParallel = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelParallel.setFont(font)
        self.labelParallel.setObjectName("labelParallel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelParallel)
        self.checkBoxParallel = QtWidgets.QCheckBox(self.groupBoxBacktestParameters)
        self.checkBoxParallel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxParallel.setText("")
        self.checkBoxParallel.setChecked(True)
        self.checkBoxParallel.setObjectName("checkBoxParallel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBoxParallel)
        self.labelDataStart = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelDataStart.setFont(font)
        self.labelDataStart.setObjectName("labelDataStart")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelDataStart)
        self.dateTimeEditDataStart = QtWidgets.QDateTimeEdit(self.groupBoxBacktestParameters)
        self.dateTimeEditDataStart.setMinimumSize(QtCore.QSize(180, 0))
        self.dateTimeEditDataStart.setDate(QtCore.QDate(2019, 2, 24))
        self.dateTimeEditDataStart.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEditDataStart.setObjectName("dateTimeEditDataStart")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditDataStart)
        self.labelBacktestStart = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelBacktestStart.setFont(font)
        self.labelBacktestStart.setObjectName("labelBacktestStart")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelBacktestStart)
        self.dateTimeEditBacktestStart = QtWidgets.QDateTimeEdit(self.groupBoxBacktestParameters)
        self.dateTimeEditBacktestStart.setMinimumSize(QtCore.QSize(180, 0))
        self.dateTimeEditBacktestStart.setDate(QtCore.QDate(2019, 2, 24))
        self.dateTimeEditBacktestStart.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEditBacktestStart.setObjectName("dateTimeEditBacktestStart")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditBacktestStart)
        self.labelBacktestEnd = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelBacktestEnd.setFont(font)
        self.labelBacktestEnd.setObjectName("labelBacktestEnd")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.labelBacktestEnd)
        self.dateTimeEditBacktestEnd = QtWidgets.QDateTimeEdit(self.groupBoxBacktestParameters)
        self.dateTimeEditBacktestEnd.setMinimumSize(QtCore.QSize(180, 0))
        self.dateTimeEditBacktestEnd.setDate(QtCore.QDate(2019, 2, 24))
        self.dateTimeEditBacktestEnd.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEditBacktestEnd.setObjectName("dateTimeEditBacktestEnd")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditBacktestEnd)
        self.pushButtonRunBacktest = QtWidgets.QPushButton(self.groupBoxBacktestParameters)
        self.pushButtonRunBacktest.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonRunBacktest.setObjectName("pushButtonRunBacktest")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.pushButtonRunBacktest)
        self.labelDataset = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelDataset.setFont(font)
        self.labelDataset.setObjectName("labelDataset")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDataset)
        self.labelStep = QtWidgets.QLabel(self.groupBoxBacktestParameters)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelStep.setFont(font)
        self.labelStep.setObjectName("labelStep")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelStep)
        self.horizontalLayout_2.addWidget(self.groupBoxBacktestParameters)
        self.tabWidget.addTab(self.tabRunBacktest, "")
        self.tabAnalyzeResults = QtWidgets.QWidget()
        self.tabAnalyzeResults.setObjectName("tabAnalyzeResults")
        self.tabWidget.addTab(self.tabAnalyzeResults, "")
        self.tabLiveTrading = QtWidgets.QWidget()
        self.tabLiveTrading.setObjectName("tabLiveTrading")
        self.tabWidget.addTab(self.tabLiveTrading, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1242, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuChange_Style = QtWidgets.QMenu(self.menuView)
        self.menuChange_Style.setObjectName("menuChange_Style")
        self.menuWindow = QtWidgets.QMenu(self.menuBar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionRun_Backtest = QtWidgets.QAction(MainWindow)
        self.actionRun_Backtest.setObjectName("actionRun_Backtest")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionClose_Window = QtWidgets.QAction(MainWindow)
        self.actionClose_Window.setObjectName("actionClose_Window")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionShow_Runner = QtWidgets.QAction(MainWindow)
        self.actionShow_Runner.setObjectName("actionShow_Runner")
        self.actionShow_Results = QtWidgets.QAction(MainWindow)
        self.actionShow_Results.setObjectName("actionShow_Results")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        self.actionZoom.setObjectName("actionZoom")
        self.actionOpen_Main_Window = QtWidgets.QAction(MainWindow)
        self.actionOpen_Main_Window.setObjectName("actionOpen_Main_Window")
        self.actionOpen_Runner = QtWidgets.QAction(MainWindow)
        self.actionOpen_Runner.setObjectName("actionOpen_Runner")
        self.actionOpen_Results = QtWidgets.QAction(MainWindow)
        self.actionOpen_Results.setObjectName("actionOpen_Results")
        self.actionOpen_Recent = QtWidgets.QAction(MainWindow)
        self.actionOpen_Recent.setObjectName("actionOpen_Recent")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHide_Toolbar = QtWidgets.QAction(MainWindow)
        self.actionHide_Toolbar.setObjectName("actionHide_Toolbar")
        self.actionHide_Control_Bar = QtWidgets.QAction(MainWindow)
        self.actionHide_Control_Bar.setObjectName("actionHide_Control_Bar")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionFusion = QtWidgets.QAction(MainWindow)
        self.actionFusion.setObjectName("actionFusion")
        self.actionWindows = QtWidgets.QAction(MainWindow)
        self.actionWindows.setObjectName("actionWindows")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.menuFile.addAction(self.actionRun_Backtest)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Recent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuChange_Style.addAction(self.actionDefault)
        self.menuChange_Style.addAction(self.actionFusion)
        self.menuChange_Style.addAction(self.actionWindows)
        self.menuChange_Style.addAction(self.actionDark)
        self.menuView.addAction(self.actionShow_Runner)
        self.menuView.addAction(self.actionShow_Results)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionHide_Toolbar)
        self.menuView.addAction(self.actionHide_Control_Bar)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuChange_Style.menuAction())
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionZoom)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionOpen_Main_Window)
        self.menuWindow.addAction(self.actionOpen_Runner)
        self.menuWindow.addAction(self.actionOpen_Results)
        self.menuHelp.addAction(self.actionHelp)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Techno Trader"))
        self.groupBoxAgentsParameters.setTitle(_translate("MainWindow", "Agent"))
        self.labelChooseAgent.setText(_translate("MainWindow", "Choose Agent:"))
        self.groupBoxMainParameters.setTitle(_translate("MainWindow", "Main Parameters"))
        item = self.tableWidgetMainParameters.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Parameter"))
        item = self.tableWidgetMainParameters.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.groupBoxOtherParameters.setTitle(_translate("MainWindow", "Other Parameters"))
        self.labelPriceLabel.setText(_translate("MainWindow", "Price Label:"))
        self.labelUseRiskFree.setText(_translate("MainWindow", "Use Risk Free:"))
        self.labelUseShorts.setText(_translate("MainWindow", "Use Shorts:"))
        self.labelUseNeutralization.setText(_translate("MainWindow", "Use Neutralization:"))
        self.labelProjectMethod.setText(_translate("MainWindow", "Projection Method:"))
        self.labelTopAmount.setText(_translate("MainWindow", "Top Amount:"))
        self.labelAgentsName.setText(_translate("MainWindow", "Agent\'s Name"))
        self.pushButtonAddAgent.setText(_translate("MainWindow", "Add Agent"))
        self.groupBoxAddedAgents.setTitle(_translate("MainWindow", "Added Agents"))
        self.pushButtonAddedEdit.setText(_translate("MainWindow", "Edit"))
        self.pushButtonAddedDelete.setText(_translate("MainWindow", "Delete"))
        item = self.tableWidgetAddedAgents.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Agent"))
        item = self.tableWidgetAddedAgents.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Main Parameters"))
        item = self.tableWidgetAddedAgents.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Other Parameters"))
        self.groupBoxBacktestParameters.setTitle(_translate("MainWindow", "Backtest\'s Parameters"))
        self.labelInstruments.setText(_translate("MainWindow", "Instruments:"))
        self.labelCandlesResolution.setText(_translate("MainWindow", " Resolution:"))
        self.labelFee.setText(_translate("MainWindow", "Fee (%):"))
        self.labelDumpPath.setText(_translate("MainWindow", "Path for Results:"))
        self.lineEditDumpPath.setText(_translate("MainWindow", "saved_files/"))
        self.labelParallel.setText(_translate("MainWindow", "Parallel:"))
        self.labelDataStart.setText(_translate("MainWindow", "Data Start:"))
        self.dateTimeEditDataStart.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.labelBacktestStart.setText(_translate("MainWindow", "Backtest Start:"))
        self.dateTimeEditBacktestStart.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.labelBacktestEnd.setText(_translate("MainWindow", "Backtest End:"))
        self.dateTimeEditBacktestEnd.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.pushButtonRunBacktest.setText(_translate("MainWindow", "Run Backtest"))
        self.labelDataset.setText(_translate("MainWindow", "Exchange or Dataset:"))
        self.labelStep.setText(_translate("MainWindow", "Step:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRunBacktest), _translate("MainWindow", "Run Backtest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAnalyzeResults), _translate("MainWindow", "Backtest Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLiveTrading), _translate("MainWindow", "Live Trading"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuChange_Style.setTitle(_translate("MainWindow", "Change Style"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionRun_Backtest.setText(_translate("MainWindow", "Run Backtest"))
        self.actionRun_Backtest.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionClose_Window.setText(_translate("MainWindow", "Close Window"))
        self.actionClose_Window.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionShow_Runner.setText(_translate("MainWindow", "Show Runner"))
        self.actionShow_Results.setText(_translate("MainWindow", "Show Results"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionMinimize.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionZoom.setText(_translate("MainWindow", "Zoom"))
        self.actionZoom.setShortcut(_translate("MainWindow", "Ctrl+Shift+M"))
        self.actionOpen_Main_Window.setText(_translate("MainWindow", "Open Main Window"))
        self.actionOpen_Main_Window.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionOpen_Runner.setText(_translate("MainWindow", "Open Runner"))
        self.actionOpen_Runner.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionOpen_Results.setText(_translate("MainWindow", "Open Results"))
        self.actionOpen_Results.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionOpen_Recent.setText(_translate("MainWindow", "Open Recent"))
        self.actionOpen_Recent.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHide_Toolbar.setText(_translate("MainWindow", "Hide Toolbar"))
        self.actionHide_Toolbar.setShortcut(_translate("MainWindow", "Ctrl+Alt+T"))
        self.actionHide_Control_Bar.setText(_translate("MainWindow", "Hide Control Bar"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionFusion.setText(_translate("MainWindow", "Fusion"))
        self.actionWindows.setText(_translate("MainWindow", "Windows"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

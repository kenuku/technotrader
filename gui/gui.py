import os
import sys
sys.path.insert(0,'../../')
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
import pytz
import json
import qdarkstyle
from technotrader.run_backtest import *
from technotrader.gui.mainwindow import Ui_MainWindow
from technotrader.gui.ui_backtest_results_window import Ui_FormPlot
from technotrader.gui.backtest_results_window import BacktestResultsWindow
from technotrader.gui.running_backtest_window import WindowRunningBacktest
from technotrader.gui.available_parameters import *
from technotrader.gui.utils_gui import *


class TechnoTraderMainWindow(Ui_MainWindow):
    def __init__(self, MainWindow, app):
        self.app = app
        self.setupUi(MainWindow)
        MainWindow.resize(1200, 800)
        self.results_dict = {}
        self.initialize_combo_boxes()
        self.initialize_buttons()
        self.process_menu_actions()
        self.make_size_settings()
        self.row_to_id = {}
        self.backtest_results_windows = []
        self.backtest_analysis_columns = [
            "show", "run_id", "run_time", "name", "exchange",
            "resolution", "step", "begin", "end", "return", "sharpe", "turnover"
        ]
        self.backtest_analysis_columns_mapping = {
            name: i for i, name in enumerate(self.backtest_analysis_columns)
        }
        self.data_type = "exchange"

    def make_size_settings(self):
        self.tableWidgetAddedAgents.setColumnWidth(0, 100)
        self.tableWidgetAddedAgents.setColumnWidth(1, 200)
        self.tableWidgetAddedAgents.setColumnWidth(2, 200)

    def initialize_combo_boxes(self):
        self.initialize_agents()
        self.comboBoxPriceLabel.addItems(PRICE_LABELS)
        self.comboBoxPriceLabel.activated[str].connect(self.choose_price_label)
        self.comboBoxProjectMethod.addItems(PROJECTIONS_METHODS)
        self.comboBoxProjectMethod.activated[str].connect(self.choose_project_method)
        self.comboBoxDataset.addItems(EXCHANGES_DATASETS)
        self.comboBoxDataset.activated[str].connect(self.choose_dataset)
        candles_resolutions = ['']
        candles_resolutions.extend(list(RESOLUTIONS.keys()))
        self.comboBoxCandlesResolution.addItems(candles_resolutions)
        self.comboBoxCandlesResolution.activated[str].connect(self.choose_candles_resolution)

    def initialize_agents_params_types(self):
        self.agent_params_types = {}
        for agent, config in self.agents_configs.items():
            self.agent_params_types[agent] = {}
            for param_name, param_value in config.items():
                self.agent_params_types[agent][param_name] = type(param_value).__name__

    def initialize_agents(self):
        agents_configs_path = "gui/default_agents_configs.json"
        with open(agents_configs_path) as f:
            self.agents_configs = json.load(f)
        self.initialize_agents_params_types()
        all_items = ['']
        all_items.extend(list(self.agents_configs.keys()))
        self.comboBoxChooseAgent.addItems(all_items)
        self.comboBoxChooseAgent.activated[str].connect(self.choose_agent)

    def initialize_buttons(self):
        self.pushButtonRunBacktest.clicked.connect(self.run_backtest)
        self.pushButtonAddAgent.clicked.connect(self.add_agent)
        self.pushButtonAddedEdit.clicked.connect(self.edit_agents)
        self.pushButtonAddedDelete.clicked.connect(self.delete_agents)
        self.pushButtonOpenResults.clicked.connect(self.file_open)
        self.pushButtonCompareBacktests.clicked.connect(self.compare_backtests)
        self.pushButtonOpenDataFile.clicked.connect(self.open_data_file)

    def show_start_end_indices(self):
        self.formLayout.removeWidget(self.dateTimeEditDataStart)
        self.dateTimeEditDataStart.deleteLater()
        self.dateTimeEditDataStart = None
        self.formLayout.removeWidget(self.dateTimeEditBacktestStart)
        self.dateTimeEditBacktestStart.deleteLater()
        self.dateTimeEditBacktestStart = None
        self.formLayout.removeWidget(self.dateTimeEditBacktestEnd)
        self.dateTimeEditBacktestEnd.deleteLater()
        self.dateTimeEditBacktestEnd = None

        self.spinBoxDataStart = QtWidgets.QSpinBox(self.groupBoxBacktestParameters)
        self.spinBoxDataStart.setMaximum(16777215)
        self.spinBoxDataStart.setObjectName("spinBoxDataStart")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.spinBoxDataStart)
        self.spinBoxBacktestStart = QtWidgets.QSpinBox(self.groupBoxBacktestParameters)
        self.spinBoxBacktestStart.setMaximum(16777215)
        self.spinBoxBacktestStart.setObjectName("spinBoxBacktestStart")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.spinBoxBacktestStart)
        self.spinBoxBacktestEnd = QtWidgets.QSpinBox(self.groupBoxBacktestParameters)
        self.spinBoxBacktestEnd.setMaximum(16777215)
        self.spinBoxBacktestEnd.setObjectName("spinBoxBacktestEnd")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.spinBoxBacktestEnd)

    def open_data_file(self):
        name = QtWidgets.QFileDialog.getOpenFileName(None, "Open File")
        print("name", name)
        self.labelOpenDataFile.setText(name[0].split("/")[-1])
        #if name[0].split(".")[-1].lower() != "csv":
        #    self.show_error("File must be in csv format!")
        #else:
        self.opened_data = pd.read_csv(name[0])
        self.data_name = name[0].split("/")[-1].split('.')[0]
        print(self.opened_data.shape)
        print(self.opened_data.head())
        if self.data_type != "csv":
            self.data_type = "csv"
            self.comboBoxCandlesResolution.setEnabled(False)
            self.spinBoxStep.setEnabled(False)
            self.dateTimeEditDataStart.setEnabled(False)
            self.dateTimeEditBacktestStart.setEnabled(False)
            self.dateTimeEditBacktestEnd.setEnabled(False)
            self.textEditInstruments.setText(str(", ".join(self.opened_data.columns)))
            self.show_start_end_indices()
            self.spinBoxBacktestStart.setValue(1)
            self.spinBoxBacktestEnd.setValue(self.opened_data.shape[0])
        else:
            self.spinBoxBacktestEnd.setValue(self.opened_data.shape[0])

    def choose_agent(self):
        self.tableWidgetMainParameters.setRowCount(0)
        agent_class = self.comboBoxChooseAgent.currentText()
        if agent_class == '':
            return
        print("agent chosen: %s" % agent_class)
        config = self.agents_configs[agent_class]
        print("config:", config)
        self.lineEditAgentsName.setText(agent_class)
        for param_name, param_value in config.items():
            numRows = self.tableWidgetMainParameters.rowCount()
            print("param_value", param_value)
            self.tableWidgetMainParameters.insertRow(numRows)
            name_widget = QtWidgets.QLabel()
            name_widget.setText(param_name)
            value_widget = QtWidgets.QLineEdit()
            value_widget.setText(str(param_value))
            self.tableWidgetMainParameters.setCellWidget(numRows, 0, name_widget)
            self.tableWidgetMainParameters.setCellWidget(numRows, 1, value_widget)

    def choose_price_label(self):
        price_label = self.comboBoxPriceLabel.currentText()
        print("price_label chosen: %s" % price_label)

    def choose_project_method(self):
        project_method = self.comboBoxProjectMethod.currentText()
        print("project_method chosen: %s" % project_method)

    def show_start_end_dates(self):
        self.formLayout.removeWidget(self.spinBoxDataStart)
        self.spinBoxDataStart.deleteLater()
        self.spinBoxDataStart = None
        self.formLayout.removeWidget(self.spinBoxBacktestStart)
        self.spinBoxBacktestStart.deleteLater()
        self.spinBoxBacktestStart = None
        self.formLayout.removeWidget(self.spinBoxBacktestEnd)
        self.spinBoxBacktestEnd.deleteLater()
        self.spinBoxBacktestEnd = None

        _translate = QtCore.QCoreApplication.translate
        self.dateTimeEditDataStart = QtWidgets.QDateTimeEdit(self.groupBoxBacktestParameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEditDataStart.sizePolicy().hasHeightForWidth())
        self.dateTimeEditDataStart.setSizePolicy(sizePolicy)
        self.dateTimeEditDataStart.setMinimumSize(QtCore.QSize(160, 0))
        self.dateTimeEditDataStart.setDate(QtCore.QDate(2019, 2, 23))
        self.dateTimeEditDataStart.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEditDataStart.setObjectName("dateTimeEditDataStart")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditDataStart)

        self.dateTimeEditBacktestStart = QtWidgets.QDateTimeEdit(self.groupBoxBacktestParameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEditBacktestStart.sizePolicy().hasHeightForWidth())
        self.dateTimeEditBacktestStart.setSizePolicy(sizePolicy)
        self.dateTimeEditBacktestStart.setMinimumSize(QtCore.QSize(160, 0))
        self.dateTimeEditBacktestStart.setDate(QtCore.QDate(2019, 2, 23))
        self.dateTimeEditBacktestStart.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEditBacktestStart.setObjectName("dateTimeEditBacktestStart")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditBacktestStart)

        self.dateTimeEditBacktestEnd = QtWidgets.QDateTimeEdit(self.groupBoxBacktestParameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEditBacktestEnd.sizePolicy().hasHeightForWidth())
        self.dateTimeEditBacktestEnd.setSizePolicy(sizePolicy)
        self.dateTimeEditBacktestEnd.setMinimumSize(QtCore.QSize(160, 0))
        self.dateTimeEditBacktestEnd.setDate(QtCore.QDate(2019, 2, 23))
        self.dateTimeEditBacktestEnd.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEditBacktestEnd.setObjectName("dateTimeEditBacktestEnd")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditBacktestEnd)
        
        self.dateTimeEditDataStart.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.dateTimeEditBacktestStart.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.dateTimeEditBacktestEnd.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))

    def choose_dataset(self):
        exchange_dataset = self.comboBoxDataset.currentText()
        if self.data_type != "exchange":
            if len(exchange_dataset):
                print("exchange_dataset chosen: %s" % exchange_dataset)
                self.data_type = "exchange"
                self.labelOpenDataFile.setText('')
                self.show_start_end_dates()
                self.comboBoxCandlesResolution.setEnabled(True)
                self.spinBoxStep.setEnabled(True)
                #self.dateTimeEditDataStart.setEnabled(True)
                #self.dateTimeEditBacktestStart.setEnabled(True)
                #self.dateTimeEditBacktestEnd.setEnabled(True)
                self.textEditInstruments.setText(str(''))
                

    def choose_candles_resolution(self):
        self.spinBoxStep.clear()
        candles_resolution = self.comboBoxCandlesResolution.currentText()
        print("candles_resolution chosen: %s" % candles_resolution)
        self.spinBoxStep.setValue(RESOLUTIONS[candles_resolution])

    def file_open(self):
        name = QtWidgets.QFileDialog.getExistingDirectory(None, "Open Directory")
        self.textEditOpenResults.setText(name)
        if len(name):
            for file in os.listdir(name):
                if file.startswith("backtest_"):
                    with open(name + '/' + file) as f:
                        results = json.load(f)
                        self.add_backtest_result(results)
                        self.results_dict[int(file.split('_')[1].split('.')[0])] = results

    def process_menu_actions(self):
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(self.close_application)
        self.actionDefault.triggered.connect(self.style_choice_default)
        self.actionFusion.triggered.connect(self.style_choice_fusion)
        self.actionWindows.triggered.connect(self.style_choice_windows)
        self.actionDark.triggered.connect(self.style_choice_dark)

    def style_choice_default(self):
        self.app.setStyleSheet('')
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("macintosh"))

    def style_choice_fusion(self):
        self.app.setStyleSheet('')
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

    def style_choice_windows(self):
        self.app.setStyleSheet('')
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Windows"))

    def style_choice_dark(self):
        self.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(
            None,
            "Quit!", "Are you sure you want to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
        )
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()

    def backtest_completed(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)          
        msg.setWindowTitle("Completed")
        msg.setText("Backtesting Completed")
        okButton = msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
        msg.exec()

    def get_agents_config(self, agent_class):
        config_other = {
            "agent_class": agent_class,
            "agent_name": self.lineEditAgentsName.text(),
            "price_label": self.comboBoxPriceLabel.currentText(),
            "use_risk_free": self.checkBoxUseRiskFree.isChecked(),
            "short_flag": self.checkBoxUseShorts.isChecked(),
            "neutralize_flag": self.checkUseNeutralization.isChecked(),
            "projection_method": self.comboBoxProjectMethod.currentText(),
            "top_amount": self.spinBoxTopAmount.value(),
            "trend_tracking": self.checkBoxTrendTracking.isChecked(),
            "window_long": self.spinBoxWindowLong.value(),
            "window_short": self.spinBoxWindowShort.value(),
            "down_trend_threshold": self.spinBoxDowntrendThreshold.value()
        }
        config_main = {}
        for row in range(self.tableWidgetMainParameters.rowCount()):
            param_name = self.tableWidgetMainParameters.cellWidget(row, 0).text()
            param_value = self.tableWidgetMainParameters.cellWidget(row, 1).text()
            print(param_value)
            param_value = param_value.replace("'", '"').replace("None", "null")
            param_value = param_value.replace("True", "true").replace("False", "false")
            if self.agent_params_types[agent_class][param_name] == "str":
                config_main[param_name] = param_value
            else:
                config_main[param_name] = json.loads(param_value)
        return config_main, config_other

    def edit_row(self, row_index):
        pass

    def edit_agents(self):
        rows = self.tableWidgetAddedAgents.selectionModel().selectedRows()
        indices_to_edit = sorted([r.row() for r in rows])
        print("Editing agents with indices:", indices_to_edit)
        for index in indices_to_edit:
            self.edit_row(row_index)

    def delete_agents(self):
        rows = self.tableWidgetAddedAgents.selectionModel().selectedRows()
        num_deleted = 0
        indices_to_delete = sorted([r.row() for r in rows])
        print("Deleting agents with indices:", indices_to_delete)
        for index in indices_to_delete:
            self.tableWidgetAddedAgents.removeRow(index - num_deleted)
            num_deleted += 1

    def insert_agent(self, agent_class, config_main_str, config_other_str):
        numRows = self.tableWidgetAddedAgents.rowCount()
        self.tableWidgetAddedAgents.insertRow(numRows)
        agent_class_label = QtWidgets.QLabel()
        agent_class_label.setText(agent_class)
        scroll_area_agent_class = QtWidgets.QScrollArea()
        scroll_area_agent_class.setWidget(agent_class_label)
        config_label_main = QtWidgets.QLabel()
        config_label_main.setText(config_main_str)
        scroll_area_main = QtWidgets.QScrollArea()
        scroll_area_main.setWidget(config_label_main)
        config_label_other = QtWidgets.QLabel()
        config_label_other.setText(config_other_str)
        scroll_area_other = QtWidgets.QScrollArea()
        scroll_area_other.setWidget(config_label_other)
        self.tableWidgetAddedAgents.setCellWidget(numRows, 0, scroll_area_agent_class)
        self.tableWidgetAddedAgents.setCellWidget(numRows, 1, scroll_area_main)
        self.tableWidgetAddedAgents.setCellWidget(numRows, 2, scroll_area_other)
        #header = self.tableWidgetAddedAgents.horizontalHeader()
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def add_agent(self):
        agent_class = self.comboBoxChooseAgent.currentText()
        if agent_class == '':
            self.show_error("Pick an agent!")
            return
        config_main, config_other = self.get_agents_config(agent_class)
        config_main_str = json.dumps(config_main)
        config_other_str = json.dumps(config_other)
        print("adding agent with config:", config_main_str, config_other_str)
        self.insert_agent(config_other["agent_class"], config_main_str, config_other_str)

    def get_instruments_list(self, instruments):
        instruments = instruments.replace("'", '').replace('"', '')
        instruments_list = [x.strip() for x in instruments.split(',')]
        return [x for x in instruments_list if len(x)]

    def parse_configs(self):
        data_begin = self.dateTimeEditDataStart.dateTime()
        data_begin = data_begin.toString(self.dateTimeEditDataStart.displayFormat())
        begin = self.dateTimeEditBacktestStart.dateTime()
        begin = begin.toString(self.dateTimeEditBacktestStart.displayFormat())
        end = self.dateTimeEditBacktestEnd.dateTime()
        end = end.toString(self.dateTimeEditBacktestEnd.displayFormat())
        exchange = self.comboBoxDataset.currentText()
        if len(exchange) == '':
            self.show_error("You should pick an exchange or dataset!")
            return
        print(data_begin)
        if begin >= end:
            self.show_error("Backtest start must be earlier than end!")
            return
        if data_begin >= end:
            self.show_error("Data start must be earlier than backtest start!")
            return
        candles_res = self.comboBoxCandlesResolution.currentText()
        step = self.spinBoxStep.value()
        if candles_res == '':
            self.show_error("Pick Candles Resolution!")
            return
        if step == 0:
            self.show_error("Pick Step!")
            return
        instruments = self.textEditInstruments.toPlainText()
        if instruments == '':
            self.show_error("Pick Instruments!")
            return
        instruments_list = self.get_instruments_list(instruments)
        data_name = "data"
        data_name += get_time_as_name_string(begin, end)
        data_name += '_' + str(step) + '_' + exchange
        data_config = {
            "data_name": data_name,
            "begin":  convert_time(data_begin),
            "end":  convert_time(end),
            "step": step,
            "candles_res": candles_res,
            "candles_res_sec": RESOLUTIONS[candles_res],
            "exchange": exchange,
            "instruments_list": instruments_list,
            "type": "exchange"
        }
        backtest_config = {
            "begin":  convert_time(begin),
            "end":  convert_time(end),
            "step": step,
            "fee": self.doubleSpinBoxFee.value(),
            "exchange": exchange,
            "candles_res": candles_res,
            "price_label": "close",
            "log_frequency": 1
        }
        return data_config, backtest_config

    def parse_agents(self, data_config):
        agents_configs = []
        for row in range(self.tableWidgetAddedAgents.rowCount()):
            agent_config = {
                "instruments_list": data_config["instruments_list"],
                "exchange": data_config["exchange"],
                "candles_res": data_config["candles_res"],
                "step": data_config["step"]
            }
            agent_class = self.tableWidgetAddedAgents.cellWidget(row, 0).widget().text()
            agent_main_params_str = self.tableWidgetAddedAgents.cellWidget(row, 1).widget().text()
            agent_other_params_str = self.tableWidgetAddedAgents.cellWidget(row, 2).widget().text()
            agent_main_params = json.loads(agent_main_params_str)
            agent_other_params = json.loads(agent_other_params_str)
            agent_config.update(agent_main_params.items())
            agent_config.update(agent_other_params.items())
            agents_configs.append((agent_class, agent_config))
        return agents_configs

    def convert_results_to_dataframe(self, backtesters_results):
        results = {}
        for agent_name, test_pc_vector_no_fee, test_pc_vector, test_turnover_vector \
                in backtesters_results:
            results[agent_name + "_returns_no_fee"] = test_pc_vector_no_fee
            results[agent_name + "_returns_with_fee"] = test_pc_vector
            results[agent_name + "_turnover"] = test_turnover_vector
        df = pd.DataFrame.from_dict(results)
        return df

    def get_backtest_id(self):
        results_path = self.lineEditDumpPath.text()
        if len(results_path) == 0:
            return 0
        list_dir = set(os.listdir(results_path))
        if "id_generator.txt" in list_dir:
            with open(results_path + "/id_generator.txt") as f:
                backtest_id = int(f.readline()) + 1
            with open(results_path + "/id_generator.txt", "w") as f:
                f.write("%d" % backtest_id)
        else:
            with open(results_path + "/id_generator.txt", "w") as f:
                f.write("0")
                backtest_id = 0
        return backtest_id

    def run_backtest(self):
        try:
            if self.data_type is None:
                self.show_error("Pick Exchange or Dataset!")
                return
            if self.data_type == "exchange":
                self.run_backtest_exchange()
            else:
                self.run_backtest_data_file()
        except Exception as e:
            self.show_error(str(e))

    def run_backtest_data_file(self):
        instruments = self.textEditInstruments.toPlainText()
        if instruments == '':
            self.show_error("Pick Instruments!")
            return
        instruments_list = self.get_instruments_list(instruments)
        print("instruments_list", instruments_list)
        data_config = {
            "data_name": self.data_name,
            "begin":  self.spinBoxDataStart.value(),
            "end":  self.spinBoxBacktestEnd.value(),
            "step": 1,
            "candles_res": "period",
            "candles_res_sec": 1,
            "exchange": self.data_name,
            "instruments_list": instruments_list,
            "type": "csv"
        }
        data_shift = 10
        backtest_config = {
            "begin":  self.spinBoxBacktestStart.value(),
            "end":  self.spinBoxBacktestEnd.value(),
            "step": 1,
            "fee": self.doubleSpinBoxFee.value(),
            "exchange": self.data_name,
            "candles_res": "period",
            "price_label": "close",
            "log_frequency": 1
        }
        agents_configs = self.parse_agents(data_config)
        if len(agents_configs) == 0:
            self.show_error("Pick agents!")
            return
        print("data_config\n", data_config)
        print("backtest_config\n", backtest_config)
        print("agents_configs:\n", agents_configs)
        path = self.lineEditDumpPath.text()
        backtest_id = self.get_backtest_id()
        backtest_config["id"] = backtest_id
        backtest_config["time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        if len(path) == 0:
            path = None
        else:
            path += ("backtest_%d.json" % backtest_id)
        print("path:", path)
        self.data_loader = DataLoader(data_config, self.opened_data)
        results = run_multi_backtest(self.data_loader, data_config, 
                                    agents_configs, backtest_config,
                                    path=path, parallel=self.checkBoxParallel.isChecked())
        print("Completed")
        self.backtest_completed()
        agents_names = [x[0] for x in agents_configs]
        self.add_backtest_result(results)
        self.show_backtest_results(results, self.data_loader)

    def run_backtest_exchange(self):
        parse_results = self.parse_configs()
        if parse_results is not None:
             data_config, backtest_config = parse_results
        else:
            return
        agents_configs = self.parse_agents(data_config)
        if len(agents_configs) == 0:
            self.show_error("Pick agents!")
            return
        print("data_config\n", data_config)
        print("backtest_config\n", backtest_config)
        print("agents_configs:\n", agents_configs)
        path = self.lineEditDumpPath.text()
        backtest_id = self.get_backtest_id()
        backtest_config["id"] = backtest_id
        backtest_config["time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        if len(path) == 0:
            path = None
        else:
            path += ("backtest_%d.json" % backtest_id)
        print("path:", path)
        self.data_loader = DataLoader(data_config)
        results = run_multi_backtest(self.data_loader, data_config, 
                                    agents_configs, backtest_config,
                                    path=path, parallel=self.checkBoxParallel.isChecked())
        #results_df = self.convert_results_to_dataframe(results)
        #self.window_run_backtest = WindowRunningBacktest()
        #self.window_run_backtest.close()
        self.backtest_completed()
        #results_df = pd.read_csv("gui/multi_poloniex_hour_1.csv")
        #agents_names = [x[:-len("_returns_no_fee")] for x in results_df.columns \
        #                    if x.endswith("_returns_no_fee")]
        agents_names = [x[0] for x in agents_configs]
        self.add_backtest_result(results)
        self.show_backtest_results(results, self.data_loader)

    def show_error(self, text):
        print("error: %s" % text)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)          
        msg.setWindowTitle("Error")
        msg.setText(text)
        okButton = msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
        msg.exec()

    def show_results(self, numRows):
        print("Showing results")
        results = self.results_dict[self.row_to_id[numRows]]
        agents_names = list(results["agents"].keys())
        self.show_backtest_results(results, None)

    def add_backtest_result(self, results):
        if len(results["agents"].keys()) == 1:
            res_agent = list(results["agents"].items())[0]
            name = res_agent[0]
            agent_dict = res_agent[1]
            returns = np.array(agent_dict["returns_no_fee"])
            final_return = np.cumprod(returns)[-1]
            sharpe = np.mean(returns - 1) / np.std(returns - 1)
            turnover = sum(agent_dict["turnover"])
        else:
            name = "multi"
            final_return = ''
            sharpe = ''
            turnover = ''
        values = {
            "run_id": results["backtest_config"]["id"],
            "run_time": results["backtest_config"]["time"],
            "name": name,
            "exchange": results["backtest_config"]["exchange"],
            "resolution": results["backtest_config"]["candles_res"],
            "step": results["backtest_config"]["step"],
            "begin": convert_time_to_str(results["backtest_config"]["begin"]),
            "end": convert_time_to_str(results["backtest_config"]["end"]),
            "return": final_return,
            "sharpe": sharpe,
            "turnover": turnover
        }
        numRows = self.tableWidgetBacktestsResults.rowCount()
        self.row_to_id[numRows] = values["run_id"]
        self.tableWidgetBacktestsResults.insertRow(numRows)
        show_widget = QtWidgets.QPushButton()
        show_widget.setText("Show")
        show_widget.clicked.connect(lambda: self.show_results(numRows))
        self.tableWidgetBacktestsResults.setCellWidget(numRows, 0, show_widget)
        for name, value in values.items():
            widget = QtWidgets.QLabel()
            if isinstance(value, str):
                str_format = "%s"
            elif isinstance(value, float):
                str_format = "%.3f"
            elif isinstance(value, int):
                str_format = "%d"
            else:
                ValueError("Wrong format")
            widget.setText(str_format % value)
            index = self.backtest_analysis_columns_mapping[name]
            self.tableWidgetBacktestsResults.setCellWidget(numRows, index, widget)

    def show_backtest_results(self, results, data_loader):
        window = BacktestResultsWindow(data_loader, results)
        self.backtest_results_windows.append(window)
        window.show()

    def compare_backtests(self):
        rows = self.tableWidgetBacktestsResults.selectionModel().selectedRows()
        print("rows:", rows)
        results = [self.results_dict[self.row_to_id[r.row()]] for r in rows]
        data_types = set()
        for r in results:
            if r["data_config"].get("type") is not None:
                data_types.add(r["data_config"]["type"])
            else:
                data_types.add("exchange")
        if len(data_types) > 1:
            self.show_error("Cannot compare backtests with different data types!")
            return
        self.show_backtest_results(results, None)

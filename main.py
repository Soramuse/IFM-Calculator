
import sys
import os
import pandas as pd

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from modules.IFM_Calculation_GUI import *
# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class Stream(QObject):
    _console_out = Signal(str)

    def write(self, text):
        self._console_out.emit(str(text))

    def flush(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        global dfa, dfb
        # FIND DISPLAY BROWSER OBJECT AND SET AS ATTRIBUTE
        # ///////////////////////////////////////////////////////////////
        self.Display_browser = self.findChild(QTextBrowser, "Display_browser")

        # REDIRECT PRINT OUTPUT TO TEXT BROWSER
        # ///////////////////////////////////////////////////////////////
        sys.stdout = Stream()
        sys.stdout._console_out.connect(self.Display_browser.insertPlainText)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        # title = "IFM Calculator"
        # description = ""
        # APPLY TEXTS
        # self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
       # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_calculate.clicked.connect(self.buttonClick)
        widgets.btn_figure.clicked.connect(self.buttonClick)
        widgets.btn_export.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # CACULATION PAGE
        widgets.Input_btn.clicked.connect(self.input_file)
        widgets.Calculate_btn.clicked.connect(self.IFM_Cal)
        widgets.Display_clear_btn.clicked.connect(self.Clear)
        widgets.Display_save_btn.clicked.connect(self.buttonClick)
        widgets.Display_next_btn.clicked.connect(self.buttonClick)

        # FIGURE PAGE
        widgets.Fig_SD_btn.clicked.connect(self.Fig_SD_fun)
        widgets.Fig_Gap_btn.clicked.connect(self.Fig_Gap_fun)
        widgets.Fig_IFM_btn.clicked.connect(self.Fig_IFM_fun)
        widgets.Fig_save_btn.clicked.connect(self.buttonClick)

        # EXPORT PAGE
        widgets.pushButton_7.clicked.connect(self.Export_fun)

        # SHOW FIGURE
        widgets.stackedWidget.currentChanged.connect(self.Page_fun)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.Home_page)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        self.fig_widget = widgets.Fig_Widget
        self.gridlayout = QVBoxLayout(self.fig_widget)

    def input_file(self):
        # GET FILE NAME
        fileName = QFileDialog.getExistingDirectory(
            self, 'Choose working directory', 'C:\\')
        # SET TEXT
        widgets.Input_line.setText(str(fileName))

    def IFM_Cal(self):
        self.Display_browser.clear()
        global dfa, dfb
        # READING FILE
        fileName = widgets.Input_line.text()
        c = IFM_Calculation_GUI.check(fileName)
        if c == "OK":
            dfa = IFM_Calculation_GUI.import_data(fileName, '1')
            dfb = IFM_Calculation_GUI.import_data(fileName, '2')
            # Calculate IFM
            try:
                float(widgets.Mesh_line.text())
                global output, row3, angle_x, angle_y, angle_z1, theta, Eulerangles, IFM_summary, Gap_summary, SD_summary, cal_status
                Accu = widgets.Mesh_line.text()
                output = None
                try:
                    df_matched = pairing(dfa, dfb)
                    row3 = len(df_matched)
                    output = IFM_Calculation(df_matched)
                    df_max = calculate_extreme_values(df_matched, float(Accu))
                    angle_x_0 = calculate_angle(np.array((df_max.iat[0, 2] - df_max.iat[1, 2], df_max.iat[0, 3] - df_max.iat[1, 3])),
                                              np.array((df_max.iat[0, 9] - df_max.iat[1, 9], df_max.iat[0, 10] - df_max.iat[1, 10])))
                    angle_x_1 = calculate_angle(np.array((df_max.iat[0, 5] - df_max.iat[1, 5], df_max.iat[0, 6] - df_max.iat[1, 6])),
                                              np.array((df_max.iat[0, 12] - df_max.iat[1, 12], df_max.iat[0, 13] - df_max.iat[1, 13])))
                    angle_y_0 = calculate_angle(np.array((df_max.iat[2, 1] - df_max.iat[3, 1], df_max.iat[2, 3] - df_max.iat[3, 3])),
                                              np.array((df_max.iat[2, 8] - df_max.iat[3, 8], df_max.iat[2, 10] - df_max.iat[3, 10])))
                    angle_y_1 = calculate_angle(np.array((df_max.iat[2, 4] - df_max.iat[3, 4], df_max.iat[2, 6] - df_max.iat[3, 6])),
                                              np.array((df_max.iat[2, 11] - df_max.iat[3, 11], df_max.iat[2, 13] - df_max.iat[3, 13])))
                    angle_z1_0 = calculate_angle(np.array((df_max.iat[2, 1] - df_max.iat[3, 1], df_max.iat[2, 2] - df_max.iat[3, 2])),
                                               np.array((df_max.iat[2, 8] - df_max.iat[3, 8], df_max.iat[2, 9] - df_max.iat[3, 9])))
                    angle_z1_1 = calculate_angle(np.array((df_max.iat[2, 4] - df_max.iat[3, 4], df_max.iat[2, 5] - df_max.iat[3, 5])),
                                               np.array((df_max.iat[2, 11] - df_max.iat[3, 11], df_max.iat[2, 12] - df_max.iat[3, 12])))
                    angle_z2_0 = calculate_angle(np.array((df_max.iat[0, 1] - df_max.iat[1, 1], df_max.iat[0, 2] - df_max.iat[1, 2])),
                                               np.array((df_max.iat[0, 8] - df_max.iat[1, 8], df_max.iat[0, 9] - df_max.iat[1, 9])))
                    angle_z2_1 = calculate_angle(np.array((df_max.iat[0, 4] - df_max.iat[1, 4], df_max.iat[0, 5] - df_max.iat[1, 5])),
                                               np.array((df_max.iat[0, 11] - df_max.iat[1, 11], df_max.iat[0, 12] - df_max.iat[1, 12])))
                    angle_x = angle_x_1 - angle_x_0
                    angle_y = angle_y_1 - angle_y_0
                    angle_z1 = angle_z1_1 - angle_z1_0
                    angle_z2 = angle_z2_1 - angle_z2_0
                    print("angle_x = " + str(angle_x))
                    print("angle_y = " + str(angle_y))
                    print("angle_z1 = " + str(angle_z1))
                    print("angle_z2 = " + str(angle_z2))
                    normal_a = calculate_normal(dfa)
                    normal_b = calculate_normal(dfb)
                    if np.dot(normal_a, normal_b) < 0:
                        normal_b = -normal_b
                    theta = np.degrees(calculate_theta(normal_a, normal_b))
                    print("Theta of two planes = ", theta)
                    R = calculate_rotation_matrix(normal_a, normal_b)
                    Eulerangles = calculate_eulerangles(R)
                    IFM_summary = output['IFM (mm)'].describe()
                    Gap_summary = output['Detachment (mm)'].describe()
                    SD_summary = output['Displacement (mm)'].describe()
                    self.Displacement_plot = plot(output, 'Displacement (mm)')
                    self.Detachement_plot = plot(output, 'Detachment (mm)')
                    self.IFM_plot = plot(output, 'IFM (mm)')
                    cal_status = 'Success'
                except Exception as e:
                    # CREATE QMessageBox INSTANCE
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(str(e))
                    msg_box.setWindowTitle("Error")
                    msg_box.exec_()
                    cal_status = str(e)
            except ValueError:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Error: Mesh size must be a positive digit.")
                msg_box.setWindowTitle("Error")
                msg_box.exec()
        else:
            # CREATE QMessageBox INSTANCE
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText(c)
            msg_box.setWindowTitle("Error")
            msg_box.exec_()

    def Clear(self):
        global cal_status
        cal_status = 'Cleared'
        widgets.Input_line.clear()
        widgets.Mesh_line.clear()
        self.Display_browser.clear()
        # Clear all plots
        for i in range(self.gridlayout.count()):
            self.gridlayout.itemAt(i).widget().deleteLater()

    def Fig_SD_fun(self):
        if cal_status == 'Success':
            self.canvas = FigureCanvas(self.Displacement_plot)
            # Clear all plots
            for i in range(self.gridlayout.count()):
                self.gridlayout.itemAt(i).widget().deleteLater()
            self.gridlayout.addWidget(self.canvas)
            self.canvas.draw()

    def Fig_Gap_fun(self):
        if cal_status == 'Success':
            self.canvas = FigureCanvas(self.Detachement_plot)
            # Clear all plots
            for i in range(self.gridlayout.count()):
                self.gridlayout.itemAt(i).widget().deleteLater()
            self.gridlayout.addWidget(self.canvas)
            self.canvas.draw()

    def Fig_IFM_fun(self):
        if cal_status == 'Success':
            self.canvas = FigureCanvas(self.IFM_plot)
            # Clear all plots
            for i in range(self.gridlayout.count()):
                self.gridlayout.itemAt(i).widget().deleteLater()
            self.gridlayout.addWidget(self.canvas)
            self.canvas.draw()

    def Page_fun(self, index):
        if index == 2:
            if cal_status == 'Success':
                widgets.Fig_IFM_btn.setChecked(True)
                self.canvas = FigureCanvas(self.IFM_plot)
                # Clear all plots
                for i in range(self.gridlayout.count()):
                    self.gridlayout.itemAt(i).widget().deleteLater()
                self.gridlayout.addWidget(self.canvas)
                self.canvas.draw()
        if index == 3:
            if cal_status == 'Success':
                widgets.node_sum_text.setText(str(row3))
                widgets.IFM_sum_text.setText(str(IFM_summary['mean']) + ' mm')
                widgets.gap_sum_text.setText(str(Gap_summary['mean']) + ' mm')
                widgets.SD_sum_text.setText(str(SD_summary['mean']) + ' mm')
                widgets.x_sum_text.setText(str(angle_x) + ' °')
                widgets.y_sum_text.setText(str(angle_y) + ' °')
                widgets.z_sum_text.setText(str(angle_z1) + ' °')
                widgets.theta_sum_text.setText(str(theta) + ' °')
                widgets.euler_sum_text.setText(str(Eulerangles))
            else:
                widgets.node_sum_text.clear()
                widgets.IFM_sum_text.clear()
                widgets.gap_sum_text.clear()
                widgets.SD_sum_text.clear()
                widgets.x_sum_text.clear()
                widgets.y_sum_text.clear()
                widgets.z_sum_text.clear()
                widgets.theta_sum_text.clear()
                widgets.euler_sum_text.clear()

    def Export_fun(self):
        if not widgets.Export_name_line.text().strip():
           # CREATE QMessageBox INSTANCE
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText('Please input the name of the export file!')
            msg_box.setWindowTitle("Error")
            msg_box.exec_()
        else:
            ExportName = widgets.Export_name_line.text()
            ExportFolder = QFileDialog.getExistingDirectory(
                self, 'Choose working directory', 'C:\\')
            # SET TEXT
            widgets.Export_folder_line.setText(str(ExportFolder))
            status = export(ExportFolder, ExportName, output, row3,
                            angle_x, angle_y, angle_z1, theta, Eulerangles, IFM_summary, Gap_summary, SD_summary)
            if status == 'Success':
                widgets.Export_label.setText("Exported successfully!")
                widgets.node_sum_text.setText(str(row3))
                widgets.IFM_sum_text.setText(str(IFM_summary['mean']) + ' mm')
                widgets.gap_sum_text.setText(str(Gap_summary['mean']) + ' mm')
                widgets.SD_sum_text.setText(str(SD_summary['mean']) + ' mm')
                widgets.x_sum_text.setText(str(angle_x) + ' °')
                widgets.y_sum_text.setText(str(angle_y) + ' °')
                widgets.z_sum_text.setText(str(angle_z1) + ' °')
                widgets.theta_sum_text.setText(str(theta) + ' °')
                widgets.euler_sum_text.setText(str(Eulerangles))
            else:
                widgets.Export_label.setText(str(status))
                widgets.node_sum_text.clear()
                widgets.IFM_sum_text.clear()
                widgets.gap_sum_text.clear()
                widgets.SD_sum_text.clear()
                widgets.x_sum_text.clear()
                widgets.y_sum_text.clear()
                widgets.z_sum_text.clear()
                widgets.theta_sum_text.clear()
                widgets.euler_sum_text.clear()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.Home_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW CALCULATE PAGE
        if btnName == "btn_calculate":
            widgets.stackedWidget.setCurrentWidget(widgets.Calculation_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW FIGURE PAGE
        if btnName == "btn_figure":
            widgets.stackedWidget.setCurrentWidget(
                widgets.Figure_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        # SHOW EXPORT PAGE
        if btnName == "btn_export":
            widgets.stackedWidget.setCurrentWidget(widgets.Export_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SAVE LOG
        if btnName == "Display_save_btn":
            fileName = QFileDialog.getSaveFileName(
                self, 'Save file', 'C:\\', "Text files (*.txt)")
            with open(fileName[0], 'w') as f:
                my_text = self.Display_browser.toPlainText()
                f.write(my_text)

        # NEXT PAGE
        if btnName == "Display_next_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.Figure_page)
            UIFunctions.resetStyle(self, btnName)
            widgets.btn_figure.setStyleSheet(
                UIFunctions.selectMenu(widgets.btn_figure.styleSheet()))

        # SAVE FIGURE
        if btnName == "Fig_save_btn":
            fileName = QFileDialog.getSaveFileName(
                self, 'Save file', 'C:\\', "PNG files (*.png)")
            self.canvas.figure.savefig(fileName[0])

        # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        # if event.buttons() == Qt.LeftButton:
        # print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        # print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/images/images/sora_logo3.png"))
    window = MainWindow()
    sys.exit(app.exec())

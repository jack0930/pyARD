# ===============================================================================
# Copyright 2021 An-Jun Liu
# Modifiy 2026 Lin Pai-Shao
# Last Modifd Date: 06/25/2026
# ===============================================================================

# import python module
import numpy as np 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
import os
import shutil
from winotify import Notification
from tkinter import *
from datetime import date

# import UI
import UI.HomePage
import UI.LinearRegression
import UI.T0Statistics
import UI.MassRatio
import UI.JCalculation
import UI.ReselectDialog
import UI.ParameterSetting
import UI.AirRatioStatistics
import UI.AgeCalculation
import UI.TypeSelect
import UI.SaltCalculation
import UI.JSelect
import UI.StatSelect
import UI.JStatistics
import UI.SaltSelect
import UI.SaltStatSelect
import UI.SaltStat
import UI.DiagramPlots_LS
import UI.DiagramPlots_SH
import UI.DiagramSelect 
import UI.DatumSelect

# import utilities
import Utilities



# load UI
# ===============================================================================
class HomePage(QtWidgets.QMainWindow, UI.HomePage.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    #def resizeEvent(self, event):
        

class TypeSelect(QtWidgets.QMainWindow, UI.TypeSelect.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class LinearRegressionPage(QtWidgets.QMainWindow, UI.LinearRegression.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    
    def resizeEvent(self, event):
        self.Isize = [100, 230, 670+event.size().width()-800, 450+event.size().height()-700]      
        self.photo.setGeometry(QtCore.QRect(self.Isize[0], self.Isize[1], self.Isize[2], self.Isize[3]))
        

class StatSelect(QtWidgets.QMainWindow, UI.StatSelect.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class JStatistics(QtWidgets.QMainWindow, UI.JStatistics.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    def resizeEvent(self, event):
        self.Isize = [100, 230, 670+event.size().width()-800, 450+event.size().height()-700]      
        self.photo.setGeometry(QtCore.QRect(self.Isize[0], self.Isize[1], self.Isize[2], self.Isize[3]))

class T0Statistics(QtWidgets.QMainWindow, UI.T0Statistics.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def resizeEvent(self, event):
        self.Isize = [150, 175, 600+event.size().width()-800, 250+event.size().height()-700]      
        self.photo.setGeometry(QtCore.QRect(self.Isize[0], self.Isize[1], self.Isize[2], self.Isize[3]))
        self.Tsize =[150, 470+event.size().height()-700, 591, 101]
        self.tableWidget.setGeometry(QtCore.QRect(self.Tsize[0], self.Tsize[1], self.Tsize[2], self.Tsize[3]))
        self.numSelectedFiles.setGeometry(QtCore.QRect(150, 580+event.size().height()-700, 200, 31))

class AirRatioStatistics(QtWidgets.QMainWindow, UI.AirRatioStatistics.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    def resizeEvent(self, event):
        self.Isize = [200, 200, 350+event.size().width()-800, 275+event.size().height()-700]      
        self.photo.setGeometry(QtCore.QRect(self.Isize[0], self.Isize[1], self.Isize[2], self.Isize[3]))
        self.Tsize =[210, 490+event.size().height()-700, 301, 111]
        self.RatioTable.setGeometry(QtCore.QRect(self.Tsize[0], self.Tsize[1], self.Tsize[2], self.Tsize[3]))
        self.numSelectedFiles.setGeometry(QtCore.QRect(150, 580+event.size().height()-700, 200, 31))
        
class MassRatio(QtWidgets.QMainWindow, UI.MassRatio.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class JCalculation(QtWidgets.QMainWindow, UI.JCalculation.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class JSelect(QtWidgets.QMainWindow, UI.JSelect.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class ReselectTable(QtWidgets.QDialog, UI.ReselectDialog.Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

class ParameterSetting(QtWidgets.QMainWindow, UI.ParameterSetting.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    
    def resizeEvent(self, event):
        self.Tsize = [220, 200, 351+event.size().width()-800, 391+event.size().height()-700]       
        self.ParameetrTable.setGeometry(QtCore.QRect(self.Tsize[0], self.Tsize[1], self.Tsize[2], self.Tsize[3]))

class AgeCalculation(QtWidgets.QMainWindow, UI.AgeCalculation.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class SaltCalculation(QtWidgets.QMainWindow, UI.SaltCalculation.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    def resizeEvent(self, event):
        self.Tsize =[200, 200, 445+event.size().width()-800, 90+event.size().height()-700]
        self.RatioTableCa.setGeometry(QtCore.QRect(self.Tsize[0], self.Tsize[1], self.Tsize[2], self.Tsize[3]))
        self.RatioTableK.setGeometry(QtCore.QRect(self.Tsize[0], self.Tsize[1], self.Tsize[2], self.Tsize[3]))
        
class SaltSelect(QtWidgets.QMainWindow, UI.SaltSelect.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
class SaltStat(QtWidgets.QMainWindow, UI.SaltStat.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    def resizeEvent(self, event):
        self.Isize = [150, 175, 600+event.size().width()-800, 250+event.size().height()-700]      
        self.photo.setGeometry(QtCore.QRect(self.Isize[0], self.Isize[1], self.Isize[2], self.Isize[3]))
        
class SaltStatSelect(QtWidgets.QMainWindow, UI.SaltStatSelect.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
class DiagramPlots_SH(QtWidgets.QMainWindow, UI.DiagramPlots_SH.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    def resizeEvent(self, event):
        self.Isize = [91, 190, 490+event.size().width()-800, 450+event.size().height()-700]     
        self.photo.setGeometry(QtCore.QRect(self.Isize[0], self.Isize[1], self.Isize[2], self.Isize[3]))
        self.Tsize =[580+event.size().width()-800, 190+event.size().height()-700, 220, 419]
        self.tableWidget.setGeometry(QtCore.QRect(self.Tsize[0], self.Tsize[1], self.Tsize[2], self.Tsize[3]))
                
class DiagramPlots_LS(QtWidgets.QMainWindow, UI.DiagramPlots_LS.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)   
        
    def resizeEvent(self, event):
        self.Isize = [91, 190, 490+event.size().width()-800, 450+event.size().height()-700]     
        self.photo.setGeometry(QtCore.QRect(self.Isize[0], self.Isize[1], self.Isize[2], self.Isize[3]))
        self.Tsize =[580+event.size().width()-800, 190+event.size().height()-700, 220, 419]
        self.tableWidget.setGeometry(QtCore.QRect(self.Tsize[0], self.Tsize[1], self.Tsize[2], self.Tsize[3]))
        
class DiagramSelect(QtWidgets.QMainWindow, UI.DiagramSelect.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
class DatumSelect(QtWidgets.QMainWindow, UI.DatumSelect.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
# main app
# ===============================================================================
class App():
    def __init__(self):
        self.work_dir = os.path.dirname(os.path.realpath(__file__))+'/' # get the absolute path of working directory

        # initilization for GUI
        QtWidgets.QApplication.setStyle('Fusion')
        self.app = QtWidgets.QApplication(sys.argv)
        self.HomePage = HomePage()
        self.T0CalculationPage = LinearRegressionPage()
        self.TypeSelect = TypeSelect()
        self.ReselectDialog = ReselectTable()
        self.StatSelectPage = StatSelect()
        self.JStatisticsPage = JStatistics()
        self.T0StatisticsPage = T0Statistics()
        self.AirRatioStatisticsPage = AirRatioStatistics()
        self.SaltStatPage = SaltStat()
        self.MassRatioPage = MassRatio()
        self.JCalculationPage = JCalculation()
        self.JSelectPage = JSelect()
        self.AgeCalculationPage = AgeCalculation()
        self.ParameterSettingPage = ParameterSetting()
        self.SaltCalculationPage = SaltCalculation()
        self.SaltSelectPage = SaltSelect()
        self.SaltStatSelectPage = SaltStatSelect()
        self.DiagramSelectPage = DiagramSelect()
        self.DiagramPlots_LSPage = DiagramPlots_LS()
        self.DatumSelectPage = DatumSelect()
        self.DiagramPlots_SHPage = DiagramPlots_SH()

        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.HomePage) #p0
        self.widget.addWidget(self.T0CalculationPage) #p1
        self.widget.addWidget(self.T0StatisticsPage) #p2
        self.widget.addWidget(self.MassRatioPage) #p3
        self.widget.addWidget(self.JCalculationPage) #p4
        self.widget.addWidget(self.ParameterSettingPage) #p5
        self.widget.addWidget(self.AgeCalculationPage) #p6
        self.widget.addWidget(self.TypeSelect) #p7
        self.widget.addWidget(self.SaltCalculationPage) #p8
        self.widget.addWidget(self.JSelectPage) #p9
        self.widget.addWidget(self.StatSelectPage) #p10
        self.widget.addWidget(self.JStatisticsPage) #p11
        self.widget.addWidget(self.SaltSelectPage) #p12
        self.widget.addWidget(self.AirRatioStatisticsPage) #p13
        self.widget.addWidget(self.DiagramSelectPage) #p14
        self.widget.addWidget(self.DiagramPlots_SHPage) #p15
        self.widget.addWidget(self.DiagramPlots_LSPage) #p16
        self.widget.addWidget(self.SaltStatPage) #p17
        self.widget.addWidget(self.SaltStatSelectPage) #p18
        self.widget.addWidget(self.DatumSelectPage) #p19
        self.widget.resize(800, 700)
        for i in range(self.widget.count()):
            self.insertLogo(self.widget.widget(i))

        # others
        self.fitting_function_list = ["Linear", "Average"]
        self.mass_pair = ['Ar39/40', 'Ar36/40', 'Ar39/36', 'Ar40/36', 'Ar38/36']
        self.data_folder = 'Data/'
        self.screenshot_folder = 'Figures/'
        with open(self.work_dir+'.work/.app_info.txt', 'r') as f:
            self.app_info = f.readlines()
        self.J_list = [28201000,128100000,523100000]
        self.J_Sigma = [46000,700000,2600000]
        self.toast = Notification(app_id="pyARD", title="Save success!",duration="short")
        self.power = 6

    def insertLogo(self, page):
        # coordinate = [x, y, w, h]
        page.logo = QtWidgets.QLabel(page.centralwidget)
        page.logo.setGeometry(QtCore.QRect(50, 25, 700, 75))
        page.logo.setText("")
        page.logo.setPixmap(QtGui.QPixmap(self.work_dir+".work/logo.png"))
        page.logo.setScaledContents(True)
        page.logo.setObjectName("logo")


    # ===============================================================================
    def run(self):
        # load parameters
        self.loadParameterSeting()

        # deal with click or keyin events
        # click button on Homepage
        self.HomePage.LRP.clicked.connect(self.toTS)
        self.HomePage.T0S.clicked.connect(self.toSS)
        self.HomePage.MR.clicked.connect(self.toMR)
        self.HomePage.JV.clicked.connect(self.toJS)
        self.HomePage.AC.clicked.connect(self.toAC)
        self.HomePage.SC.clicked.connect(self.toSCS)
        self.HomePage.DF.clicked.connect(self.toDS)
        self.HomePage.DP.clicked.connect(self.toDPS)
        self.HomePage.PS_button.clicked.connect(self.toPS)
        self.HomePage.actionParameter_Setting.triggered.connect(self.toPS)
        self.HomePage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.HomePage.actionCheck_Update.triggered.connect(self.checkVersion)

        # click button on TypeSelect
        self.TypeSelect.MB.clicked.connect(self.toLRP_MB)
        self.TypeSelect.PBa.clicked.connect(self.toLRP_PBa)
        self.TypeSelect.AS.clicked.connect(self.toLRP_AS)
        self.TypeSelect.PBs.clicked.connect(self.toLRP_PBs)
        self.TypeSelect.SP.clicked.connect(self.toLRP_SP)
        self.TypeSelect.TP.clicked.connect(self.toLRP_TP)
        self.TypeSelect.ST.clicked.connect(self.toLRP_ST)
        self.TypeSelect.actionParameter_Setting.triggered.connect(self.toPS)
        self.TypeSelect.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.TypeSelect.actionCheck_Update.triggered.connect(self.checkVersion)
        self.TypeSelect.goHome.triggered.connect(self.toMain)

        # click button on Linear Regression Page
        self.T0CalculationPage.return_2.clicked.connect(self.toMain)
        self.T0CalculationPage.save.clicked.connect(self.LRP_save)
        self.T0CalculationPage.reselect.clicked.connect(self.LRP_reselect)
        self.T0CalculationPage.linear.clicked.connect(self.LRP_useLinear)
        self.T0CalculationPage.average.clicked.connect(self.LRP_useAverage)
        self.T0CalculationPage.new_2.clicked.connect(self.toTS)
        
        # click button on Stat Select
        self.StatSelectPage.T0.clicked.connect(self.toT0S)
        self.StatSelectPage.J.clicked.connect(self.toJSS)
        self.StatSelectPage.ARS.clicked.connect(self.toARS)
        self.StatSelectPage.Salt.clicked.connect(self.toSSS)
        self.StatSelectPage.actionParameter_Setting.triggered.connect(self.toPS)
        self.StatSelectPage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.StatSelectPage.actionCheck_Update.triggered.connect(self.checkVersion)
        self.StatSelectPage.goHome.triggered.connect(self.toMain)
        
        # click button on T0 statistics page
        self.T0StatisticsPage.return_2.clicked.connect(self.toMain)
        self.T0StatisticsPage.save.clicked.connect(self.T0S_save)
        self.T0StatisticsPage.new_2.clicked.connect(self.toSS)
        self.T0StatisticsPage.reselect.clicked.connect(self.T0_reselect)
        
        # click button on Salt statistics select page
        self.SaltStatSelectPage.Ca36.clicked.connect(self.toS36Ca)
        self.SaltStatSelectPage.Ca39.clicked.connect(self.toS39Ca)
        self.SaltStatSelectPage.K40.clicked.connect(self.toS40K)
        self.SaltStatSelectPage.K38.clicked.connect(self.toS38K)
        self.SaltStatSelectPage.K39.clicked.connect(self.toS39K)
        self.SaltStatSelectPage.actionParameter_Setting.triggered.connect(self.toPS)
        self.SaltStatSelectPage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.SaltStatSelectPage.actionCheck_Update.triggered.connect(self.checkVersion)
        self.SaltStatSelectPage.goHome.triggered.connect(self.toMain)
        
        # click button on Salt statistics page
        self.SaltStatPage.return_2.clicked.connect(self.toMain)
        self.SaltStatPage.save.clicked.connect(self.SSC_save)
        self.SaltStatPage.new_2.clicked.connect(self.toSS)
        self.SaltStatPage.reselect.clicked.connect(self.Salt_reselect)
        
        # click button on J statistics page
        self.JStatisticsPage.return_2.clicked.connect(self.toMain)
        self.JStatisticsPage.save.clicked.connect(self.JSS_save)
        self.JStatisticsPage.new_2.clicked.connect(self.toSS)
        self.JStatisticsPage.reselect.clicked.connect(self.J_reselect)
        
        # click button on Air Ratio Statistics page
        self.AirRatioStatisticsPage.return_2.clicked.connect(self.toMain)
        self.AirRatioStatisticsPage.save.clicked.connect(self.ARS_save)
        self.AirRatioStatisticsPage.new_2.clicked.connect(self.toSS)

        # click button on Mass Ratio page
        self.MassRatioPage.return_2.clicked.connect(self.toMain)
        self.MassRatioPage.save.clicked.connect(self.MR_save)
        self.MassRatioPage.new_2.clicked.connect(self.toMR)

        # click button on J Volume Calculation page
        self.JCalculationPage.return_2.clicked.connect(self.toMain)
        self.JCalculationPage.save.clicked.connect(self.JV_save)
        self.JCalculationPage.new_2.clicked.connect(self.toJS)
        
         # click button on JSelect
        self.JSelectPage.FSC.clicked.connect(self.toJV_FSC)
        self.JSelectPage.LP6.clicked.connect(self.toJV_LP6)
        self.JSelectPage.MMHB.clicked.connect(self.toJV_MMHB)
        self.JSelectPage.actionParameter_Setting.triggered.connect(self.toPS)
        self.JSelectPage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.JSelectPage.actionCheck_Update.triggered.connect(self.checkVersion)
        self.JSelectPage.goHome.triggered.connect(self.toMain)

        # click button on Parameter Setting page
        self.ParameterSettingPage.return_2.clicked.connect(self.toMain)
        self.ParameterSettingPage.change.clicked.connect(self.PS_change)
        self.ParameterSettingPage.save.clicked.connect(self.PS_save)
        self.ParameterSettingPage.raw.clicked.connect(self.PS_raw)
        self.ParameterSettingPage.cancel.clicked.connect(self.PS_cancel)

        # click button on Age Calculation page
        self.AgeCalculationPage.return_2.clicked.connect(self.toMain)
        self.AgeCalculationPage.save.clicked.connect(self.AC_save)
        self.AgeCalculationPage.new_2.clicked.connect(self.toAC)

        self.widget.show()
        
         # click button on Salt Calculation page
        self.SaltCalculationPage.return_2.clicked.connect(self.toMain)
        self.SaltCalculationPage.save.clicked.connect(self.SC_save)
        self.SaltCalculationPage.new_2.clicked.connect(self.toSCS)
        
         # click button on SaltSelect
        self.SaltSelectPage.Ca.clicked.connect(self.toSCa)
        self.SaltSelectPage.K.clicked.connect(self.toSK)
        self.SaltSelectPage.actionParameter_Setting.triggered.connect(self.toPS)
        self.SaltSelectPage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.SaltSelectPage.actionCheck_Update.triggered.connect(self.checkVersion)
        self.SaltSelectPage.goHome.triggered.connect(self.toMain)
        
        # click button on Diagram Plots SH Page
        self.DiagramPlots_SHPage.return_2.clicked.connect(self.toMain)
        self.DiagramPlots_SHPage.save.clicked.connect(self.DFSH_save)
        self.DiagramPlots_SHPage.new_2.clicked.connect(self.toDS)
        self.DiagramPlots_SHPage.reselect.clicked.connect(self.SH_reselect)
        self.DiagramPlots_SHPage.N.clicked.connect(self.DF_SN)
        self.DiagramPlots_SHPage.I.clicked.connect(self.DF_SI)
        self.DiagramPlots_SHPage.W.clicked.connect(self.DF_SW)
        self.DiagramPlots_SHPage.A.clicked.connect(self.DF_SA)
        self.DiagramPlots_SHPage.box.currentIndexChanged.connect(self.show_SH)
        self.DiagramPlots_SHPage.box2.currentIndexChanged.connect(self.show_SH)
        
        # click button on Diagram Plots LS Page
        self.DiagramPlots_LSPage.return_2.clicked.connect(self.toMain)
        self.DiagramPlots_LSPage.save.clicked.connect(self.DFLS_save)
        self.DiagramPlots_LSPage.new_2.clicked.connect(self.toDS)
        self.DiagramPlots_LSPage.reselect.clicked.connect(self.LS_reselect)
        self.DiagramPlots_LSPage.N.clicked.connect(self.DF_SN)
        self.DiagramPlots_LSPage.I.clicked.connect(self.DF_SI)
        self.DiagramPlots_LSPage.K.clicked.connect(self.DF_SK)
        self.DiagramPlots_LSPage.P.clicked.connect(self.DF_P)
        self.DiagramPlots_LSPage.box.currentIndexChanged.connect(self.show_LS)
        self.DiagramPlots_LSPage.box2.currentIndexChanged.connect(self.show_LS)
        
        # click button on Diagram Plots Select Page
        self.DiagramSelectPage.SH.clicked.connect(self.toDF_SH)
        self.DiagramSelectPage.LS.clicked.connect(self.toDF_LS)
        self.DiagramSelectPage.actionParameter_Setting.triggered.connect(self.toPS)
        self.DiagramSelectPage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.DiagramSelectPage.actionCheck_Update.triggered.connect(self.checkVersion)
        self.DiagramSelectPage.goHome.triggered.connect(self.toMain)
        
        # click button on Datum Select Pag
        self.DatumSelectPage.TT.clicked.connect(self.toDP)
        self.DatumSelectPage.isor.clicked.connect(self.toDPR)
        self.DatumSelectPage.actionParameter_Setting.triggered.connect(self.toPS)
        self.DatumSelectPage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.DatumSelectPage.actionCheck_Update.triggered.connect(self.checkVersion)
        self.DatumSelectPage.goHome.triggered.connect(self.toMain)
        
        # close program when pressing x(esc)
        sys.exit(self.app.exec_())
    
    # methods added for UI operation
    # ===============================================================================
    # back to Homepage
    def toMain(self):
        self.widget.setCurrentIndex(0)

    # popup message box
    def Popup(self, msg_type, msg_title, msg_content):
        '''
        msg_type:
        0 NoIcon
        1 Information
        2 Warning
        3 Critical
        4 Question
        '''
        msg = QtWidgets.QMessageBox()
        msg.setIcon(msg_type)
        msg.setText("<font size = 10> {} </font> ".format(msg_title))
        msg.setInformativeText("<font size = 5> {} </font> ".format(msg_content.replace('\n', '<br>')))
        msg.setWindowTitle("")
        msg.exec_()

    # adjust table column and row size
    def TableAdjust(self, table):
        header = table.horizontalHeader()
        for i in range(table.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = table.verticalHeader()
        for i in range(table.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    # display system info
    def systemInfo(self):
        self.Popup(1, "System Info", "".join(self.app_info))

    # check if current app is up to date
    def checkVersion(self):
        app_info_url = 'https://raw.githubusercontent.com/jack0930/pyADR/main/.work/.app_info.txt'
        try:
            page = requests.get(app_info_url)
            if page.ok:
                latest_version = page.text.split('\n')[1].rstrip()
                current_version = self.app_info[1].rstrip()
                version_msg = "Installed Version: {}\nLatest Version: {}\n".format(current_version, latest_version)
                if current_version == latest_version:
                    self.Popup(1, "No updates available at this time", version_msg)
                else:
                    git_repo_url = "https://github.com/jack0930/pyARD.git"
                    self.Popup(1, "There are updates available at this time", version_msg+"Please go to {} to update to the latest version!\n".format(git_repo_url))
            else:
                self.Popup(2, "HTTP request failed!", "HTTP status {}".format(page.status_code))
        except:
            self.Popup(2, "No internet connection!", "Please check your internet connection!")

    # methods for parameters setting page
    # ===============================================================================
    def loadParameterSeting(self):
        with open(self.work_dir+'.work/setting.csv', 'r') as f:
            data = f.readlines()

        self.numParamters = int(data[1].split(',')[1])
        self.parameters = []
        self.parameters_name = []
        # first row is header and second row is # of parameters
        for i in range(self.numParamters):
            self.parameters_name.append(data[i+2].split(',')[0].rstrip())
            self.parameters.append(data[i+2].split(',')[1].rstrip())
        f.close()
        
        with open(self.work_dir+'.work/rawpath.txt', 'r') as f:
            self.rawpath = str(f.readline())
        f.close()


    def toPS(self):
        # fill the table and set the item as disabled
        for i in range(self.numParamters):
            item = QtWidgets.QTableWidgetItem(self.parameters[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.ParameterSettingPage.ParameetrTable.setItem(i, 0, item)
            
        # show the page
        self.TableAdjust(self.ParameterSettingPage.ParameetrTable)
        self.ParameterSettingPage.change.show()
        self.ParameterSettingPage.cancel.hide()
        self.ParameterSettingPage.save.hide()
        self.widget.setCurrentIndex(5)

    def PS_change(self):
        # show the save and cancel button, hide the change button
        self.ParameterSettingPage.cancel.show()
        self.ParameterSettingPage.save.show()
        self.ParameterSettingPage.change.hide()

        # enable edit (need better way to implement)
        for i in range(self.numParamters):
            item = QtWidgets.QTableWidgetItem(self.parameters[i])
            self.ParameterSettingPage.ParameetrTable.setItem(i, 0, item) # make cell editable

    def PS_save(self):
        error_msg = ''
        changed = 0
        invalid = 0
        

        for i in range(self.numParamters):
            item = self.ParameterSettingPage.ParameetrTable.item(i, 0)
            content = item.text().rstrip()

            # value changed
            if content != self.parameters[i]:
                error_type = 0
                # check if valid
                try:
                    if self.ParameterSettingPage.ParameetrTable.verticalHeaderItem(i).text() == 'numCycle':
                        if int(content) <= 0:
                            error_type = 1
                    else:
                        if float(content) < 0:
                            error_type = 2
                except:
                    error_type = 1 if i > 9 else 2
                
                # new valid value
                if error_type == 0:
                    self.parameters[i] = content # update the parameter
                    changed = 1 # need rewrite setting.csv

                # restore the value
                else:
                    item.setText(self.parameters[i]) 
                    invalid = 1
                    error_msg += '{} should be a {}.\n\n'.format(self.parameters_name[i], 
                    'positive integer' if error_type == 1 else 'non-negative number')

            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit

        self.ParameterSettingPage.change.show()
        self.ParameterSettingPage.cancel.hide()
        self.ParameterSettingPage.save.hide()

        # rewite setting.csv with update parameters value if necessary
        if changed:
            new_ps = ['parameter,value\n', 'numParameters,{}\n'.format(self.numParamters)]
            for i in range(self.numParamters):
                new_ps.append('{},{}\n'.format(self.parameters_name[i], self.parameters[i]))

            with open(self.work_dir+'.work/setting.csv', 'w') as f:
                f.writelines(new_ps)

        if invalid:
            self.Popup(2, 'Invalid Typed Parameters!', error_msg)
        
    def PS_raw(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self.widget,"Open Directory",)
        self.rawpath = dir
        with open(self.work_dir+'.work/rawpath.txt', 'w') as f:
            f.write(dir)
        f.close()

    def PS_cancel(self):
        # restore to previous value
        for i in range(self.numParamters):
            item = self.ParameterSettingPage.ParameetrTable.item(i, 0)
            item.setText(self.parameters[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit

        self.ParameterSettingPage.change.show()
        self.ParameterSettingPage.cancel.hide()
        self.ParameterSettingPage.save.hide()


    # methods for age calculation page
    # ===============================================================================
    def toAC(self):

        measurement, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select measurement file (csv)" , self.data_folder, "(*.csv)")
        
        if len(measurement) > 0:
            try:
                J = float(self.parameters[self.parameters_name.index('J value')])
                J_std = float(self.parameters[self.parameters_name.index('J std')])
                J_int = float(self.parameters[self.parameters_name.index('J int')])
                self.AgeCalculation_result = Utilities.calcAge(measurement, J, J_std,J_int, [float(x) for x in self.parameters[:15]])
            
                # fill the table
                for i in range(55):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.AgeCalculation_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.AgeCalculationPage.tableWidget.setItem(i//2 if i < 48 else i-24, i%2 if i < 48 else 0, item)

                self.AgeCalculationPage.age.setAlignment(QtCore.Qt.AlignLeft)
                self.AgeCalculationPage.age.setText('Age = {:.5} Ma +- {:.5}'.format(self.AgeCalculation_result[46]/10**6,self.AgeCalculation_result[47]/10**6))
                self.AgeCalculationPage.age.setFont(QtGui.QFont('Times', 20))

                # show the page
                self.TableAdjust(self.AgeCalculationPage.tableWidget)
                self.widget.setCurrentIndex(6)
            except:
                self.Popup(2, "Error!", "Please check the selected data format or the parameters!")

    def AC_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Age Calculation result" , self.data_folder+'Agecalc/', "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Samp#,t,Min,iradiation PK 90%,Variable,Value,Sigma\n")
            for i in range(self.AgeCalculationPage.tableWidget.rowCount()):
                f.write('{},{},{},{},{},{},{},\n'.format(self.AgeCalculation_result[55],self.AgeCalculation_result[56],self.AgeCalculation_result[57],self.AgeCalculation_result[58],self.AgeCalculationPage.tableWidget.verticalHeaderItem(i).text(),
                self.AgeCalculation_result[2*i] if i < 24 else self.AgeCalculation_result[i + 24],
                self.AgeCalculation_result[2*i+1] if i < 24 else 'N/A'))    
            f.close()



    # methods for J
    # ===============================================================================
    def toJS(self):             
        self.widget.setCurrentIndex(9)
    
    def toJV_FSC(self):
        index = 0
        self.jt = 'FSC/'
        self.measurement, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select measurement file (csv)" , self.data_folder+'/MassRatio/Standerd/FSC/', "(*.csv)")
        
        if len(self.measurement) > 0:
            try:
                # set the cell of the table of the T0 statistics
                self.J_Calculation_result = Utilities.getJVolumeStatistics(self.measurement, self.J_list[index],self.J_Sigma[index],[float(x) for x in self.parameters[:15]])
                
                for i in range(5):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_Calculation_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.JCalculationPage.RatioTable.setItem(0, i, item)
                    item2 = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_Calculation_result[i+5]))
                    item2.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.JCalculationPage.RatioTable2.setItem(0, i, item2)


                # show the page
                self.TableAdjust(self.JCalculationPage.RatioTable)
                self.widget.setCurrentIndex(4)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")
                
    def toJV_LP6(self):
        index = 1
        self.jt = 'LP6/'
        self.measurement, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select measurement file (csv)" , self.data_folder+'/MassRatio/Standerd/LP6/', "(*.csv)")
        
        if len(self.measurement) > 0:
            try:
                # set the cell of the table of the T0 statistics
                self.J_Calculation_result = Utilities.getJVolumeStatistics(self.measurement, self.J_list[index],self.J_Sigma[index],[float(x) for x in self.parameters[:15]])
                
                for i in range(5):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_Calculation_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.JCalculationPage.RatioTable.setItem(0, i, item)
                    item2 = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_Calculation_result[i+5]))
                    item2.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.JCalculationPage.RatioTable2.setItem(0, i, item2)

                # show the page
                self.TableAdjust(self.JCalculationPage.RatioTable)
                self.widget.setCurrentIndex(4)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")
    
    def toJV_MMHB(self):
        index = 2
        self.jt = 'MMHB/'
        self.measurement, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select measurement file (csv)" , self.data_folder+'/MassRatio/Standerd/MMHB/', "(*.csv)")
        
        if len(self.measurement) > 0:
            try:
                # set the cell of the table of the T0 statistics
                self.J_Calculation_result = Utilities.getJVolumeStatistics(self.measurement, self.J_list[index],self.J_Sigma[index],[float(x) for x in self.parameters[:15]])
                
                for i in range(5):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_Calculation_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.JCalculationPage.RatioTable.setItem(0, i, item)
                    item2 = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_Calculation_result[i+5]))
                    item2.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.JCalculationPage.RatioTable2.setItem(0, i, item2)


                # show the page
                self.TableAdjust(self.JCalculationPage.RatioTable)
                self.TableAdjust(self.JCalculationPage.RatioTable2)
                self.widget.setCurrentIndex(4)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")
    
    def JV_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save J value Calculation result" , self.data_folder+'/J value/'+self.jt, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("file name,36Ar(a)[V],37Ar(ca)[V],39Ar(k)[V],40Ar(r)[V],40Ar(r)(%),39Ar(k)(%),K/Ca,K/Ca Sigma,J value,J Sigma,J Sigma int\n")
            f.write("{},{},{},{},{},{},{},{},{},{},{},{}\n".format(self.measurement,self.J_Calculation_result[0], self.J_Calculation_result[1],self.J_Calculation_result[2],self.J_Calculation_result[3],self.J_Calculation_result[4],self.J_Calculation_result[5],self.J_Calculation_result[6],self.J_Calculation_result[7],self.J_Calculation_result[8],self.J_Calculation_result[9],self.J_Calculation_result[10]))
            f.close()

    # methods for Mass Ratio
    # ===============================================================================
    def toMR(self):
        # select mass and preline
        mass, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select mass file (csv)" , self.data_folder, "(*.csv)")
        bg, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select preline file (csv)" , self.data_folder, "(*.csv)")

        if len(mass) > 0 and len(bg) > 0:
            try:
                self.ratio_result = Utilities.calculateMassRatio(mass, bg, self.parameters[self.parameters_name.index('OG Date')])

                for i in range(5):
                    for j in range(5):
                        item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.ratio_result[i][j]))
                       
                        item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                        if i < 3:
                            self.MassRatioPage.ValueTable.setItem(j, i, item)
                        else:
                            self.MassRatioPage.RatioTable.setItem(j, i-3, item)

                self.TableAdjust(self.MassRatioPage.ValueTable)
                self.TableAdjust(self.MassRatioPage.RatioTable)
                self.widget.setCurrentIndex(3)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")
        else:
            self.Popup(2, "Wrong Usage!", "Please select exactly one mass file first and then eactly one preline file")

    def MR_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Measurement T0 result" , self.data_folder+'/MassRatio/', "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Samp#,t,Min,iradiation PK 90%,Mass,Raw,Measurment,Measurement's Sigma,Ratio,Value,Ratio's Sigma\n")
            f.writelines(["{},{},{},{},Ar{},{},{},{},{},{},{}\n".format(self.ratio_result[5],self.ratio_result[6],self.ratio_result[7],self.ratio_result[8],i+36, self.ratio_result[0][i], self.ratio_result[1][i], self.ratio_result[2][i],self.mass_pair[i], self.ratio_result[3][i], self.ratio_result[4][i]) for i in range(5)])
            f.close()
    
    # methods for Salt Calculation
    # ===============================================================================
    def toSC(self):
        if self.salt == 'Ca':
            salt, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select Salt file (csv)" , self.data_folder+'MassRatio/Salt/CaF/', "(*.csv)")
            if len(salt) > 0:
                
                    self.salt_result,self.info = Utilities.calculateSlatCa(salt)

                    for i in range(2):
                        for j in range(2):
                            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.salt_result[i][j]))
                            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                            self.SaltCalculationPage.RatioTableCa.setItem(i, j, item)
                            
                    self.TableAdjust(self.SaltCalculationPage.RatioTableCa)
                    self.widget.setCurrentIndex(8)
                
        if self.salt == 'K':
            salt, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select Salt file (csv)" , self.data_folder+'MassRatio/Salt/Ksalt/', "(*.csv)")
            if len(salt) > 0:
                    self.salt_result,self.info = Utilities.calculateSlatK(salt)

                    for i in range(3):
                        for j in range(2):
                            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.salt_result[i][j]))
                            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                            self.SaltCalculationPage.RatioTableK.setItem(i, j, item)
                            
                    self.TableAdjust(self.SaltCalculationPage.RatioTableK)
                    self.widget.setCurrentIndex(8)
                
        
        
    def SC_save(self):
        if self.salt == 'Ca':
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Measurement T0 result" , self.data_folder+'SaltRatio/CaF/', "(*.csv)")
            if len(filename) > 0:
                f = open(filename, 'w')
                f.write("Samp#,,Ratio,Sigma\n")
                f.writelines(["{},[36Ar/37Ar]Ca,{},{}\n".format(self.info,self.salt_result[0][0], self.salt_result[1][0])])
                f.writelines(["{},[39Ar/37Ar]Ca,{},{}\n".format(self.info,self.salt_result[0][1], self.salt_result[1][1])])
                f.close()
        if self.salt == 'K':
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Measurement T0 result" , self.data_folder+'SaltRatio/Ksalt/', "(*.csv)")
            if len(filename) > 0:
                f = open(filename, 'w')
                f.write("Samp#,,Ratio,Sigma\n")
                f.writelines(["{},[40Ar/39Ar]K,{},{}\n".format(self.info,self.salt_result[0,0], self.salt_result[0,1])])
                f.writelines(["{},[38Ar/39Ar]K,{},{}\n".format(self.info,self.salt_result[1,0], self.salt_result[1,1])])
                f.writelines(["{},[39Ar/37Ar]K,{},{}\n".format(self.info,self.salt_result[2,0], self.salt_result[2,1])])
                f.close()
        
    def toSCa(self):
        self.salt = "Ca"
        self.SaltCalculationPage.RatioTableK.setVisible(False)
        self.SaltCalculationPage.RatioTableCa.setVisible(True)
        self.toSC()


    def toSK(self):
        self.salt = "K"
        self.SaltCalculationPage.RatioTableCa.setVisible(False)
        self.SaltCalculationPage.RatioTableK.setVisible(True)
        self.toSC()

    def toSCS(self):
       self.widget.setCurrentIndex(12)

    # methods for Statistics
    # ===============================================================================
    def toSS(self):             
        self.widget.setCurrentIndex(10)
    
    def T0_setReselectTable(self):
        w = self.ReselectDialog.frameGeometry().width()
        h = self.ReselectDialog.frameGeometry().height()
        self.ReselectDialog.ReselectTable = QtWidgets.QTableWidget(self.ReselectDialog)
        self.ReselectDialog.ReselectTable.setGeometry(QtCore.QRect(int(0.1*w), int(0.2*h), int(0.8*w), int(0.5*h)))
        self.ReselectDialog.ReselectTable.setObjectName("ReselectTable")
        self.ReselectDialog.ReselectTable.setColumnCount(len(self.T0filename))
        self.ReselectDialog.ReselectTable.setRowCount(1)
        self.ReselectDialog.ReselectTable.setVerticalHeaderLabels(['T0'])
        self.ReselectDialog.ReselectTable.setHorizontalHeaderLabels(['{}'.format(i) for i in range(1, self.numCycle+1)])
        
        header = self.ReselectDialog.ReselectTable.horizontalHeader()
        for i in range(self.ReselectDialog.ReselectTable.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.ReselectDialog.ReselectTable.verticalHeader()
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.ReselectDialog.ReselectTable.setItem(i, j, item)

    def T0_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.T0_checkReselectTable)
    
    def T0_checkReselectTable(self):
        for j in range(self.ReselectDialog.ReselectTable.columnCount()):
            item = self.ReselectDialog.ReselectTable.item(0,j)
            if item.checkState() == QtCore.Qt.Unchecked:
                self.mask[j] = 0
            else:
                self.mask[j] = 1
        
        self.T0_statistics_result,re_n = Utilities.REgetT0Statistics(self.T0filename,self.mask)
        for i in range(5):
                    for j in range(2):
                        item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.T0_statistics_result[i, j]))
                        item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                        self.T0StatisticsPage.tableWidget.setItem(j+2, i, item)

                # set # of selected files
        self.T0StatisticsPage.numSelectedFiles.setText("n={} RE n={}".format(len(self.T0filename),re_n))
        self.T0StatisticsPage.numSelectedFiles.setFont(QtGui.QFont('Times', 12))

        # set image
        self.T0StatisticsPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/T0S.png"))
               
        # show the page
        self.TableAdjust(self.T0StatisticsPage.tableWidget)

      
    
    def J_setReselectTable(self):
        w = self.ReselectDialog.frameGeometry().width()
        h = self.ReselectDialog.frameGeometry().height()
        self.ReselectDialog.ReselectTable = QtWidgets.QTableWidget(self.ReselectDialog)
        self.ReselectDialog.ReselectTable.setGeometry(QtCore.QRect(int(0.1*w), int(0.2*h), int(0.8*w), int(0.5*h)))
        self.ReselectDialog.ReselectTable.setObjectName("ReselectTable")
        self.ReselectDialog.ReselectTable.setColumnCount(len(self.Jfilename))
        self.ReselectDialog.ReselectTable.setRowCount(1)
        self.ReselectDialog.ReselectTable.setVerticalHeaderLabels(['J'])
        self.ReselectDialog.ReselectTable.setHorizontalHeaderLabels(['{}'.format(i) for i in range(1, self.numCycle+1)])
        
        header = self.ReselectDialog.ReselectTable.horizontalHeader()
        for i in range(self.ReselectDialog.ReselectTable.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.ReselectDialog.ReselectTable.verticalHeader()
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.ReselectDialog.ReselectTable.setItem(i, j, item)

    def J_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.J_checkReselectTable)
        
    def J_checkReselectTable(self):
        for j in range(self.ReselectDialog.ReselectTable.columnCount()):
            item = self.ReselectDialog.ReselectTable.item(0,j)
            if item.checkState() == QtCore.Qt.Unchecked:
                self.mask[j] = 0
            else:
                self.mask[j] = 1
            
        # set the cell of the table of the J statistics
        self.J_statistics_result = Utilities.REgetJStatistics(self.Jfilename,self.mask)
        for i in range(4):
            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_statistics_result[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.JStatisticsPage.tableWidget.setItem(0, i, item)
            
        # set image
        self.JStatisticsPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/J.png"))
            
        # show the page
        self.TableAdjust(self.JStatisticsPage.tableWidget)
        
    def toT0S(self):

        self.T0filename, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get T0 statistics" , self.data_folder+'T0/', "(*.csv)") # select list of files

        if len(self.T0filename) > 0:
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])
            self.T0_setReselectTable()  # setup the reselect table here
            self.mask = np.ones(len(self.T0filename))
                   
                # set the cell of the table of the T0 statistics
            self.T0_statistics_result,self.mask,og_result,re_n = Utilities.getT0Statistics(self.T0filename,self.mask)
                
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                if self.mask[j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(0,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
                
                for i in range(5):
                    for j in range(2):
                        item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(og_result[i, j]))
                        item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                        self.T0StatisticsPage.tableWidget.setItem(j, i, item)
                    for j in range(2):
                        item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.T0_statistics_result[i, j]))
                        item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                        self.T0StatisticsPage.tableWidget.setItem(j+2, i, item)

                # set # of selected files
                self.T0StatisticsPage.numSelectedFiles.setText("n={} RE n={}".format(len(self.T0filename),re_n))
                self.T0StatisticsPage.numSelectedFiles.setFont(QtGui.QFont('Times', 12))

                # set image
                self.T0StatisticsPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/T0S.png"))

                # show the page
                self.TableAdjust(self.T0StatisticsPage.tableWidget)
                self.widget.setCurrentIndex(2)
            

    def toJSS(self):

        self.Jfilename, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get J statistics" , self.data_folder+'J value/', "(*.csv)") # select list of files

        if len(self.Jfilename) > 0:
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])
            self.J_setReselectTable()  # setup the reselect table here
            self.mask = np.ones(len(self.Jfilename))
            
            # set the cell of the table of the J statistics
            self.J_statistics_result,self.madk = Utilities.getJStatistics(self.Jfilename,self.mask)
            
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                if self.mask[j] == 0:
                    item = self.ReselectDialog.ReselectTable.item(0,j)
                    item.setCheckState(QtCore.Qt.Unchecked)
            
            for i in range(4):
                item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.J_statistics_result[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                self.JStatisticsPage.tableWidget.setItem(0, i, item)
            
           

            # set image
            self.JStatisticsPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/J.png"))

            # show the page
            self.TableAdjust(self.JStatisticsPage.tableWidget)
            self.widget.setCurrentIndex(11)
            

    def T0S_save(self):
        
        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0 Statistics result" , self.data_folder+'Statistics/T0/', "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,Mean,STD\n")
            f.writelines(["Ar{},{},{}\n".format(i+36, self.T0_statistics_result[i,0], self.T0_statistics_result[i,1]) for i in range(5)])
            f.close()

    def JSS_save(self):
        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save J Statistics result" , self.data_folder+'Statistics/J/', "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Avg,STD,Wmean,Wmean STD\n")
            f.writelines(["{},{},{},{}\n".format(self.J_statistics_result[0], self.J_statistics_result[1], self.J_statistics_result[2], self.J_statistics_result[3])])
            f.close()
    
    # methods for Air Ratio Statistics
    # ===============================================================================
    def toARS(self):

        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get Air Ratio statistics" , self.data_folder+'MassRatio/AirRatio/', "(*.csv)") # select list of files

        if len(filelist) > 0:
            try:
                # set the cell of the table of the T0 statistics
                self.AirRatio_statistics_result,n = Utilities.getAirRatioStatistics(filelist)
                for i in range(2):
                    for j in range(2):
                        item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.AirRatio_statistics_result[i, j]))
                        item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                        self.AirRatioStatisticsPage.RatioTable.setItem(j, i, item)

                # set # of selected files
                self.AirRatioStatisticsPage.numSelectedFiles.setText("n = {}".format(n))
                self.AirRatioStatisticsPage.numSelectedFiles.setFont(QtGui.QFont('Times', 20))

                # set image
                self.AirRatioStatisticsPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/ARS.png"))

                # show the page
                self.TableAdjust(self.AirRatioStatisticsPage.RatioTable)
                self.widget.setCurrentIndex(13)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")

    def ARS_save(self):
        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Air Ratio Statistics result" , self.data_folder+'Statistics/AS/', "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Air Ratio,Mean,STD\n")
            f.write("Ar 40/36,{},{}\n".format(self.AirRatio_statistics_result[0, 0], self.AirRatio_statistics_result[0, 1]))
            f.write("Ar 38/36,{},{}\n".format(self.AirRatio_statistics_result[1, 0], self.AirRatio_statistics_result[1, 1]))
            f.close()

    # methods for Salt Statistics
    # ===============================================================================
    def toSSS(self):
        
        self.widget.setCurrentIndex(18)
    
    def toS36Ca(self):
        
        self.salt=36
        self.toSSC()
    
    def toS39Ca(self):
        
        self.salt=39
        self.toSSC()
    
    def toS40K(self):
        
        self.salt=40
        self.toSSC()
        
    def toS38K(self):
        
        self.salt=38
        self.toSSC()
        
    def toS39K(self):
         
        self.salt=37
        self.toSSC()
        
    def toSSC(self):

        self.Saltfilename, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get Salt statistics" , self.data_folder+'SaltRatio/', "(*.csv)") # select list of files

        if len(self.Saltfilename) > 0:
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])
            self.Salt_setReselectTable()  # setup the reselect table here
            self.mask = np.ones(len(self.Saltfilename))
                   
            # set the cell of the table of the J statistics
            self.Salt_statistics_result,self.madk = Utilities.getSaltStatistics(self.Saltfilename,self.mask,self.salt)
           
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                if self.mask[j] == 0:
                    item = self.ReselectDialog.ReselectTable.item(0,j)
                    item.setCheckState(QtCore.Qt.Unchecked)
            
            for i in range(4):
                item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.Salt_statistics_result[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                self.SaltStatPage.tableWidget.setItem(0, i, item)
            
           

            # set image
            self.SaltStatPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/Salt.png"))

            # show the page
            self.TableAdjust(self.SaltStatPage.tableWidget)
            self.widget.setCurrentIndex(17)
                
    def Salt_setReselectTable(self):
        w = self.ReselectDialog.frameGeometry().width()
        h = self.ReselectDialog.frameGeometry().height()
        self.ReselectDialog.ReselectTable = QtWidgets.QTableWidget(self.ReselectDialog)
        self.ReselectDialog.ReselectTable.setGeometry(QtCore.QRect(int(0.1*w), int(0.2*h), int(0.8*w), int(0.5*h)))
        self.ReselectDialog.ReselectTable.setObjectName("ReselectTable")
        self.ReselectDialog.ReselectTable.setColumnCount(len(self.Saltfilename))
        self.ReselectDialog.ReselectTable.setRowCount(1)
        self.ReselectDialog.ReselectTable.setVerticalHeaderLabels(['Salt'])
        self.ReselectDialog.ReselectTable.setHorizontalHeaderLabels(['{}'.format(i) for i in range(1, self.numCycle+1)])
        
        header = self.ReselectDialog.ReselectTable.horizontalHeader()
        for i in range(self.ReselectDialog.ReselectTable.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.ReselectDialog.ReselectTable.verticalHeader()
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.ReselectDialog.ReselectTable.setItem(i, j, item)

    def Salt_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.Salt_checkReselectTable)
        
    def Salt_checkReselectTable(self):
        for j in range(self.ReselectDialog.ReselectTable.columnCount()):
            item = self.ReselectDialog.ReselectTable.item(0,j)
            if item.checkState() == QtCore.Qt.Unchecked:
                self.mask[j] = 0
            else:
                self.mask[j] = 1
            
        # set the cell of the table of the Salt statistics
        self.Salt_statistics_result = Utilities.REgetSaltStatistics(self.Saltfilename,self.mask,self.salt)
        for i in range(4):
            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.Salt_statistics_result[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.SaltStatPage.tableWidget.setItem(0, i, item)
            
        # set image
        self.SaltStatPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/Salt.png"))
            
        # show the page
        self.TableAdjust(self.SaltStatPage.tableWidget)    
        
    def SSC_save(self):
        # save statistics
        if(self.salt == 36):
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Salt Statistics result" , self.data_folder+'Statistics/Salt/[36Ar37Ar]Ca/', "(*.csv)")
        elif(self.salt == 39):    
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Salt Statistics result" , self.data_folder+'Statistics/Salt/[39Ar37Ar]Ca/', "(*.csv)")
        elif(self.salt == 40):    
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Salt Statistics result" , self.data_folder+'Statistics/Salt/[40Ar39Ar]K/', "(*.csv)")
        elif(self.salt == 38):    
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Salt Statistics result" , self.data_folder+'Statistics/Salt/[38Ar39Ar]K/', "(*.csv)")
        elif(self.salt == 37):    
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Salt Statistics result" , self.data_folder+'Statistics/Salt/[39Ar37Ar]K/', "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Avg,STD,Wmean,Wmean STD\n")
            f.writelines(["{},{},{},{}\n".format(self.Salt_statistics_result[0], self.Salt_statistics_result[1], self.Salt_statistics_result[2], self.Salt_statistics_result[3])])
            f.close()

    # methods for T0 Calculation Page
    # ===============================================================================
    def toTS(self):             
        self.widget.setCurrentIndex(7)

    def toLRP_MB(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0",
                                                            self.rawpath+"/MB/", "")  # select file
        self.rawfilename = fdilename.replace(self.rawpath+"/MB/", '')
        if len(filename) > 0:
            self.T0type = 'MB'
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable()  # setup the reselect table here

            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return

            self.T0_fitting_function = 0  # default fitting function is linear
            self.mask = np.ones((5, self.numCycle))  # 1 means select this data point

            result,self.mask = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)  # make LRP
            for i in range(5):
                for j in range(self.numCycle):
                    if self.mask[i,j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(i,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
            [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:]
            self.T0CalculationPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/LR.png"))  # set image in the page
            self.T0CalculationPage.current_fit_func.setText(
                "Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)

    def toLRP_PBa(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0",
                                                            self.rawpath+"/PBa/", "")  # select file
        self.rawfilename = filename.replace(self.rawpath+'/PBa/', '')

        if len(filename) > 0:
            self.T0type = 'PBa'
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable()  # setup the reselect table here

            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return

            self.T0_fitting_function = 0  # default fitting function is linear
            self.mask = np.ones((5, self.numCycle))  # 1 means select this data point

            result,self.mask = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)  # make LRP
            for i in range(5):
                for j in range(self.numCycle):
                    if self.mask[i,j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(i,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
            [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:]
            self.T0CalculationPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/LR.png"))  # set image in the page
            self.T0CalculationPage.current_fit_func.setText(
                "Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)

    def toLRP_AS(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0",
                                                            self.rawpath+"/AS/", "")  # select file
        self.rawfilename = filename.replace(self.rawpath+'/AS/', '')

        if len(filename) > 0:
            self.T0type = 'AS'
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable()  # setup the reselect table here

            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return

            self.T0_fitting_function = 0  # default fitting function is linear
            self.mask = np.ones((5, self.numCycle))  # 1 means select this data point

            result,self.mask = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)  # make LRP
            for i in range(5):
                for j in range(self.numCycle):
                    if self.mask[i,j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(i,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
            [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:]
            self.T0CalculationPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/LR.png"))  # set image in the page
            self.T0CalculationPage.current_fit_func.setText(
                "Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)

    def toLRP_PBs(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0",
                                                            self.rawpath+"/PBs/", "")  # select file
        self.rawfilename = filename.replace(self.rawpath+'/PBs/', '')

        if len(filename) > 0:
            self.T0type = 'PBs'
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable()  # setup the reselect table here

            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return

            self.T0_fitting_function = 0  # default fitting function is linear
            self.mask = np.ones((5, self.numCycle))  # 1 means select this data point

            result,self.mask = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)  # make LRP
            for i in range(5):
                for j in range(self.numCycle):
                    if self.mask[i,j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(i,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
            [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:]
            self.T0CalculationPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/LR.png"))  # set image in the page
            self.T0CalculationPage.current_fit_func.setText(
                "Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)

    def toLRP_SP(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0",
                                                           self.rawpath+"/Sample/", "")  # select file

        if len(filename) > 0:
            self.T0type = 'Sample'
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable()  # setup the reselect table here

            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return
                     
            self.T0_fitting_function = 0  # default fitting function is linear
            self.mask = np.ones((5, self.numCycle))  # 1 means select this data point

            result,self.mask = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)  # make LRP
            for i in range(5):
                for j in range(self.numCycle):
                    if self.mask[i,j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(i,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
            [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:]
            self.T0CalculationPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/LR.png"))  # set image in the page
            self.T0CalculationPage.current_fit_func.setText(
                "Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)

    def toLRP_TP(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0",
                                                            self.rawpath+"/Standerd/", "")  # select file

        if len(filename) > 0:
            self.T0type = 'Standerd'
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable()  # setup the reselect table here

            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return

            self.T0_fitting_function = 0  # default fitting function is linear
            self.mask = np.ones((5, self.numCycle))  # 1 means select this data point

            result,self.mask = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)  # make LRP
            for i in range(5):
                for j in range(self.numCycle):
                    if self.mask[i,j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(i,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
            [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:]
            self.T0CalculationPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/LR.png"))  # set image in the page
            self.T0CalculationPage.current_fit_func.setText(
                "Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)
            
    def toLRP_ST(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0",
                                                            self.rawpath+"/Salt/", "")  # select file

        if len(filename) > 0:
            self.T0type = 'Salt'
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable()  # setup the reselect table here

            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return

            self.T0_fitting_function = 0  # default fitting function is linear
            self.mask = np.ones((5, self.numCycle))  # 1 means select this data point

            result,self.mask = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)  # make LRP
            for i in range(5):
                for j in range(self.numCycle):
                    if self.mask[i,j] == 0:
                        item = self.ReselectDialog.ReselectTable.item(i,j)
                        item.setCheckState(QtCore.Qt.Unchecked)
            [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:]
            self.T0CalculationPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/LR.png"))  # set image in the page
            self.T0CalculationPage.current_fit_func.setText(
                "Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)
            
    def LRP_loadRawData(self, filename):
        try:
            with open(filename, 'r') as f:
                data = f.readlines()

            # find the starting line of meaningful data
            for i in reversed(range(len(data))):
                stl = i
                if len(data[i].split()) == 4:
                    break
            stl -= (6*self.numCycle-2)

            # extract the data
            self.info = [0,0,0,0,0]
            if (data[2].rstrip()) == "": #R
                self.info[0] = ((data[17].split())[2])+" "+((data[4].split())[3])
                self.info[1] = ((data[18].split())[2])
                self.info[2] = ((data[0].split())[1])
                self.info[3] = ((data[21].split())[2])
                self.info[4] = ((data[23].split())[2])
            else: #SH
                self.info[0] = ((data[15].split())[2])
                self.info[1] = ((data[16].split())[2])
                self.info[2] = ((data[0].split())[1])
                self.info[3] = ((data[19].split())[2])
                self.info[4] = ((data[21].split())[2])
            self.v_t = np.zeros((5, self.numCycle, 2))
            for i in range(self.numCycle):
                for j in range(5):
                    self.v_t[j, i, 0] = float((data[stl + 6*i + j].split())[2])
                    self.v_t[j, i, 1] = float((data[stl + 6*i + j].split())[3])
            return 1

        except:
            self.Popup(2, "Error!", "Please check the selected data format or the parameter numCycle!")
            return 0


    def LRP_save(self):
        pn = self.work_dir+self.screenshot_folder+'T0/'+self.T0type+'/'
        sn = self.data_folder+'T0/'+self.T0type+'/'
        # save screenshot
        if self.T0type == 'MB' or self.T0type == 'PBa' or self.T0type == 'AS' or self.T0type == 'PBs':
            shutil.copyfile(self.work_dir + '.work/LR.png', pn+self.rawfilename+'.png')
            f = open(sn+self.rawfilename+'.csv', 'w')
            f.write("Samp#,Min,T,Date,iradiation PK 90%,Mass,T0,T0_SIGMA,R^2\n")
            f.writelines(["{},{},{},{},{},Ar{},{},{},{}\n".format(self.info[0],self.info[1],self.info[2],self.info[3],self.info[4],i+36, self.tmp_T0[i], self.tmp_T0_SIGMA[i], self.R[i]) for i in range(5)])
            f.close()
            self.toast.show()
        else:    
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0 Calculation result" , pn, "Images (*.png *.jpg *.jpeg)")
            if len(filename) > 0:
                shutil.copyfile(self.work_dir + '.work/LR.png', filename)

            # save T0
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0 Calculation result" , sn, "(*.csv)")
            if len(filename) > 0:
                f = open(filename, 'w')
                f.write("Samp#,Min,T,Date,iradiation PK 90%,Mass,T0,T0_SIGMA,R^2\n")
                f.writelines(["{},{},{},{},{},Ar{},{},{},{}\n".format(self.info[0],self.info[1],self.info[2],self.info[3],self.info[4],i+36, self.tmp_T0[i], self.tmp_T0_SIGMA[i], self.R[i]) for i in range(5)])
                f.close()
                
    def LRP_setReselectTable(self):
        w = self.ReselectDialog.frameGeometry().width()
        h = self.ReselectDialog.frameGeometry().height()
        self.ReselectDialog.ReselectTable = QtWidgets.QTableWidget(self.ReselectDialog)
        self.ReselectDialog.ReselectTable.setGeometry(QtCore.QRect(int(0.1*w), int(0.2*h), int(0.8*w), int(0.5*h)))
        self.ReselectDialog.ReselectTable.setObjectName("ReselectTable")
        self.ReselectDialog.ReselectTable.setColumnCount(self.numCycle)
        self.ReselectDialog.ReselectTable.setRowCount(5)
        self.ReselectDialog.ReselectTable.setVerticalHeaderLabels(['Ar {}'.format(i) for i in range(36, 41)])
        self.ReselectDialog.ReselectTable.setHorizontalHeaderLabels(['{}'.format(i) for i in range(1, self.numCycle+1)])
        
        header = self.ReselectDialog.ReselectTable.horizontalHeader()
        for i in range(self.ReselectDialog.ReselectTable.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.ReselectDialog.ReselectTable.verticalHeader()
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.ReselectDialog.ReselectTable.setItem(i, j, item)

    def LRP_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.LRP_checkReselectTable)

    def LRP_checkReselectTable(self):
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = self.ReselectDialog.ReselectTable.item(i, j)
                if item.checkState() == QtCore.Qt.Unchecked:
                    self.mask[i, j] = 0
                else:
                    self.mask[i, j] = 1

        result = Utilities.REcalculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle)
        [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:4]
        self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
        self.ReselectDialog.close()

        if result[0] == 1:
            self.Popup(2, "Fitting Error!", "Unable to fit the manually selected data with {} fucntion!".format(self.fitting_function_list[self.T0_fitting_function]))

    def LRP_useLinear(self):
        self.LRP_switch_fitting_func(0)
    
    def LRP_useAverage(self):
        self.LRP_switch_fitting_func(1)

    def LRP_switch_fitting_func(self, fit_func_type):
        
        self.T0_fitting_function = fit_func_type
        result = Utilities.REcalculateT0(self.T0_fitting_function, self.v_t, self.mask,self.numCycle) # make LRP
        [self.tmp_T0, self.tmp_T0_SIGMA, self.R] = result[1:4]
        self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
        self.T0CalculationPage.current_fit_func.setText("Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

        if result[0] == 1:
            self.Popup(2, "Fitting Error!", "Unable to fit the data with {} fucntion after manually removing the outliers!".format(self.fitting_function_list[self.T0_fitting_function]))
    
    # methods for Diagram Plots Page
    # ===============================================================================
    def toDS(self):             
        self.widget.setCurrentIndex(14)
    
    def toDF_LS(self):
        self.Dfilename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select Datum file (csv)" , self.data_folder+"Publish/", "(*.csv)")
        if len(self.Dfilename) > 0:
            
                self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])
                with open(self.Dfilename, 'r') as f:
                    self.data = f.readlines()
                if self.data[0].rstrip() != "Samp#,Min,IRR,deg C,J,J_std,J_int,36Ar(a),36Ar(a)_std,37Ar(ca),37Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,40Ar(r),40Ar(r)_std,Age(Ma),Age_std(Ma),40Ar(r)(%),39Ar(k)(%),40Ar(r)(%)(step heating),39Ar(k)(%)(step heating),K/Ca,K/Ca_std,Degassing Patterns,36Ar(a),36Ar(a)_std,36Ar(c),36Ar(c)_std,36Ar(ca),36Ar(ca)_std,36Ar(cl),36Ar(cl)_std,37Ar(ca),37Ar(ca)_std,38Ar(a),38Ar(a)_std,38Ar(c),38Ar(c)_std,38Ar(k),38Ar(k)_std,38Ar(ca),38Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,39Ar(ca),39Ar(ca)_std,40Ar(r),40Ar(r)_std,40Ar(a),40Ar(a)_std,40Ar(c),40Ar(c)_std,40Ar(k),40Ar(k)_std,Additional Parameters,40(r)/39(k),40(r)/39(k)_std,40(r+a),40(r+a)_std,40Ar/39Ar,40Ar/39Ar_std,37Ar/39Ar,37Ar/39Ar_std,36Ar/39Ar,36Ar/39Ar_std,Parameters,39Ar/37Ar(ca),39Ar/37Ar(ca)_std,36Ar/37Ar(ca),36Ar/37Ar(ca)_std,40Ar/39Ar(k),40Ar/39Ar(k)_std,38Ar/39Ar(k),38Ar/39Ar(k)_std,36Ar/38Ar(cl),36Ar/38Ar(cl)_std,40Ar/36Ar(a),40Ar/36Ar(a)_std,38Ar/36Ar(a),38Ar/36Ar(a)_std,?,numCycle":
                    raise Exception("Wrong data format!")
                j = 0
                for i in range (len(self.data)-2):
                    if float(self.data[i+1-j].split(',')[46])/float(self.data[i+1-j].split(',')[7]) < 0 or float(self.data[i+1-j].split(',')[61])/float(self.data[i+1-j].split(',')[7]) < 0 :
                        self.data.pop(i-j)
                        j=j+1  
                    if self.data[i+1-j].split(',')[17] == "nan":
                        self.data.pop(i-j)
                        j=j+1    
                
                self.DF_setReselectTable()  # setup the reselect table here
                self.mask = np.ones(len(self.data)-2)
                self.DF_result = Utilities.getDFStatistics_ls(self.Dfilename, self.mask, self.parameters, 'r','o')
                Utilities.getDFStatistics_t(self.Dfilename, self.mask,self.power)
                
                for i in range(3):
                    item = QtWidgets.QTableWidgetItem('{}'.format(self.data[1].split(',')[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.DiagramPlots_LSPage.tableWidget.setItem(0, i, item)  
                    
                for i in range(2):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(float(self.data[1].split(',')[4+i])))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.DiagramPlots_LSPage.tableWidget.setItem(0, i+3, item)    
                
                for i in range(8):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.DF_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.DiagramPlots_LSPage.tableWidget.setItem(0, i+5, item)
                    
                self.DiagramPlots_LSPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFN.png"))  # set image in the page    
                self.pname = "DFN"
                self.TableAdjust(self.DiagramPlots_LSPage.tableWidget)
                
                self.widget.setCurrentIndex(16)
                f.close()
                
    def show_LS(self):
        self.DLSC = self.DiagramPlots_LSPage.box.currentText()
        self.DLSS = self.DiagramPlots_LSPage.box2.currentText()
        Utilities.getDFStatistics_ls(self.Dfilename, self.mask, self.parameters, self.DLSC, self.DLSS)
        if(self.pname == "DFN"):
            self.DiagramPlots_LSPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFN.png"))  # set image in the page    
            self.pname = "DFN"
            self.TableAdjust(self.DiagramPlots_LSPage.tableWidget)
        if(self.pname == "DFI"):
            self.DiagramPlots_LSPage.photo.setPixmap(
                    QtGui.QPixmap(self.work_dir + ".work/DFI.png"))  # set image in the page 
            self.pname = "DFI"
       
    def toDF_SH(self):
        self.Dfilename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select Datum file (csv)" , self.data_folder+"Publish/", "(*.csv)")
        if len(self.Dfilename) > 0:
            
                self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])
                with open(self.Dfilename, 'r') as f:
                    self.data = f.readlines()
                if self.data[0].rstrip() != "Samp#,Min,IRR,deg C,J,J_std,J_int,36Ar(a),36Ar(a)_std,37Ar(ca),37Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,40Ar(r),40Ar(r)_std,Age(Ma),Age_std(Ma),40Ar(r)(%),39Ar(k)(%),40Ar(r)(%)(step heating),39Ar(k)(%)(step heating),K/Ca,K/Ca_std,Degassing Patterns,36Ar(a),36Ar(a)_std,36Ar(c),36Ar(c)_std,36Ar(ca),36Ar(ca)_std,36Ar(cl),36Ar(cl)_std,37Ar(ca),37Ar(ca)_std,38Ar(a),38Ar(a)_std,38Ar(c),38Ar(c)_std,38Ar(k),38Ar(k)_std,38Ar(ca),38Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,39Ar(ca),39Ar(ca)_std,40Ar(r),40Ar(r)_std,40Ar(a),40Ar(a)_std,40Ar(c),40Ar(c)_std,40Ar(k),40Ar(k)_std,Additional Parameters,40(r)/39(k),40(r)/39(k)_std,40(r+a),40(r+a)_std,40Ar/39Ar,40Ar/39Ar_std,37Ar/39Ar,37Ar/39Ar_std,36Ar/39Ar,36Ar/39Ar_std,Parameters,39Ar/37Ar(ca),39Ar/37Ar(ca)_std,36Ar/37Ar(ca),36Ar/37Ar(ca)_std,40Ar/39Ar(k),40Ar/39Ar(k)_std,38Ar/39Ar(k),38Ar/39Ar(k)_std,36Ar/38Ar(cl),36Ar/38Ar(cl)_std,40Ar/36Ar(a),40Ar/36Ar(a)_std,38Ar/36Ar(a),38Ar/36Ar(a)_std,?,numCycle":
                    raise Exception("Wrong data format!")
                j = 0
                for i in range (len(self.data)-2):
                    if self.data[i+1-j].split(',')[17] == "nan":
                        self.data.pop(i-j)
                        j=j+1    
                
                self.DF_setReselectTable()  # setup the reselect table here
                self.mask = np.ones(len(self.data)-2)
                self.DF_result = Utilities.getDFStatistics_sh(self.Dfilename, self.mask, self.parameters,'r','o')
                self.sh_result = Utilities.getSHStatistics(self.Dfilename, self.mask, self.parameters)
                
                for i in range(3):
                    item = QtWidgets.QTableWidgetItem('{}'.format(self.data[1].split(',')[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.DiagramPlots_SHPage.tableWidget.setItem(0, i, item)  
                    
                for i in range(2):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(float(self.data[1].split(',')[4+i])))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.DiagramPlots_SHPage.tableWidget.setItem(0, i+3, item)    
                
                for i in range(2):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.sh_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.DiagramPlots_SHPage.tableWidget.setItem(0, i+5, item)
                
                for i in range(8):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.DF_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.DiagramPlots_SHPage.tableWidget.setItem(0, i+7, item)
                    
                self.DiagramPlots_SHPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFN.png"))  # set image in the page    
                self.pname = "DFN"
                self.TableAdjust(self.DiagramPlots_SHPage.tableWidget)
                
                self.widget.setCurrentIndex(15)
                f.close()

    def show_SH(self):
        self.DHSC = self.DiagramPlots_SHPage.box.currentText()
        self.DHSS = self.DiagramPlots_SHPage.box2.currentText()
        Utilities.getDFStatistics_sh(self.Dfilename, self.mask, self.parameters, self.DHSC, self.DHSS)
        if(self.pname == "DFN"):
            self.DiagramPlots_SHPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFN.png"))  # set image in the page    
            self.pname = "DFN"
            self.TableAdjust(self.DiagramPlots_SHPage.tableWidget)
        if(self.pname == "DFI"):
            self.DiagramPlots_SHPage.photo.setPixmap(
                    QtGui.QPixmap(self.work_dir + ".work/DFI.png"))  # set image in the page 
            self.pname = "DFI"

    def DF_SN(self):
        self.DiagramPlots_LSPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFN.png"))  # set image in the page 
        self.DiagramPlots_SHPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFN.png"))  # set image in the page 
        self.pname = "DFN"

    def DF_SI(self):
        self.DiagramPlots_LSPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFI.png"))  # set image in the page 
        self.DiagramPlots_SHPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFI.png"))  # set image in the page 
        self.pname = "DFI"
        
    def DF_SK(self):
        Utilities.getDFStatistics_t(self.Dfilename, self.mask,self.power)
        self.DiagramPlots_LSPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFK.png"))  # set image in the page 
        self.pname = "DFK"
    
    def submit(self):
        self.power = self.entry.get()
    
    def DF_P(self):
        self.window = Tk()
        self.window.title("Power")
        self.entry = Entry()
        self.entry.pack()
        self.submit = Button(self.window,text="submit",command=self.submit)
        self.submit.pack(side = RIGHT)
        self.window.mainloop()
        
    def DF_SW(self):
        self.DiagramPlots_SHPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFW.png"))  # set image in the page 
        self.pname = "DFW"
        
    def DF_SA(self):
        self.DiagramPlots_SHPage.photo.setPixmap(
                QtGui.QPixmap(self.work_dir + ".work/DFA.png"))  # set image in the page 
        self.pname = "DFA"

    def DFLS_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save DF plot result" , self.screenshot_folder+'Publish/LaserOB/', "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            shutil.copyfile(self.work_dir + '.work/DFN.png', filename)
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save DF plot result" , self.screenshot_folder+'Publish/LaserOB/', "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            shutil.copyfile(self.work_dir + '.work/DFI.png', filename)
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save DF plot result" , self.screenshot_folder+'Publish/LaserOB/', "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            shutil.copyfile(self.work_dir + '.work/DFK.png', filename)
        
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save plot result" , self.data_folder+'Publish/LaserOB/', "(*.csv)")
        if len(file) > 0:
            f = open(file, 'w')
            f.write("Weighted Plateau,Total Fusion Age,39/36 Int,39/36 Int std,36/40 Int,36/40 Int std,MSWD,WMA,Int age,Int age std\n")
            f.write("na,na,")
            for i in range(8):
                f.write("{},".format(self.DF_result[i]))
            f.close()
    
    def DFSH_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save DF plot result" , self.screenshot_folder+'Publish/StepHeating/', "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            shutil.copyfile(self.work_dir + '.work/DFN.png', filename)
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save DF plot result" , self.screenshot_folder+'Publish/StepHeating/', "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            shutil.copyfile(self.work_dir + '.work/DFI.png', filename)
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save DF plot result" , self.screenshot_folder+'Publish/StepHeating/', "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            shutil.copyfile(self.work_dir + '.work/DFW.png', filename)
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save DF plot result" , self.screenshot_folder+'Publish/StepHeating/', "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            shutil.copyfile(self.work_dir + '.work/DFA.png', filename)
            
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save plot result" , self.data_folder+'Publish/StepHeating/', "(*.csv)")
        if len(file) > 0:
            f = open(file, 'w')
            f.write("Weighted Plateau,Total Fusion Age,39/36 Int,39/36 Int std,36/40 Int,36/40 Int std,MSWD,WMA,Int age,Int age std\n")
            for i in range(2):
                f.write("{},".format(self.sh_result[i]))
            for i in range(8):
                f.write("{},".format(self.DF_result[i]))
            f.close()

    def DF_setReselectTable(self):
        w = self.ReselectDialog.frameGeometry().width()
        h = self.ReselectDialog.frameGeometry().height()
        self.ReselectDialog.ReselectTable = QtWidgets.QTableWidget(self.ReselectDialog)
        self.ReselectDialog.ReselectTable.setGeometry(QtCore.QRect(int(0.1*w), int(0.2*h), int(0.8*w), int(0.5*h)))
        self.ReselectDialog.ReselectTable.setObjectName("ReselectTable")
        self.ReselectDialog.ReselectTable.setColumnCount(len(self.data)-2)
        self.ReselectDialog.ReselectTable.setRowCount(1)
        self.ReselectDialog.ReselectTable.setVerticalHeaderLabels(['J'])
        self.ReselectDialog.ReselectTable.setHorizontalHeaderLabels(['{}'.format(i) for i in range(1, self.numCycle+1)])
        
        header = self.ReselectDialog.ReselectTable.horizontalHeader()
        for i in range(self.ReselectDialog.ReselectTable.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.ReselectDialog.ReselectTable.verticalHeader()
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.ReselectDialog.ReselectTable.setItem(i, j, item)

    def LS_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.LS_checkReselectTable)
        
    def LS_checkReselectTable(self):
        for j in range(self.ReselectDialog.ReselectTable.columnCount()):
            item = self.ReselectDialog.ReselectTable.item(0,j)
            if item.checkState() == QtCore.Qt.Unchecked:
                self.mask[j] = 0
            else:
                self.mask[j] = 1
        
        self.DF_result = Utilities.getDFStatistics_ls(self.Dfilename, self.mask, self.parameters)
        Utilities.getDFStatistics_t(self.Dfilename, self.mask,self.power)
                
        for i in range(3):
            item = QtWidgets.QTableWidgetItem('{}'.format(self.data[1].split(',')[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.DiagramPlots_LSPage.tableWidget.setItem(0, i, item)  
            
        for i in range(2):
            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(float(self.data[1].split(',')[4+i])))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.DiagramPlots_LSPage.tableWidget.setItem(0, i+3, item)    
                
        for i in range(8):
            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.DF_result[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.DiagramPlots_LSPage.tableWidget.setItem(0, i+5, item)
        
        # set image
        self.DiagramPlots_LSPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/"+self.pname+".png"))
            
        # show the page
        self.TableAdjust(self.DiagramPlots_LSPage.tableWidget)
    
    def SH_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.SH_checkReselectTable)
        
    def SH_checkReselectTable(self):
        for j in range(self.ReselectDialog.ReselectTable.columnCount()):
            item = self.ReselectDialog.ReselectTable.item(0,j)
            if item.checkState() == QtCore.Qt.Unchecked:
                self.mask[j] = 0
            else:
                self.mask[j] = 1
        
        self.DF_result = Utilities.getDFStatistics_sh(self.Dfilename, self.mask, self.parameters)
        self.sh_result = Utilities.getSHStatistics(self.Dfilename, self.mask, self.parameters)
                
        for i in range(3):
            item = QtWidgets.QTableWidgetItem('{}'.format(self.data[1].split(',')[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.DiagramPlots_SHPage.tableWidget.setItem(0, i, item)  
            
        for i in range(2):
            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(float(self.data[1].split(',')[4+i])))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.DiagramPlots_SHPage.tableWidget.setItem(0, i+3, item)    
                
        for i in range(2):
            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.sh_result[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.DiagramPlots_SHPage.tableWidget.setItem(0, i+5, item)
                
        for i in range(8):
            item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.DF_result[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.DiagramPlots_SHPage.tableWidget.setItem(0, i+7, item)
        
        # set image
        self.DiagramPlots_SHPage.photo.setPixmap(QtGui.QPixmap(self.work_dir+".work/"+self.pname+".png"))
            
        # show the page
        self.TableAdjust(self.DiagramPlots_SHPage.tableWidget)
    
    # methods for Datum Publication Page
    # ===============================================================================
    def toDPS(self):
        self.widget.setCurrentIndex(19)
    
    def toDP(self):
        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get Datum statistics" , self.data_folder+'Agecalc/', "(*.csv)") # select list of files
        if len(filelist) > 0:
            try:
                file, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Datum result" , self.data_folder+'Publish/', "(*.csv)")
                if len(file) > 0:
                    f = open(file, 'w')
                    f.write("Samp#,Min,IRR,deg C,J,J_std,J_int,36Ar(a),36Ar(a)_std,37Ar(ca),37Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,40Ar(r),40Ar(r)_std,Age(Ma),Age_std(Ma),40Ar(r)(%),39Ar(k)(%),40Ar(r)(%)(step heating),39Ar(k)(%)(step heating),K/Ca,K/Ca_std,Degassing Patterns,36Ar(a),36Ar(a)_std,36Ar(c),36Ar(c)_std,36Ar(ca),36Ar(ca)_std,36Ar(cl),36Ar(cl)_std,37Ar(ca),37Ar(ca)_std,38Ar(a),38Ar(a)_std,38Ar(c),38Ar(c)_std,38Ar(k),38Ar(k)_std,38Ar(ca),38Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,39Ar(ca),39Ar(ca)_std,40Ar(r),40Ar(r)_std,40Ar(a),40Ar(a)_std,40Ar(c),40Ar(c)_std,40Ar(k),40Ar(k)_std,Additional Parameters,40(r)/39(k),40(r)/39(k)_std,40(r+a),40(r+a)_std,40Ar/39Ar,40Ar/39Ar_std,37Ar/39Ar,37Ar/39Ar_std,36Ar/39Ar,36Ar/39Ar_std,Parameters,39Ar/37Ar(ca),39Ar/37Ar(ca)_std,36Ar/37Ar(ca),36Ar/37Ar(ca)_std,40Ar/39Ar(k),40Ar/39Ar(k)_std,38Ar/39Ar(k),38Ar/39Ar(k)_std,36Ar/38Ar(cl),36Ar/38Ar(cl)_std,40Ar/36Ar(a),40Ar/36Ar(a)_std,38Ar/36Ar(a),38Ar/36Ar(a)_std,?,numCycle\n")
                    ar36a_sum = 0.0
                    ar37ca_sum = 0.0
                    ar38cl_sum = 0.0
                    ar39k_sum = 0.0
                    ar40r_sum = 0.0
                    ar39k_s_sum = 0.0
                    ar40r_s_sum = 0.0
                    for i, filename in enumerate(filelist):
                        with open(filename, 'r') as d:
                            data = d.readlines()
                        if data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Variable,Value,Sigma":
                            raise Exception("Wrong data format!")
                        ar38cl = float((data[6].split(','))[5]) - float((data[7].split(','))[5]) - float((data[8].split(','))[5])
                        ar36a_sum = float((data[2].split(','))[5]) + ar36a_sum
                        ar37ca_sum = float((data[5].split(','))[5]) + ar37ca_sum
                        ar38cl_sum = ar38cl + ar38cl_sum
                        ar39k_sum = float((data[10].split(','))[5]) + ar39k_sum 
                        ar40r_sum = float((data[13].split(','))[5]) + ar40r_sum
                        ar39k_s_sum = float((data[10].split(','))[5]) / float((data[9].split(','))[5]) + ar39k_s_sum
                        ar40r_s_sum = float((data[27].split(','))[5]) + ar40r_s_sum
                    for i, filename in enumerate(filelist):
                        with open(filename, 'r') as d:
                            data = d.readlines()
                        if data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Variable,Value,Sigma":
                            raise Exception("Wrong data format!")
                        ar36c = 0
                        ar38c = 0
                        ar38ca = 0
                        ar40c = 0
                        ar40r = round(float(data[27].split(',')[5]),4)*100
                        ar39k = round(float((data[10].split(','))[5]) / float((data[9].split(','))[5]),4)*100
                        ar39k_s = round(ar39k/ar39k_s_sum*100,4)
                        ar40r_s = round(float((data[27].split(','))[5])/ar40r_s_sum*100,4)
                        ar38cl = float((data[6].split(','))[5]) - float((data[7].split(','))[5]) - float((data[8].split(','))[5])
                        KCa = (float((data[10].split(','))[5])*0.52)/float((data[5].split(','))[5])
                        KCa_std = (KCa)*(np.sqrt((float((data[10].split(','))[6])/float((data[10].split(','))[5]))**2 + (float((data[5].split(','))[6])/float((data[5].split(','))[5]))**2 + (0.02/0.52)**2))
                        ar36cl = float(self.parameters[self.numParamters[self.parameters_name.index("Production Ratio 38Ar/39Ar(k)")]])*ar38cl
                        ra40 = float((data[13].split(','))[5]) +float((data[14].split(','))[5])
                        ra40_std = float((data[13].split(','))[6]) +float((data[14].split(','))[6])
                        f.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},,{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},,{},{},{},{},{},{},{},{},{},{},,{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                            (data[1].split(','))[0],(data[1].split(','))[2],(data[1].split(','))[3],(data[1].split(','))[1],(data[23].split(','))[5],(data[23].split(','))[6],(data[25].split(','))[5],(data[2].split(','))[5],(data[2].split(','))[6],(data[5].split(','))[5],(data[5].split(','))[6],ar38cl,ar38cl,(data[10].split(','))[5],(data[10].split(','))[6],(data[13].split(','))[5],(data[13].split(','))[6],(float((data[24].split(','))[5])/1000000),(float((data[24].split(','))[6])/1000000),ar40r,ar39k,ar40r_s,ar39k_s,KCa,KCa_std,(data[2].split(','))[5],(data[2].split(','))[6],ar36c,ar36c,(data[3].split(','))[5],(data[3].split(','))[6],ar36cl,ar36cl,(data[5].split(','))[5],(data[5].split(','))[6],(data[7].split(','))[5],(data[7].split(','))[6],ar38c,ar38c,(data[8].split(','))[5],(data[8].split(','))[6],ar38ca,ar38ca,ar38cl,ar38cl,(data[10].split(','))[5],(data[10].split(','))[6],(data[11].split(','))[5],(data[11].split(','))[6],(data[13].split(','))[5],(data[13].split(','))[6],(data[14].split(','))[5],(data[14].split(','))[6],ar40c,ar40c,(data[15].split(','))[5],(data[15].split(','))[6],(data[19].split(','))[5],(data[19].split(','))[6],ra40,ra40_std,(data[20].split(','))[5],(data[20].split(','))[6],(data[22].split(','))[5],(data[22].split(','))[6],(data[21].split(','))[5],(data[21].split(','))[6],
                            self.parameters[self.parameters_name.index("Production Ratio 39Ar/37Ar(ca)")],
                            self.parameters[self.parameters_name.index("Production Ratio 39Ar/37Ar(ca)_std")], 
                            self.parameters[self.parameters_name.index("Production Ratio 36Ar/37Ar(ca)")],
                            self.parameters[self.parameters_name.index("Production Ratio 36Ar/37Ar(ca)_std")],
                            self.parameters[self.parameters_name.index("Production Ratio 40Ar/39Ar(k)")],
                            self.parameters[self.parameters_name.index("Production Ratio 40Ar/39Ar(k)_std")],
                            self.parameters[self.parameters_name.index("Production Ratio 38Ar/39Ar(k)")],
                            self.parameters[self.parameters_name.index("Production Ratio 38Ar/39Ar(k)_std")],
                            self.parameters[self.parameters_name.index("Production Ratio 36Ar/38Ar(cl)")],
                            self.parameters[self.parameters_name.index("Production Ratio 36Ar/38Ar(cl)_std")],
                            self.parameters[self.parameters_name.index("Atmospheric Ratio 40/36(a)")],
                            self.parameters[self.parameters_name.index("Atmospheric Ratio 40/36(a)_std")],
                            self.parameters[self.parameters_name.index("Atmospheric Ratio 38/36(a)")],
                            self.parameters[self.parameters_name.index("Atmospheric Ratio 38/36(a)_std")],
                            self.parameters[self.parameters_name.index("L")],
                
                            #self.parameters[self.parameters_name.index("λ_std for age calculation")],
                            
                            self.parameters[self.parameters_name.index("J int")])
                            )
                    f.write(",,,,,,SUM,{},,{},,{},,{},,{}".format(ar36a_sum,ar37ca_sum,ar38cl_sum,ar39k_s_sum,ar40r_sum))
                    f.close()
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")
                f.close()
                
    def toDPR(self):
        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get Datum statistics" , self.data_folder+'MassRatio/', "(*.csv)") # select list of files
        if len(filelist) > 0:
            try:
                file, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Datum result" , self.data_folder+'Publish/', "(*.csv)")
                if len(file) > 0:
                    f = open(file, 'w')
                    f.write("39/40,err[39/40],36/40,err[36/40],39/36,err[39/36],39,Samp#\n")
                    for i, filename in enumerate(filelist):
                        with open(filename, 'r') as d:
                            data = d.readlines()
                        if data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Mass,Raw,Measurment,Measurement's Sigma,Ratio,Value,Ratio's Sigma":
                            raise Exception("Wrong data format!")
                        ar3940 = float((data[1].split(','))[9])
                        ar3940std = float((data[1].split(','))[10])
                        ar3640 = float((data[2].split(','))[9])
                        ar3640std = float((data[2].split(','))[10])
                        ar3936 = float((data[3].split(','))[9])
                        ar3936std = float((data[3].split(','))[10])
                        ar39 = float((data[4].split(','))[6])
                        f.write("{},{},{},{},{},{},{},{}\n".format(ar3940,ar3940std,ar3640,ar3640std,ar3936,ar3936std,ar39,(data[1].split(','))[0]))
                    f.close()
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")
                f.close()
# main program
# ===============================================================================
ntnu_arar_app = App()
ntnu_arar_app.run()
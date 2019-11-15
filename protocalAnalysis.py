import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow
from PyQt5.QtGui import QTextCursor
from protocalFile import Protocal


protocal = Protocal()  # 自定义Protocal类中定义了各种协议的解析方法
# 定义协议类型与处理方法之间的对应关系字典
protocal_dict = {'1808F456(CML)': protocal.cmlPileMaximumOutputCapability,  # cml充电桩最大输出能力报文
                 '181056F4(BCL)': protocal.bclBatteryChargingDemand,     # bcl电池充电需求报文
                 '1826F456(CHM)': protocal.chmHandshake,     # chm充电机握手报文
                 '182756F4(BHM)': protocal.bhmHandshake,     # BHM车辆握手报文
                 '1801F456(CRM)': protocal.crm_identify,     # CRM充电机辨识报文
                 '100956F4(BRO)': protocal.broCarReadyOk,    # BRO车辆准备就绪报文
                 '100AF456(CRO)': protocal.croChargerReadyOk,   # CRO充电机准备就绪报文
                 '1812F456(CCS)': protocal.ccsChargerState,    # CCS充电机充电状态报文
                 '181356F4(BSM)': protocal.bsmBatteryStatus,    # BSM动力蓄电池状态信息报文
                 'BCS多包数据报文': protocal.bcsMulPackets,      # BCS多包数据报文（2包）
                 '101956F4(BST)': protocal.bstEndCharge,    # BMS中止充电原因报文(BST)
                 '101AF456(CST)': protocal.cstEndCharge,      # 充电机中止充电报文（CST）
                 'BMV多包数据报文': protocal.bmvMulitiPackets,   # 单体动力蓄电池电压报文（BMV)
                 'BCP多包数据报文': protocal.bcpChargePamrameters,   # 动力蓄电池充电参数报文（BCP）
                 'BMT多包数据报文': protocal.bmtMultiPackes,       # 动力蓄电池温度报文（BMT）
                 'BRM多包数据报文': protocal.brmMuitiPackes,         # BMS和车辆辨识报文（BRM）
                 '181C56F4(BSD)': protocal.bsd,       # BMS统计数据报文(BSD)
                 '181DF456(CSD)': protocal.csd,       # 充电机统计数据报文（CSD）
                 '081E56F4(BEM)': protocal.bem,       # 充电机统计数据报文（CSD）
                 '081FF456(CEM)': protocal.cem        # 充电机错误报文（CEM）
                 }


# 界面显示类
class Win_Form(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(Win_Form, self).setupUi(MainWindow)
        #self.cmbx_protocalType.setEditable(True)
        self.pbtn_Analysis.clicked.connect(self.process)
        self.btnClear.clicked.connect(self.clear)

    # 点击解析按钮的槽函数：获取协议类型和数据，利用自定义Protocal类中的方法对协议进行解析
    def process(self):
        type = self.cmbx_protocalType.currentText()     # 获取协议类型
        data = self.txtEdt_protocalData.toPlainText()   # 获取协议数据
        result = protocal_dict[type](data) + '\n'     # 协议解析，在返回对结果上加上回车符
        self.txtEdt_result.append(result)  # 把解析结果显示在界面上
        QApplication.processEvents()
        self.txtEdt_result.moveCursor(QTextCursor.End)  # 让结果显示框的滚动条移动到最底部以显示最新的解析信息。
        QApplication.processEvents()

    # 点击清空按钮的槽函数：清空解析结果框中的内容
    def clear(self):
        self.txtEdt_result.clear()
        QApplication.processEvents()


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()

    ui = Win_Form()
    ui.setupUi(win)

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


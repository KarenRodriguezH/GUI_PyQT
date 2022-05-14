from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2    
#import imutils
#import 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(249, 255, 207);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 551, 311))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Robot1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_Open_Image = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open_Image.setGeometry(QtCore.QRect(610, 120, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Open_Image.setFont(font)
        self.pushButton_Open_Image.setStyleSheet("background-color: rgb(170, 0, 127);\n"
"background-color: rgb(174, 176, 216);")
        self.pushButton_Open_Image.setObjectName("pushButton_Open_Image")
        self.pushButton_Open_Image_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open_Image_2.setGeometry(QtCore.QRect(610, 190, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Open_Image_2.setFont(font)
        self.pushButton_Open_Image_2.setStyleSheet("background-color: rgb(170, 0, 127);\n"
"background-color: rgb(174, 176, 216);")
        self.pushButton_Open_Image_2.setObjectName("pushButton_Open_Image_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())       


        self.retranslateUi(MainWindow)
        self.pushButton_Open_Image.clicked.connect(self.open_image)
        self.pushButton_Open_Image_2.clicked.connect(self.label.clear)
        self.actionOpen.triggered.connect(self.open_image)
        self.actionExit.triggered.connect(self.exitt)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Load image with QFile - access to the path (*.*) all files
    def open_image(self):        
        self.filename = QFileDialog.getOpenFileName(filter= "Image (*.*)")[0] 
        #We need to read the image, so:
        self.image = cv2.imread(self.filename)
        # (1) We need to set the image on the label 
        self.setimage(self.image)  #the image (self.image)

    #(1) Function to show image on the label
    def setimage(self,image): #pass image by parameter      
        self.temp_image = image
        image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))


    def exitt(self):
        sys.exit()   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Open_Image.setText(_translate("MainWindow", "OPEN IMAGE"))
        self.pushButton_Open_Image_2.setText(_translate("MainWindow", "CLEAN"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


#Giovanny Cerna
#Nick Tralongo
#Adrian Ortiz
#cst205 Avner
#3-8-18
#Photo and video editor

import sys

from PIL import Image
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox,
                                QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox,
                                QInputDialog, QFileDialog)
from PyQt5.QtGui import QPixmap, QIcon


#used for combo box
filters = [ "Choose filters: defaut(none)", "Sepia", "negative", "grayscale", "Flip image"]
choices = [ "Sample CSUMB image", "Sample Stanford Image", "Sample Harved Image", "Sample Beach image"]

id = [ "csumb", "stanford", "Harvard",
       "Beach"]
#used for uploaded image
dir = []

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

#where all buttons go
        hbox1 = QHBoxLayout()

#button for option to chose image
        self.my_combo_box2 = QComboBox()
        self.my_combo_box2.addItems(choices)
        hbox1.addWidget(self.my_combo_box2)

        gbox1 = QGroupBox('Edit your photo here')
        gbox1.setLayout(hbox1)

#buttons depending on choice
        self.button = QPushButton('Use Sample', self)
        self.button2 = QPushButton('Upload Own image', self)
        self.button3 = QPushButton('Run Own image', self)

        #filter box
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(filters)
#creates buttons
        hbox1.addWidget(self.button)
        hbox1.addWidget(self.button2)
        hbox1.addWidget(self.button3)
        hbox1.addWidget(self.my_combo_box)

        self.setLayout(hbox1)
        self.title = 'Photo and Video Editor'
        self.left = 200
        self.top = 300
        self.width = 640
        self.height = 480
        self.initUI()

#Button clicked
        self.button3.clicked.connect(self.open2)
        self.button2.clicked.connect(self.run)
        self.button.clicked.connect(self.open)

#inits the buttons
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

#runs file explorer for user upload
    def run(self):
        self.saveFile()

#runs and saves the file uploaded
    def saveFile(self):
        option = QFileDialog.Options()
        option |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=option)
#saves file directory and appends it to the dir dictionary
        if fileName:
            dir.append(fileName)

#sets windows
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
#opens the image in a new window
        self.show()

#opens images
    def open(self):
#image is the picture from the samples
        image = Image.open("images/" + id[self.my_combo_box2.currentIndex()] + ".jpg")

#filters
        if(self.my_combo_box.currentIndex() == 0 ):
            image.save('pic.jpg')

        elif (self.my_combo_box.currentIndex() == 1 ):
            self.sepia_list = map(lambda a : self.sepia(a) , image.getdata())
            image.putdata(list(self.sepia_list))
            image.save('pic.jpg')

        elif(self.my_combo_box.currentIndex() == 2 ):
            negative_list = map(lambda a : (255 - a[0], 255 - a[1], 255 - a[2]) , image.getdata())
            image.putdata(list(negative_list))
            image.save('pic.jpg')

        elif (self.my_combo_box.currentIndex() == 3 ):
            grayscale_list = map(lambda a : (int((a[0] + a[1] + a[2]) /3),)*3 , image.getdata())
            image.putdata(list(grayscale_list))
            image.save('pic.jpg')

        elif (self.my_combo_box.currentIndex() == 4 ):
            flip = image.rotate(180)
            flip.save('pic.jpg')

#opens pic in another window
        self.new_win = QWidget()

        new_lb = QLabel(self.new_win)
        pixmap = QPixmap("pic.jpg")

        new_lb .setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()

    #opens2 is the user uploaded image

    def open2(self):
#saves uploaded user image as image
        image = Image.open(dir[0])

    #filters
        if(self.my_combo_box.currentIndex() == 0 ):
                image.save('user.jpg')

        elif (self.my_combo_box.currentIndex() == 1 ):
                self.sepia_list = map(lambda a : self.sepia(a) , image.getdata())
                image.putdata(list(self.sepia_list))
                image.save('user.jpg')

        elif(self.my_combo_box.currentIndex() == 2 ):
            negative_list = map(lambda a : (255 - a[0], 255 - a[1], 255 - a[2]) , image.getdata())
            image.putdata(list(negative_list))
            image.save('user.jpg')

        elif (self.my_combo_box.currentIndex() == 3 ):
            grayscale_list = map(lambda a : (int((a[0] + a[1] + a[2]) /3),)*3 , image.getdata())
            image.putdata(list(grayscale_list))
            image.save('user.jpg')

        elif (self.my_combo_box.currentIndex() == 4):
            flip = image.rotate(180)
            flip.save('user.jpg')

    #opens pic in another window
        self.new_win = QWidget()
        new_lb = QLabel(self.new_win)
        pixmap = QPixmap("user.jpg")
        new_lb .setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()


#sepia filter
    def sepia(self,a):
         if a[0] < 63:
             r,g,b = int(a[0] * 1.1), a[1], int(a[2] * 0.9)
         elif a[0] > 62 and a[0] < 192:
             r,g,b = int(a[0] * 1.15), a[1], int(a[2] * 0.85)
         else:
             r = int(a[0] * 1.08)
             if r > 255:
                 r = 255
             g,b = a[1], int(a[2] * 0.5)

         return r, g, b

app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())

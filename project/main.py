#Giovanny Cerna
#Nick Tralongo
#Adrian Ortiz
#cst205 Avner
#3-8-18
#Photo and video editor

import sys
import numpy as np
import cv2

from PIL import Image
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox,
                                QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox,
                                QInputDialog, QFileDialog, QSlider, QSizePolicy, QStyle, QMainWindow, QAction)
from PyQt5.QtGui import QPixmap, QIcon


#used for combo box
combo = [ "Choose filters: defaut(none)", "Sepia", "negative", "grayscale", "Flip image"]
choices = [ "Sample CSUMB image", "Sample Stanford Image", "Sample Harved Image", "Sample Beach image"]
Videos = [ "Sample car video", "Sample fish video", "Sample clouds video", "Sample sand video"]
filt = [ "Choose filters: defaut(none)", "Sepia", "negative", "grayscale", "Flip video"]

id = [ "csumb", "stanford", "Harvard", "Beach"]
cd = [ "car", "fish", "clouds", "sand"]
#used for uploaded image
dir = []

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
#creates section for photos
        hbox1 = QHBoxLayout()
#button for option to choose image
        self.pic_combo_box2 = QComboBox()
        self.pic_combo_box2.addItems(choices)
        hbox1.addWidget(self.pic_combo_box2)

#buttons depending on choice
        self.button = QPushButton('Use Sample', self)
        self.button2 = QPushButton('Upload Your Own Image', self)
        self.button3 = QPushButton('Run Your Own Image', self)
        hbox1.addWidget(self.button)
        hbox1.addWidget(self.button2)
        hbox1.addWidget(self.button3)

#filter box
        self.pic_combo_box = QComboBox()
        self.pic_combo_box.addItems(combo)

        hbox1.addWidget(self.pic_combo_box)

        gbox1 = QGroupBox('Edit Photos Here')
        gbox1.setLayout(hbox1)


#creates a second section for videos
        hbox2 = QHBoxLayout()
#button for option to choose an image
        self.vid_combo_box = QComboBox()
        self.vid_combo_box.addItems(Videos)
        hbox2.addWidget(self.vid_combo_box)

#buttons depending on choice
        self.b = QPushButton('Use Sample', self)
        self.b2 = QPushButton('Upload Your Own Video', self)
        self.b3 = QPushButton('Run Your Own Video', self)
        hbox2.addWidget(self.b)
        hbox2.addWidget(self.b2)
        hbox2.addWidget(self.b3)

#filter box
        self.vid_combo_box2 = QComboBox()
        self.vid_combo_box2.addItems(filt)
        hbox2.addWidget(self.vid_combo_box2)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox2)

        gbox2 = QGroupBox("Edit Videos Here")
        gbox2.setLayout(vbox)

        mbox = QVBoxLayout()
        mbox.addWidget(gbox1)
        mbox.addWidget(gbox2)

        self.setLayout(mbox)
        self.title = 'Photo and Video Editor'
        self.left = 200
        self.top = 300
        self.width = 640
        self.height = 480
        self.initUI()
#Button clicked
        self.button3.clicked.connect(self.openIm2)
        self.button2.clicked.connect(self.run)
        self.button.clicked.connect(self.openIm)

        # self.b3.clicked.connect(self.openVid2)
        # self.b2.clicked.connect(self.run)
        # self.b.clicked.connect(self.openVid)
#inits the buttons
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
#runs file explorer for user upload
    def run(self):
        self.saveFileDialog()
#runs and saves the file uploaded
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
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
    def openIm(self):
#image is the picture from the samples
        image = Image.open("images/" + id[self.pic_combo_box2.currentIndex()] + ".jpg")

#if statements for filters
        if(self.pic_combo_box.currentIndex() == 0 ):
            image.save('pic.jpg')
        elif (self.pic_combo_box.currentIndex() == 1 ):
            self.sepia_list = map(lambda a : self.sepia(a) , image.getdata())
            image.putdata(list(self.sepia_list))
            image.save('pic.jpg')

        elif(self.pic_combo_box.currentIndex() == 2 ):
            negative_list = map(lambda a : (255 - a[0], 255 - a[1], 255 - a[2]) , image.getdata())
            image.putdata(list(negative_list))
            image.save('pic.jpg')

        elif (self.pic_combo_box.currentIndex() == 3 ):
            grayscale_list = map(lambda a : (int((a[0] + a[1] + a[2]) /3),)*3 , image.getdata())
            image.putdata(list(grayscale_list))
            image.save('pic.jpg')
        elif (self.pic_combo_box.currentIndex() == 4 ):
            flip = image.rotate(180)
            flip.save('pic.jpg')

#opens image in new window
        self.new_win = QWidget()

        new_lb = QLabel(self.new_win)
        pixmap = QPixmap("pic.jpg")

        new_lb .setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()

#openIm2 is the user uploaded image

    def openIm2(self):
#saves uploaded user image as image
        image = Image.open(dir[0])
#statements are for filters
        if(self.pic_combo_box.currentIndex() == 0 ):
                image.save('user.jpg')
        elif (self.pic_combo_box.currentIndex() == 1 ):
                self.sepia_list = map(lambda a : self.sepia(a) , image.getdata())
                image.putdata(list(self.sepia_list))
                image.save('user.jpg')

        elif(self.pic_combo_box.currentIndex() == 2 ):
            negative_list = map(lambda a : (255 - a[0], 255 - a[1], 255 - a[2]) , image.getdata())
            image.putdata(list(negative_list))
            image.save('user.jpg')

        elif (self.pic_combo_box.currentIndex() == 3 ):
            grayscale_list = map(lambda a : (int((a[0] + a[1] + a[2]) /3),)*3 , image.getdata())
            image.putdata(list(grayscale_list))
            image.save('user.jpg')
        elif (self.pic_combo_box.currentIndex() == 4):
            flip = image.rotate(180)
            flip.save('user.jpg')

#opens image in new window and saves it
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

class Video(QMainWindow):

    def __init__(self, parent=None):
        super(Video, self).__init__(parent)
        self.setWindowTitle("Video Editor")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
# slider
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

# Upload video
        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.openFile)

# Exit video
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

# Menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

# Window content
        wid = QWidget(self)
        self.setCentralWidget(wid)

# Layouts for widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = Video()
    player.resize(1240, 880)
    player.show()
    sys.exit(app.exec_())

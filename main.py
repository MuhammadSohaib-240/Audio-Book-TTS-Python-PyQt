# IMPORTING PACKAGES/MODULES
import sys
import pyttsx3
import threading
import cv2

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QCursor
from PyQt6.uic import loadUi

# DECLARING GLOBAL VARIABLES
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Initial voice speed
voices = engine.getProperty('voices')  # Getting voiced from pyttsx3 engine
voice_array = ["Microsoft David (Male - American Accent)", "Microsoft Zara (Female - American Accent)"]


# MAIN WINDOW
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('main.ui', self)

        # EVENTS
        self.play_button.clicked.connect(self.play_audio_book)  # Play button click event
        self.speed_slider.valueChanged.connect(self.change_speed)  # Speed slider value change event
        self.voices_combo_box.addItems(voice_array)  # Adding voices to combo-box

    # PLAY AUDIO BOOK BUTTON
    def play_audio_book(self):
        x = threading.Thread(target=self.play)
        x.start()

    def play(self):
        self.play_button.setEnabled(False)
        self.speed_slider.setEnabled(False)
        self.play_button.setCursor(QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        voice_text = str(self.voices_combo_box.currentText())
        if voice_text == "Microsoft David (Male - American Accent)":
            engine.setProperty('voice', voices[0].id)

        elif voice_text == "Microsoft Zara (Female - American Accent)":
            engine.setProperty('voice', voices[1].id)
        text = self.text.toPlainText()
        engine.say(text)
        engine.runAndWait()
        self.play_button.setEnabled(True)
        self.speed_slider.setEnabled(True)

    # CHANGING SPEED SLIDER
    def change_speed(self):
        speed = self.speed_slider.value()
        self.speed_number.setText(str(speed))
        engine.setProperty('rate', speed)


# MAIN
if __name__ == '__main__':
    '''=======================>
        CREATING WINDOW
    ==========================>'''
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(400)
    widget.setFixedWidth(500)
    widget.setWindowTitle("Audio Book")
    widget.show()
    app.exec()

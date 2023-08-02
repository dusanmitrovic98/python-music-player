import sys
import os
import configparser
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSlider, QPushButton, QFileDialog, QListWidget, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QUrl, QTime, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setStyleSheet(
            "background-color: #1c1c1c; color: #f0f0f0; selection-color: #f0f0f0; selection-background-color: #444444;")

        self.mediaPlayer = QMediaPlayer(self)
        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.play_music)

        self.pauseButton = QPushButton("Pause")
        self.pauseButton.clicked.connect(self.pause_or_resume_music)

        self.stopButton = QPushButton("Stop")
        self.stopButton.clicked.connect(self.stop_music)

        self.addButton = QPushButton("+")
        self.addButton.setFixedSize(25, 25)
        self.addButton.clicked.connect(self.add_music)

        self.removeButton = QPushButton("-")
        self.removeButton.setFixedSize(25, 25)
        self.removeButton.clicked.connect(self.remove_music)

        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.clear_list)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)

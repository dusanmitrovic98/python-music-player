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

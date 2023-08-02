import sys
import os
import configparser
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSlider, QPushButton, QFileDialog, QListWidget, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QUrl, QTime, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class MusicPlayer(QWidget):

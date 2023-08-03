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
        self.volumeSlider.setValue(50)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setTickPosition(QSlider.TicksAbove)
        self.volumeSlider.setStyleSheet(
            "QSlider::groove:horizontal {background: #444444; height: 8px; border-radius: 4px;}"
            "QSlider::sub-page:horizontal {background: #bb86fc; height: 8px; border-radius: 4px;}"
            "QSlider::handle:horizontal {background: #bb86fc; width: 14px; border: 1px solid #444; border-radius: 8px;}"
            "QSlider::handle:horizontal:hover {background: #f0f0f0; border: 1px solid #444; border-radius: 8px;}"
            "QSlider::sub-page:horizontal:disabled {background: #666666; border-color: #999;}"
            "QSlider::handle:horizontal:disabled {background: #666666; border: 1px solid #444; border-radius: 8px;}"
        )
        self.volumeSlider.valueChanged.connect(self.change_volume)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setMinimum(0)
        self.positionSlider.setMaximum(0)
        self.positionSlider.setSingleStep(1000)
        self.positionSlider.setStyleSheet(
            "QSlider::groove:horizontal {background: #444444; height: 8px; border-radius: 4px;}"
            "QSlider::sub-page:horizontal {background: #bb86fc; height: 8px; border-radius: 4px;}"
            "QSlider::handle:horizontal {background: #bb86fc; width: 14px; border: 1px solid #444; border-radius: 8px;}"
            "QSlider::handle:horizontal:hover {background: #f0f0f0; border: 1px solid #444; border-radius: 8px;}"
            "QSlider::sub-page:horizontal:disabled {background: #666666; border-color: #999;}"
            "QSlider::handle:horizontal:disabled {background: #666666; border: 1px solid #444; border-radius: 8px;}"
        )
        self.positionSlider.sliderPressed.connect(self.pause_music)
        self.positionSlider.sliderReleased.connect(self.update_position)

        self.musicList = QListWidget()

        self.timeLabel = QLabel("00:00 / 00:00")
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.statusLabel = QLabel()

        self.config = configparser.ConfigParser()
        self.config.read("mp3_player_config.ini")
        if not self.config.has_section("Music"):
            self.config.add_section("Music")

        saved_music_list = self.config.get("Music", "Files", fallback="")
        self.musicList.addItems(saved_music_list.splitlines())

        main_layout = QVBoxLayout()

        controls_layout = QHBoxLayout()
        controls_layout.addWidget(self.addButton)
        controls_layout.addWidget(self.removeButton)
        controls_layout.addWidget(self.clearButton)
        controls_layout.addWidget(self.playButton)
        controls_layout.addWidget(self.pauseButton)
        controls_layout.addWidget(self.stopButton)
        controls_layout.addWidget(self.volumeSlider)

        main_layout.addWidget(self.musicList)
        main_layout.addWidget(self.positionSlider)
        main_layout.addWidget(self.timeLabel)
        main_layout.addLayout(controls_layout)
        main_layout.addWidget(self.statusLabel)

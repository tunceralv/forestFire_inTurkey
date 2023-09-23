import sys
import typing
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QWidget
from PyQt5.QtGui import QFont
import io
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings # pip install PyQtWebEngine
import numpy as np
from data import df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbs
from harita import MainWindow

#Görüntüle
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
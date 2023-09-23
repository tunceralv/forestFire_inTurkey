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
from imageProcecing import YananAlanTespit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NBR Map in Turkey")
        self.setStyleSheet("\n"
"background-color: rgb(50,50,50);\n"
"border-radius:20px;\n"
"")
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.setGeometry(0,0, 1920,1500)
        self.setFixedSize(1920,1500)

        coordinate = (36.8261,28.21956)
        m = folium.Map(
        	
        	zoom_start=13,
        	location=coordinate,
            tiles='Stamen Terrain' 
        )
        

        #Bilgi etiketi
        self.label_Bilgi = QLabel(self)
        self.label_Bilgi.setStyleSheet("\n"
            "background-color: rgb(255,0,0);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.label_Bilgi.setText("  Muğla Yangın Verileri ")
        self.label_Bilgi.setGeometry(1638,20, 268, 70)

        #Tarih etiketi
        self.label_Tarih = QLabel(self)
        self.label_Tarih.setStyleSheet("\n"
            "background-color: rgb(50,50,50);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.label_Tarih.setText("    Yangın" "\n" "   Tarihleri -> ")
        self.label_Tarih.setGeometry(1605,120, 140, 100)

        #Tarih etiketi(değer)
        self.label_Tarih = QLabel(self)
        self.label_Tarih.setStyleSheet("\n"
            "background-color: rgb(50,50,50);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt  \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.label_Tarih.setText("  29.07.2021" "\n" "  04.08.2021 ")
        self.label_Tarih.setGeometry(1730,120, 120, 100)


        #Toplam Nokta Etiketi
        self.label_ToplamNokta = QLabel(self)
        self.label_ToplamNokta.setStyleSheet("\n"
            "background-color:rgb(50,50,50);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.label_ToplamNokta.setText("     Yanan" "\n" "    Noktalar ->" )
        self.label_ToplamNokta.setGeometry(1603,360, 140, 100)


        #Toplam Nokta Etiketi(Değer)
        self.label_ToplamNokta = QLabel(self)
        self.label_ToplamNokta.setStyleSheet("\n"
            "background-color:rgb(50,50,50);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.label_ToplamNokta.setText(str(len(df))+"(Nokta)")
        self.label_ToplamNokta.setGeometry(1730,370, 120, 100)


        #Yanan Alan Etiketi
        self.label_yananAlan = QLabel(self)
        self.label_yananAlan.setStyleSheet("\n"
            "background-color: rgb(50,50,50);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.label_yananAlan.setText("    Toplam" "\n" "    Alan ->" )
        self.label_yananAlan.setGeometry(1603,600, 140, 100)

        self.label_yananAlan = QLabel(self)
        self.label_yananAlan.setStyleSheet("\n"
            "background-color: rgb(50,50,50);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.label_yananAlan.setText(str(YananAlanTespit.toplamAlan)+"(piksel)")
        self.label_yananAlan.setGeometry(1730,600, 140, 100)


        #Buton 
        self.nasaButon = QPushButton(self)
        self.nasaButon.setStyleSheet("\n"
            "background-color: rgb(100,100,100);\n"
            "color:rgb(255,255,255);\n"
            "font: 87 12pt \"Display\";\n"
            "border-radius:20px;\n"
            "")
        self.nasaButon.setText(" Yanan" "\n" "   Bölgeleri Göster ")
        self.nasaButon.setGeometry(1650,850, 240, 100)
        self.nasaButon.clicked.connect(self.AlanHaritasi_Goster)
        
    
        coordinates = list(zip(df['latitude'], df['longitude']))
        for coord in coordinates:
         latitude, longitude = coord  # Koordinatları ayırın
         folium.Marker(location=[latitude, longitude], icon=folium.Icon(icon='fire', color='red')).add_to(m)
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        # Etiketler oluştur
        self.label = QWebEngineView(self)
        self.label.setHtml(data.getvalue().decode())
        self.label.setGeometry(10, 2, 1600,1220)
        self.label.setStyleSheet("\n"
"background-color: rgb(150,150,150);\n"
"border-radius:20px;\n"
"")
        
#Butona bağlı fonk.
    def AlanHaritasi_Goster(self):
       self.alanHaritasi=AlanHaritasi()
       self.alanHaritasi.show()

#İkinci Sayfa
class AlanHaritasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NBR Map in Turkey")
        self.setStyleSheet("\n"
"background-color: rgb(50,50,50);\n"
"border-radius:20px;\n"
"")  
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setGeometry(0,0, 1600,1200)
        self.setFixedSize(1250,800)

        self.label_resim=QLabel()
        label = QLabel(self)
        pixmap = QPixmap("isleme_sonrasi_resim.jpg")  # Resim dosyasının yolunu belirtin
        label.setPixmap(pixmap)
        label.setGeometry(0,50, pixmap.width(), pixmap.height())  # Resmin boyutuna göre QLabel boyutunu ayarlayın





    
     
    
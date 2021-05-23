import sys

import pytz
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
from datetime import datetime

label = QFont("Arial", 12)
label_sehir_ülke_C = QFont("Centhury Gothic", 20)


class anaekran(QWidget):

    def tasarim(self):
        self.arama_girdi = QLineEdit(self)
        self.arama_girdi.setPlaceholderText("Arama yapmak istediğiniz şehir...")
        self.arama_girdi.setGeometry(240, 50, 250, 60)
        self.arama_girdi.setFont(label)

        self.ara = QPushButton("Arama", self)
        self.ara.setFont(label)
        self.ara.setGeometry(550, 50, 250, 60)

        self.sehirveulke = QLabel("Şehir - Ülke :",self)
        self.sehirveulke.setFont(label_sehir_ülke_C)
        self.sehirveulke.move(40,155)

        self.sehiralani = QLabel(self)
        self.sehiralani.setFont(label_sehir_ülke_C)
        self.sehiralani.setGeometry(210, 142, 460, 60)
        self.sehiralani.setStyleSheet("color:red")

        self.sicaklik_label = QLabel("Sıcaklık :",self)
        self.sicaklik_label.setFont(label_sehir_ülke_C)
        self.sicaklik_label.move(40,213)

        self.sicaklik_lbl = QLabel(self)
        self.sicaklik_lbl.setFont(label_sehir_ülke_C)
        self.sicaklik_lbl.setGeometry(155, 200, 460, 60)
        self.sicaklik_lbl.setStyleSheet("color:red")

        self.hava_duru = QLabel("Durum : ",self)
        self.hava_duru.setFont(label_sehir_ülke_C)
        self.hava_duru.move(40,268)

        self.hava = QLabel(self)
        self.hava.setFont(label_sehir_ülke_C)
        self.hava.setGeometry(155, 255, 460, 60)
        self.hava.setStyleSheet("color:red")

        self.min_sicaklik_lbl = QLabel("Minimum Sıcaklık : ",self)
        self.min_sicaklik_lbl.setFont(label_sehir_ülke_C)
        self.min_sicaklik_lbl.move(40,326)

        self.min_sicaklik = QLabel(self)
        self.min_sicaklik.setFont(label_sehir_ülke_C)
        self.min_sicaklik.setGeometry(270, 313, 460, 60)
        self.min_sicaklik.setStyleSheet("color:red")

        self.max_sıcaklık_lbl = QLabel("Maksimum Sıcaklık : ",self)
        self.max_sıcaklık_lbl.setFont(label_sehir_ülke_C)
        self.max_sıcaklık_lbl.move(40,384)

        self.max_sıcaklık = QLabel(self)
        self.max_sıcaklık.setFont(label_sehir_ülke_C)
        self.max_sıcaklık.setGeometry(285, 370, 460, 60)
        self.max_sıcaklık.setStyleSheet("color:red")

        self.rüzgar_hızı_lbl = QLabel("Rüzgar Hızı :",self)
        self.rüzgar_hızı_lbl.setFont(label_sehir_ülke_C)
        self.rüzgar_hızı_lbl.move(40,442)

        self.rüzgar_hızı = QLabel(self)
        self.rüzgar_hızı.setFont(label_sehir_ülke_C)
        self.rüzgar_hızı.setGeometry(205, 431, 460, 60)
        self.rüzgar_hızı.setStyleSheet("color:red")

        self.nem_lbl = QLabel("Nem Oranı : ",self)
        self.nem_lbl.setFont(label_sehir_ülke_C)
        self.nem_lbl.move(40,500)

        self.nem = QLabel(self)
        self.nem.setFont(label_sehir_ülke_C)
        self.nem.setGeometry(200, 485, 460, 60)
        self.nem.setStyleSheet("color:red")

        self.enlemboylam_lbl = QLabel("Enlem ve Boylam : ",self)
        self.enlemboylam_lbl.setFont(label_sehir_ülke_C)
        self.enlemboylam_lbl.move(40,558)

        self.enlemboylam = QLabel(self)
        self.enlemboylam.setFont(label_sehir_ülke_C)
        self.enlemboylam.setGeometry(267, 547, 460, 60)
        self.enlemboylam.setStyleSheet("color:red")

        self.icon = QLabel(self)
        self.icon.setGeometry(490, 90, 510, 520)

    def hava_durumu(self, sehir):
        p = {'q': sehir, 'appid': my_api, 'lang': 'tr'}
        veri = requests.get(url, params=p).json()
        if veri:
            self.sehir = veri['name'].upper()
            self.country = veri['sys']['country']
            self.sicaklik = float(veri['main']['temp'] - 273.15)
            self.hava_durumm = veri['weather'][0]['description'].upper()
            self.min_temp = float(veri['main']['temp_min'] - 273.15)
            self.max_temp = float(veri['main']['temp_max'] - 273.15)
            self.wind_speed = float(veri['wind']['speed'])
            self.humidity = float(veri['main']['humidity'])
            self.enlem = float(veri['coord']['lat'])
            self.boylam = float(veri['coord']['lon'])
            self.min_temp = round(self.min_temp, 1)
            self.sicaklik = round(self.sicaklik, 1)
            self.max_temp = round(self.max_temp, 1)
            self.wind_speed = round(self.wind_speed, 1)
            self.humidity = round(self.humidity, 1)
            print(veri)
            return self.sehir, self.country, self.sicaklik, self.hava_durumm, self.min_temp, self.max_temp, self.wind_speed, self.humidity, self.enlem, \
                   self.boylam

    def main(self):
        self.sehir_girdi = self.arama_girdi.text()
        self.sehir_girdi.upper()
        hava = self.hava_durumu(self.sehir_girdi)
        if hava:
            # QMessageBox.information(self, "Bilgilendirme", "Şehir hava bilgileri aşşağıdadır !")
            self.sehiralani.setText('{} - {}'.format(hava[0], hava[1]))
            self.sicaklik_lbl.setText('{} °C'.format(hava[2]))
            self.hava.setText('{}'.format(hava[3]))
            self.min_sicaklik.setText('{} °C'.format(hava[4]))
            self.max_sıcaklık.setText('{} °C'.format(hava[5]))
            self.rüzgar_hızı.setText('{}'.format(hava[6]))
            self.nem.setText('%{}'.format(hava[7]))
            self.enlemboylam.setText('{} - {}'.format(hava[8], hava[9]))
        if self.hava_durumm == 'AZ BULUTLU':
            resim = QPixmap("fewcloud.png")
            self.icon.setPixmap(resim)
        elif self.hava_durumm == 'AÇIK':
            resim = QPixmap("sunny.png")
            self.icon.setPixmap(resim)
        elif self.hava_durumm == 'PARÇALI AZ BULUTLU' or self.hava_durumm == 'PARÇALI BULUTLU':
            resim = QPixmap('parcaliazbulutlu.png')
            self.icon.setPixmap(resim)
        elif self.hava_durumm == 'KAPALI' or self.hava_durumm == 'ÇOK BULUTLU':
            resim = QPixmap('kapalı.png')
            self.icon.setPixmap(resim)
        elif self.hava_durumm == 'HAFIF YAĞMUR' or self.hava_durumm == 'ORTA ŞIDDETLI YAĞMUR':
            resim = QPixmap('rainy.png')
            self.icon.setPixmap(resim)
        else:
            self.icon.clear()

    def __init__(self):
        super().__init__()
        self.tasarim()
        self.width = 1000
        self.height = 650
        self.setMaximumSize(self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setWindowIcon(QIcon("icon.png"))
        self.ara.clicked.connect(self.main)
        self.show()


uygulama = QApplication(sys.argv)
pencere = anaekran()
pencere.setWindowTitle("HAVA DURUMU")
sys.exit(uygulama.exec_())

import sys
from PyQt5 import QtWidgets, QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)  # Tətbiqi başladır
    pencere = QtWidgets.QWidget()  # Pəncərə yaradır
    pencere.setWindowTitle("Pyqt5 Lesson 2")  # Başlığı təyin edir

    etiket = QtWidgets.QLabel(pencere)  # Mətn üçün label yaradır
    etiket1 = QtWidgets.QLabel(pencere)  # Şəkil üçün label yaradır
    etiket.setText("Hello PyQt5")  # Mətni yazır
    etiket1.setPixmap(QtGui.QPixmap("python.jpg"))  # Şəkli yükləyir

    etiket.move(200, 60)  # Mətni yerləşdirir (x=200, y=60)
    etiket1.move(150, 100)  # Şəkli yerləşdirir (x=150, y=100)

    pencere.setGeometry(100, 100, 500, 500)  # Pəncərənin ölçü və mövqeyini verir
    pencere.show()  # Pəncərəni göstərir

    sys.exit(app.exec_())  # Çıxışı idarə edir


Pencere()  # İşə salır
import sys
from PyQt5 import QtWidgets, QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)  # Tətbiqi başladır
    pencere = QtWidgets.QWidget()  # Pəncərə yaradır
    pencere.setWindowTitle("Pyqt5 Lesson 3")  # Başlığı təyin edir

    buton = QtWidgets.QPushButton(pencere)  # Düymə yaradır
    buton.setText("Click me")  # Düyməyə yazı yazır
    etiket = QtWidgets.QLabel(pencere)  # Mətn üçün label yaradır
    etiket.setText("Hello World")  # Mətni yazır

    etiket.move(200, 30)  # Mətni yerləşdirir (x=200, y=30)
    buton.move(190, 80)  # Düyməni yerləşdirir (x=190, y=80)

    pencere.setGeometry(100, 100, 500, 500)  # Pəncərənin ölçü və mövqeyini verir
    pencere.show()  # Pəncərəni göstərir

    sys.exit(app.exec_())  # Çıxışı idarə edir


Pencere()  # İşə salır
import sys
from PyQt5 import QtWidgets, QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)   # PyQt5 tətbiqini başladır və əmr sətiri arqumentlərini (sys.argv) qəbul edir
    pencere = QtWidgets.QWidget()           # Əsas pəncərə obyektini (pəncərə elementini) yaradır
    pencere.setWindowTitle("Pyqt5 Lesson 1")      # Pəncərənin başlığını təyin edir  

    pencere.show()      # Pəncərəni ekranda göstərir

    sys.exit(app.exec_())       # Tətbiqin dövrəsini (event loop) başladır və pəncərə bağlananda proqramdan təhlükəsiz çıxış edir


Pencere()

    
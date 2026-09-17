import sys
from PyQt5 import QtWidgets, QtGui

# 1. Ana Pencere sınıfını oluşturuyoruz
class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    # 2. Kullanıcı arayüzü (Uİ) birleşmelerini tanlımlama
    def init_ui(self):

        # 3. Metn girişi və buton nesnelerini oluşturma
        self.yazi_alanı = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdır = QtWidgets.QPushButton("Yazdır")

        # 4. Vekroial oluşturma ve elemanları ekleme
        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazi_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addStretch()

        # 5. Pencerenin düzenini belirleme
        self.setLayout(v_box)

        # 6. Buton tıklama olaylarını (click fonksiyonuna) bağlama
        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)

        # 7. Pencereyi ekranda gösterme
        self.show()

    # 8. Butonları təkladığımızda çalışacak fonksiyon
    def click(self):

        # Tıklanan butonu tesbit etme
        sender = self.sender()

        # 9. "Temizle" butonuna basıldıysa metni sil
        if sender.text() == "Temizle":
            self.yazi_alanı.clear()

        # 10. "Yazdır" butonuna basıldıysa metni terminale yazdır
        else:
            print(self.yazi_alanı.text())

# 11. Uygulama nesnesini  (QApplication) başlatma
app = QtWidgets.QApplication(sys.argv)

# 12. Pencere nesnesini oluşturma və başlığı ayarlama
pencere = Pencere()
pencere.setWindowTitle("Pyqt5 Lesson 6")

# 13. Uygulamanın sonsuz döngüsünü başlatma ve güvenli çıkış sağlama
sys.exit(app.exec_())
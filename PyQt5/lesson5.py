import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()  # Üst sinifin (QWidget) init metodunu çağırır
        self.init_ui()  # İstifadəçi interfeysini yaradan metodu çağırır

    def init_ui(self):
        self.setWindowTitle("Tıklama Sayacı")  # Pəncərə başlığını təyin edir
        self.setGeometry(100, 100, 300, 200)  # Pəncərənin ölçü və mövqeyini verir

        self.yazi_alani = QtWidgets.QLabel(
            "Bana henüz tıklanmadı..."
        )  # Mətn label-i yaradır
        self.buton = QtWidgets.QPushButton("Bana Tıkla")  # Düymə yaradır
        self.say = 0  # Klik sayğacını sıfırdan başladır

        v_box = QtWidgets.QVBoxLayout()  # Şaquli (vertikal) düzülüş yaradır
        v_box.addStretch()  # Yuxarıdan boşluq əlavə edir
        v_box.addWidget(self.buton)  # Düyməni şaquli düzülüşə əlavə edir
        v_box.addWidget(self.yazi_alani)  # Mətni şaquli düzülüşə əlavə edir
        v_box.addStretch()  # Aşağıdan boşluq əlavə edir

        h_box = QtWidgets.QHBoxLayout()  # Üfüqi (horizontall) düzülüş yaradır
        h_box.addStretch()  # Soldan boşluq əlavə edir
        h_box.addLayout(v_box)  # Şaquli düzülüşü mərkəzə yerləşdirir
        h_box.addStretch()  # Sağdan boşluq əlavə edir

        self.setLayout(h_box)  # Hazır düzülüşü pəncərəyə tətbiq edir

        self.buton.clicked.connect(
            self.click
        )  # Düyməyə klikləyəndə click() metodunu işə salır

        self.show()  # Pəncərəni ekranda göstərir

    def click(self):
        self.say += 1  # Klik sayını 1 vahid artırır
        self.yazi_alani.setText(
            f"Bana {self.say} defa tıklandı"
        )  # Yeni sayı ekranda yeniləyir


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Tətbiqi başladır
    pencere = Pencere()  # Obyekti yaradır
    sys.exit(app.exec_())  # Proqramdan təhlükəsiz çıxışı idarə edir
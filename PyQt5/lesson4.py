import sys
from PyQt5 import QtWidgets, QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    # 1. Düymələrin yaradılması
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("Iptal")
    save = QtWidgets.QPushButton("Kaydet")
    discard = QtWidgets.QPushButton("Vazgeç")
    yes = QtWidgets.QPushButton("Evet")
    no = QtWidgets.QPushButton("Hayır")


    # 2. Birinci horizontal box layout yaradılması
    h_box1 = QtWidgets.QHBoxLayout()
    h_box1.addStretch() 
    h_box1.addWidget(okay)
    h_box1.addWidget(cancel)

    
    # 3. İkinci horizontal box layout yaradılması
    h_box2 = QtWidgets.QHBoxLayout()
    h_box2.addStretch()
    h_box2.addWidget(yes)
    h_box2.addWidget(no)
    
    # 4. Üçüncü horizontal box layout yaradılması
    h_box3 = QtWidgets.QHBoxLayout()
    h_box3.addStretch()
    h_box3.addWidget(save)
    h_box3.addWidget(discard)
    
    # 5. Əsas vertical box layut yaradılması
    v_box4 = QtWidgets.QVBoxLayout()
    v_box4.addLayout(h_box1)
    v_box4.addLayout(h_box2)
    v_box4.addLayout(h_box3)
    
    # 6. Pəncərə ayarları
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt5 Lesson 4")
    pencere.setLayout(v_box4)
    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()
print("""********************************
ATM Makinesine Hoş Geldiniz.....

İşlemler:

1. Bakiye Sorgulama:

2. Para Yatırma:

3. Para Çekme:


Proqramdan çıkmak üçün  'q' basin.
******************************
""")

bakiye = 1000

while True:
    islem = input("İşlemi seçiniz:")

    if (islem == "q"):
        print("Yene bekleriz.....")
    elif (islem == "1"):
        print("Bakiyeniz {} tldir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Miktari giriniz:"))

        bakiye += miktar
    elif (islem == "3"):
        miktar = int(input("Miktarı giriniz:"))

        if (bakiye - miktar < 0):
            print("Yetersiz işlem")
            continue
        bakiye -= miktar

    else:
        print("Gecersiz islem.....")
print("""*****************
Hesab Makinesi Programi


İşlemler:

1. Toplama işlemi

2. Çıkarma işlemi

3. Çarpma işlemi

4. Bölme işlemi
**********************
""")


a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))

islem = input("İşlem Giriniz:")

if islem == "1":
    print("{} ile {} isleminin toplami {} dir".format(a, b, a+b))

elif islem == "2":
    print("{} ile {} isleminin cikarmasi {} dir".format(a, b, a-b))

elif islem == "3":
    print("{} ile {} isleminin carpimi {} dir".format(a, b, a*b))

elif islem == "4":
    print("{} ile {} isleminin bolumu {} dir".format(a, b, a/b))
    
else:
    print("Geçersiz işlem!")
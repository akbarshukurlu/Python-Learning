def ekstra(func):

    def wrapper(numbers):
        çift_toplamı = 0
        çift_sayılar = 0
        tek_toplamı = 0
        tek_sayılar = 0
        for sayı in numbers:
            if (sayı % 2 == 0 ):
                çift_sayılar +=1
                çift_toplamı += sayı
            else:
                tek_sayılar += 1
                tek_toplamı += sayı
        print("Çift Sayıların Ortalaması:", çift_toplamı/çift_sayılar)
        func(numbers)
        print("Tek Sayıların Ortalaması:", tek_toplamı / tek_sayılar)
    return wrapper

@ekstra
def ortalama(numbers):
    toplam = 0

    for i in numbers:

        toplam += i

    print("Genel Ortalama:",toplam/len(numbers))

ortalama([1,2,3,4,5,6,7,8,9,10])

import random

sayi = random.randint(1,10)
# Kaç kere tahminde bulunduğuna göre artacak.
count = 0
# Oyunu oynayan kişinin gireceği sayı
kullanici_verisi = 0

while(True):
    kullanici_verisi = input("Tahmininizi giriniz: " )

    count += 1

    if(kullanici_verisi == "Çık"):
        print("Oyundan çıktınız!")
        break
    kullanici_verisi = int(kullanici_verisi)
    if(kullanici_verisi > sayi):
        print("Daha Küçük Olması Gerekiyor")
    elif(kullanici_verisi < sayi):
        print("Daha Büyük Bir Tahmin Yapın")
    else:
        print("Kazandın!")
        print("Tur sayın : ", str(count))
        break

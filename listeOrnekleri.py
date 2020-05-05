# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:06:38 2020

@author: musta
"""

#VERI YAPILARI

#Listeler

#[] list() -> liste oluşturma yöntemleri

notlar = [90,90,70,59]

#list bir üst veri tipidir.
type(notlar)

#Listeler birbirinden farklı değerleri tutabilir.
#liste = ["a",19.3,90]

len(notlar)

#Liste içi Tip Sorgulama

type(notlar[0])

#iki listeyi birleştirmek için
#liste_genis = [notlar,liste]
#del liste_genis

#Liste Eleman İşlemleri

liste = [10,20,30,40,50]
liste[0]

#Aralıklar vererek eleman seçimi yapalım
#Slice işlemleri denir.
liste[0:2] # 0 dan 2 yekadar
liste[:2] #yukarıdaki ile aynı işlemi yapacak

yeni_liste = liste = ["a",10,[30,40,50]]

yeni_liste[2]

yeni_liste[2][0]

#Liste - Eleman Değiştirme

liste1 = ["ali","veli","berkcan","ayse"]
liste1

liste1[1] = "velinin babası"
liste1[0:3] = "alinin_babasi","velinin_babasi","berkcanin_babasi"
liste1

#listeye yeni eleman eklemek istersek
liste1 = liste1 + ["Kemal"]
liste1

#listeden eleman silmek istersek...
del liste1[2]
liste1
#liste metotları

liste = ["ali","veli","isik"]
dir(liste)
liste 
#eleman eklemek için append metodu kullanılır
liste.append("Berkcan")
liste

liste.remove("Berkcan")
liste

#insert index e göre eleman eklemek için kullanılmakta.
liste.insert(0,"Mustafa")
liste
liste.insert(2,"Ayşe")
liste
#listenin sadece son indexine eleman eklemek için
liste.insert(len(liste),"Beren")
liste

#pop metodu da eleman silmek için kullanılır.
liste.pop(0)
liste

#count sayma metodu
liste = ["ali","veli","isik","ali","veli"]
liste

#copy metodu
#Elimizideki mevcut listeyi yedeklemek için kullanabiliriz.

liste_yedek = liste.copy()
liste_yedek

#extend metodu listeyi genişletmek için kullanılıyor. listeyi başka bir liste ile genişlettik
liste.extend(["a","b",10])
liste

#bir elemanın hangi indexte olduğuna erişmek için index metodu kullanılır.
liste.index("ali")

#reverse metodu elemanları terse çevirme işlemi
#gerçekleştiriyor.

liste.reverse()
liste

#sort metodu da sıralama yapmak için kullanılır.
liste = [30,10,20,40]
liste.sort()
liste
#clear metodu listeyi temizlemeye yarar
liste.clear()
liste

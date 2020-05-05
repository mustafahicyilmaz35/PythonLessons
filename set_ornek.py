# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:12:51 2020

@author: musta
"""

#Veri Yapıları - Setler


# Setler sırasızdır. İndexleri yoktur.
# Setler içindeki veriler tekrar edemez.
# Setler değiştirilebilir türden veri yapısıdır.
# Performans odaklı veri tipleridir.

# Set oluşturmak


l = [1, "a","ali",123]
s = set()
s

t = ("a","ali")

s = set(t)
s

ali = "Lütfen_ata_bakma_uzaya_git"

type(ali)

s = set(ali)
s

l = ["ali","lutfen","ata","bakma","uzaya","git",
     "git","ali","git"]

l

s=set(l)
s

len(s)
s[0]

#setlere eleman ekleme çıkarma işlemleri
l = ["geleceği","yazanlar"]

s = set(l)

s

dir(s)
s.add("ile")
s

s.add("geleceg_git")
s
#s.remove("ile")
s.discard("yazanlar") # discard fonksiyonu hata üretmeden silme işlemi yapar ve kod akışı kesilmez.
s.discard("yazanlar")

s

# setlerde fark işlemleri

# difference ile her iki kümenin farkını alıyoruz.

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)
set2.difference(set1)
#simetrik differecne ile ikisinde aynı anda bakarız.

set1.symmetric_difference(set2)
set1 - set2 #Toplama işlemi yapacağımız anlamına gelmez.

#setlerde kesişim ve birleştirme işlemleri

set1.intersection(set2)
set2.intersection(set1)
kesisim = set1 & set2
kesisim

#Kümelerin birleşimi
birlesim = set1.union(set2)
birlesim

#Kesişim güncelleme
set1.intersection_update(set2)
set1 # Kesişimin değerleri artık set1 in değeri olmuş durumda

#setlerde sorgu işlemleri
set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#İki kümenin kesişiminin boş olup olmadığını sorgulayacağız.

set1.isdisjoint(set2)

#Bir kümenin elemanlarının başka bir küme içerisinde yer alıp almadığı

set1.issubset(set2) # alt küme olması durumunu sorguladık.

#Bir küme diğer kümeyi kapsıyor mu?

set2.issuperset(set1)








# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:56:16 2020

@author: musta
"""

# Sözlükler kapsayıcıdır, sırasızdır, değiştirilebilirdir.
# key value yapısına dayanan bir veri yapısıdır.

sozluk = {'REG' : ['Regresyon Modeli',10],
          'LOJ' : ['Lojistik Regresyon',20],
          'CART':{'RMSE':'Classification and Reg'}}
sozluk
sozluk['REG']
len(sozluk)

sozluk['REG']

# Sözlük eleman işlemleri

sozluk['CART']['RMSE']

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk
sozluk["REG"] = "Regresyon Modeli"
sozluk["REG"]
sozluk[1] = "Yapay Sinir Ağları"
sozluk[1]


#listeyi key değeri olarak atayayabiliriz.

l = [1]

sozluk[l] = "Yeni Bir Şey"

# Sözlük keyları sadece sabit verilerle atanabilir.
# Keyların sabitliğinden endişe etmemeliyiz.

t = ("tupple",)
sozluk[t] = "Yeni Bir Şey"
sozluk[t]

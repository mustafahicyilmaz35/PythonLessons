# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:05:41 2020

@author: musta
"""

# tupple bir veri yapısıdır.
# tupplelar değiştirilemezler.
#Kapsayıcıdırlar, Sıralıdırlar, Değiştirilemezler

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t= "ali","Veli",1,2,3.2, [1,2,3,4] #Bu şekilde de tupple oluşturulabiliyor.
#tupple() ile tupple oluşturulabilir.

t = ("eleman",)
type(t) #Tek elemanlı tupplerda elemanın sonunda , kullanılmaz
        #elemanın değeri cinsinde type değeri döner
        
#Elemanlara erişirken aynı listelerdeki gibi erişiriz.
        
t = ("Ali","Veli",1,2,3,[1,2,3,4])

t[1]
t[2]= 99

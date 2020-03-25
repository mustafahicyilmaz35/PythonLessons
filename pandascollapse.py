import pandas as pd
import warnings 
import numpy as np
"""Warningleri g�rmemek i�in..."""
warnings.filterwarnings('ignore')
"""Pandas�n array olu�turmak i�in series leri vard�r."""
a = pd.Series([1,2,3,4])
print(a)
type(a)
print(a[2])
"""Stringlerden olu�an diziyi bir object �eklinde d�nd�r�yor."""
b = pd.Series(['a','b','c'])
print(b)
"""Pandas ile zaman serileri de olu�turabiliriz"""
t = pd.date_range(start="22.03.2020", end="25.03.2020")
print(t)
type(t)
"""Pandas�n kullan�lma sebeplerinde birisi de dataframe man�pilasyonlard�r."""

temp = np.random.randint(low=20,high=100,size = [20,])
name = np.random.choice(['Mustafa','Hasan','�znur','S�la','Ebrar'],20)
random = np.random.choice([1,2,3,4,5],20)
a = list(zip(temp,name,random)) #zip ile objeye �evirip daha sonra liste cast ettik
df = pd.DataFrame(data = a,columns=['temp','name','random'])
print(df)
type(df)
df.head() #�lk be� sat�r� d�nd�recek
df.tail() #Son be� sat�r� d�nd�recek
df.shape #dataframe in sat�r ve s�t�n say�s�n� d�nd�r�r.
print(df.columns) #Column isimlerini d�nd�recek
print(df.name) #name column a ait datalar� d�nd�recek.
print(df["temp"].describe()) # Bu �ekilde de column datas� d�nd�rebiliriz. describe metodu ile de a��klay�c� istatistik bilgileri ekrana yazd�rabiliriz.and
print(df.info()) #Dataframe in bilgilerini d�nd�r�r.
print(df.values) # Dataframe verilerini array olarak g�sterir.
print(df.set_index("temp",inplace = True)) # index s�tununu man�pile eder.
print(df)
print(df.sort_values(by="random",ascending=False)) # index e g�re b�y�kten k����e s�ralama yapar.and
print(df.drop(["random"], axis = 1)) #Dataframe den columnu atmak i�in kullan�l�r.and
print(df.iloc[[0,1]]) # g�rmek istedi�imiz sat�rlar� bize d�nd�r�r.and
print(df.iloc[1:3,1]) # birinci ve ���nc� sat�r de�erlerinin sadece bir columnda olanlar�n� d�nd�r�.and
"""print(df.iloc[[True,True,False,True]])""" #3. sat�r hari� di�er sat�lar� d�nd�r�r.and
"""df.loc[20,:]""" #loc fonksiyonu block
#Liste olarak column ve data belirlemek
d1 = pd.DataFrame([['a',1],['b',2]],columns=['col1','number'])
d2 = pd.DataFrame([['c',3,'lion'],['d',4,'Tiger']],columns=['letter','number','animal'])
print(d1)
print(d2)
# �ki data frame i birle�tirmek
print(pd.concat([d1,d2],ignore_index=True))
#Dictionary ile dataframe olu�turma
d3 = pd.DataFrame({"city":["delhi","luknov","kampur"],"humidity":[65,80,90]})
print(d3)
# dataframeleri join yapmak
df = pd.merge(d1,d2,on="city")
print(df)
#left join block
#pd ile csv dosyalar�n� okuyup excel olarak d��a aktarabiliriz.


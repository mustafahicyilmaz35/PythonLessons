import pandas as pd
import warnings 
import numpy as np
"""Warningleri görmemek için..."""
warnings.filterwarnings('ignore')
"""Pandasýn array oluþturmak için series leri vardýr."""
a = pd.Series([1,2,3,4])
print(a)
type(a)
print(a[2])
"""Stringlerden oluþan diziyi bir object þeklinde döndürüyor."""
b = pd.Series(['a','b','c'])
print(b)
"""Pandas ile zaman serileri de oluþturabiliriz"""
t = pd.date_range(start="22.03.2020", end="25.03.2020")
print(t)
type(t)
"""Pandasýn kullanýlma sebeplerinde birisi de dataframe manüpilasyonlardýr."""

temp = np.random.randint(low=20,high=100,size = [20,])
name = np.random.choice(['Mustafa','Hasan','Öznur','Sýla','Ebrar'],20)
random = np.random.choice([1,2,3,4,5],20)
a = list(zip(temp,name,random)) #zip ile objeye çevirip daha sonra liste cast ettik
df = pd.DataFrame(data = a,columns=['temp','name','random'])
print(df)
type(df)
df.head() #Ýlk beþ satýrý döndürecek
df.tail() #Son beþ satýrý döndürecek
df.shape #dataframe in satýr ve sütün sayýsýný döndürür.
print(df.columns) #Column isimlerini döndürecek
print(df.name) #name column a ait datalarý döndürecek.
print(df["temp"].describe()) # Bu þekilde de column datasý döndürebiliriz. describe metodu ile de açýklayýcý istatistik bilgileri ekrana yazdýrabiliriz.and
print(df.info()) #Dataframe in bilgilerini döndürür.
print(df.values) # Dataframe verilerini array olarak gösterir.
print(df.set_index("temp",inplace = True)) # index sütununu manüpile eder.
print(df)
print(df.sort_values(by="random",ascending=False)) # index e göre büyükten küçüðe sýralama yapar.and
print(df.drop(["random"], axis = 1)) #Dataframe den columnu atmak için kullanýlýr.and
print(df.iloc[[0,1]]) # görmek istediðimiz satýrlarý bize döndürür.and
print(df.iloc[1:3,1]) # birinci ve üçüncü satýr deðerlerinin sadece bir columnda olanlarýný döndürü.and
"""print(df.iloc[[True,True,False,True]])""" #3. satýr hariç diðer satýlarý döndürür.and
"""df.loc[20,:]""" #loc fonksiyonu block
#Liste olarak column ve data belirlemek
d1 = pd.DataFrame([['a',1],['b',2]],columns=['col1','number'])
d2 = pd.DataFrame([['c',3,'lion'],['d',4,'Tiger']],columns=['letter','number','animal'])
print(d1)
print(d2)
# Ýki data frame i birleþtirmek
print(pd.concat([d1,d2],ignore_index=True))
#Dictionary ile dataframe oluþturma
d3 = pd.DataFrame({"city":["delhi","luknov","kampur"],"humidity":[65,80,90]})
print(d3)
# dataframeleri join yapmak
df = pd.merge(d1,d2,on="city")
print(df)
#left join block
#pd ile csv dosyalarýný okuyup excel olarak dýþa aktarabiliriz.


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
try:
 a=input()
 col_name=['user_id','item_id','rating','timestamp']
 df=pd.read_csv('u.data',sep='\t',names=col_name)
 # for i in df["title"]:
   
 #print(df.head())
 movietitle=pd.read_csv('Movie_Id_Titles')
 # print(movietitle.head())

 df=pd.merge(df,movietitle,on='item_id')
 # print(df.head())
 # sns.set_style('white')
 # print(df.groupby('title')['rating'].mean().sort_values(ascending=False).head())
 # print('___________________________________________________')
 # print(df.groupby('title')['rating'].count().sort_values(ascending=False).head())
 ratings=pd.DataFrame(df.groupby('title')['rating'].mean())
 ratings['No of ratings']=pd.DataFrame(df.groupby('title')['rating'].count())
 # print(ratings.head())
 ratings['No of ratings'].hist(bins=80)
 ratings['rating'].hist(bins=80)

 # sns.jointplot(x='rating',y='No of ratings',data=ratings,alpha=0.5)
 # plt.show()

 mm=df.pivot_table(index='user_id',columns='title',values='rating')
 # print(mm.head())
 # print(ratings.sort_values('No of ratings',ascending=False).head(10))

 starwar_rate=mm[a]
 # print(starwar_rate.head())

 #now to set correlation

 same_as_starwars=mm.corrwith(starwar_rate)
  
 corr_starwars=pd.DataFrame(same_as_starwars,columns=['Correlation'])
 corr_starwars.dropna(inplace=True)
 # print(corr_starwars.sort_values('Correlation',ascending=False).head(15))
 corr_starwars=corr_starwars.join(ratings['No of ratings'])
 #print(corr_starwars.head())
 temp=corr_starwars[corr_starwars['No of ratings']>100].sort_values('Correlation',ascending=False).head().index
 for x in temp:
     print(x)
 #print("Correlation with starwar movie")
 #print(corr_starwars[corr_starwars['No of ratings']>100].sort_values('Correlation',ascending=False).head())
except:
    print("Movie Not Available")
import pandas as pd

df1=pd.read_csv('allcolumns_final.csv',dtype={'name':object})
df2=pd.read_csv('newtid.csv',dtype={'name':object})
googleid=df2['googleid']
name=df2['name']
songname=df1['title']
recommendations=df1['recommendations']
tags=df1['tags']
artist=df1['artist']
df=pd.DataFrame({'googleid':googleid,'name':name,'songname':songname,'recommendations':recommendations,'tags':tags,'artist':artist})
print(df)
df.to_csv('forupload_final.csv')
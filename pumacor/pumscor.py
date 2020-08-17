import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
path='I:/PUMSCOR/'



# 2013-2017
# CD11
df=pd.read_csv(path+'PUMS20132017.csv',dtype=str)
df=df[['ST','PUMA','WGTP','BLD','VEH','YBL']]
df=df[(df['ST']=='36')&(df['PUMA']=='03804')]
df=df.dropna(how='any')
df['WGTP']=pd.to_numeric(df['WGTP'])
df['YBL']=pd.to_numeric(df['YBL'])
df['BLD']=pd.to_numeric(df['BLD'])
df['VEH']=pd.to_numeric(df['VEH'])
df['YBL2']=np.where(np.isin(df['YBL'],[1,2,3,4,5,6,7,8]),'PRE',
           np.where(np.isin(df['YBL'],[9,10,11,12,13,14,15,16,17,18,19,20,21]),'POST',''))
df['BLD2']=np.where(np.isin(df['BLD'],[2,3,4,5]),'LOW',
           np.where(np.isin(df['BLD'],[6,7,8,9]),'HIGH',''))
df['VEH2']=np.where(df['VEH']==0,df['WGTP']*0,
           np.where(df['VEH']==1,df['WGTP']*1,
           np.where(df['VEH']==2,df['WGTP']*2,
           np.where(df['VEH']==3,df['WGTP']*3,
           np.where(df['VEH']==4,df['WGTP']*4,
           np.where(df['VEH']==5,df['WGTP']*5,
           np.where(df['VEH']==6,df['WGTP']*6.5,0)))))))

sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['WGTP']) # 0.44 (74)
sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['WGTP']) # 0.18 (1376)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['WGTP']) # 0.19 (4)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['WGTP']) # 0.26 (163)
sum(df['VEH2'])/sum(df['WGTP']) # 0.20 (1622)


# Manhattan
df=pd.read_csv(path+'PUMS20132017.csv',dtype=str)
df=df[['ST','PUMA','WGTP','BLD','VEH','YBL']]
df=df[(df['ST']=='36')&(np.isin(df['PUMA'],['03801','03802','03803','03804','03805','03806','03807','03808','03809','03810']))]
df=df.dropna(how='any')
df['WGTP']=pd.to_numeric(df['WGTP'])
df['YBL']=pd.to_numeric(df['YBL'])
df['BLD']=pd.to_numeric(df['BLD'])
df['VEH']=pd.to_numeric(df['VEH'])
df['YBL2']=np.where(np.isin(df['YBL'],[1,2,3,4,5,6,7,8]),'PRE',
           np.where(np.isin(df['YBL'],[9,10,11,12,13,14,15,16,17,18,19,20,21]),'POST',''))
df['BLD2']=np.where(np.isin(df['BLD'],[2,3,4,5]),'LOW',
           np.where(np.isin(df['BLD'],[6,7,8,9]),'HIGH',''))
df['VEH2']=np.where(df['VEH']==0,df['WGTP']*0,
           np.where(df['VEH']==1,df['WGTP']*1,
           np.where(df['VEH']==2,df['WGTP']*2,
           np.where(df['VEH']==3,df['WGTP']*3,
           np.where(df['VEH']==4,df['WGTP']*4,
           np.where(df['VEH']==5,df['WGTP']*5,
           np.where(df['VEH']==6,df['WGTP']*6.5,0)))))))

sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['WGTP']) # 0.86 (1028)
sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['WGTP']) # 0.23 (19404)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['WGTP']) # 0.84 (36)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['WGTP']) # 0.26 (1572)
sum(df['VEH2'])/sum(df['WGTP']) # 0.26 (22064)





# 2008-2012
# CD11
df=pd.read_csv(path+'PUMS20082012.csv',dtype=str)
df=df[['ST','PUMA00','PUMA10','WGTP','BLD','VEH','YBL']]
df=df[(df['ST']=='36')&((df['PUMA00']=='03804')|(df['PUMA10']=='03804'))]
df=df.dropna(how='any')
df['WGTP']=pd.to_numeric(df['WGTP'])
df['YBL']=pd.to_numeric(df['YBL'])
df['BLD']=pd.to_numeric(df['BLD'])
df['VEH']=pd.to_numeric(df['VEH'])
df['YBL2']=np.where(np.isin(df['YBL'],[1,2,3,4,5,6,7,8]),'PRE',
           np.where(np.isin(df['YBL'],[9,10,11,12,13,14,15,16]),'POST',''))
df['BLD2']=np.where(np.isin(df['BLD'],[2,3,4,5]),'LOW',
           np.where(np.isin(df['BLD'],[6,7,8,9]),'HIGH',''))
df['VEH2']=np.where(df['VEH']==0,df['WGTP']*0,
           np.where(df['VEH']==1,df['WGTP']*1,
           np.where(df['VEH']==2,df['WGTP']*2,
           np.where(df['VEH']==3,df['WGTP']*3,
           np.where(df['VEH']==4,df['WGTP']*4,
           np.where(df['VEH']==5,df['WGTP']*5,
           np.where(df['VEH']==6,df['WGTP']*6.5,0)))))))

sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['WGTP']) # 0.53 (104)
sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['WGTP']) # 0.20 (1527)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['WGTP']) # 0.00 (1)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['WGTP']) # 0.19 (80)
sum(df['VEH2'])/sum(df['WGTP']) # 0.22 (1717)


# Manhattan
df=pd.read_csv(path+'PUMS20082012.csv',dtype=str)
df=df[['ST','PUMA00','PUMA10','WGTP','BLD','VEH','YBL']]
df=df[(df['ST']=='36')&
      ((np.isin(df['PUMA00'],['03801','03802','03803','03804','03805','03806','03807','03808','03809','03810']))|
       (np.isin(df['PUMA10'],['03801','03802','03803','03804','03805','03806','03807','03808','03809','03810'])))]
df=df.dropna(how='any')
df['WGTP']=pd.to_numeric(df['WGTP'])
df['YBL']=pd.to_numeric(df['YBL'])
df['BLD']=pd.to_numeric(df['BLD'])
df['VEH']=pd.to_numeric(df['VEH'])
df['YBL2']=np.where(np.isin(df['YBL'],[1,2,3,4,5,6,7,8]),'PRE',
           np.where(np.isin(df['YBL'],[9,10,11,12,13,14,15,16]),'POST',''))
df['BLD2']=np.where(np.isin(df['BLD'],[2,3,4,5]),'LOW',
           np.where(np.isin(df['BLD'],[6,7,8,9]),'HIGH',''))
df['VEH2']=np.where(df['VEH']==0,df['WGTP']*0,
           np.where(df['VEH']==1,df['WGTP']*1,
           np.where(df['VEH']==2,df['WGTP']*2,
           np.where(df['VEH']==3,df['WGTP']*3,
           np.where(df['VEH']==4,df['WGTP']*4,
           np.where(df['VEH']==5,df['WGTP']*5,
           np.where(df['VEH']==6,df['WGTP']*6.5,0)))))))

sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['WGTP']) # 0.60 (1198)
sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['WGTP']) # 0.23 (24252)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['WGTP']) # 0.67 (18)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['WGTP']) # 0.27 (972)
sum(df['VEH2'])/sum(df['WGTP']) # 0.25 (26485)





# 2017
# CD11
df=pd.read_csv(path+'PUMS2017.csv',dtype=str)
df=df[['ST','PUMA','WGTP','BLD','VEH','YBL']]
df=df[(df['ST']=='36')&(df['PUMA']=='03804')]
df=df.dropna(how='any')
df['WGTP']=pd.to_numeric(df['WGTP'])
df['YBL']=pd.to_numeric(df['YBL'])
df['BLD']=pd.to_numeric(df['BLD'])
df['VEH']=pd.to_numeric(df['VEH'])
df['YBL2']=np.where(np.isin(df['YBL'],[1,2,3,4,5,6,7,8]),'PRE',
           np.where(np.isin(df['YBL'],[9,10,11,12,13,14,15,16,17,18,19,20,21]),'POST',''))
df['BLD2']=np.where(np.isin(df['BLD'],[2,3,4,5]),'LOW',
           np.where(np.isin(df['BLD'],[6,7,8,9]),'HIGH',''))
df['VEH2']=np.where(df['VEH']==0,df['WGTP']*0,
           np.where(df['VEH']==1,df['WGTP']*1,
           np.where(df['VEH']==2,df['WGTP']*2,
           np.where(df['VEH']==3,df['WGTP']*3,
           np.where(df['VEH']==4,df['WGTP']*4,
           np.where(df['VEH']==5,df['WGTP']*5,
           np.where(df['VEH']==6,df['WGTP']*6.5,0)))))))

sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['WGTP']) # 0.24 (18)
sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['WGTP']) # 0.20 (272)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['WGTP']) # 0.43 (2)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['WGTP']) # 0.11 (40)
sum(df['VEH2'])/sum(df['WGTP']) # 0.20 (333)


# Manhattan
df=pd.read_csv(path+'PUMS2017.csv',dtype=str)
df=df[['ST','PUMA','WGTP','BLD','VEH','YBL']]
df=df[(df['ST']=='36')&(np.isin(df['PUMA'],['03801','03802','03803','03804','03805','03806','03807','03808','03809','03810']))]
df=df.dropna(how='any')
df['WGTP']=pd.to_numeric(df['WGTP'])
df['YBL']=pd.to_numeric(df['YBL'])
df['BLD']=pd.to_numeric(df['BLD'])
df['VEH']=pd.to_numeric(df['VEH'])
df['YBL2']=np.where(np.isin(df['YBL'],[1,2,3,4,5,6,7,8]),'PRE',
           np.where(np.isin(df['YBL'],[9,10,11,12,13,14,15,16,17,18,19,20,21]),'POST',''))
df['BLD2']=np.where(np.isin(df['BLD'],[2,3,4,5]),'LOW',
           np.where(np.isin(df['BLD'],[6,7,8,9]),'HIGH',''))
df['VEH2']=np.where(df['VEH']==0,df['WGTP']*0,
           np.where(df['VEH']==1,df['WGTP']*1,
           np.where(df['VEH']==2,df['WGTP']*2,
           np.where(df['VEH']==3,df['WGTP']*3,
           np.where(df['VEH']==4,df['WGTP']*4,
           np.where(df['VEH']==5,df['WGTP']*5,
           np.where(df['VEH']==6,df['WGTP']*6.5,0)))))))

sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='LOW')]['WGTP']) # 0.90 (231)
sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='PRE')&(df['BLD2']=='HIGH')]['WGTP']) # 0.22 (3958)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='LOW')]['WGTP']) # 0.60 (10)
sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['VEH2'])/sum(df[(df['YBL2']=='POST')&(df['BLD2']=='HIGH')]['WGTP']) # 0.23 (329)
sum(df['VEH2'])/sum(df['WGTP']) # 0.26 (4533)


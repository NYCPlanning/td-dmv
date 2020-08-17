import pandas as pd
import sqlalchemy as sal



pd.set_option('display.max_columns', None)
path='C:/Users/mayij/Desktop/DOC/DCP2020/DMV2020/'
eg=pd.read_csv(path+'engine.csv').loc[0,'engine']





df=pd.read_csv(path+'dmv.csv',dtype=str)
df['type']=df['Record Type'].str.strip().str.upper()
df['vin']=df['VIN'].str.strip().str.upper()
df['class']=df['Registration Class'].str.strip().str.upper()
df['city']=df['City'].str.strip().str.upper()
df['state']=df['State'].str.strip().str.upper()
df['zip']=df['Zip'].str.strip().str.upper()
df['county']=df['County'].str.strip().str.upper()
df['modelyear']=pd.to_numeric(df['Model Year'],errors='coerce')
df['make']=df['Make'].str.strip().str.upper()
df['body']=df['Body Type'].str.strip().str.upper()
df['fuel']=df['Fuel Type'].str.strip().str.upper()
df['unladenwt']=pd.to_numeric(df['Unladen Weight'],errors='coerce')
df['maxgrosswt']=pd.to_numeric(df['Maximum Gross Weight'],errors='coerce')
df['passengers']=pd.to_numeric(df['Passengers'],errors='coerce')
df['validdate']=pd.to_datetime(df['Reg Valid Date'].str.strip(),format='%m/%d/%Y',errors='coerce')
df['expiredate']=pd.to_datetime(df['Reg Expiration Date'].str.strip(),format='%m/%d/%Y',errors='coerce')
df['color']=df['Color'].str.strip().str.upper()
df['scofflaw']=df['Scofflaw Indicator'].str.strip().str.upper()
df['suspension']=df['Suspension Indicator'].str.strip().str.upper()
df['revocation']=df['Revocation Indicator'].str.strip().str.upper()
df=df[['type','vin','class','city','state','zip','county','modelyear','make','body','fuel','unladenwt','maxgrosswt',
       'passengers','validdate','expiredate','color','scofflaw','suspension','revocation']].reset_index(drop=True)
df.to_csv(path+'dmv202007full.csv',index=False)




# Set up database table schema
engine=sal.create_engine(str(eg))
con=engine.connect()
trans=con.begin()
sql="""
    CREATE TABLE dmv202007full
    (
      type VARCHAR(10),
      vin VARCHAR(50),
      class VARCHAR(10),
      city VARCHAR(50),
      state VARCHAR(10),
      zip VARCHAR(10),
      county VARCHAR(50),
      modelyear REAL,
      make VARCHAR(10),
      body VARCHAR(10),
      fuel VARCHAR(50),
      unladenwt REAL,
      maxgrosswt REAL,
      passengers REAL,
      validdate DATE,
      expiredate DATE,
      color VARCHAR(10),
      scofflaw VARCHAR(10),
      suspension VARCHAR(10),
      revocation VARCHAR(10)
      )
    """
con.execute(sql)
trans.commit()
con.close()


# Manually copy the csv to the cloud
# Copy the csv to the table
engine=sal.create_engine(str(eg))
con=engine.connect()
trans=con.begin()
sql="""
    COPY dmv202007full
    FROM '/home/mayijun/DMV2020/dmv202007full.csv'
    DELIMITER ','
    CSV header
    """
con.execute(sql)
trans.commit()
con.close()













df=pd.read_csv(path+'dmv202008trimmed.csv',dtype=str)

# Set up database table schema
engine=sal.create_engine(str(eg))
con=engine.connect()
trans=con.begin()
sql="""
    CREATE TABLE dmv202008trimmed
    (
      VIN VARCHAR(50),
      County VARCHAR(50),
      ModelYear REAL,
      Make VARCHAR(10),
      RegValDate DATE,
      RegExpDate DATE,
      RegClass VARCHAR(10),
      Reg_Category VARCHAR(50),
      Zip VARCHAR(10)
      )
    """
con.execute(sql)
trans.commit()
con.close()


# Manually copy the csv to the cloud
# Copy the csv to the table
engine=sal.create_engine(str(eg))
con=engine.connect()
trans=con.begin()
sql="""
    COPY dmv202008trimmed
    FROM '/home/mayijun/DMV2020/dmv202008trimmed.csv'
    DELIMITER ','
    CSV header
    """
con.execute(sql)
trans.commit()
con.close()








engine=sal.create_engine(str(eg))
con=engine.connect()
sql="""
    WITH dmv7 AS (SELECT vin AS vin7,county AS county7, modelyear AS modelyear7, make AS make7, regvaldate AS regvaldate7, 
    regexpdate AS regexpdate7,regclass AS regclass7, reg_category AS reg_category7, zip AS zip7 FROM dmv202007trimmed),
    dmv8 AS (SELECT vin AS vin8,county AS county8, modelyear AS modelyear8, make AS make8, regvaldate AS regvaldate8, 
    regexpdate AS regexpdate8,regclass AS regclass8, reg_category AS reg_category8, zip AS zip8 FROM dmv202008trimmed)
    SELECT * FROM dmv7 FULL OUTER JOIN dmv8 ON dmv7.vin7=dmv8.vin8 WHERE dmv7.vin7 IS NULL OR dmv8.vin8 IS NULL
    """
df=pd.read_sql_query(sql,con)
df['id']=df.index
df=pd.wide_to_long(df,stubnames=['vin','county','modelyear','make','regvaldate','regexpdate','regclass',
                                 'reg_category','zip'],i='id',j='month').reset_index(drop=False)
df=df[pd.notna(df['vin'])].reset_index(drop=True)








engine=sal.create_engine(str(eg))
con=engine.connect()
sql="""
    WITH dmv7 AS (SELECT vin AS vin7,county AS county7, modelyear AS modelyear7, make AS make7, regvaldate AS regvaldate7, 
    regexpdate AS regexpdate7,regclass AS regclass7, reg_category AS reg_category7, zip AS zip7 FROM dmv202007trimmed),
    dmv8 AS (SELECT vin AS vin8,county AS county8, modelyear AS modelyear8, make AS make8, regvaldate AS regvaldate8, 
    regexpdate AS regexpdate8,regclass AS regclass8, reg_category AS reg_category8, zip AS zip8 FROM dmv202008trimmed)
    SELECT * FROM dmv7 INNER JOIN dmv8 ON dmv7.vin7=dmv8.vin8
    WHERE dmv8.regexpdate8-dmv7.regexpdate7<>730 AND dmv8.regexpdate8-dmv7.regexpdate7<>0
    """
df=pd.read_sql_query(sql,con)

    


k=df[(df['vin7']==df['vin8'])&(df['county7']==df['county8'])&(df['modelyear7']==df['modelyear8'])&(df['make7']==df['make8'])&(df['regvaldate7']==df['regvaldate8'])&(df['regexpdate7']==df['regexpdate8'])&(df['regclass7']==df['regclass8'])&(df['reg_category7']==df['reg_category8'])&(df['zip7']==df['zip08'])]
k['days7']=[x.days for x in k['regexpdate7']-k['regvaldate7']]
k=k[k['days7']==730]
k['days7'].hist()
















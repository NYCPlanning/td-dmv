import pandas as pd
import sqlalchemy as sal



pd.set_option('display.max_columns', None)



# Set up database tables
engine=sal.create_engine('postgres://postgres:123456@159.65.64.166:5432/postgres')
con=engine.connect()
trans=con.begin()
sql="""
    CREATE TABLE dmv20200809
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
# Manually import csv into database




df=pd.read_csv('C:/Users/mayij/Desktop/dmv.csv',dtype=str)
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
df.to_csv('C:/Users/mayij/Desktop/dmv20200809.csv',index=False)



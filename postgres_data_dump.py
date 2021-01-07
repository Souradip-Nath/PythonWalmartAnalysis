import pandas as pd
import psycopg2 as pg
path=r"C:\Users\souradipn408\Documents\Data Science\ScikitLearn\simplilearnProject\Walmart_Store_sales.csv"
df = pd.read_csv(path,index_col=False)
#print(df)
dns="jdbc:postgresql://localhost:5432/mydb"
user="test"
psw="Test@1234#"
enc = "UTF-8"
conn=conn=pg.connect(user="test",password="Test@1234#",host="localhost",database = "mydb",port="5432")
cur=conn.cursor()
print ( conn.get_dsn_parameters(),"\n")
print(df.columns)
cur.execute("truncate table myschema.walmart_store_sales")
conn.commit()
for i in df.index:
    cur.execute("insert into myschema.walmart_store_sales values ("+str(df['Store'][i])+",to_date('"+str(df['Date'][i])+\
    "','dd-mm-yyyy'),"+str(df['Weekly_Sales'][i])+","+str(df['Holiday_Flag'][i])+","+str(df['Temperature'][i])+","+str(df['Fuel_Price'][i])+"\
    ,"+str(df['CPI'][i])+","+str(df['Unemployment'][i])+")")
conn.commit()
conn.close()
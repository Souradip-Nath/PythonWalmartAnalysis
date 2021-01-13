import read_data
import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.2f' % x)
path=r"C:\Users\souradipn408\Documents\Data Science\ScikitLearn\PythonWalmartAnalysis\Walmart_Store_sales.csv"
df2=read_data.read_data(path)
def max_sale_store(df2):
    df3=df2.groupby(["Store"])["Weekly_Sales"].sum().reset_index(name="Overall_Sales").sort_values("Overall_Sales",ascending=False)
    print("Store with Maximum Sales")
    print(df3.head(1).to_string(index=False))

def max_std_store(df2):
    df6=pd.merge(df2[["Store","Weekly_Sales"]].groupby(["Store"])["Weekly_Sales"].std().reset_index(name="STD_Sales")\
    .sort_values("STD_Sales",ascending=False),df2[["Store","Weekly_Sales"]].groupby(["Store"])["Weekly_Sales"]\
    .mean().reset_index(name="Mean_Sales"),on="Store")
    df6["Ratio_std_by_mean"]=(df6["STD_Sales"]/df6["Mean_Sales"]).map('{:,.5f}'.format)
    df6["Coeff_Variation"]=((df6["STD_Sales"]/df6["Mean_Sales"])*100).map('{:,.2f}%'.format)
    print("\nStore with max Standard Deviation\n")
    print(df6.head(1)[["Store","STD_Sales","Ratio_std_by_mean","Coeff_Variation"]].to_string(index=False))

def quaterly_growth_rate(df2):
    print("Calculating growth for top 5 Stores")
    print("Walmart Financial Year starts from February.\nHence measuring Q3 as Aug-Sep-Oct\n")
    df2["Date"]=pd.to_datetime(df2["Date"])
    mask=((df2["Date"]>="2012-08-01") & (df2["Date"]<="2012-10-31"))
    dfq3=df2.loc[mask]
    dfq3=dfq3[["Store","Weekly_Sales"]].groupby(["Store"])["Weekly_Sales"].sum().reset_index(name="Q3_Sales_2012")
    mask=((df2["Date"]>="2012-05-01") & (df2["Date"]<="2012-07-31"))
    dfq2=df2.loc[mask]
    dfq2=dfq2[["Store","Weekly_Sales"]].groupby(["Store"])["Weekly_Sales"].sum().reset_index(name="Q2_Sales_2012")
    df3=pd.merge(dfq2,dfq3,on="Store")
    df3["Q-o-Q Growth"]=((df3["Q3_Sales_2012"]-df3["Q2_Sales_2012"])/df3["Q2_Sales_2012"])*100
    df3=df3.sort_values("Q-o-Q Growth",ascending=False)
    df3["Q-o-Q Growth"]=df3["Q-o-Q Growth"].map('{:,.2f}%'.format)
    mask=((df2["Date"]>="2011-08-01") & (df2["Date"]<="2011-10-31"))
    dfq2=df2.loc[mask]
    dfq2=dfq2[["Store","Weekly_Sales"]].groupby(["Store"])["Weekly_Sales"].sum().reset_index(name="Q3_Sales_2011")
    df4=pd.merge(dfq2,dfq3,on="Store")
    df4["Y-o-Y Growth"]=(((df4["Q3_Sales_2012"]-df4["Q3_Sales_2011"])/df4["Q3_Sales_2011"])*100)
    df4=df4.sort_values("Y-o-Y Growth",ascending=False)
    df4["Y-o-Y Growth"]=df4["Y-o-Y Growth"].map('{:,.2f}%'.format)
    print(df3.head().to_string(index=False))
    print("\n")
    print(df4.head().to_string(index=False))

def high_sale_holidays(df2):
    print("\nHolidays where sale went higher than non-holiday sales\n")
    mean_hol=df2[df2['Holiday_Flag']==0][["Weekly_Sales"]].mean()["Weekly_Sales"]
    print((df2["Date"][(df2["Holiday_Flag"]==1)&(df2["Weekly_Sales"]>mean_hol)]).drop_duplicates().to_frame().to_string(index=False))

def monthly_sales(df2):
    df2["mod_dt"]=df2.Date.str[6:]+"-"+df2.Date.str[3:5]
    return df2.groupby(["mod_dt"])["Weekly_Sales"].sum().reset_index('mod_dt').sort_values('mod_dt',ascending=True)

def semester_sales(df2):
    df2["mod_dt"]=df2.Date.str[6:]+"-"+df2.Date.str[3:5]
    df2["semester"]=np.where(df2.mod_dt.str[5:7].astype('int64')<=6,df2.mod_dt.str[:4]+' - First Sem',df2.mod_dt.str[:4]+' - Second Sem')
    return df2.groupby(["semester"])["Weekly_Sales"].sum().reset_index('semester').sort_values('semester',ascending=True)
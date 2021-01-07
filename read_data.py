import pandas as pd
#def_path=r"C:\Users\souradipn408\Documents\Data Science\ScikitLearn\simplilearnProject\Walmart_Store_sales.csv"
def read_data(path):
    df1=pd.read_csv(path)
    return df1

#print(read_data(def_path).head())

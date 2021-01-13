import read_data
import basic_stats as bs
path=r"C:\Users\souradipn408\Documents\Data Science\ScikitLearn\PythonWalmartAnalysis\Walmart_Store_sales.csv"
raw_data=read_data.read_data(path)
monthly_sales=bs.monthly_sales(raw_data)
sem_sales=bs.semester_sales(raw_data)
#print(monthly_sales)
#input()
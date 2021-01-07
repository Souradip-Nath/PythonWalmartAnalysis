import read_data
import basic_stats as bs
path=r"C:\Users\souradipn408\Documents\Data Science\ScikitLearn\simplilearnProject\Walmart_Store_sales.csv"
raw_data=read_data.read_data(path)
bs.quaterly_growth_rate(raw_data)
#input()
import pandas as pd
import numpy as np

file_path = './starbucks_store_worldwide.csv'
# read cvs file
df = pd.read_csv(file_path)
# dataframe grouped
# grouped = df.groupby(by="Country")
# country_count = grouped['Brand'].count()

# print(country_count)
# print(country_count['US'])
# print(country_count['CN'])

# china_data = df[df['Country']=='CN']
# grouped = china_data.groupby(by='City').count()['Brand']
# print(grouped)

# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))

grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
grouped2= df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]

print('groupp1 type ', type(grouped1))
print('groupp2 type ', type(grouped2))
print('groupp3 type ', type(grouped3))

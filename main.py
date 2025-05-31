import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# print(df.head()); print(df.tail()); print(df.info())  # Getting overall information about the data
# print(df.shape); print(df.isnull().sum())  # Checking if there missing values

#__________________________________________________________________________________

# CLEANING DATA

# df.columns = df.columns.str.strip()  # cleaning before converting


# df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# for col in df.select_dtypes(include='object'):
#     print(col, df[col].nunique())  # shows all unique elements in each column
# df['Category'] = df['Category'].str.strip().str.title()  # if found any element with spaces around it which makes it different from the others, this code will strip it and makes elements equal


# print(df.duplicated().sum())# check if there any duplicates
# df.drop_duplicates(inplace=True) # if found any, removes

#__________________________________________________________________________________

# EXPLORATORY DATA ANALSYS + VISUALIZATION

import seaborn as sns

#   WHICH PRODUCTS WERE SOLD THE MOST?
# top_5 = df.groupby("Product Name")['Quantity'].sum().sort_values(ascending=False).head()
# plt.figure(figsize=(10,5))
# top_5.plot(kind='bar')
# plt.title('Eng ko‘p sotilgan 5 mahsulot')
# plt.ylabel('Sotilgan dona miqdori')
# plt.xlabel('Mahsulot nomi')
# plt.show()


#   WHICH SEGMENTS WERE MOST PROFITABLE?
# df.groupby("Segment")["Profit"].sum()
# plt.figure(figsize=(1,5))
# sns.barplot(data=df, x='Segment', y='Profit', estimator=sum)
# plt.title('Segmentlar bo‘yicha jami foyda')
# plt.show()


#   TOTAL SALES IN EACH YEAR
# df['Order Date'] = pd.to_datetime(df['Order Date'])  #Converting date to datetime format
# total_sales = df.groupby(df["Order Date"].dt.year)['Sales'].sum()  # shows total sales per year
# total_sales.plot(kind='line', marker='o', color='green')
# plt.title("Total Sales per year")
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()


#   WHICH SUB-CATEGORIES ARE PROFITABLE AND WHICH ARE NOT
# s = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)
# s.plot(kind='bar', color='coral')
# plt.show()


print(*df.columns)




































































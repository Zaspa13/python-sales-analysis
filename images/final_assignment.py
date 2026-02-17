import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('data/finance_liquor_sales.csv')

#Καθαρισμός Dataset
print(df.dtypes)
print(df.isna().sum())
df = df.dropna(subset=['store_location', 'county_number', 'county', 'category', 'category_name'])

#Task 1
sales = df.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
top_items = sales.sort_values(['zip_code', 'item_number'], ascending=[True, False]).groupby('zip_code').head(1).reset_index(drop=True)

fig=px.scatter(top_items, x='zip_code', y='bottles_sold', size='bottles_sold', color='bottles_sold', 
               hover_data=['item_number'], title='Most Popular Item per Zip Code',
               labels={'zip_code': 'Zip Code', 'bottles_sold': 'Total Bottles Sold', 'item_number': 'Top Item'})
fig.update_xaxes(type='category', nticks=20)
fig.show()

#Task 2
total_sales = df.groupby('store_name')['sale_dollars'].sum().reset_index()
total_sales['percent'] = total_sales['sale_dollars'] / total_sales['sale_dollars'].sum() * 100
total_sales = total_sales.sort_values('percent', ascending=False)
top_sales = total_sales.head(15)

fig=px.bar(top_sales, x='percent', y='store_name', orientation='h', color='percent', 
               title='Sales Percentage Share by Store',
               labels={'percent': 'Sales Share (%)', 'store_name': 'Store Name'})
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.update_traces(texttemplate='%{x:.2f}%', textposition='outside')
fig.show()
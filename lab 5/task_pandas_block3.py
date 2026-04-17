import pandas as pd
from task_numpy_block2 import rows




#21 task
df = pd.DataFrame(rows)
df["quantity"] = 1

#22 task
df.loc[df['product_name'] == 'Mouse', 'quantity'] = 2
df["total_price"] = df["price"] * df['quantity']

#23 task
orders_df = df[['order_id', 'total_price']].rename(columns={'total_price': 'total'})
users_df = df[['order_id', 'user_name']].copy()
merged_df = pd.merge(orders_df, users_df, on='order_id')
name_instead_id_df = merged_df[['order_id', 'user_name' ,'total']]
short_df = name_instead_id_df[['order_id', 'user_name' ,'total']]

#24 task
total_more_100 = short_df[short_df['total'] > 100]

#25 task
groupby_name_df = short_df.groupby('user_name')['total'].sum().reset_index()

#26 task
groupby_mean_df = short_df.groupby('user_name')['total'].mean().reset_index().rename(columns={'total': 'mean_total'})

#27 task
groupby_count_df = short_df.groupby('user_name')['order_id'].count().reset_index().rename(columns={'order_id': 'orders_count'})

#28 task
category_mean_tp_df = df.groupby('category')['total_price'].mean().reset_index().rename(columns={'total_price': 'mean_price'})

#29 task
df['discounted_price'] = df['price'] * 0.9

#30 task
sorted_df = df.sort_values(by=['price'], ascending=False)

#31 task
#21 task та жасалынып қойған

#32 task
#22 task та жасалынып қойған

#33 task
category_electronics_df = df[df['category'] == 'Electronics'][['product_name', 'price']]

#34 task
category_count = df['category'].value_counts()

#35 task
category_mean_p_df = df.groupby('category')['price'].mean().reset_index().rename(columns={'price': 'mean_price'})
print(category_mean_p_df)


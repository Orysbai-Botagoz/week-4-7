import pandas as pd
from pandas.core.algorithms import nunique_ints
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
total_sum = short_df.groupby('user_name')['total'].sum().reset_index().rename(columns={'total': 'total_sum'})
df = df.merge(total_sum, on='user_name', how='left')

#26 task
groupby_mean_df = short_df.groupby('user_name')['total'].mean().reset_index().rename(columns={'total': 'mean_total'})

#27 task
orders_count_df = df.groupby('user_name')['order_id'].count().reset_index().rename(columns={'order_id': 'total_orders'})


#28 task
category_mean_tp_df = df.groupby('category')['total_price'].mean().reset_index().rename(columns={'total_price': 'mean_price'})


#29 task
df['discounted_price'] = df['price'] * 0.9

#30 task
sorted_price_df = df.sort_values(by=['price'], ascending=False)

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

#36 task
sorted_total_price_df = df.sort_values(by=['total_price'], ascending=False)

#37 task
top_3_total_price_df = df.sort_values(by=['total_price'], ascending=False).head(3)

#38 task
#23 task та жасалынып қойған

#39 task
#26 task та жасалынып қойған

#40 task
#27 task та жасалынып қойған

#41 task
max_order = df.groupby('user_name')['total_price'].max().reset_index().rename(columns={'total_price': 'max_order'})
df = df.merge(max_order, on='user_name', how='left')

#42 task
total_orders = df.groupby('user_name')['category'].nunique().reset_index().rename(columns={'category': 'total_orders'})
df = df.merge(total_orders, on='user_name', how='left')

#43 task
df['VIP'] = df['total_sum'] >= 1000


#44 task
df['mean_total'] = df.groupby('user_name')['total_price'].transform('mean')
sorted_tp_mean_df = df.sort_values(by=['total_price', 'mean_total'], ascending=[False, True])

#45 task
result = df[[
    'user_name',
    'total_orders',
    'total_sum',
    'mean_total',
    'max_order',
    'VIP'
]].drop_duplicates("user_name")

print(result)


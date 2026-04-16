import pandas as pd
from task_numpy_block2 import rows

#21 task
df = pd.DataFrame(rows)
df["quantity"] = 1

#22 task
df.loc[df['product_name'] == 'Mouse', 'quantity'] = 2
df["total_price"] = df["price"] * df['quantity']

#23


print(df)
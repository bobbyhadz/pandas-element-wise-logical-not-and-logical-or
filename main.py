# Pandas: Element-wise logical NOT operator

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'salary': [175.1, 180.2, 190.3, 205.4],
    'is_subscribed': pd.Series([True, False, False, True])
})

print(df)

print('-' * 50)

inverted = ~df['is_subscribed']

print(inverted)
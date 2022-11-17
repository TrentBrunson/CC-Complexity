#%%
import pandas as pd
import numpy as np
# %%
df = pd.read_excel('data\input\HC CC list - Offer Ops - Nov15.xlsx')
# %%
df
# %%
df.shape
# %%
df.info
# %%
df.describe()
# %%
df.columns
# %%
df.value_counts()
# %%
df.value_counts().sum()
# %%
df.count()
# %%
df.columns
# %%
# check for duplicate rows
dupes = df.duplicated()
sum(dupes)
# %%
# check for nulls
# df.isnull - not useful

df.isna().sum()
# %%
df['HC Cost Center'].unique()
# %%
NumUniqueCC = df['HC Cost Center'].nunique()
NumUniqueCC
# %%
df.groupby(['HC Cost Center']).size()
# %%
df.groupby(['L6']).size()

# %%
df.groupby(['L6']).count()
# %%
test = df.groupby(['L6', 'HC Cost Center'])
# %%
test.first()
# %%
newDF = df[[
    'L6',
    'HC Cost Center'
]]
newDF
# %%
newDF.groupby(['L6']).size()
# %%
g = newDF.groupby('L6')['HC Cost Center'].apply(lambda x: list(np.unique(x)))
# %%
aggDF = newDF.groupby('L6').agg(set)
aggDF
# %%
print(aggDF)
# %%

#%%
import pandas as pd
import numpy as np
import itertools
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
# gNP = newDF.groupby('L6')['HC Cost Center'].apply(lambda x: list(np.unique(x)))
# %%
aggDF = newDF.groupby('L6').agg(set)
aggDF
# %%
# print(aggDF)
# %%
g = df.groupby('L6')['HC Cost Center'].apply(set)
g
# %%
rows = []
total = len(df['HC Cost Center'].unique())
total
# %%
for a, b in itertools.combinations(g.index, 2):
    rows.append({
        'L6-1' : a,
        'L6-2' : b,
        'Number of CC for L6-1' : len(g[a]),
        'Number of CC for L6-2' : len(g[b]),
        'All CC' : total,
        'Common CC' : len(g[a] & g[b])
    })

finalDF = pd.DataFrame(rows)
finalDF
# %%

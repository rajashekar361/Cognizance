
import pandas as pd
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv")
df.head(100)

print(df['LotFrontage'].isnull())

print(df.isnull().sum())

df['LotFrontage'].fillna(1, inplace=True)

print(df['LotFrontage'])

print(df['Alley'].isnull())

df['Alley'].fillna('no alley here', inplace=True)
print(df['Alley'])

print(df['BsmtQual'].isnull())

df[df['BsmtQual'].isnull()]

df['BsmtQual'].fillna('no value', inplace=True)
df.tail(10)

df[df['BsmtQual'].isnull()]

print(df['BsmtCond'].isnull())

df[df['BsmtCond'].isnull()]

df['BsmtCond'].fillna('No condition', inplace=True)
df.tail(10)

df[df['BsmtCond'].isnull()]

print(df['BsmtExposure'].isnull())

df[df['BsmtExposure'].isnull()]

df['BsmtExposure'].fillna('No exposure', inplace=True)
df.tail(10)

df[df['BsmtExposure'].isnull()]

df[df['BsmtFinType1'].isnull()]

df['BsmtFinType1'].fillna('value not assigned ', inplace=True)
df.tail(10)

df[df['BsmtFinType1'].isnull()]

print(df['BsmtFinType2'].isnull())

df[df['BsmtFinType2'].isnull()]

df['BsmtFinType2'].fillna('values not found', inplace=True)
df.tail(10)

df[df['BsmtFinType2'].isnull()]

print(df.isnull().sum())


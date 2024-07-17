import pandas as pd
df= pd.read_csv('datacleaning.csv')
print(df)

print(df.isnull().sum())
df.info()

df_cleaned=df.dropna()
print(df_cleaned)

#fill missing
df_filled=df.fillna({
    'Age':df['Age'].mean(),
    'Salary':df['Salary'].mean()
})
print(df_filled)

# #backward fill
# df_back=df.fillna(method='bfill')

# #forward fill
# df_for=df.fillna(method='ffill')

#add duplicate
df=pd.concat([df,df.iloc[[0]] , df.iloc[[1]]],ignore_index=True)
print("Before removing duplicates")
print(df)
print("after removing duplicates")
df_no_duplicates=df.drop_duplicates()
print(df_no_duplicates)

#replace incorrect values
df_corrected=df.replace({'Department' : {'HR': 'Human Resource', 'IT':'Information and Technology'}})
print(df_corrected)

#convert
df['Department']=df['Department'].str.lower()
print(df['Department'])


#min - MaX Normalisation  -[0,1]
#X NORMALISATION = X - X MIN/ X MAX-X MIN

df_normalised= df.copy()
for col in ['Age','Salary']:
    df_normalised[col]= (df[col]-df[col].min()) / (df[col].max()-df[col].min())

print("original data frame")
print(df)
print("normalised data frame")
print(df_normalised)

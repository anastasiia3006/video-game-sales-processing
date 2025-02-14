# this file processed a database on the production and sale of video games

import pandas as pd

df = pd.read_csv('vgchartz-2024.csv')


#group data by genre for becoming a mean value
grouped_df = df.groupby('genre').agg({'critic_score': 'mean', 'total_sales':'mean', 'na_sales':'mean', 'jp_sales':'mean', 'pal_sales':'mean', 'other_sales':'mean'})

avg_values_by_genre = grouped_df.to_dict(orient='index')

# result
for column in ['critic_score', 'total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']:
    df[column] = df.groupby('genre')[column].transform(lambda x: x.fillna(x.mean()).round(2))
    df[column] =df[column].fillna(0)

df['developer'] = df['developer'].fillna('Unknown')

#convert to datatime and filling with NaT
for col in ['release_date','last_update']:
    df[col] = pd.to_datetime(df[col],errors = 'coerce')
    df[col] = df[col].fillna(pd.NaT)


#print(df.head())
#print(df.isnull().sum())
#print(df.info())

df.to_csv('filled_data_vgchartz.csv', index =False)



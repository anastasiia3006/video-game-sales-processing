import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.animation as animation
import seaborn as sns

df = pd.read_csv('filled_data_vgchartz.csv')

# - 1 Which genre is most in demand, which is most purchased?

group_genre_sales = df.groupby('genre')['total_sales'].sum()
most_pop_genre = group_genre_sales.idxmax()
print(f'The most popular genre is: "{most_pop_genre}" genre')

top_5_genre = group_genre_sales.nlargest(5)
print(f'Top 5 most popular genre: {top_5_genre}')

#visualisation most 5 popular genre
fig ,ax = plt.subplots()
genres = top_5_genre.index.tolist()
counts = top_5_genre.values.tolist()
bar_label = ['blue', 'red', 'pink','orange','green']
bar_color = ['tab:blue', 'tab:red','tab:pink','tab:orange','tab:green']

ax.bar(genres, counts, label = bar_label, color = bar_color)
ax.set_ylabel('Sales')
ax.set_title('most popular video game genres')
#plt.show()


# - 2 Which year had the biggest sales?
df['year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
group_sales_by_year = df.groupby('year')['total_sales'].sum()
highest_sales = group_sales_by_year.idxmax()
top_5_years = group_sales_by_year.nlargest(5)
print(top_5_years)

#visualisation for top 5 years
df = df[df['year'] >= df['year'].max() - 20]

# Grouping data by years and genres
grouped = df.groupby(['year', 'genre'])['total_sales'].sum().reset_index()

# Get a list of unique years
years = sorted(grouped['year'].unique())

# Creating a figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, max(grouped['total_sales']))
ax.set_ylim(-0.5, 4.5)

# empty graph
bars = ax.barh([], [])

# Initialization function
def init():
    ax.set_xlabel("Total Sales")
    ax.set_title("Top 5 Genres Over Time")
    return bars

# Frame update
def update(year):
    ax.clear()
    data = grouped[grouped['year'] == year].nlargest(5, 'total_sales')
    bars = ax.barh(data['genre'], data['total_sales'])
    ax.set_xlim(0, max(grouped['total_sales']))
    ax.set_title(f"Top 5 Genres in {year}")
    return bars

# animation start
ani = animation.FuncAnimation(fig, update, frames=years, init_func=init, blit=False, interval=500)

#plt.show()


# - 3 Do any consoles seem to specialize in a particular genre?
group_console = df.groupby(['console','genre']).size().reset_index(name='count')
most_popular_genre = group_console.loc[group_console.groupby('console')['count'].idxmax()]
filltered_genres = most_popular_genre[most_popular_genre['count']>=250]

print(f'The most popular genre {filltered_genres}')

#visualisation
plt.figure(figsize=(12,6))
sns.barplot(data=filltered_genres, x='count',y='console', hue='genre', palette='viridis')
plt.xlabel('Number of Games')
plt.ylabel('Console')
plt.title('Most Popular Genre per Console')
#plt.show()

























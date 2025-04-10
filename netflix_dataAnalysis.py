import pandas as pd
import os
df = pd.read_csv(r"C:\Users\Dell\Desktop\Python\Projects\chatbot_project\netflix_titles.csv")


# print(df)
# print(len(df))
# print(df[df.show_id=='s5023'])
# print(max(df.show_id.str.len()))
# print(max(df.rating.dropna().str.len()))
# print(max(df.type.dropna().str.len()))
# print(max(df.title.dropna().str.len()))
# print(max(df.director.dropna().str.len()))
# print(max(df.cast.dropna().str.len()))
# print(max(df.country.dropna().str.len()))
# print(max(df.duration.dropna().str.len()))
# print(max(df.listed_in.dropna().str.len()))
# print(max(df.description.dropna().str.len()))
# print(df.head())
# print(df[df.show_id=='s5023'])

# print(df.isna().sum())

# -------------------------------Analysis---------------------------------
df['title_upper'] = df['title'].str.upper()
df_cleaned = df.drop_duplicates(subset=['title_upper', 'type'])
# print(df_cleaned)
df_cleaned['date_added'] = pd.to_datetime(df_cleaned['date_added'], errors='coerce')
df_cleaned['duration'] = df_cleaned['duration'].fillna(df_cleaned['rating'])  
netflix = df_cleaned[['show_id', 'type', 'title', 'date_added', 'release_year', 'rating', 'duration', 'description']]
# print(netflix)
netflix_genre = df[['show_id', 'listed_in']].copy()
# print(netflix_genre)
netflix_genre['genre'] = netflix_genre['listed_in'].str.split(',')
# print(netflix_genre['genre'])
netflix_genre = netflix_genre.explode('genre')
# print(netflix_genre)
netflix_genre['genre'] = netflix_genre['genre'].str.strip()
# print(netflix_genre['genre'])

netflix_directors = df[['show_id', 'director']].dropna()
# print(netflix_directors)

netflix_country = df[['show_id', 'country']].dropna()
# print(netflix_country)

# ----------------------------------------Analysis1-----------------------------------
df1 = netflix.merge(netflix_directors, on='show_id')
director_counts = df1.groupby(['director', 'type'])['show_id'].nunique().unstack(fill_value=0)
director_counts = director_counts[(director_counts['Movie'] > 0) & (director_counts['TV Show'] > 0)]
# print(director_counts)

df2 = netflix.merge(netflix_genre, on='show_id').merge(netflix_country, on='show_id')
comedy_movies = df2[(df2['genre'] == 'Comedies') & (df2['type'] == 'Movie')]
top_country = comedy_movies['country'].value_counts().idxmax()
# print(top_country)

df3 = df1[df1['type'] == 'Movie'].copy()
df3['year_added'] = df3['date_added'].dt.year
top_directors_per_year = (
    df3.groupby(['year_added', 'director'])['show_id'].count().reset_index(name='movie_count')
)
top_directors_per_year = top_directors_per_year.sort_values(['year_added', 'movie_count'], ascending=[True, False])
top_director_each_year = top_directors_per_year.groupby('year_added').first().reset_index()
# print(top_director_each_year)

df4 = netflix.merge(netflix_genre, on='show_id')
df4 = df4[df4['type'] == 'Movie'].copy()
df4['duration_num'] = df4['duration'].str.replace(' min', '', regex=False).astype(float)
avg_duration = df4.groupby('genre')['duration_num'].mean().reset_index(name='avg_duration')
# print(avg_duration)

df5 = df1.merge(netflix_genre, on='show_id')
df5 = df5[(df5['type'] == 'Movie') & (df5['genre'].isin(['Comedies', 'Horror Movies']))]

pivot = df5.groupby(['director', 'genre'])['show_id'].nunique().unstack(fill_value=0)
both_genres = pivot[(pivot['Comedies'] > 0) & (pivot['Horror Movies'] > 0)].reset_index()
both_genres.rename(columns={'Comedies': 'no_of_comedy', 'Horror Movies': 'no_of_horror'}, inplace=True)
# print(both_genres)

# ---------------------------Visulization-----------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

top_avg_duration = avg_duration.sort_values(by='avg_duration', ascending=False).head(10)
sns.barplot(x='avg_duration', y='genre', data=top_avg_duration)
plt.title('Top 10 Genres by Average Movie Duration')
plt.xlabel('Average Duration (min)')
plt.ylabel('Genre')
plt.show()







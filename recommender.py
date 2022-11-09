import pandas as pd
import random

movie_list_df = pd.read_csv('movie_list_df.csv')
MOVIES = list(movie_list_df['movies'])

print(random.sample(MOVIES, 10))
import numpy as np
import pandas as pd


def get_rating_matrix(filename):
    df_movie = pd.read_csv(filename)
    movie_table = df_movie.pivot_table(
    values = ["rating"],
    index = df_movie.source,
    columns = df_movie.target,
    aggfunc="sum",
    fill_value=0
)
    return movie_table.values
    


def get_frequent_matrix(filename, dtype=np.float32):
    pass

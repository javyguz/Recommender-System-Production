import pandas as pd
import numpy as np


# Function to recommend by content based
def recommend(s, data, title):

    # Convert the index into series
    indices = pd.Series(data.index, index=data['title'])

    # Get the index corresponding to original_title
    try:
        idx = indices[title]
    except:
        column_names = ['title', 'image']
        empty_df = pd.DataFrame(columns=column_names)
        print("error, empty df")

    if type(idx) == np.int64:
        movie_indices = s.loc[idx]

    else:
        movie_indices = s.loc[idx[-1]]

    # Top 5 book recommendation
    rec = pd.DataFrame(data[['title', 'image_url']].iloc[movie_indices])

    return rec

import pandas as pd


# Function to recommend by content based
def recommend(sg, data, title):
    # Convert the index into series
    indices = pd.Series(data.index, index=data['title'])

    # Get the index corresponding to original_title
    try:
        idx = indices[title]
    except:
        column_names = ['title', 'image', 'subjects']
        empty_df = pd.DataFrame(columns=column_names)
        print("error, empty df")
        return empty_df

    # Get the pairwsie similarity scores
    sig = list(enumerate(sg[idx]))

    # Sort the books
    sig = sorted(sig, key=lambda x: x[1], reverse=True)

    # Scores of the 5 most similar books
    sig = sig[1:6]

    # Book indicies
    movie_indices = [i[0] for i in sig]

    # Top 5 book recommendation
    rec = pd.DataFrame(data[['title', 'image', 'subjects']].iloc[movie_indices])

    return rec
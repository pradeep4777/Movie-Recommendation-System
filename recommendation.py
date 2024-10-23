import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie dataset
movies_data = pd.read_csv("movies.csv")

selected_features = ["genres", "keywords", "tagline", "cast", "director"]

# Fill missing values with empty strings
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna("")

# Combine features into a single string
combined_features = (
    movies_data["genres"]
    + " "
    + movies_data["keywords"]
    + " "
    + movies_data["tagline"]
    + " "
    + movies_data["cast"]
    + " "
    + movies_data["director"]
)

# Convert text data to numerical vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Calculate similarity between movies
similarity = cosine_similarity(feature_vectors)


# Function to get movie recommendations
def get_movie_recommendations(movie_name):
    list_of_all_titles = movies_data["title"].tolist()
    close_matches = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not close_matches:
        return []

    close_match = close_matches[0]
    index_of_movie = movies_data[movies_data.title == close_match].index[0]
    similarity_scores = list(enumerate(similarity[index_of_movie]))
    sorted_similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i, movie in enumerate(sorted_similar_movies[1:11], start=1):
        index = movie[0]
        recommended_movie = movies_data.loc[index, "title"]
        recommended_movies.append(recommended_movie)

    return recommended_movies

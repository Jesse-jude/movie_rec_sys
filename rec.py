import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Loading data from csv file
movies_data = pd.read_csv("movies.csv")

#printing the first 5 rows of the data
movies_data.head()

#number of rows and columns in the data frame
movies_data.shape

#selecting a relevant features 
selected_features = ['genres', 'keywords', 'tagline', 'cast','director']
print(selected_features)

#replacing the null values with null strings
for features in selected_features:
    movies_data[features] = movies_data[features].fillna('')

#combining all the selected features into a single string
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
print(combined_features)

#initializing TfidfVectorizer to convert text to feature vectors
vectorizer = TfidfVectorizer()

#fitting and transforming the combined features to create feature vectors
feature_vectors  = vectorizer.fit_transform(combined_features)
print(feature_vectors)

#getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)
print(similarity)

#getting the movie name from the user
mov_name = input("enter your fav movie: ")

#creating a list with all the movies given in the data set
list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

#finding the close match for the movie name given by the user
find_close_values = difflib.get_close_matches(mov_name, list_of_all_titles)
print(find_close_values)

# Check if a close match was found
if not find_close_values:
    print("No close match found. Please try another movie.")
else:
    #getting the first and closest match
    close_match = find_close_values[0]
    print(close_match)

    #finding the index of the movie with the matched title
    index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    print(index_of_movie)

    #getting a list of similarity scores for the selected movie
    similarity_score = list(enumerate(similarity[index_of_movie]))
    print(similarity_score)

    #sorting the movies based on their similarity score in descending order
    sorted_similar_movies = sorted(similarity_score, key=lambda x:x[1], reverse = True)
    print(sorted_similar_movies)

    #print the name of similar movies based on the index
    print('Movies Suggested For You: ')
    i = 1
    # loop through the sorted list and print the top 30 movies
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['title'].values[0]
        if (i <= 30):
            print(i, '.',title_from_index)
            i+=1
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    api_key = "1b16bd917e05ee3b7dd27db3bed1b03d"
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    )
    data = response.json()
    if 'poster_path' in data:
        return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    else:
        return "https://via.placeholder.com/400x600.png?text=No+Poster+Available"


def recommend(movie, movies_data):
    movie_index = movies_data[movies_data['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies_data.iloc[i[0]].id
        recommended_movies.append(movies_data.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# Load data
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list['movie_id'] = movies_list.index
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("MOVIE RECOMMENDER SYSTEM")

selected_movie_name = st.selectbox(
    "How would you like to be recommended?",
    movies_list['title'].values
)

if st.button("Show Recommendation"):
    recommendations, posters = recommend(selected_movie_name, movies_list)

    cols = st.columns(5)
    for idx, (name, poster) in enumerate(zip(recommendations, posters)):
        with cols[idx]:
            st.image(poster)
            st.write(name)
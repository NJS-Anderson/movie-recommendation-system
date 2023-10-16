import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    # Here we store the vectors for a given movie that tells how similar it is to other movies and finding the top 5 similar movies leaving the first that is itself
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies





movies_dict = pickle.load(open("C:\\Users\\mayank\\OneDrive\\Desktop\\codeey\\project\\youtube project\\move-recommender-system\\movie_dict.pkl",'rb'))
movies= pd.DataFrame(movies_dict)
st.title('Movie Recommender System')

similarity = pickle.load(open("C:\\Users\\mayank\\OneDrive\\Desktop\\codeey\\project\\youtube project\\move-recommender-system\\similarity.pkl",'rb'))


selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

# st.write('You selected:', option)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

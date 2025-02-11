import streamlit as st
import pickle
import pandas 

def recommend(movie):
    movie_data = []
    
    movie_index = dataframe[dataframe['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1] )[1:6]

    for i in movie_list:
        temp = dataframe.iloc[i[0]]['title']
        movie_data.append(temp)
    return movie_data

dataframe = pickle.load(open('movie.pkl', 'rb'))
print(type(dataframe))
movie_list = dataframe['title']

similarity = pickle.load(open('simi.pkl', 'rb'))

st.title("Movie recommendation system")

selected_movie_name = st.selectbox(
    'Select the movie Please', movie_list 
)

if st.button("recommend") :
    data = recommend(selected_movie_name)
    for i in data :
        st.write(i)

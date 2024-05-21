import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import NearestNeighbors
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Spotify API credentials
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
    

df = pd.read_pickle('music_df.pkl')

numerical_columns = df.select_dtypes(include=['float64']).columns
df_numerical = df[numerical_columns]

# Scale the combined feature set
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numerical)

knn = NearestNeighbors(n_neighbors = 5, algorithm='auto')
knn.fit(df_scaled)

def find_similar_songs(track_name, n_neighbors=5):
    try:
        track_index = df.index[df['Track'] == track_name][0]
    except IndexError:
        return [], []  # Return empty lists if the track is not found

    # Get the k-nearest neighbors
    distances, indices = knn.kneighbors([df_scaled[track_index]], n_neighbors=n_neighbors+1)
    
    recommended_music_names = []
    recommended_music_posters = []
    
    # Exclude the first index as it is the song itself
    similar_songs_indices = indices.flatten()[1:]
    
    for idx in similar_songs_indices:
        # Get the artist and track name using the index
        artist = df.iloc[idx].Artist
        track = df.iloc[idx].Track
        
        # Append the track name and album cover URL to the respective lists
        recommended_music_names.append(track)
        recommended_music_posters.append(get_song_album_cover_url(track, artist))
    
    return recommended_music_names, recommended_music_posters

st.title(':red[Music] :orange[Reco]:green[mmen]:blue[dation] :violet[System]')

music_list = df['Track'].values
selected_music = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    st.header('Similar songs by other Artists', divider='rainbow')
    recommended_music_names,recommended_music_posters = find_similar_songs(selected_music)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
        
        
    one_hot_encoder = OneHotEncoder()
    artist_encoded = one_hot_encoder.fit_transform(df[['Artist']]).toarray()

    # Combine numerical features and artist encoded features
    df_combined = np.hstack((df_numerical, artist_encoded))

    # Scale the combined feature set
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_combined)
    
    knn = NearestNeighbors(n_neighbors = 5, algorithm='auto')
    knn.fit(df_scaled)
    
    st.header('Similar songs by Same Artist', divider='rainbow')
    recommended_music_names,recommended_music_posters = find_similar_songs(selected_music)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
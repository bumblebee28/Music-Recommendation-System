Deployed App - https://mymusicrecommendationsystem.streamlit.app/

# Music Recommendation System

## Overview
This project implements a music recommendation system using machine learning algorithms and the Spotify API. It suggests similar songs by different artists as well as the same artist based on the input track selected by the user, considering various features such as danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, and the artist.

## Features
- Recommends similar songs based on selected input track.
- Considers both numerical features and artist information for recommendations.
- Utilizes the Spotify API to fetch album cover images for recommended songs.
- Allows users to interactively select a song from the dropdown menu and view recommendations.

## Technologies Used
- Python
- Streamlit: For building the interactive web application.
- scikit-learn: For machine learning algorithms and data preprocessing.
- Spotify API: For fetching track information and album cover images.

## Usage
1. Install the necessary Python dependencies listed in `requirements.txt`.
2. Obtain Spotify API credentials and replace `YOUR_SPOTIFY_CLIENT_ID` and `YOUR_SPOTIFY_CLIENT_SECRET` in the code.
3. Run the Streamlit app using the command `streamlit run app.py`.
4. Select a song from the dropdown menu and click the "Show Recommendation" button to view similar song recommendations.

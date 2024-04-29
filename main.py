import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import os 
import pandas as pd
from dotenv import load_dotenv


#----------
track_ids = []
track_name= []


#----------
#Take environment variables from .env file and scope
load_dotenv()  
client_id = os.getenv("Client_ID")
client_secret = os.getenv("Client_secret")
redirect_uri= os.getenv("redirect_uri")


#----------
sp = spotipy.Spotify(
                    auth_manager=SpotifyOAuth(client_id= client_id,
                                            client_secret=client_secret,
                                            redirect_uri= redirect_uri,
                                            scope='user-read-recently-played')
                    )

st.set_page_config(page_title="Spotify Extract&Analysis Project", page_icon="🎵")
st.title('Spotify API Project')
base="dark"



#----------
top_tracks = sp.current_user_recently_played(limit=50)
for idx, item in enumerate(top_tracks['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'], "-", track ['id'])
    track_ids.append(track['id'])
    track_name.append(track['name'])


#----------
audio_features = sp.audio_features(track_ids)
df = pd.DataFrame(audio_features)
df['track_name'] = track_name
df = df[['track_name', 'danceability', 'energy', 'valence']]
df.set_index('track_name', inplace = True)

#----------
st.subheader('Audio Features for my latest tracks')
st.bar_chart(df, height= 500)


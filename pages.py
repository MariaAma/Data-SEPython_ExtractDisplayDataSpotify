import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import pandas as pd
from collections import Counter
import time

global num
num = 0
client_id =''
client_secret = ''
df1 = None


def log():
    global num, client_id, client_secret
    st.session_state["client_id"] = ""
    st.session_state["client_secret"] = ""
    
    st.subheader(':red[On this login page:]')
    st.write(':red[You need to enter the Client ID and Client Secret each time you visit.]')
    client_id = st.text_input(":grey[Enter your Client ID]")
    client_secret = st.text_input(":grey[Enter your Client Secret]")
    if st.button(':red[Login in]'):
        if client_id and client_secret:
            global num
            num +=1
            st.write(":red[Client ID and User ID have been entered.]")
            st.write(":grey[It's time to dive into Analysis or Chatbot with the elements, you gave me.]")
            st.write(':red[Wait a minute to load data and then move on Analysis or Chatbot.]')
            sp_json()
        else: 
             st.write(':red[Please give a accurate Client ID and Client Secret.]')


def first_function():
        try:
                app()
        except:
                st.write(':grey[Wait a minute to load data.]')
                time.sleep(15)
                try: 
                     app1()
                except:
                    st.subheader(':red[Please give a accurate Client ID and Client Secret.]')
            

def sp_json():
        global client_secret, client_id, top_tracks, sp, counter, track_ids, track_name
        track_ids = []
        track_name= []
        artist_gerne = []
        top_tracks =[]

        redirect_uri= "http://localhost:3000"

        #----------
        sp = spotipy.Spotify(
                                auth_manager=SpotifyOAuth(client_id= client_id,
                                                        client_secret=client_secret,
                                                        redirect_uri= redirect_uri,
                                                        scope='user-read-recently-played')
                                )
        top_tracks = sp.current_user_recently_played(limit=50)
        
        #----------
        for item in top_tracks['items']:
                track = item['track']
                result = sp.search(track['artists'][0]['name'], limit=1, type="artist")
                artists = result["artists"]
                if artists["items"][0]["genres"] != []:
                    artist_gerne = artist_gerne + artists["items"][0]["genres"]
                
                track_ids.append(track['id'])
                track_name.append(track['name'])

        #----------
        d = Counter(artist_gerne)
        counter = dict(d)

def app():        
        global sp, df1, counter, track_ids, track_name,top_tracks

        #----------
        audio_features = sp.audio_features(track_ids)

        #----------
        st.title('Spotify API Project')
        st.write("This bar chart displays the latest 50 songs I've listened to on Spotify. It provides an overview of my current music trends by focusing on distinct tracks, regardless of how many times I play each song.")
        

        #----------
        audio_features = sp.audio_features(track_ids)
        df1 = pd.DataFrame(audio_features)
        df1['track_name'] = track_name
        df1 = df1[['track_name', 'danceability', 'energy', 'instrumentalness','speechiness', 'valence']]
        df1.set_index('track_name', inplace = True)


        #----------
        df2 = pd.DataFrame(counter.items(), columns=['Genre', 'Count'])


        #----------
        st.subheader('Audio Features for my latest tracks')
        st.bar_chart(df1, height= 400)
        st.write(df1)

        #----------
        st.subheader("Music Genre Counts")
        st.write("This bar chart displays the count of different music genres.")
        st.bar_chart(df2.set_index('Genre'), height= 400)
        st.write(df2)

def app1():
        #----------
        audio_features = sp.audio_features(track_ids)
        df1 = pd.DataFrame(audio_features)
        df1['track_name'] = track_name
        df1 = df1[['track_name', 'danceability', 'energy', 'instrumentalness','speechiness', 'valence']]
        df1.set_index('track_name', inplace = True)


        #----------
        df2 = pd.DataFrame(counter.items(), columns=['Genre', 'Count'])


        #----------
        st.subheader('Audio Features for my latest tracks')
        st.bar_chart(df1, height= 400)
        st.write(df1)

        #----------
        st.subheader("Music Genre Counts")
        st.write("This bar chart displays the count of different music genres.")
        st.bar_chart(df2.set_index('Genre'), height= 400)
        st.write(df2)


def chatbot():
    global consecutive_pairs, top_tracks,  df1, counter, track_ids, track_name,top_tracks, sp

    # Initialize session state to store chat history
    st.subheader(":red[------------:balloon: Welcome to the Chatbot Interface :balloon:]")
    
    st.write(":grey[-------------------------Please share information about the song you'd like to hear.]")
    st.write(":grey[-------------------------Use a scale from 0 to 1 to describe any of the following attributes: ]")
    st.write(":grey[-------------------------danceability, energy, instrumentalness,speechiness and valence.]")
    st.write(":grey[---------------Please note that numbers below 0 and above 1 are not accepted (max 2 decimal places).]")
    st.write(":grey[-----------------------------Also, do not concatenate or join the values with any symbol]")
    st.write(":grey[------------------------------such as a comma, underscore, or colon, or use capital letters.]")
    st.write(":grey[------------e.g. I want to hear a song with danceability close to 0.5 or danceability : 0.7 and 0.9 : energy.]")



    user_text = st.text_input('')
    st.button("Submit")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    try:
        audio_features = sp.audio_features(track_ids)
        df1 = pd.DataFrame(audio_features)
        df1['track_name'] = track_name
        df1 = df1[['track_name', 'danceability', 'energy', 'instrumentalness','speechiness', 'valence']]
        df1.set_index('track_name', inplace = True)

        user_text = user_text.split()
        remain_text = []
        
        for word in user_text:
            if word in {"danceability", "energy", "instrumentalness", "speechiness", "valence"}:
                remain_text.append(word)
            elif is_number(word):
                if len(word)<=4:
                 if float(word)<=1 and float(word)>=0 :
                    remain_text.append(word)

        if is_even(len(remain_text)) and len(remain_text)!=0:
            st.balloons()
            time.sleep(1)
            st.balloons()

            st.subheader(":grey[Thank you, please wait a minute to get the results.]")
            consecutive_pairs = [(remain_text[i], remain_text[i+1]) for i in range(len(remain_text) - 1) if is_even(i)]
            l=[]
            for pair in consecutive_pairs:
                if pair[0] =="danceability" or pair[1] == 'danceability':
                    if len(pair[1])< len(pair[0]):  
                        attribute = pair[0]
                        value = float(pair[1])
                        df1['danceability'] = (df1['danceability'] - value).abs()
                        df1['danceability'] = df1['danceability']**2
                        l.append('danceability')
                    else:
                        attribute = pair[1]
                        value = float(pair[0])
                        df1['danceability'] = (df1['danceability'] - value).abs()
                        df1['danceability'] = df1['danceability']**2
                        l.append('danceability')

                elif pair[0] =="energy" or pair[1] == 'energy':
                    if len(pair[1])< len(pair[0]):  
                        attribute = pair[0]
                        value = float(pair[1])
                        df1['energy'] = (df1['energy'] - value).abs()
                        df1['energy'] = df1['energy']**2
                        l.append('energy')

                    else:
                        attribute = pair[1]
                        value = float(pair[0])
                        df1['energy'] = (df1['energy'] - value).abs()
                        df1['energy'] = df1['energy']**2
                        l.append('energy')

                elif pair[0] =="instrumentalness" or pair[1] == 'instrumentalness':
                    if len(pair[1])< len(pair[0]):  # Εξασφαλίζει ότι η τιμή είναι αριθμητική
                        attribute = pair[0]
                        value = float(pair[1])
                        df1['instrumentalness'] = (df1['instrumentalness'] - value).abs()
                        df1['instrumentalness'] = df1['instrumentalness']**2
                        l.append('instrumentalness')

                    else:
                        attribute = pair[1]
                        value = float(pair[0])
                        df1['instrumentalness'] = (df1['instrumentalness'] - value).abs()
                        df1['instrumentalness'] = df1['instrumentalness']**2
                        l.append('instrumentalness')

                elif pair[0] =="speechiness" or pair[1] == 'speechiness':
                    if len(pair[1])< len(pair[0]):  # Εξασφαλίζει ότι η τιμή είναι αριθμητική
                        attribute = pair[0]
                        value = float(pair[1])
                        df1['speechiness'] = (df1['speechiness'] - value).abs()
                        df1['speechiness'] = df1['speechiness']**2
                        l.append('speechiness')

                    else:
                        attribute = pair[1]
                        value = float(pair[0])
                        df1['speechiness'] = (df1['speechiness'] - value).abs()
                        df1['speechiness'] = df1['speechiness']**2
                        l.append('speechiness')

                elif pair[0] =="valence" or pair[1] == 'valence':
                    if len(pair[1])< len(pair[0]):  # Εξασφαλίζει ότι η τιμή είναι αριθμητική
                        attribute = pair[0]
                        value = float(pair[1])
                        df1['valence'] = (df1['valence'] - value).abs()
                        df1['valence'] = df1['valence']**2
                        l.append('valence')

                    else:
                        attribute = pair[1]
                        value = float(pair[0])
                        df1['valence'] = (df1['valence'] - value).abs()
                        df1['valence'] = df1['valence']**2
                        l.append('valence')
                
            selected_df = df1[l]
            df1['Sum'] = selected_df.sum(axis=1)
            min_sum = df1['Sum'].min()
            row_with_min_sum = df1[df1['Sum'] == min_sum]
            row_with_min_sum.reset_index(inplace=True)

            message_printed = True
            track_min = row_with_min_sum['track_name'].tolist()[0]
                
            artist_chat =[]
            my_list = []
            for item in top_tracks['items']:
                    track = item['track']
                    if track_min in track['name']:
                            artist_chat.append(track)
                            if message_printed:
                                st.write("The song derived from the elements you gave me is:")
                                message_printed = False
                            for item in artist_chat:
                                if item['id'] not in my_list:
                                    st.write(item['artists'][0]['name']," - ", item['name'], "-", item['id'])
                                    my_list.append(item['id'])

        elif remain_text == []:
                st.subheader(':red[--------------You give me wrong text elements.]')
                st.subheader(':grey[-----------------------------------OR]')
                st.subheader(':red[--------------You didn\'t give any element at all.]')
                st.subheader(':grey[---------------------------Please try again:balloon:]')

    except:
        st.write(':grey[---------------------------------------------------Please, wait to load data.]')
        time.sleep(15)
        st.subheader(':red[-----------------Please, put Client ID and Client Secret.]')


def is_even(n):
    return n % 2 == 0 

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

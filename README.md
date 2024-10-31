# Spotify Audio Features Analysis with Spotipy

Spotify Audio Features Analysis with Spotipy
This project uses the Spotipy library to analyze the audio features of the last 50 songs a user has listened to on Spotify. By extracting key data such as danceability, energy, instrumentalness, speechiness, and valence, the project aims to provide insights into the user's music preferences and mood based on their recent listening history.

Users need to provide their Spotify client ID and client secret to authenticate and access the necessary data. Once authenticated, the program retrieves the user's recent listening history and analyzes each track's audio features.

In addition, the program allows users to interact with a texttbox where they can specify desired values for danceability, energy, instrumentalness, speechiness, and valence. Based on these criteria, the program identifies and returns the song from the recent listening history that best matches the given parameters.

With this information, users can better understand their music taste and possibly discover new tracks or artists that align with their preferences. This project is useful for those interested in gaining deeper insights into their Spotify listening habits and exploring music recommendations based on specific audio features.

# Technologies Used:
Python: Used for data retrieval and visualization.
Spotipy: Python library for interacting with the Spotify Web API.
Streamlit: Python library for building interactive web applications with ease.
OAuth: Secure authentication mechanism to access user-specific Spotify data.

# Examples with my Authentication and a demo playlist: [[playlist link](https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO)].

Homepage:

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_15_59 PM](https://github.com/user-attachments/assets/14d6c73c-22d5-41a6-b513-8a342e4765ce)

Authentication: This application performs automatic authentication with the Spotify API. However, users need to provide their client ID and client secret for the authentication process to proceed without active intervention:

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_16_23 PM](https://github.com/user-attachments/assets/90fbe677-f47f-4b65-8ced-6719c28cba22)

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 2_57_00 PM](https://github.com/user-attachments/assets/93166a3d-90e9-4731-af39-9f5a7f2235cc)


Data Retrieval: Retrieve the user's recently played tracks using Spotipy.
Audio Feature Extraction: This application extracts danceability, energy, instrumentalness, speechiness, and valence for each track, and identifies the genre or type of music associated with each artist. Users can access this information to explore and categorize music based on its genre or style.
Visualization: Plot the extracted audio features on a bar chart for analysis:

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_17_26 PM](https://github.com/user-attachments/assets/158265d5-a539-4a61-9230-10285ac51d37)

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_17_37 PM](https://github.com/user-attachments/assets/f74ee8e8-1c32-4cd3-9c0a-ddbd0d570809)

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_17_48 PM](https://github.com/user-attachments/assets/d529e241-3fa1-4eea-aa97-347226ab5e35)


Textbox: You can easily specify the danceability, energy, instrumentalness, speechiness, and valence you desire, and it will provide you with the closest song from the latest 50 songs you have heard:

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_17_56 PM](https://github.com/user-attachments/assets/78d888c1-3969-4511-a845-d1219d69fab7)

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_18_23 PM](https://github.com/user-attachments/assets/d721f3a2-4c6b-43ed-a7c1-06795790feef)

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_18_40 PM](https://github.com/user-attachments/assets/ea56e08b-8783-4b31-82be-c620fc428253)

Once you log in with a specific ClientID and ClientSecret, you cannot log in again using a different ClientID and ClientSecret unless you restart the application and wait for a few hours. Even if you restart the application and enter a new ClientID and ClientSecret, the cache will still cause the application to display the data retrieved from the previous session if you don't wait some time:

![Spotify Extract Analysis Project - Personal - Microsoft​ Edge 8_29_2024 3_19_03 PM](https://github.com/user-attachments/assets/fcf40d36-e461-4b84-9368-640a33bddabc)

# Third-Party Libraries and Licenses
This project uses the following libraries:

- **Spotipy**, which is licensed under the MIT License.
- **Streamlit**, which is licensed under the Apache 2.0 License.

# Contributions:
Contributions, feedback, and suggestions are welcome! Feel free to fork the repository, make improvements, and submit pull requests to enhance the project further.

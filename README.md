# In process, I'm making some changes to the project to enhance its functionality. These updates are not major overhauls, but they add more detail and fine-tuning to improve overall performance and user experience.

# Spotify Audio Features Analysis with Spotipy

Spotify Audio Features Analysis with Spotipy
This project uses the Spotipy library to analyze the audio features of the last 50 songs a user has listened to on Spotify. By extracting key data such as danceability, energy, instrumentalness, speechiness, and valence, the project aims to provide insights into the user's music preferences and mood based on their recent listening history.

Users need to provide their Spotify client ID and client secret to authenticate and access the necessary data. Once authenticated, the program retrieves the user's recent listening history and analyzes each track's audio features.

In addition, the program allows users to interact with a chatbox where they can specify desired values for danceability, energy, instrumentalness, speechiness, and valence. Based on these criteria, the program identifies and returns the song from the recent listening history that best matches the given parameters.

With this information, users can better understand their music taste and possibly discover new tracks or artists that align with their preferences. This project is useful for those interested in gaining deeper insights into their Spotify listening habits and exploring music recommendations based on specific audio features.

# Key Features:
Spotify Integration: Connects with the Spotify API to fetch the last 50 songs a user has listened to.
Audio Features Extraction: Retrieves and analyzes audio features for each song, including danceability, energy, instrumentalness, speechiness, and valence.
User Interaction: Includes a chatbox for users to enter desired values for the above-mentioned audio features, allowing them to explore their listening history based on specific criteria.
Song Matching: Compares the specified audio feature values against the user's recent listening history to find the song that best matches those criteria.
Music Preferences Analysis: Offers insights into the user's music preferences and listening patterns based on the audio features of their recently played songs.
Authentication: Requires Spotify client ID and client secret to authenticate and access user data, ensuring secure data retrieval.
Flexible Use Cases: Useful for exploring personal music tastes, discovering patterns in listening behavior, and creating custom music recommendations based on audio features.
Compatibility: Compatible with Python environments and relies on the Spotipy library for Spotify API interactions.

# Technologies Used:
Python: Used for data retrieval and visualization.
Spotipy: Python library for interacting with the Spotify Web API.
Streamlit: Python library for building interactive web applications with ease.
OAuth: Secure authentication mechanism to access user-specific Spotify data.

# Example Usage:
Authentication: Authenticate your application with Spotify API using OAuth to access user data.
Data Retrieval: Retrieve the user's recently played tracks using Spotipy.
Audio Feature Extraction: Extract danceability, energy, instrumentalness, speechiness, and valence for each track.
Visualization: Plot the extracted audio features on a bar chart for analysis and interpretation.

# Contributions:
Contributions, feedback, and suggestions are welcome! Feel free to fork the repository, make improvements, and submit pull requests to enhance the project further.

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

# Examples with my Authentication and a demo playlist: [[playlist link](https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO)].

Homepage:

![Spotify Extract Analysis Project - Προσωπικό - Microsoft​ Edge 6_5_2024 7_32_03 μμ](https://github.com/MariaAma/Data-SEPython_ExtractDisplayDataSpotify/assets/79280783/ff48ea20-3860-4073-8504-07d504606376)

Authentication: This application performs automatic authentication with the Spotify API. However, users need to provide their client ID and client secret for the authentication process to proceed without active intervention:

![Spotify Extract Analysis Project - Προσωπικό - Microsoft​ Edge 6_5_2024 7_32_15 μμ](https://github.com/MariaAma/Data-SEPython_ExtractDisplayDataSpotify/assets/79280783/b3ef1b38-d472-4733-a056-cc2fef25b528)

Data Retrieval: Retrieve the user's recently played tracks using Spotipy.
Audio Feature Extraction: This application extracts danceability, energy, instrumentalness, speechiness, and valence for each track, and identifies the genre or type of music associated with each artist. Users can access this information to explore and categorize music based on its genre or style.
Visualization: Plot the extracted audio features on a bar chart for analysis and interpretation:

![Spotify Extract Analysis Project - Προσωπικό - Microsoft​ Edge 13_5_2024 6_20_25 μμ](https://github.com/MariaAma/Data-SEPython_ExtractDisplayDataSpotify/assets/79280783/c694024e-a0bd-4cb9-ad2e-2f0596d2d130)

![Spotify Extract Analysis Project - Προσωπικό - Microsoft​ Edge 13_5_2024 6_20_39 μμ](https://github.com/MariaAma/Data-SEPython_ExtractDisplayDataSpotify/assets/79280783/8b37676c-c08c-47db-a043-3b5d24817e2d)

![Spotify Extract Analysis Project - Προσωπικό - Microsoft​ Edge 13_5_2024 6_20_53 μμ](https://github.com/MariaAma/Data-SEPython_ExtractDisplayDataSpotify/assets/79280783/0881095e-03cc-4149-b8df-33336d66fbda)

Chatbot: You can easily specify the danceability, energy, instrumentalness, speechiness, and valence you desire, and it will provide you with the closest song from the latest 50 songs you have heard:

![Spotify Extract Analysis Project - Προσωπικό - Microsoft​ Edge 6_5_2024 7_32_38 μμ](https://github.com/MariaAma/Data-SEPython_ExtractDisplayDataSpotify/assets/79280783/d98877d8-7b35-402c-9169-b91e465a25be)

![Spotify Extract Analysis Project - Προσωπικό - Microsoft​ Edge 13_5_2024 6_29_43 μμ](https://github.com/MariaAma/Data-SEPython_ExtractDisplayDataSpotify/assets/79280783/62619a37-ca8a-4753-ac7b-6eaa6239f828)




# Contributions:
Contributions, feedback, and suggestions are welcome! Feel free to fork the repository, make improvements, and submit pull requests to enhance the project further.

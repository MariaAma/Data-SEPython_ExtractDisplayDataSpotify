import streamlit as st

def app():
    base="dark"
    st.title(':red[**Welcome!**]')
    st.subheader(":grey[Let\'s dive in—no snorkel required!]")
    st.write(":grey[This project compain Data Engineer & Software Engineer!]")
    st.write(':red[Keep in mind that the whole project has to do with API, so it needs some time to load the dataset.]')

    image_url = 'https://images.unsplash.com/flagged/photo-1579965852521-492eea74ef02?q=80&w=1834&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    st.image(image_url, caption='Photo from Unsplash - Created by Norbert Buduczki')

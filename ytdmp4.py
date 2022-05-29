import streamlit as st
from pytube import YouTube
import os

st.title("Youtube Video Donwloader")
st.subheader("Enter the URL:")
url = st.text_input(label='URL')
yt = YouTube(url)
print(yt.streams)
if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(yt.title, yt.length, yt.rating))
    video = yt.streams
    if len(video) > 0:
        downloaded = False
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio MP3")
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Completed....")
    else:
        st.subheader("Sorry, this audio can not be downloaded")

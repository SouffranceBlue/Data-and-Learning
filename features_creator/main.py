import streamlit as st
from audio_tools import record, save_record



st.markdown("**Recording features**")
stop = st.button(f"Click to stop recording")
start = st.b(f"Click to record")
counter = 0
st.text("It is going to be started the microphone")
while not stop:
    myrecording = record(10,44100)
    path_myrecording = f"./own_features/feature({counter})"
    save_record(path_myrecording, myrecording,44100)
    counter += 1
    

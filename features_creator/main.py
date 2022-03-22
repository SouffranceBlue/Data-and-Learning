import streamlit as st
from audio_tools import record, save_record



st.markdown("**Recording features**")
stop = st.button(f"Click to stop recording")
start = st.button(f"Click to record")
counter = 9165
st.text("RECORDING FEATURES🔴🔴")
while not stop:
    myrecording = record(10,44100)
    path_myrecording = f"./own_features/feature({counter})"
    save_record(path_myrecording, myrecording,44100)
    counter += 1
    

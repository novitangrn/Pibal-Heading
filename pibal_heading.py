import streamlit as st
from datetime import datetime

def generate_output():
    tanggal = datetime.now().strftime("%d")
    hour = datetime.now().hour

    if 0 <= hour < 12:
        jam = "06"
    elif 12 <= hour < 24:
        jam = "12"
    else:
        jam = "00"

    UPID = "UPID53" + " " + "WARR" + " " + str(tanggal).zfill(2) + str(jam).zfill(2) + "00"
    PPAA = "PPAA" + " " + str(50 + int(tanggal)) + str(jam).zfill(2) + "1" + " " + "96935"
    UGID = "UGID53" + " " + "WARR" + " " + str(tanggal).zfill(2) + str(jam).zfill(2) + "00"
    PPBB = "PPBB" + " " + str(50 + int(tanggal)) + str(jam).zfill(2) + "1" + " " + "96935"

    output = UPID + "\n" + PPAA + "\n\nNNNN\n\n" + UGID + "\n" + PPBB + "\n\nNNNN"

    return output

# Streamlit app
st.title("Pilot Balloon Heading")
output = generate_output()

# Display real-time datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M")
st.write(f"Current Datetime: {formatted_datetime}")

# Display generated output
st.code(output, language="python")

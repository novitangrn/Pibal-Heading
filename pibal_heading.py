import streamlit as st
from datetime import datetime

def automate_generate_output():
    date_now = datetime.now().strftime("%d")
    hournow = datetime.now().hour

    if 0 <= hournow < 12:
        hour_now = "06"
    elif 12 <= hournow < 24:
        hour_now = "12"
    else:
        hour_now = "00"

    UPID = "UPID53" + " " + "WARR" + " " + str(date_now).zfill(2) + str(hour_now).zfill(2) + "00"
    PPAA = "PPAA" + " " + str(50 + int(date_now)) + str(hour_now).zfill(2) + "1" + " " + "96935"
    UGID = "UGID53" + " " + "WARR" + " " + str(date_now).zfill(2) + str(hour_now).zfill(2) + "00"
    PPBB = "PPBB" + " " + str(50 + int(date_now)) + str(hour_now).zfill(2) + "1" + " " + "96935"

    output = UPID + "\n" + PPAA + "\n\nNNNN\n\n" + UGID + "\n" + PPBB + "\n\nNNNN"

    return output

def manual_generate_output(tanggal, jam):
    UPID = "UPID53" + " " + "WARR" + " " + str(tanggal).zfill(2) + str(jam).zfill(2) + "00"
    PPAA = "PPAA" + " " + str(50 + int(tanggal)) + str(jam).zfill(2) + "1" + " " + "96935"
    UGID = "UGID53" + " " + "WARR" + " " + str(tanggal).zfill(2) + str(jam).zfill(2) + "00"
    PPBB = "PPBB" + " " + str(50 + int(tanggal)) + str(jam).zfill(2) + "1" + " " + "96935"

    output = UPID + "\n" + PPAA + "\n\nNNNN\n\n" + UGID + "\n" + PPBB + "\n\nNNNN"

    return output

# Streamlit app
st.title("Pilot Balloon Heading")

# Sidebar
sidebar_option = st.sidebar.radio("Choose Output Generation", ("Manual", "Automated"))

if sidebar_option == "Manual":
    # User input
    tanggal = st.number_input("Enter the tanggal (1-31):", min_value=1, max_value=31, value=1, step=1)
    jam = st.selectbox("Select the jam:", options=["06", "12"])

    # Generate output based on user input
    manual_output = manual_generate_output(tanggal, jam)

    # Display generated output
    st.code(manual_output, language="markdown")

else:
    # Generate output automatically
    automate_output = automate_generate_output()

    # Display generated output
    st.code(automate_output, language="markdown")

# Display real-time datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M")
st.write(f"Current Datetime: {formatted_datetime}")

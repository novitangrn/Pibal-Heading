import streamlit as st
from datetime import datetime

def manual_generate_output(tanggal, jam):
    UPID = "UPID53" + " " + "WARR" + " " + str(tanggal).zfill(2) + str(jam).zfill(2) + "00"
    PPAA = "PPAA" + " " + str(50 + int(tanggal)) + str(jam).zfill(2) + "1" + " " + "96935"
    UGID = "UGID53" + " " + "WARR" + " " + str(tanggal).zfill(2) + str(jam).zfill(2) + "00"
    PPBB = "PPBB" + " " + str(50 + int(tanggal)) + str(jam).zfill(2) + "1" + " " + "96935"

    output = UPID + "\n" + PPAA + "\n\nNNNN\n\n" + UGID + "\n" + PPBB + "\n\nNNNN"

    return output

def automate_generate_output():
    tanggal = datetime.now().strftime("%d")
    hour = datetime.now().hour

    if 0 <= hour < 12:
        jam = "06"
    elif 12 <= hour < 24:
        jam = "18"
    else:
        jam = "00"

    output = manual_generate_output(tanggal, jam)

    return output


# Streamlit app
st.title("Pilot Balloon Heading")

# Sidebar
sidebar_option = st.sidebar.radio("Generate Output", ("Manual", "Automated"))

if sidebar_option == "Manual":
    # User input
    tanggal = st.number_input("Masukkan tanggal (1-31):", min_value=1, max_value=31, value=1, step=1)
    jam = st.selectbox("Masukkan jam:", options=["06", "18"])

    # Generate output based on user input
    date_now = datetime.now().strftime("%d")
    if tanggal == int(date_now):
        manual_output = manual_generate_output(tanggal, jam)
        st.success("Heading siap digunakan.")

    else:
        manual_output = manual_generate_output(tanggal, jam)
        st.error("Tanggal tidak sesuai dengan tanggal hari ini.")

else:
    # Generate output automatically
    automate_output = automate_generate_output()

    # Display generated output
    st.code(automate_output, language="markdown")
    st.success("Heading PIBAL siap digunakan.")

# Display real-time datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M")
st.write(f"Current Datetime: {formatted_datetime}")

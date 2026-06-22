import streamlit as st

st.title("Data Preprocessing")

st.write("Preprocessing page")

import streamlit as st

st.title("📊 Data Preprocessing")

left, center, right = st.columns([1,2,1])

with left:

    st.subheader("Selected Data")

    st.multiselect(
        "Features",
        [
            "Latitude",
            "Longitude",
            "Cu",
            "Pb",
            "Zn",
            "Ni",
            "Co",
            "Fe"
        ]
    )

with center:

    st.subheader("Map View")

    st.info("Map Preview")

with right:

    st.subheader("Preprocessing")

    st.checkbox("Remove Null Values")
    st.checkbox("Remove Duplicates")
    st.checkbox("Standardization")
    st.checkbox("Log Transform")
    st.checkbox("MinMax Scaling")

    st.button("Show Anomaly Map")

st.title("Data Preprocessing")

if "geochem_raw" not in st.session_state:

    st.warning("Upload data first")

else:

    df = st.session_state["geochem_raw"]

    st.success("Data received")

    st.write(df.head())

st.write(st.session_state["geochem_raw"].head())

if st.button("Next ➜"):
    st.switch_page("pages/3_Feature_Engineering.py")

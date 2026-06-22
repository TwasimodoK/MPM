
import streamlit as st

st.title("Fusion")

if "geochem_result" in st.session_state:

    st.success("Geochem results available")

else:

    st.warning("Run clustering first")

if st.button("Next ➜"):
    st.switch_page("pages/3_Feature_Engineering.py")

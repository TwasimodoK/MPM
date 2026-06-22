
import streamlit as st

st.title("Fusion")

if "geochem_result" in st.session_state:

    st.success("Geochem results available")

else:

    st.warning("Run clustering first")

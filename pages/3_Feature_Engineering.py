import streamlit as st

st.title("Feature Engineering")

left,center,right = st.columns([1,2,1])

with left:

    st.subheader("Selected Data")

    st.checkbox("Geochemistry",True)
    st.checkbox("Gravity")
    st.checkbox("Magnetic")

with center:

    st.subheader("Display")

    st.info("Plots appear here")

with right:

    st.subheader("Feature Engineering")

    st.selectbox(
        "Geochemistry",
        [
            "None",
            "CLR",
            "ILR",
            "RPCA",
            "Robust PCA"
        ]
    )

    st.selectbox(
        "Geophysics",
        [
            "None",
            "VD",
            "ASVD",
            "Log Transform"
        ]
    )

    st.checkbox("Normalize")
    st.checkbox("Correlation Filter")

st.button("Next")

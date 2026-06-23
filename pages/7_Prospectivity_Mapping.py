import streamlit as st

st.title("Mineral Prospectivity Mapping")

left,center,right = st.columns([1,2,1])

with left:

    clusters = st.multiselect(
        "Prospective Clusters",
        [
            "Cluster 1",
            "Cluster 2",
            "Cluster 3",
            "Cluster 4"
        ]
    )

    mineral = st.selectbox(
        "Mineral",
        [
            "Copper",
            "Gold",
            "Nickel",
            "REE"
        ]
    )

with center:

    st.subheader("Prospectivity Map")

    st.info("Interactive map")

with right:

    st.metric(
        "High Prospectivity Area",
        "18.5%"
    )

    st.button("Generate Map")

    st.download_button(
        "Download CSV",
        data="sample"
    )

if st.button("Next ➜"):
    st.switch_page("pages/app.py")

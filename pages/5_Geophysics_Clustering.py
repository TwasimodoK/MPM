import streamlit as st

st.title("Geophysical_Clustering")

left,center,right = st.columns([1,2,1])

with left:

    algorithm = st.radio(
        "Algorithm",
        [
            "SOM",
            "GMM",
            "SOM + GMM",
            "Hybrid SOM + GMM"
        ]
    )

with center:

    st.subheader("Cluster Map")

    st.info("Cluster visualization")

with right:

    st.subheader("Parameters")

    n_clusters = st.slider(
        "Clusters",
        2,
        15,
        5
    )

    som_grid = st.slider(
        "SOM Grid",
        5,
        30,
        10
    )

st.button("Run Clustering")

from algorithms.geophysical import run_geophysical_pipeline

import streamlit as st

st.title("Geophysical Clustering")

if st.button("Run Geophysical Pipeline"):

    df = st.session_state["geophysical_raw"]

    result = run_geophysical_pipeline(df)

    st.session_state["geophysical_result"] = result

    st.success("Completed")
from algorithms.geophysical import run_geophysical_pipeline

if st.button("Run Geochem"):

    result = run_geophysical_pipeline(
        st.session_state["geophysical_raw"]
    )

    st.session_state["geophysical_result"] = result

    st.success("Done")
    
if st.button("Next ➜"):
    st.switch_page("pages/3_Feature_Engineering.py")

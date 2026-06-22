import streamlit as st

st.title("Geochemical_Clustering")

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

from algorithms.geochem import run_geochem_pipeline

import streamlit as st

st.title("Geochemical Clustering")

if st.button("Run Geochem Pipeline"):

    df = st.session_state["geochem_raw"]

    result = run_geochem_pipeline(df)

    st.session_state["geochem_result"] = result

    st.success("Completed")
from algorithms.geochem import run_geochem_pipeline

if st.button("Run Geochem"):

    result = run_geochem_pipeline(
        st.session_state["geochem_raw"]
    )

    st.session_state["geochem_result"] = result

    st.success("Done")
    
if st.button("Next ➜"):
    st.switch_page("pages/3_Feature_Engineering.py")

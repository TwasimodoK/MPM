import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="MPM Dashboard",
    page_icon="⛏️",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("Mineral Prospectivity Mapping Dashboard")

st.divider()

# ---------------- LAYOUT ---------------- #

left, center, right = st.columns([1, 2.5, 1])

# ================= LEFT PANEL ================= #

with left:

    st.subheader("📂 Data Input")

    csv_file = st.file_uploader(
        "Upload Geochemical CSV",
        type=["csv"]
    )

    shp_file = st.file_uploader(
        "Upload Shapefile ZIP",
        type=["zip"]
    )

    raster_file = st.file_uploader(
        "Upload Raster",
        type=["tif", "tiff"]
    )

    st.markdown("---")

    st.subheader("🗂 Layers")

    geo = st.checkbox("Geochemistry", value=True)
    mag = st.checkbox("Magnetic")
    grav = st.checkbox("Gravity")
    fault = st.checkbox("Faults")
    lith = st.checkbox("Lithology")

# ================= CENTER PANEL ================= #

with center:

    st.subheader("🗺️ Map View")

    st.info(
        "Future Folium / Leaflet map will appear here"
    )

    if csv_file is not None:

        try:

            df = pd.read_csv(csv_file)

            # Save dataframe globally for all pages
            st.session_state["geochem_raw"] = df

            st.success("✅ CSV Loaded Successfully")

            st.dataframe(
                df,
                use_container_width=True,
                height=500
            )

        except Exception as e:

            st.error(f"Error reading file: {e}")

# ================= RIGHT PANEL ================= #

with right:

    st.subheader("⚙️ Filters")

    algorithm = st.selectbox(
        "Algorithm",
        [
            "SOM + GMM",
            "Random Forest",
            "XGBoost",
            "K-Means"
        ]
    )

    mineral = st.selectbox(
        "Target Mineral",
        [
            "Copper",
            "Gold",
            "Nickel",
            "Lithium",
            "REE"
        ]
    )

    cluster = st.multiselect(
        "Clusters",
        [
            "Cluster 1",
            "Cluster 2",
            "Cluster 3",
            "Cluster 4",
            "Cluster 5"
        ]
    )

    st.markdown("---")

    if st.button("Run Analysis"):
        st.success(
            f"Running {algorithm}"
        )

# ---------------- FOOTER ---------------- #

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    if "geochem_raw" in st.session_state:
        samples = len(st.session_state["geochem_raw"])
    else:
        samples = 0

    st.metric("Samples", samples)

with col2:
    st.metric("Layers", "5")

with col3:
    st.metric("Status", "Ready")

# ---------------- NEXT PAGE ---------------- #

if "geochem_raw" in st.session_state:

    st.success("Dataset ready for preprocessing")

    if st.button("Next ➜ Preprocessing"):

        st.switch_page("pages/2_Preprocessing.py")

import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap


# Fetches data from the provided URL
@st.cache_data
def fetch_data(base_url, max_records):
    all_data = gpd.GeoDataFrame()
    offset = 0

    while True:
        query_params = {
            "where": "VACIND%20%3D%20'Y'",
            "outFields": "PIN,VACIND",
            "outSR": "4326",
            "f": "geojson",
            "resultOffset": offset,
            "resultRecordCount": max_records,
        }
        query_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in query_params.items()])}"
        data_chunk = gpd.read_file(query_url)
        if data_chunk.empty:
            break
        all_data = pd.concat([all_data, data_chunk], ignore_index=True)
        offset += max_records
    gdf = all_data.to_crs(epsg=3857)
    gdf["geometry"] = gdf["geometry"].centroid
    gdf = gdf.to_crs(epsg=4326)
    return gdf


# Streamlit application start
def main():
    st.title("Vacant Properties Heatmap")
    base_url = "https://geodata.baltimorecity.gov/egis/rest/services/CityView/Realproperty_OB/FeatureServer/0/query"
    max_records = 1000

    gdf = fetch_data(base_url, max_records)

    # Slider for user input
    radius = st.sidebar.slider("Radius", 5, 30, 5)
    blur = st.sidebar.slider("Blur", 1, 30, 7)
    min_opacity = st.sidebar.slider("Min Opacity", 0.0, 1.0, 0.3, 0.1)

    # Create a folium map
    m = folium.Map(
        location=[gdf.geometry.y.mean(), gdf.geometry.x.mean()],
        tiles="cartodbpositron",
        zoom_start=11,
    )

    heat_data = [
        [row["geometry"].y, row["geometry"].x] for index, row in gdf.iterrows()
    ]
    HeatMap(
        heat_data,
        radius=radius,
        blur=blur,
        min_opacity=min_opacity,
        max_zoom=13,
    ).add_to(m)
    st_folium(m, width=800, height=600)


if __name__ == "__main__":
    main()

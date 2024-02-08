# Vacant Properties Heatmap Application

This Python application utilizes Streamlit, GeoPandas, and Folium to visualize the heatmap of vacant properties in Baltimore. It fetches geospatial data from Baltimore's open data server and displays it in an interactive map.

## Features

- Interactive map visualization using Folium.
- Data fetched in real-time from Baltimore's open data server.
- User controls for adjusting the heatmap's radius, blur, and minimum opacity.
- Real-time data fetching with caching to improve performance.

## Installation

To run this application, you need to have Python installed along with the following libraries:
- streamlit
- geopandas
- pandas
- folium
- streamlit_folium

You can install these packages using pip:

```bash
pip install streamlit geopandas pandas folium streamlit_folium
```
Usage
1. Clone the repository or download app.py.
2. Run the Streamlit application
```bash
streamlit run app.py
```
3. Adjust the heatmap settings using the sliders in the sidebar.

## Functionality
The application's main functionality includes:

Fetching geospatial data from a specified URL.
Converting the data into a GeoDataFrame.
Visualizing the data on an interactive map using Folium.
## Code Overview
`fetch_data`: Fetches data from the provided URL and returns a GeoDataFrame.

`main`: The main function of the Streamlit app, which includes the creation of the map and Streamlit widgets.
Data Source
The application fetches data from Baltimore's open data server. The data includes the location of vacant properties in the city.

## Author
Developed by Will Fedder, in collaboration with the Maryland Institute for Progressive Policy

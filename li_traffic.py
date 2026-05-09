import pandas as pd
import plotly.express as px

LI_511_Events = pd.read_csv('/Users/newman789/Downloads/511_NY_Events__Beginning_2010_20260501.csv')

LI_511_Events["Create Time"] = pd.to_datetime(
    LI_511_Events ["Create Time"],
    format="%m/%d/%Y %I:%M:%S %p",
    errors="coerce"
)

li_traffic = LI_511_Events.sort_values("Create Time", ascending = True)
li_traffic.to_csv("/Users/newman789/Downloads/LI_Traffic_Incidents.csv", index=False)

valid_lat = []
invalid_lat = []

min_lat = 40.34
max_lat = 41.09
min_lon = -73.67
max_lon = -71.87

def valid_latitude(li_traffic, min_lat, max_lat):
    filtered_li_traffic = li_traffic[(li_traffic["Latitude"] >= min_lat) & (li_traffic["Latitude"] <= max_lat)]
    return filtered_li_traffic
      
def valid_longitude(li_traffic, min_long, max_long):
    filtered_li_traffic = li_traffic[(li_traffic["Longitude"] >= min_long) & (li_traffic["Longitude"] <= max_long)]
    return filtered_li_traffic

li_traffic = valid_latitude(li_traffic, min_lat, max_lat)
li_traffic = valid_longitude(li_traffic, min_lon, max_lon)
li_traffic = li_traffic[
    ~li_traffic["Event Type"].isin([
        "disabled train",
        "accident, misplaced tractor trailer",
        "accident investigation, pedestrian accident",
        "fuel spill, overturned truck"
    ])
]

li_traffic.to_csv("/Users/newman789/Downloads/LI_Traffic_Incidents.csv", index=False)

fig = px.scatter_mapbox(li_traffic, 
                        lat="Latitude", 
                        lon="Longitude", 
                        hover_name="Event Type", 
                        color="Event Type",
                        mapbox_style="carto-positron", 
                        center={"lat": 40.8, "lon": -73.3},
                        zoom = 9,
                        color_discrete_map = {"accident":"red", "disabled vehicle": "orange", "tractor trailer fire":"black"},
                        title = ("Long Island Traffic Incidents Throughout the Years"), 
                        hover_data = ["Event Type", "Facility Name", "Direction", "City", "County", "Create Time", "Close Time", "Event Description", "Georeference"])


fig.update_layout(
    hoverlabel=dict(
        font_size=10
    )
)

fig.update_layout(
    title=dict(
        text="Long Island Traffic Incidents",
        font=dict(color="red", size=50)
    )
)


fig.show()


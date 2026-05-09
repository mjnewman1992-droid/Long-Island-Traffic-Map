# Long Island Traffic Map

This project is an interactive Python map of traffic incidents across Long Island, New York, with a focus on Nassau and Suffolk counties.

## Project Overview

The goal of this project is to visualize Long Island traffic incidents on an interactive map using real incident data. Each point on the map represents one incident, and the hover information shows details such as the event type, facility name, direction, city, county, time, and event description.

## Data Source

The data comes from New York State traffic incident data and was cleaned in Python before being mapped.

## Features

- Interactive map of Long Island traffic incidents
- One point per incident
- Points plotted using latitude and longitude
- Event types shown with color
- Hover information for each incident
- Data cleaning for date/time and coordinate filtering

## Tools Used

- Python
- pandas
- Plotly Express

## Current Workflow

The script currently:

1. Loads the traffic incident dataset
2. Converts the `Create Time` column to datetime format
3. Sorts incidents by date and time
4. Filters incidents by latitude and longitude bounds for Long Island
5. Removes selected unwanted event types
6. Creates an interactive map with hover details

## File

- `li_traffic.py` — main Python script for cleaning the data and building the map

## Future Improvements

- Add better event type grouping
- Improve color choices for event categories
- Add filters for county, city, or event type
- Turn the map into a full interactive dashboard

## Author

Michael Newman


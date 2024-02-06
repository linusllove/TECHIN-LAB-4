import streamlit as st
from datetime import datetime
import pytz

# Title of the web app
st.title('World Clock')

# Selection box for locations
locations = ['Asia/Tokyo', 'Europe/London', 'America/New_York', 'Australia/Sydney']
selected_locations = st.multiselect('Select up to 4 locations:', locations, default=locations[0])

# Display time for selected locations
for location in selected_locations:
    timezone = pytz.timezone(location)
    time = datetime.now(timezone)
    st.write(f"Time in {location}: {time.strftime('%Y-%m-%d %H:%M:%S')}")

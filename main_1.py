# 1. Make api request to https://random-data-api.com/api/v2/blood_types?size=100&response_type=json to get the data
# MANIS SAHA

import requests
import pandas as pd

# URL for the API request
url = "https://random-data-api.com/api/v2/blood_types?size=100&response_type=json"

# Making the request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Convert data to DataFrame for table representation
    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)
else:
    print(f"Failed to retrieve data: {response.status_code}")

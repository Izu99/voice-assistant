import re
import requests
from bs4 import BeautifulSoup

def find_temperature(command):
    # Extract the location from the user's command
    match = re.search(r"(?<=temperature\s)(?:in\s)?(\w+)|(\w+)\stemperature", command)
    location = match.group(1) or match.group(2) or match.group(3)

    # Construct the search query
    search = f"temperature in {location}"

    # Send a request to Google and parse the response
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")

    # Extract the temperature from the response
    temp = data.find("div", class_="BNeawe").text

    # Return the temperature along with the location
    return f"{location} temperature is {temp}"

# Example usage:


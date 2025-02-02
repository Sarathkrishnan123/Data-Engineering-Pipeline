import requests
import json

url = 'https://www.olx.in/api/relevance/v4/search?category=84&facet_limit=100&location=2001160&location_facet_limit=20&platform=web-desktop&relaxedFilters=true&size=40&user=18c8aba1820xe792f74&lang=en-IN'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.5'
}

req = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if req.status_code == 200:
    # Parse the JSON response
    data = req.json()

    # Save the JSON data to a local file
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
    
    print("JSON data saved to 'output.json'")
else:
    print(f"Request failed with status code {req.status_code}")

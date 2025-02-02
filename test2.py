import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Import the webdriver manager
import time

# Initialize the webdriver using webdriver manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL of OLX website
url = 'https://www.olx.in/'

# Open OLX website
driver.get(url)

# Wait for the page to load (you might need to adjust the waiting time)
time.sleep(2)

# Locate the search box and enter a search query
search_box = driver.find_element(By.NAME, 'q')
search_query = 'your_search_query'
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

# Extract data from the search results
results = driver.find_elements(By.CLASS_NAME, 'IKo3_')

# Create a list to store the results
data_list = []

# Extract information and add to the list
for result in results:
    title = result.text
    # You can extract other information here
    
    # Store the information in a dictionary
    data_dict = {
        'title': title,
        # Add other fields as needed
    }
    
    # Add the dictionary to the list
    data_list.append(data_dict)

# Close the browser window
driver.quit()

# Convert the list of dictionaries to JSON
json_data = json.dumps(data_list, indent=2)

# Print or save the JSON data
print(json_data)

# If you want to save the JSON data to a file
# with open('olx_data.json', 'w') as json_file:
#     json_file.write(json_data)

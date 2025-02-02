'''
def car_details(json_data):
    id_values = []
    data = json_data.get("data", [])
    for item in data:
        item_id = item.get("id")
        if item_id is not None:
            id_values.append(item_id)
    return id_values
def get_title(json_data):
    titles = []
    data = json_data.get("data", [])
    for item in data:
        title = item.get("title")
        if title is not None:
            titles.append(title)
    return titles
def get_km_driven(json_data):
    km_driven_values = []
    data = json_data.get("data", [])
    for item in data:
        parameters = item.get("parameters", [])
        km_driven_value = None
        for param in parameters:
            if param.get("key_name") == "KM driven":
                km_driven_value = param.get("value_name")
                break
        if km_driven_value is not None:
            km_driven_values.append(km_driven_value)
    return km_driven_values
def get_fuel_type(json_data):
    fuel_values = []
    data = json_data.get("data", [])
    for item in data:
        parameters = item.get("parameters", [])
        fuel_value = None
        for param in parameters:
            if param.get("key_name") == "Fuel":
                fuel_value = param.get("value_name")
                break
        if fuel_value is not None:
            fuel_values.append(fuel_value)
    return fuel_values
'''
import pandas as pd
from read_json import read_json1

def get_additional_details(json_data):
    years = []
    fuels = []
    transmissions = []
    owners = []
    vehicle_names = []
    km_driven_values = []
    currencies = []
    prices = []
    
    data = json_data.get('data', [])
    
    for item in data:
        parameters = item.get("parameters", [])
        year, fuel, transmission, owner, make, model, variant, km_driven_value = [None] * 8
        price_info = item.get("price", {}).get("value", {})
        currency = price_info.get("currency", {}).get("iso_4217")
        price = price_info.get("raw")
        
        for param in parameters:
            key_name = param.get("key_name")
            value_name = param.get("value_name")
            value = param.get("value")
            
            if key_name == "Year":
                year = value_name
            elif key_name == "Fuel":
                fuel = value_name
            elif key_name == "Transmission":
                transmission = value_name
            elif key_name == "No. of Owners":
                owner = value_name
            elif key_name == "Brand":
                make = value_name
            elif key_name == "Model":
                model = value_name
            elif key_name == "Variant":
                variant = value_name
            elif key_name == "KM driven":
                km_driven_value = value_name
        
        vehicle_name = f"{make} {model} {variant}"
        
        years.append(year)
        fuels.append(fuel)
        transmissions.append(transmission)
        owners.append(owner)
        vehicle_names.append(vehicle_name)
        km_driven_values.append(km_driven_value)
        currencies.append(currency)
        prices.append(price)
        
    car_details_df = pd.DataFrame({
        "Year": years,
        "Fuel": fuels,
        "Transmission": transmissions,
        "No. of Owners": owners,
        "Vehicle Name": vehicle_names,
        "KM driven": km_driven_values,
        "Currency": currencies,
        "Price": prices
    })
    
    #car_details_df.to_csv('car_details.csv', index=False, encoding='utf-8')  # Specify encoding here
    
    print("DataFrame saved to car_details.csv")
    
    return car_details_df






    
f
    



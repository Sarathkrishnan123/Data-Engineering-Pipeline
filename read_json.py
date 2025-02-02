import json

def read_json1(file_path):
    '''
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return json_data
        '''
    
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file '{file_path}': {e}")
        return None

'''
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Unable to decode JSON from file '{file_path}'.")
        return None    
# Example usage:
#file_path = "output.json"  # Replace 'data.json' with the path to your JSON file
#json_dict = read_json(file_path)
#car=car_details(json_data)
#if json_dict is not None:
    #print(json_dict)
'''

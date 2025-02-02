from read_json import read_json1
from derive_df import get_additional_details
from pg_load import load_data_frame_to_postgresql
from notification import send_notification
import asyncio
if __name__ == "__main__":
    # Path to the JSON file
    file_path = r'C:\Users\91949\Desktop\data pipeline\output.json'
    json_data = read_json1(file_path)
    if json_data:
    # Proceed with further processing
        pass
    else:
    # Handle the case where JSON data couldn't be read
        pass
    
    # Derive DataFrame from JSON data
    car_details_df = get_additional_details(json_data)
    
    # Connection string for PostgreSQL
    connection_string = 'postgresql://postgres:admin@localhost:5432/test'
    
    # Table name in PostgreSQL
    table_name = 'car_details'
    
    # Load DataFrame into PostgreSQL
    status,text = load_data_frame_to_postgresql(car_details_df, table_name, connection_string)
    
    if status == "success":
        print("DataFrame loaded into PostgreSQL successfully.")
        # Send success notification
        bot_token = "7068520741:AAHI4JOmZmB8VEwiSp8GMddFQhWIoVm8OnA"
        chat_id = "-1001859293149"
        message = "success."
        asyncio.run(send_notification(bot_token, chat_id, message))
    else:
        print("Failed to load DataFrame into PostgreSQL.")
        # Send failure notification
        bot_token = "7068520741:AAHI4JOmZmB8VEwiSp8GMddFQhWIoVm8OnA"
        chat_id = "-1001859293149"
        message = "Failed to load"
        asyncio.run(send_notification(bot_token, chat_id, message))

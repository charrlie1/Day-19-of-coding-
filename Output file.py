try:
    file_handle = open("meter_readings.txt", 'r')
    all_data = file_handle.read()
    print("--- Entire file content ---")
    print(all_data)
    file_handle.close()
except FileNotFoundError:
    print("Error: meter_readings.txt not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#This code reads the entire content of meter_readings.txt as a single string and then prints it

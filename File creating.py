try:
    file_handle = open("meter_readings.txt", 'w')
    file_handle.write("Timestamp, Consumption (kW)\n")  # Write a header
    file_handle.write("2025-04-29 21:00:00, 1.23\n")
    file_handle.write("2025-04-29 21:05:00, 1.18\n")
    file_handle.write("2025-04-29 21:10:00, 1.25\n")
    file_handle.close()
    print("Data written to meter_readings.txt")
except Exception as e:
    print(f"An error occurred: {e}")
#This code creates a new file named meter_readings.txt (or overwrites it if it already exists) and writes the header and some initial smart meter readings to it.

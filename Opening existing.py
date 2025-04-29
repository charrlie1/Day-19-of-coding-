try:
    file_handle = open("meter_readings.txt", 'r')
    print("File meter_readings.txt opened for reading.")
    file_handle.close()
except FileNotFoundError:
    print("Error: meter_readings.txt not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#
This code attempts to open the meter_readings.txt file in read mode. If the file exists, it opens it; otherwise, it raises

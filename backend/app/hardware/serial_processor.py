import serial

arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

def read_data():
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()  # Read a line, decode it and remove extra spaces
            print(f"Received Data: {data}")
            process_data(data)

def process_data(data):
    try:
        parts = data.split(',')
        if len(parts) == 15:
            joyXValue = float(parts[0])
            joyYValue = float(parts[1])
            latitude = float(parts[2])
            latitudeDirection = parts[3]
            longitude = float(parts[4])
            longitudeDirection = parts[5]
            voltage = float(parts[6])
            current = float(parts[7])
            satellite = float(parts[8])
            day = parts[9]
            month = int(parts[10])
            year = int(parts[11])
            adjustedHour = int(parts[12])
            adjustedMinute = int(parts[13])
            second = int(parts[14])
            
            print(f"Processed Data: Heart Rate - {joyXValue}, Oxygen Level - {joyYValue}")
        else:
            print("Invalid data format")
    except ValueError as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    read_data()

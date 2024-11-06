import serial
import time

# Initialize the serial port to communicate with Arduino
# Make sure to replace 'COM3' with your actual port (for Windows) or '/dev/ttyUSB0' (for Linux/Raspberry Pi)
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for the Arduino to initialize

def read_data():
    while True:
        # Read a line from the Arduino
        data = arduino.readline().decode('utf-8').strip()

        # If the line is not empty
        if data:
            # Print the received data to the terminal
            print(f"Received Data: {data}")
            # Parse the temperature and light level from the received data
            if "Temperature:" in data and "Light Level:" in data:
                try:
                    temperature = float(data.split("Temperature:")[1].split(",")[0].strip())
                    light_level = int(data.split("Light Level:")[1].strip())
                    print(f"Temperature: {temperature:.2f} °C")
                    print(f"Light Level: {light_level} %")
                except ValueError as e:
                    print("Error parsing data:", e)
        time.sleep(1)  # Wait a bit before reading the next data

if __name__ == '__main__':
    try:
        read_data()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
        arduino.close()

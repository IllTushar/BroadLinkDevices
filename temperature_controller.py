import broadlink as bl
from typing import List
from temp_model import Model  # Assuming Model is a class that contains device details
'''
When you connect broadlink device then disable the lock info from the broadlink app
otherwise auth issue occurs 
'''
if __name__ == "__main__":
    # Discover Broadlink devices on the network
    devices = bl.discover(timeout=5)

    if not devices:
        print("No Broadlink devices found.")
        exit()

    # Print discovered devices and store their information
    for item in devices:
        print(f"Discovered device: {item}")
        print("Device Details:")
        print(f"  Host: {item.host[0]}")  # Correctly access the IP address from the tuple
        print(f"  MAC Address: {item.mac.hex()}")  # MAC address in hexadecimal
        print(f"  Device Type: {hex(item.devtype)}")  # This prints the device type as a hex string
      
    for item in devices:
        host = item.host  # Device IP address (host already contains the tuple)
        mac = bytearray.fromhex(item.mac.hex())  # Device MAC address (hex)
        device_type = item.devtype  # Device type should be an integer (no need to convert to hex)

        # Ensure host is passed as a tuple (IP address, port)
        if isinstance(host, tuple):
            host = host[0], host[1]  # Extract tuple elements if needed (IP address and port)
        else:
            host = (host, 80)  # Default port 80 if host is not a tuple

        try:
            # Initialize the device using the device's type, host, and MAC address
            device = bl.gendevice(device_type, host, mac)

            # Authenticate with the device (without passing a password)
            if device.auth():  # No argument needed
                print("Authentication successful.")
            else:
                print("Authentication failed. This may indicate an incorrect password or a setup issue.")
                exit()
          

            # Fetch temperature and humidity data (if supported)
            try:
                data = device.check_sensors()  # Ensure your device supports this function
                temperature = data.get("temperature", "N/A")
                humidity = data.get("humidity", "N/A")
                print(f"Temperature: {temperature}°C")
                print(f"Humidity: {humidity}%")
            except AttributeError:
                print("This device does not support sensor data.")
            except Exception as e:
                print(f"Error while fetching sensor data: {e}")

        except Exception as e:
            print(f"Error initializing device: {e}")

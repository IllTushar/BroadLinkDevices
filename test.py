import broadlink as bl

# Discover Broadlink devices
devices = bl.discover(timeout=5)

if not devices:
    print("No Broadlink devices found.")
else:
    for device in devices:
        print(f"Found device: {device}")
        try:
            # Authenticate with the device
            if device.auth():
                print("Authentication successful!")
            else:
                print("Authentication failed!")
        except Exception as e:
            print(f"Error during authentication: {e}")

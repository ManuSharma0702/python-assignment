import subprocess
import os
import requests
def create_virtual_device(avd_name="TestDevice"):
    """Create a virtual device (AVD) using the Android Emulator."""
    print("Creating virtual device...")
    try:
        # Ensure proper system image path
        subprocess.run([
            "avdmanager", "create", "avd", "-n", avd_name, "-k", "system-images;android-35;google_apis;x86_64", "--force"
        ], shell=True)
        print(f"Virtual device '{avd_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual device: {e}")
        exit(1)

def start_emulator(avd_name="TestDevice"):
    """Launch the virtual device using the emulator."""
    print("Starting the emulator...")
    emulator_path = os.path.join(os.environ.get("ANDROID_SDK_ROOT", ""), "emulator", "emulator.exe")
    if not os.path.exists(emulator_path):
        print(f"Emulator executable not found at {emulator_path}. Check ANDROID_SDK_ROOT.")
        exit(1)
    process = subprocess.Popen([
        emulator_path, "-avd", avd_name, "-no-snapshot-load", "-no-boot-anim"
    ])
    return process


def install_apk(apk_path, device_serial="emulator-5554"):
    """Install a sample APK into the virtual device."""
    print(f"Installing APK: {apk_path}")
    try:
        subprocess.run([
            "adb", "-s", device_serial, "install", apk_path
        ], check=True)
        print("APK installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing APK: {e}")

def get_system_info(device_serial="emulator-5554"):
    """Retrieve system information from the virtual device."""
    print("Fetching system information...")
    try:
        os_version = subprocess.check_output([
            "adb", "-s", device_serial, "shell", "getprop ro.build.version.release"
        ]).decode().strip()
        model = subprocess.check_output([
            "adb", "-s", device_serial, "shell", "getprop ro.product.model"
        ]).decode().strip()
        memory = subprocess.check_output([
            "adb", "-s", device_serial, "shell", "cat /proc/meminfo"
        ]).decode().splitlines()[0]
        system_info = {
            "app_name": model,
            "version": os_version,
            "description": memory
        }
        print(f"System Info: {system_info}")
        return system_info
    except subprocess.CalledProcessError as e:
        print(f"Error fetching system information: {e}")
        return {}
    
def send_data_to_server(system_info, server_url):
    """Send system information to the backend server and log the response."""
    print(f"Sending data to server: {server_url}")
    try:
        response = requests.post(server_url, json=system_info)
        response.raise_for_status()
        print(f"Server response: {response.json()}")
    except requests.RequestException as e:


        print(f"Error connecting to server: {e}")
from utils import *

def main():
    avd_name = "VirtualAndroid"
    apk_path = "C:/Users/USER/python_assignment/android/UC Browser-Safe, Fast, Private_13.9.0.1328_APKPure.apk"  # Replace with the path to your APK file
    server_url = "http://127.0.0.1:5000/add-app"
    # Step 1: Create Virtual Device
    create_virtual_device(avd_name)

    # Step 2: Start Emulator
    emulator_process = start_emulator(avd_name)

    # Wait for the emulator to boot
    while True:
        try:
            boot_completed = subprocess.check_output([
                "adb", "shell", "getprop sys.boot_completed"
            ], stderr=subprocess.DEVNULL).decode().strip()
            if boot_completed == "1":
                print("Emulator booted successfully.")
                break
        except subprocess.CalledProcessError:
            pass

    # Step 3: Install APK
    install_apk(apk_path)

    # Step 4: Retrieve and Log System Information
    system_info = get_system_info()

    send_data_to_server(system_info, server_url)

    # Terminate emulator
    input("Press Enter to close the emulator...")
    emulator_process.terminate()

if __name__ == "__main__":
    # Set ANDROID_SDK_ROOT if not already set
    if "ANDROID_SDK_ROOT" not in os.environ:
        os.environ["ANDROID_SDK_ROOT"] = "C:/Users/USER/AppData/Local/Android/Sdk"
    main()

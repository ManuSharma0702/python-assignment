Setup and Run Instructions for the Virtual Android System Script
This script automates the setup, launch, and interaction with a virtual Android device. It includes steps to create an Android Virtual Device (AVD), start an emulator, retrieve system info, and send data to a backend server.

Prerequisites
Android SDK and Emulator Tools

Install Android Studio or the standalone Android SDK command-line tools.
Ensure the following tools are installed and accessible via PATH:
adb
emulator
avdmanager
Configure the ANDROID_HOME environment variable pointing to your SDK location (e.g., C:\Users\<USER>\AppData\Local\Android\Sdk).
Python Environment

Python 3.7 or higher.
Install required Python libraries:
```bash
pip install requests
```
Backend Server

Ensure a backend server is running on http://127.0.0.1:5000/api/device-info.
The server should accept POST requests with JSON payloads.
Sample APK

Place the APK file you want to install on the virtual device. Update the apk_path variable in the script with the APK file's path.
Setup Steps
Clone or Copy the Script

Copy the Python script to your working directory and save it as test.py.
Configure Environment Variables

Add the Android SDK to your system's PATH.
Set the ANDROID_HOME environment variable to the SDK directory.

Windows:
```bash
set ANDROID_HOME=C:\Users\<USER>\AppData\Local\Android\Sdk
set PATH=%PATH%;%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\emulator;%ANDROID_HOME%\cmdline-tools\latest\bin
```
Linux/Mac:
```bash
export ANDROID_HOME=~/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/cmdline-tools/latest/bin
```

Create Required Directories

Ensure that the ~/.android/avd directory exists for storing AVDs.
Run the Script
Launch the Script Run the script using Python:

```bash
python test.py
```

Steps Performed by the Script

Create a Virtual Device: Uses avdmanager to create an AVD named VirtualAndroid.
Start Emulator: Launches the Android Emulator.
Install APK: Installs the APK specified in the apk_path.
Fetch Device Info: Collects OS version, device ID, and model info using adb.
Send Data to Server: Sends system information to the specified backend server URL.
Terminate Emulator

The emulator will continue running until you press Enter in the console.
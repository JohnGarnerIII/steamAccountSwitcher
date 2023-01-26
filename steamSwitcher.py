import os
import subprocess

# Kill any running Steam process
subprocess.call(["taskkill.exe", "/F", "/IM", "steam.exe"])

# Clear the console
os.system("cls")

# Print menu
print("Select your account")
print("=======================================")
print("1) Main")
print("2) Second")

# Get user input
account = input("Select: ")

# Set the username based on the user's choice
# Where it says "username", type in your Steam username
username = ""
if account == "1":
    username = "username"
elif account == "2":
    username = "username"

# Add the AutoLoginUser and RememberPassword keys to the registry
subprocess.call(["reg", "add", "HKCU\\Software\\Valve\\Steam", "/v", "AutoLoginUser", "/t", "REG_SZ", "/d", username, "/f"])
subprocess.call(["reg", "add", "HKCU\\Software\\Valve\\Steam", "/v", "RememberPassword", "/t", "REG_DWORD", "/d", "1", "/f"])

# Start Steam
subprocess.call(["start", "steam://open/main"])

# Exit script
exit()
import os
import subprocess
from tkinter import *

def select_account():
    # Kill any running Steam process
    subprocess.call(["taskkill.exe", "/F", "/IM", "steam.exe"])

    # Get the selected account
    account = var.get()

    # Set the username based on the user's choice
    username = ""
    if account == 1:
        username = "username1"
    elif account == 2:
        username = "username2"

    # Add the AutoLoginUser and RememberPassword keys to the registry
    subprocess.call(["reg", "add", "HKCU\\Software\\Valve\\Steam", "/v", "AutoLoginUser", "/t", "REG_SZ", "/d", username, "/f"])
    subprocess.call(["reg", "add", "HKCU\\Software\\Valve\\Steam", "/v", "RememberPassword", "/t", "REG_DWORD", "/d", "1", "/f"])

    # Start Steam
    os.startfile("steam://open/main")

    # Exit script
    exit()

root = Tk()
root.title("Select Steam Account")

var = IntVar()

main_account = Radiobutton(root, text="Main", variable=var, value=1)
main_account.pack()

second_account = Radiobutton(root, text="Second", variable=var, value=2)
second_account.pack()

select_button = Button(root, text="Select", command=select_account)
select_button.pack()

root.mainloop()
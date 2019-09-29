import os
from shutil import copyfile

### Get current working directory and set file locations ###
#print("Before starting, please ensure this is being run from the same directory as ssh and wpa_supplicant.conf")
cwd = os.getcwd()
wpa_default = cwd + "/default_wpa_supplicant.conf"
wpa_edit = cwd + "/edit_wpa_supplicant.conf"
wpa_proper = cwd + "/wpa_supplicant.conf"
ssh_file = cwd + "/ssh"

### Set paste directory and file names ###
paste_dir = "/Volumes/boot"
wpa_paste = paste_dir + "/wpa_supplicant.conf"
ssh_paste = paste_dir + "/ssh"

### Check if variables for wpa_supplicant.conf have been set before ###
wpa_check = os.path.isfile(wpa_proper)
if wpa_check:
    print("Using existing wpa_supplicant.conf file... If you are connecting to a new network delete that file and try again")
else:
    country = input("Please enter network country code (GB, US, FR, DE, SE, etc.): ")
    ssid = input("Please enter your case-sensitive SSID exactly as setup: ")
    password = input("Please enter your network's case-sesitive password: ")

    copyfile(wpa_default, wpa_edit)
    with open(wpa_edit, 'r') as file:
        wpa_text = file.read()
    wpa_text = wpa_text.replace('COUNTRY', country)
    wpa_text = wpa_text.replace('NETWORK_SSID', ssid)
    wpa_text = wpa_text.replace('PASSWORD', password)
    with open(wpa_edit, 'w') as file:
        file.write(wpa_text)
    copyfile(wpa_edit, wpa_proper)
    os.remove(wpa_edit)

### Copy wpa_supplicant.conf to `boot` ###
copyfile(wpa_proper, wpa_paste)
### Copy SSH file to `boot` ###
copyfile(ssh_file, ssh_paste)

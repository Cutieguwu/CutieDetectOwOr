from sys import exit
from os import name as osname

#Temporarily hard coded library into script

def init_lib():
    global threats
    threats = ["Fractureiser", "Skyrage"]

def init_lib_linux_filesearch():

    #Fractureiser
    global sus_linux_files_fractureiser
    sus_linux_files_fractureiser = ["~/.config/.data/lib.jar", "~/.config/systemd/user/systemd-utility.service", "/etc/systemd/system/systemd-utility.service"]
    
    #Skyrage
    global sus_linux_files_skyrage
    sus_linux_files_skyrage = ["/bin/vmd-gnu", "/etc/systemd/system/vmd-gnu.service"]

def init_lib_win_filesearch():

    #Fractureiser
    global sus_win_files_fractureiser
    sus_win_files_fractureiser = [r'%LOCALAPPDATA%\\Microsoft Edge\\libWebGL64.jar']

    #Skyrage
    global sus_win_files_skyrage
    sus_win_files_skyrage = [r'%AppData%\\Microsoft\\Start Menu\\Programs\\Startup\\jawaw.jar', r'%AppData%\\..\\LocalLow\\Microsoft\\Internet Explorer\\DOMStore\\microsoft-vm-core']

def init_lib_linux():
    print("Initializing Linux Library: File Locations")
    init_lib_linux_filesearch()
    print("Signature checks not implemented yet.")

def init_lib_win():
    init_lib_win_filesearch()
    print("Signature checks not implemented yet.")

def scan_linux():
    l = 0
    i = len(sus_linux_files_fractureiser)
    for i in sus_linux_files_fractureiser:
        print(i) #Do check for files. If not found raise exception filenotfound and continue to next without report. If found, report file found and possible related threat.
        l = l + 1

def run():

    init_lib()
    # if OS is Windows, do Windows inits and scan, elif OS is Linux, do Linux inits and scan

    if osname == "nt":
        print("Windows system detected.")
        print("Ending here; Not implemented yet.")
        exit()
    elif osname == "posix":
        print("Posix compliant (Linux) system detected")
        init_lib_linux()

        scan_linux()

        #Insert final summary here

        exit()
try:
    while True:
        run()
except KeyboardInterrupt:
    exit()
from sys import exit
from os import name as osname
from os import path

#Temporarily hard coded library into script

def init_lib_linux_filesearch():
   
    #Fractureiser
    global sus_linux_files_fractureiser
    sus_linux_files_fractureiser = [
        "~/.config/.data/lib.jar",
        "~/.config/systemd/user/systemd-utility.service",
        "/etc/systemd/system/systemd-utility.service"
    ]
    
    #Skyrage
    global sus_linux_files_skyrage
    sus_linux_files_skyrage = [
        "/bin/vmd-gnu",
        "/etc/systemd/system/vmd-gnu.service"
    ]

def init_lib_win_filesearch():

    #Fractureiser
    global sus_win_files_fractureiser
    sus_win_files_fractureiser = [
        r'%LOCALAPPDATA%\\Microsoft Edge\\libWebGL64.jar'
    ]

    #Skyrage
    global sus_win_files_skyrage
    sus_win_files_skyrage = [
        r'%AppData%\\Microsoft\\Start Menu\\Programs\\Startup\\jawaw.jar',
        r'%AppData%\\..\\LocalLow\\Microsoft\\Internet Explorer\\DOMStore\\microsoft-vm-core'
    ]

def init_lib_linux():
    print("Initializing Linux Library: File Locations")
    init_lib_linux_filesearch()
    print("NOTICE: Signature checks not implemented yet.")

def init_lib_win():
    init_lib_win_filesearch()
    print("NOTICE: Signature checks not implemented yet.")

def scan_linux():
    global threats
    global threats_names

    for i in range(len(threats)):                                                               #For each library, scan for each known sus file.
        current_search_object = threats[i]
        print("\n-- Scanning for", threats_names[i], " --")
        for l in range(len(current_search_object)):
            if path.exists(path.expanduser(current_search_object[l])) == True:                  #If sus file found, warn and add to list of found files for final summary.
                global threats_found

                threats_found = []
                threats_found.append(current_search_object[l])
                print(current_search_object[l], "Found in system. Possible threat detected!")
            else:
                pass

def scan_summary():
    global threats_found

    print("Scan returned", len(threats_found), "threats")

    if len(threats_found) > 0:
        for i in threats_found:
            print("FOUND:", i)
    else:
        pass

def run():
    if osname == "nt":                                                                          #If OS is Windows, do Windows inits and scan, elif OS is Linux, do Linux inits and scan.
        print("Windows system detected.")
        print("Ending here; Not implemented yet.")
        exit()
    elif osname == "posix":
        print("Posix compliant (Linux) system detected")
        init_lib_linux()
        global threats
        threats = [
            sus_linux_files_fractureiser, 
            sus_linux_files_skyrage
        ]
        global threats_names
        threats_names = [
            "Fractureiser {Files}",
            "Skyrage {Files}"
        ]

        scan_linux()

        scan_summary()

        exit()
try:
    while True:
        run()
except KeyboardInterrupt:
    exit()
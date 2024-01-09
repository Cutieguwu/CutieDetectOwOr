from os import name as osname, path

__DEBUG_RUN = True
__DEBUG_LIBRARY = False
__DEBUG_SCAN = False

class __DEBUG():
    def run(report1, report2=""):
        if __DEBUG_RUN == True:
            print("__DEBUG_RUN >>>", report1, report2)
    
    def library(report1, report2=""):
        if __DEBUG_LIBRARY == True:
            print("__DEBUG_LIBRARY >>>", report1, report2)
    
    def scan(report1, report2=""):
        if __DEBUG_SCAN == True:
            print("__DEBUG_SCAN >>>", report1, report2)

#Temporarily hard coded library into script

def init_lib_filesearch():
    __DEBUG.scan("Loading Library - Filesearch")

    #Fractureiser
    global sus_files_fractureiser
    sus_files_fractureiser = [
        "~/.config/.data/lib.jar",
        "~/.config/systemd/user/systemd-utility.service",
        "/etc/systemd/system/systemd-utility.service"
    ]
    
    #Skyrage
    global sus_files_skyrage
    sus_files_skyrage = [
        "/bin/vmd-gnu",
        "/etc/systemd/system/vmd-gnu.service"
    ]

def init_lib():
    print("Initializing Library: File Locations")
    init_lib_filesearch()
    print("NOTICE: Signature checks not implemented yet.")

def scan():
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

def scan_summary():
    global threats_found

    print("\nScan returned", len(threats_found), "threats")

    if len(threats_found) > 0:
        for _ in threats_found:
            print("FOUND:", _)

def run():
    __DEBUG.run("Checking OS")

    if osname == "nt":                                                                          #If OS is Windows, do Windows inits and scan, elif OS is Linux, do Linux inits and scan.
        __DEBUG.run("Windows system detected.")

        print("Ending here; Windows is not supported.")
        raise SystemExit

    elif osname == "posix":

        __DEBUG.run("Posix compliant (Linux) system detected")
        init_lib()

        global threats
        threats = [
            sus_files_fractureiser, 
            sus_files_skyrage
        ]
        global threats_names
        threats_names = [
            "Fractureiser {Files}",
            "Skyrage {Files}"
        ]

        scan()
        scan_summary()

        raise SystemExit
    else:
        __DEBUG.run("Unknown System detected. Exiting")


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        raise SystemExit
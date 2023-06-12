from sys import exit

#Need some form of OS detection for Windows vs Linux

def init_lib_linux_filesearch():
    sus_linux_files_fractureiser["~/.config/.data/lib.jar", "~/.config/systemd/user/systemd-utility.service", "/etc/systemd/system/systemd-utility.service"]
    sus_linux_files_skyrage["/bin/vmd-gnu", "/etc/systemd/system/vmd-gnu.service"]

def init_lib_win_filesearch():
    sus_win_files_fractureiser[r'%LOCALAPPDATA%\\Microsoft Edge\\libWebGL64.jar']
    sus_win_files_skyrage[r'%AppData%\\Microsoft\\Start Menu\\Programs\\Startup\\jawaw.jar', r'%AppData%\\..\\LocalLow\\Microsoft\\Internet Explorer\\DOMStore\\microsoft-vm-core']

def init_lib_linux():
    init_lib_linux_filesearch()
    print("Signature checks not implemented yet.")

def init_lib_win():
    init_lib_win_filesearch()
    print("Signature checks not implemented yet.")

# if OS is Windows, do Windows inits, elif OS is Linux, do Windows inits
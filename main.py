import os, sys
import time

import argparse

from smb.SMBConnection import SMBConnection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.sysUtils as u
import lib.logger

# Show Usage demo of this program
DEMO = False

# TODO: Variables that are parsed from cmd
ARGS = None

def CMDParam():
    ''' TODO: TEMPLATE
    To parse cmd parameters
    '''
    global ARGS
    parser = argparse.ArgumentParser(description='Manual to this script')
    parser.add_argument('--bhMode',
                        type=int,
                        default=1,
                        help="1, to directly run with local settings without user interface; \
                            0, to show a user interface. \
                            (default: show a user interface)")
    ARGS = parser.parse_args() == 1

def copy(src, dst, keyword="", fullCopy=True):
    '''
    Copy all matched files and folders from src to dst

    @param:
        - src - a folder names to be copied.
        - dst - a folder names to copy from src to.
        - keyword - a keyword to operate all matched target(can be regular expression).
        - full - True to fully copy; otherwise, copy increased file (default to True).
    '''
    if not os.path.isdir(dst):
        os.makedirs(dst)
    for name in u.searchFolder(src, keyword):
        src_name = os.path.join(src, name)
        dst_name = os.path.join(dst, name)
        u.copyFolder(src_name, dst_name, full=fullCopy)
        print("Copy Finished! from "+src_name+" to "+dst_name)

def main():
    '''
    Main Usage
    '''
    if DEMO:
        # TEMPLATE USAGE:
        #     copy all folders with name "lib" from folder "." to folder "a"
        #     (if folder "a" doesn't exit, then create a new folder named "a")
        copy(".", "a", "lib")

        # Copy folders from server(mapped network device)
        copy("A:\Dumps", "114514", "AMDVer_11_45_14114_5140")

    Manual_Program = int(input("Start with Manually Input Program?(\"1\":True; \"0\":False):"))==1
    while Manual_Program:
        src = input("Input source folder to be copied: ")
        dst = input("Input dest folder to copy to: ")
        keyword = input("Input keyword to search(can be Regular Expression): ")
        fullCopy = int(input("Increasing Copy?(\"1\":True; \"0\":False): "))==1
        copy(src, dst, keyword, fullCopy)
        print("Finished!\n")

    # Auto_Program = int(input("Start with Auto Program?(\"1\":True; \"0\":False):"))==1
    # if Auto_Program:
    try:
        print("\n***** Running Auto-Sync *****\n")
        src = input("Input source folder to be copied: ")
        dst = input("Input dest folder to copy to: ")
        keyword = input("Input keyword to search(can be Regular Expression): ")
        fullCopy = int(input("Increasing Copy?(\"1\":True; \"0\":False): "))==0
        timer = int(input("Auto-Syncing Time Period (in seconds):"))
        while True:
            copy(src, dst, keyword, fullCopy)
            print("Waiting for %s seconds..."%timer)
            time.sleep(timer)
    except Exception:
        print("ERROR OCCURRED!\n")

    print("Program finished!")
    input("PRESS ANYKEY TO QUIT:")

if __name__ == "__main__":
    main()
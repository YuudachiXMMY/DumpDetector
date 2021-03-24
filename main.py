import os, sys
import argparse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.logger
import lib.sysUtils as u

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

def copy(start, dest, keyword=""):
    '''
    Copy all matched files and folders from start to dest

    @param:
        - start - a folder names to be copied.
        - dest - a folder names to copy from start to.
        - keyword - a keyword to operate all matched target(can be regular expression).
    '''
    for name in u.searchFolder(start, keyword):
        u.copyFolder(name, dest)

def main():
    '''
    '''
    #TEMPLATE USAGE:
    #   copy all folders with name "lib" from folder "." to folder "a"
    #   (if folder "a" doesn't exit, then create a new folder named "a")
    copy(".", "a", "lib")

if __name__ == "__main__":
    '''
    '''
    main()
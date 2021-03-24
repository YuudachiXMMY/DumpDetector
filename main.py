import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.logger
import lib.sysUtils as u

def main():
    '''
    '''
    for name in u.searchFolder(".", "lib"):
        u.copyFolder(name, "tar")

if __name__ == "__main__":
    '''
    '''
    main()
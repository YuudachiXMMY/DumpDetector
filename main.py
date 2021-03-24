import os, sys
import argparse

from smb.SMBConnection import SMBConnection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.logger
import lib.sysUtils as u

USERNAME = None
PASSWORD = None
USERNAME = "amd\\haironwu"

ADDRESS = "win-q7pd8mubrg3.amd.com/oca/Dumps/"
HOST = "172.29.157.40"

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

def login():
    '''
    '''
    host=HOST
    username=USERNAME
    password=PASSWORD
    conn=SMBConnection(username, password, "mt-PC", "SP-STORAGE", use_ntlm_v2 = True)
    result = conn.connect(host, 445) #smb协议默认端口445
    print("登录成功")

def get_script_file():
    '''
    '''
    conn = SMBConnection('anonymous', '', 'mt-PC', 'SP-STORAGE', use_ntlm_v2 = True)
    assert conn.connect(HOST, 139)
    sharelist = conn.listShares()#列出共享目录
    for i in sharelist:
        print(i)
    file_obj = open('c:/2.txt', 'w')
    file_attributes, filesize = conn.retrieveFile('share', '/Test/test.txt', file_obj)
    file_obj.close()

def main():
    '''
    Main Usage
    '''
    # TEMPLATE USAGE:
    #     copy all folders with name "lib" from folder "." to folder "a"
    #     (if folder "a" doesn't exit, then create a new folder named "a")

    copy(".", "a", "lib")

if __name__ == "__main__":
    # main()
    login()
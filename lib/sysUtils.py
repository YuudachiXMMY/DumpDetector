import os, sys, subprocess, re
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.logger

logger = lib.logger.logger("utils")

def get_MD5(file_path):
    '''
    通过校验MD5 判断B内的文件与A 不同

    @param:
        - file_path - a folder names to be copied.
    '''
    # files_md5 = os.popen('md5 %s' % file_path).read().strip()
    files_md5 = os.popen('certutil -hashfile %s MD5' % file_path).read().strip()
    file_md5 = files_md5.replace('MD5 (%s) = ' % file_path, '')
    return file_md5

def copyFolder(start, dest):
    '''
    Move all files and folders from start folder to dest folder.

    @param:
        - start - a folder names to be copied.
        - dest - a folder names to copy from start to.
    '''
    logger.info("Copying Folders: %s..."%start)

    if not os.path.isdir(start):
        logger.warn("Start Folder not found: %s..."%start)
        return
    if not os.path.isdir(dest):
        logger.warn("Dest Folder not found!")
        logger.info("New Folder Created: %s..."%start)
        os.makedirs(dest)

    for files in os.listdir(start):
        start_name = os.path.join(start, files)
        dest_name = os.path.join(dest, files)
        if os.path.isfile(start_name):
            if os.path.isfile(dest_name):
                # (Optional) To check the MD% code matched
                if get_MD5(start_name) != get_MD5(dest_name):
                    shutil.copy(start_name, dest_name)
            else:
                shutil.copy(start_name, dest_name)
        else:
            if not os.path.isdir(dest_name):
                os.makedirs(dest_name)
            copyFolder(start_name, dest_name)

    logger.info("Copy Finished! from "+start+" to "+dest)
    # TODO: cmd command=> xcopy /s/e "D:\A_FOLDER" "E:\B_FOLDER\"

def searchFolder(pathname, foldername, recursive=False):
    '''
    Return all matched folder names under a specific path.

    @param:
        - pathname - a specific path to search for.
        - foldername - a filename to search for (Regular Expression can be used).
        - recursive - search recursively(all) [NOT AVAILABLE SO FAR]

    @RETURN:
        - A list of sting representing all matched folder names
    '''
    logger.info("Searching Folders: %s..."%foldername)

    matchedFolder =[]
    for name in os.listdir(pathname):
        if re.match(foldername, name) and not os.path.isfile(name):
            matchedFolder.append(name)

    logger.info("Matched Folders: %s!"%foldername)
    return matchedFolder

def searchFile(pathname, filename):
    '''
    Return all matched files under a specific path.

    @param:
        - pathname - a specific path to search for.
        - filename - a filename to search for (Regular Expression can be used).

    @RETURN:
        - A list of sting representing all matched file names
    '''
    logger.info("Searching Files: %s..."%filename)

    matchedFile =[]
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if re.match(filename, file):
                file_name = os.path.abspath(os.path.join(root, file))
                matchedFile.append(file_name)

    logger.info("Matched Files: %s!"%matchedFile)
    return matchedFile

def searchLog(starting_time):
    ''' TODO: TEMPLATE
    Search for Benchmark result under "{DOCUMENT}/SniperEliteV2_Benchmark"
    - return a LIST of .txt log names, which represents success in benchmarking
    - return [], which represents failure to benchmark
    '''
    f = []
    c = starting_time
    while(c < datetime.datetime.now()):
        cur_time = ( c ).strftime("%Y-%m-%d__%H-%M")
        res = utils.searchFile("{DOCUMENT_ROOT}//{GAME_DIRECTORY}//".format(DOCUMENT_ROOT=DOCUMENT_ROOT, GAME_DIRECTORY=GAME_DIRECTORY), "SEV2__%s.txt"%(cur_time))
        if res:
            f.extend(res)
            return f
        c = c + datetime.timedelta(minutes=1)
    return f

def main():
    '''
    '''
    print("NOTHING TO BE RUN")
    pass

if __name__ == '__main__':
    main()
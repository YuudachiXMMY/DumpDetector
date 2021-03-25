import os, sys, subprocess, re
import shutil
import pickle as p

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.logger

logger = lib.logger.logger("utils")

def getMD5(file_path):
    '''
    通过校验MD5 判断B内的文件与A 不同

    @param:
        - file_path - a folder names to be copied.
    '''
    # files_md5 = os.popen('md5 %s' % file_path).read().strip()
    files_md5 = os.popen('certutil -hashfile %s MD5' % file_path).read().strip()
    file_md5 = files_md5.replace('MD5 (%s) = ' % file_path, '')
    return file_md5

def getMD5Dump(md5file):
    '''
    '''
    with open(md5file, "rb") as f:
        return p.load(f)

def addMD5Dump(src, dst, md5file):
    '''
    '''
    md5new = {}
    md5new[dst] = getMD5(src)

    with open(md5file, "wb") as f:
        p.dump(md5new, f)

def isInMD5Dump(src, dst, md5file):
    '''
    Check whether the src and dst exist to be the same in md5file

    @param:
        - src - a folder names to be copied.
        - dst - a folder names to copy from src to.
        - full - True to fully copy; otherwise, copy increased file (default to True).
        - md5file - a dump file that can be utilized to check md5 codes.
    '''
    md5new = {}
    md5new[dst] = getMD5(src)
    md5old = getMD5Dump(md5file)

    return md5old.get(dst) == md5new[dst]

def copyFolder(src, dst, full=True, md5file="./lib/md5.data"):
    '''
    Move all files and folders from src folder to dst folder.

    @param:
        - src - a folder names to be copied.
        - dst - a folder names to copy from src to.
        - full - True to fully copy; otherwise, copy increased file (default to True).
        - md5file - a dump file that can be utilized to check md5 codes (default file:"./lib/md5.data").
    '''
    logger.info("Copying Folders: %s..."%src)

    if not os.path.isdir(src):
        logger.warn("src Folder not found: %s..."%src)
        return
    if not os.path.isdir(dst):
        logger.warn("dst Folder not found!")
        logger.info("New Folder Created: %s..."%src)
        os.makedirs(dst)

    md5new = {}

    for files in os.listdir(src):
        src_name = os.path.join(src, files)
        dst_name = os.path.join(dst, files)
        if os.path.isfile(src_name):
            addMD5Dump(src_name, dst_name, md5file)
            if os.path.isfile(dst_name):
                # (Optional) To check the MD% code matched
                if (full and getMD5(src_name) != getMD5(dst_name)) or \
                    (not full and not isInMD5Dump(src_name, dst_name, md5file)):
                    shutil.copy(src_name, dst_name)
            else:
                if full or \
                    (not full and not isInMD5Dump(src_name, dst_name, md5file)):
                    shutil.copy(src_name, dst_name)
        else:
            if not os.path.isdir(dst_name):
                os.makedirs(dst_name)
            copyFolder(src_name, dst_name)

    logger.info("Copy Finished! from "+src+" to "+dst)
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
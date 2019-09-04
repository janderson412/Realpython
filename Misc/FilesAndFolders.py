import os

if __name__ == '__main__':
    allfiles = []
    for dirpath, dirnames, filenames in os.walk('C:\\Temp'):
        #allfiles.append([dirpath + os.pathsep + f for f in filenames])
        for filename in filenames:
            fullpath = dirpath + os.sep + filename
            allfiles.append(fullpath)

    print(allfiles)
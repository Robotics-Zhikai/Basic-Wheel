import os
import sys
import time
import shutil
# from stat import ST_ATIME, ST_CTIME, ST_MTIME

def walkfiles(RootFilePath):
    for root,dirs,files in os.walk(RootFilePath):
        for f in files:
            print(f==f)
        # print(root)
        # print(dirs)
        # print(files)
        # print(os.path.join(root,files[0]))
        # for f in files:
        #     modifidTime = time.localtime(os.stat(os.path.join(root,f)).st_mtime)
        #     print(modifidTime==modifidTime)
        #     mTime = time.strftime('%Y-%m-%d %H:%M:%S', modifidTime)
        #
        #     print(mTime)
        #     print(f)
            # print(os.path.join(root,f))

def FetchFiles(FileName,rootpath):
    result = []
    for root,dirs,files in os.walk(rootpath):
        for f in files:
            if f == FileName:
                result.append(os.path.join(root,f))
    return result

def ReturnLatestFileIndex(fileslist): #得到最新更新的文件
    maxindex = -1;
    if len(fileslist)!=0:
        Timelist = []
        for i in range(len(fileslist)):
            timethis = time.localtime(os.stat(fileslist[i]).st_mtime)
            Timelist.append(timethis)
            # mTime = time.strftime('%Y-%m-%d %H:%M:%S', timethis)
            # print(mTime)
        if len(Timelist)!=0:
            maxtime = Timelist[0]
            maxindex = 0
            for i in range(len(Timelist)):
                if Timelist[i]>maxtime:
                    maxtime = Timelist[i]
                    maxindex = i
    return maxindex

# walkfiles("D:\Study\硕士\就业相关资料收集")

# BasicWheelDir = "D:/Study/硕士/我的工作/Python/分布式更新文件/before"
BasicWheelDir = "D:/Study/硕士/我的工作/GitHubUpdate/Basic-Wheel"
SourceFilesDir = "D:/Study/硕士/我的工作/GitHubUpdate"
# SourceFilesDir = "D:\Study\硕士\我的工作\Python\分布式更新文件"
# BasicWheelDir = "D:/Study/硕士/我的工作/复现文献"
for root,dirs,files in os.walk(BasicWheelDir):
    # testtimtmp = []
    if '.git' in root:
        continue;
    for f in files:
        if f == 'README.md':
            continue
        filesList = FetchFiles(f,SourceFilesDir)
        RecentlyFileIndex = ReturnLatestFileIndex(filesList)

        if RecentlyFileIndex != -1:
            timeorigin = time.localtime(os.stat(os.path.join(root,f)).st_mtime)
            timeRecently = time.localtime(os.stat(filesList[RecentlyFileIndex]).st_mtime)
            # print(timeorigin)
            # testtimtmp.append(timeorigin)
            # if len(testtimtmp)>=2:
                # print(testtimtmp[1]==testtimtmp[0])
            if timeRecently>timeorigin:
                print(filesList[RecentlyFileIndex],"将要替换",os.path.join(root,f))
                shutil.copyfile(filesList[RecentlyFileIndex],os.path.join(root,f))
                time.sleep(2)
                #以下是把文件复制时保持修改时间一致的方法，但是可能会有问题，所以暂时先不用
                # file_stat = os.stat(filesList[RecentlyFileIndex])
                # os.utime("D:\\Study\\硕士\\我的工作\\ConvexHull.cpp", (file_stat[ST_CTIME], file_stat[ST_MTIME]))
                # print(time.localtime(os.stat(filesList[RecentlyFileIndex]).st_mtime)==time.localtime(os.stat("D:\\Study\\硕士\\我的工作\\ConvexHull.cpp").st_mtime))
            else:
                print(filesList[RecentlyFileIndex],"保持不动",os.path.join(root,f))
        elif RecentlyFileIndex == -1:
            print("说明BasicWheelDir和SourceFilesDir是互相独立的，在sourceFilesDir中没有找到需要修改的文件，什么操作都不做")




#
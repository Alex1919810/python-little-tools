import os


# 利用os.listdir()、os.walk()获取文件夹和文件名
def GetFileName(fileDir):
    for dir in os.listdir(fileDir):  # 获取当前目录下所有文件夹和文件(不带后缀)的名称
        filePath = os.path.join(fileDir, dir)  # 得到文件夹和文件的完整路径
        if os.path.isdir(filePath):
            # 获取根目录路径、子目录路径，根目录和子目录下所有文件名
            for root, subDir, files in os.walk(filePath):
                for fileName in files:
                    fileName = os.path.splitext(fileName)[0]  # 分割，不带后缀名
                    if fileName == 'quanben':  # 将特定文件的文件名修改为父目录名称
                        src = os.path.join(root, 'quanben.html')
                        dst = os.path.join(root, f'{dir}.html')
                        os.rename(src, dst)


fileDir = "D:\\pythonProject3"  # 输入文件夹路径
GetFileName(fileDir)

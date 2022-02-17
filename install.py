from util.log import log
import os
PATH=os.path.join(os.getcwd())
if os.path.isfile(PATH+"/requirements.txt"):
    log.info("存在文件requirements.txt")
    libs = []
    for line in open(PATH+"/requirements.txt", "r"):  # 设置文件对象并读取每一行文件
        libs.append(line)  # 将每一行文件加入到list中
    try:
        for lib in libs:
            print("start install {0}".format(lib))
            os.system("pip install " + lib)
            print("{} install successful".format(lib))
        print("All Successful")
    except:
        print("Failed SomeHow")



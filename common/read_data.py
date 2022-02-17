import yaml
import os
import codecs
import configparser

class ReadConfig():
    def __init__(self):
        prj = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        configPath = os.path.join(prj, "config","pytest.ini")
        fd = open(configPath)
        data = fd.read()
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w",encoding='utf-8')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_host(self, name):
        value = self.cf.get("host", name)
        return value
    def get_email(self, name):
        value = self.cf.get("email", name)
        return value

class ReadFileData():
    def __init__(self,filename):

        path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.filepath=os.path.join(path,'util','data')+'/'+filename

    def get_yaml_data(self):
        with open(self.filepath,'r',encoding='utf-8')as f:
            #调用load方法加载文件流
            return yaml.load(f,Loader=yaml.FullLoader)

r=ReadConfig()


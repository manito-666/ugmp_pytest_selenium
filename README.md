
## 项目说明

本项目在实现过程中，把整个项目拆分成slenium基类、公共方法封装、数据封装、测试用例等模块。

首先利用Python编写测试用例，调用selenium基类方法，测试数据则通过YAML文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。


## 项目部署

工程首先通过 pip 工具生成 requirements.txt 文件方便其他用户导包使用，执行命令：

```
pip freeze > requirements.txt

```
在根目录下找到 ```install.py``` 文件,执行后可以下载导入工程需要的包


接着，修改 ```config/pytest.ini``` 配置文件，在相应环境下，安装相应依赖之后，在命令行窗口执行命令：
执行page文件目录下的所有测试集
```
pytest page
```
也可执行单个测试用例
```
pytest  page/test_page1.py
```
## 项目结构

- common ====>> 各种公共方法，selenium基类、读取配置与yaml方法、发送邮件等
- config ====>> 配置文件
- page====>> 存放测试用例，conftest文件、生成测试报告
- util ====>> 存放yaml类型的测试数据、log文件
- requirements.txt ====>> 相关依赖包文件
- install.py ====>> 自动下载依赖包文件

## 编写用例说明
引入conftest定义好的driver = login_fixtrue方法，在yaml文件中把定位方式与元素按列表形式排列
ReadFileData方法读取数据，实际编写时数据需要转化为元组类型，调用slenium的公共方法进行编写


## 测试报告效果展示
执行 main.py后所有测试用例查看报告

在命令行执行命令：```pytest``` 运行用例后，会得到一个测试报告的原始文件，但这个时候还不能打开成HTML的报告，还需要在项目根目录下，执行命令启动 ```allure``` 服务：

```
# 需要提前配置allure环境，才可以直接使用命令行
pytest  page -s -q --alluredir=./page/result/
生成allure的json文件
allure generate ./page/result -o ./page/report --clean
生成html报告 打开index.html进行查看

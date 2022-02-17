import platform
from selenium import webdriver
import pytest
import time
from util.log import log
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def login_fixtrue(driver):
    #登录前置操作
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    return driver
def pytest_addoption(parser):
    '''添加命令行参数'''
    parser.addoption('--headless', action = "store",
                     default = 'no', help = 'set chrome headless option yes or no'
    )
@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    if platform.system()=='Windows':
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
        chrome_options.add_argument('--headless')  # 无界面
        log.info("当前运行的操作系统为windows")
        _driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        log.info('当前运行的操作系统为mac')
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
        chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')#禁用GPU硬件加速，如果软件渲染器没有就位，则GPU进程将不会启动
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')  # 无界面
        _driver = webdriver.Chrome(chrome_options=chrome_options)

    def end():
        log.info("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        _driver.quit()
    request.addfinalizer(end)
    return _driver

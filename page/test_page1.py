import time
from common.basepage import Base
from common.read_data import *
from util.log import log
import allure
import pytest
testelement = ReadFileData("login_page.yml").get_yaml_data()

class Test_BPC():
    @allure.feature("功能点：BPC用户查询")
    @allure.story("用例：登陆ugmp后查询帐号数据")
    def test_page1(self,login_fixtrue):
        driver = login_fixtrue
        web = Base(driver)
        driver.get(r.get_host('url'))
        loc1 = tuple((testelement["login_element"])[0])
        with allure.step("点击项目图标"):
            web.click(loc1)
        loc2 = tuple((testelement["login_element"])[1])
        with allure.step("选择项目"):
            web.switch_handle("ugmp")
            web.click(loc2)
            time.sleep(2)
        loc3 = tuple((testelement["login_element"])[2])
        with allure.step("选择BPC"):
            web.click(loc3)
            time.sleep(2)
        loc4 = tuple((testelement["login_element"])[3])
        with allure.step("选择BPC"):
            web.click(loc4)
            log.info("进入BPC项目成功")




if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_page1.py"])
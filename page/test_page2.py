import time
from common.basepage import Base
from common.read_data import *
from util.log import log
import allure
import pytest
testelement = ReadFileData("login_page.yml").get_yaml_data()

class Test_AOD():
    @allure.feature("功能点：AOD帐号查询-角色查询")
    @allure.story("用例：登陆ugmp后查询帐号数据")
    @pytest.mark.parametrize("server,role",testelement['account message'])
    def test_page2(self,login_fixtrue,server,role):
        driver = login_fixtrue
        web = Base(driver,30,0.5)
        driver.get(r.get_host('url'))
        loc1 = tuple((testelement["ugmp_element"])[0])
        with allure.step("点击UGMP图标"):
            web.click(loc1)
            log.info("进入UGMP")
        loc2 = tuple((testelement["ugmp_element"])[1])
        web.switch_handle("UGMP")
        with allure.step("点击项目"):
            web.click(loc2)
            time.sleep(2)
        loc3 = tuple((testelement["ugmp_element"])[2])
        with allure.step("选择项目AOD"):
            web.click(loc3)
            time.sleep(2)
            log.info("进入UGMP-帐号查询页面")
        loc4 = tuple((testelement["ugmp_element"])[3])
        with allure.step("点击进入管理"):
            web.click(loc4)
            time.sleep(2)
            log.info("进入帐号查询页面成功")
        loc5 = tuple((testelement["ugmp_element"])[4])
        loc6 = tuple((testelement["ugmp_element"])[5])
        with allure.step("选择渠道"):
            web.click(loc5)
            time.sleep(2)
            web.click(loc6)
            time.sleep(2)
            log.info("选择渠道为dev")
        loc7 = tuple((testelement["ugmp_element"])[6])
        loc8 = tuple((testelement["ugmp_element"])[7])
        with allure.step("输入区服"):
            web.input(loc7,text=tuple(server))
            time.sleep(2)
            log.info("输入区服:{}".format(server))
        with allure.step("输入角色"):
            web.input(loc8,text=tuple(role))
            time.sleep(2)
            log.info("输入角色:{}".format(role))
        loc9=tuple((testelement["ugmp_element"])[8])
        with allure.step("点击查询"):
            web.click(loc9)
            log.info("查询角色")
        try:
            loc10=web.get_text(tuple((testelement["ugmp_element"])[9]))
            log.info("测试成功，通行证id为：{}".format(loc10))
            time.sleep(3)
        except Exception as e:
            log.error("测试失败: " + format(e))
            web.get_windows_img()



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_page2.py"])





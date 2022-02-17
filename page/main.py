import os
import pytest
from util.log import log
case_path = os.path.join(os.getcwd())
PATH = os.path.split(os.path.realpath(__file__))[0]
print(PATH)
failureException = AssertionError

if __name__ == '__main__':
    log.info("%s --alluredir=./report" % case_path)
    pytest.main(["-sq", "--alluredir", "./allure-results"])
    os.popen("allure generate ./allure-results/ -o ./allure-report/ --clean")
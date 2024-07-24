import allure
import pytest

@allure.epic('项目名称：Mss的接口测试自动化')

@allure.feature('模块名称：用户模块')
class TestLogin:
    @allure.story('接口名称：登录接口')
    @allure.title('用例1：验证登录接口')
    @allure.severity(allure.severity_level.BLOCKER)
    # allure.severity 测试用例的等级
    @allure.description('用例说明')
    @allure.link('接口访问链接')
    @allure.issue('bug链接')
    @allure.testcase('测试用例链接')
    def test_login(self,connect_sql):
        print('登录成功')

    @allure.story('接口名称：注册接口')
    @allure.title('用例1：用户注册接口')
    # 用例层面写法1
    def test_register(self):
        print('注册测试用例')

    # 用例层面写法2
    @allure.story('接口名称：增加用例接口')
    def test_add(self,connect_sql):
        print('增加测试用例:%s'%connect_sql)
        # @allure.dynamic.title('接口增加')
        assert 'a' in 'anc'

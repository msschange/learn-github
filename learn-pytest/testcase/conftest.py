import pytest


@pytest.fixture(scope='function',autouse=False,params=("case01","case02"))
def connect_sql(request):
    print('连接数据库')
    yield request.param
    print('关闭数据库')


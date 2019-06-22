import pytest
from day04 import Shell
if __name__ == '__main__':
    sell = Shell.Shell()
    # pytest.main(['-s','-q','./day04'])
    pytest.main(['-s', '-q','--alluredir','./Report/xml/', './day04'])
    sell.invoke('allure generate ./Report/xml -o ./Report/html')

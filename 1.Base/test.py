import requests
from module1 import foo
import module2

url = 'http://api.tianapi.com/hotreview/index?key=e89542fddbb0effa0e21a4785fdd8846'

re = requests.post(url)

print(re.content.decode('utf-8'))


foo()
module2.foo()
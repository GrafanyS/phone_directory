import jmespath
from unicodedata import name

fail = r"phone_directory.csv"
with open(fail, 'r', encoding = 'utf-8') as f:
    data = []
    ex = jmespath.compile('f[0].age')
    res = ex.search('phone_directory')
print(res)

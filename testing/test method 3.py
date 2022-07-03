import sys
sys.path.append('../methods')
from method3 import main as method3

res=method3()
print(res)
print(res.draw())
print(res.analytics_report())

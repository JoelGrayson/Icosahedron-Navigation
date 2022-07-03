import sys
sys.path.append('../methods')
from method2 import main as method3

res=method3()
print(res)
print(res.draw())
print(res.analytics_report())

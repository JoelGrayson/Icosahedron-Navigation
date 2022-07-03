import sys
sys.path.append('../methods')
from method1 import main as method1

res=method1()
print(res)
print(res.analytics_report())

import sys
sys.path.append('../methods')
from method1 import main as method1
from method2 import main as method2
from method3 import main as method3

NUM_ATTEMPTS=500
accuracy={
    "method 1": None,
    "method 2": None,
    "method 3": None,
}
moves={
    "method 1": None,
    "method 2": None,
    "method 3": None,
}
markers={
    "method 1": None,
    "method 2": None,
    "method 3": None
}


def get_accuracy(method):
    num_successes=0
    for i in range(NUM_ATTEMPTS):
        if method().get_location()['num']==12:
            num_successes+=1

    return num_successes/NUM_ATTEMPTS

def get_moves(method):
    num_moves=[]
    for i in range(NUM_ATTEMPTS):
        num_moves.append(method().analytics_report()['num_moves'])
    return sum(num_moves)/len(num_moves)

def get_markers(method):
    res=method().analytics_report()
    return {
        "marker_types": res['marker_types'],
        "num_unique_markers": len(res['marker_types']),
        "num_markers": res['num_markers']
    }


accuracy['method 1']=get_accuracy(method1)
accuracy['method 2']=get_accuracy(method2)
accuracy['method 3']=get_accuracy(method3)

moves['method 1']=get_moves(method1)
moves['method 2']=get_moves(method2)
moves['method 3']=get_moves(method3)

markers['method 1']=get_markers(method1)
markers['method 2']=get_markers(method2)
markers['method 3']=get_markers(method3)

print(f"""
|{'-'*66}|
|{'Results': ^66}|
| {'': <16} {'Method 1': ^15} {'Method 2': ^15} {'Method 3': ^15} |
| {'Accuracy': <16} {accuracy['method 1']: <15} {accuracy['method 2']: <15} {accuracy['method 3']: <15} |
| {'Moves': <16} {moves['method 1']: <15} {moves['method 2']: <15} {moves['method 3']: <15} |
| {'#Total markers': <16} {markers['method 1']['num_markers']: <15} {markers['method 2']['num_markers']: <15} {markers['method 3']['num_markers']: <15} |
| {'#Unique Markers': <16} {markers['method 1']['num_unique_markers']: <15} {markers['method 2']['num_unique_markers']: <15} {markers['method 3']['num_unique_markers']: <15} |
|{'-'*66}|
""")

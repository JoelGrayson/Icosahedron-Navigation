import sys
sys.path.append('../icosahedron')
from SuperIcosahedron import SuperIcosahedron

def main():
    # Red (R) - first layer
    # Orange (O) - second layer
    # Yellow (Y) - fifth layer
    # Green (G) - fourth layer

    ic=SuperIcosahedron(1)
    num_marked={
        "R": 0,
        "O": 0,
        "G": 0
    }
    # First row
    ic.set_marker('R')
    num_marked['R']=1

    # Second row
    while num_marked['O']<5: #until 5 O's are marked
        ic.go_to('R') #move until back home
        ic.move()

        if ic.get_marker()=='O':
            continue
        else:
            ic.set_marker('O')
            num_marked['O']+=1

    # Third row
    while num_marked['G']<5: #until 5 G's are marked
        ic.go_to('O')
        while ic.get_marker()=='O':
            ic.move()

        if ic.get_marker()==None: #only mark if empty
            ic.set_marker('G')
            num_marked['G']+=1
        
    while ic.get_marker() is not None:
        ic.move()
   
    return ic

import sys
sys.path.append('../icosahedron/')
from SuperIcosahedron import SuperIcosahedron

def main():
    # Red (R) - first layer
    # Orange (O) - second layer
    # Yellow (Y) - fifth layer
    # Green (G) - fourth layer

    ic=SuperIcosahedron(1)
    num_marked={
        "R": 0,
        "O": 0,
        "G": 0
    }
    # First row
    ic.set_marker('R')
    num_marked['R']=1

    # Second row
    while num_marked['O']<5: #until 5 O's are marked
        ic.go_to('R') #move until back home
        ic.move()

        if ic.get_marker()=='O':
            continue
        else:
            ic.set_marker('O')
            num_marked['O']+=1

    # Third row
    while num_marked['G']<5: #until 5 G's are marked
        ic.go_to('O')
        while ic.get_marker()=='O':
            ic.move()

        if ic.get_marker()==None: #only mark if empty
            ic.set_marker('G')
            num_marked['G']+=1
        
    while ic.get_marker() is not None:
        ic.move()
   
    return ic

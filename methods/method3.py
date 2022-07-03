import sys
sys.path.append('../icosahedron')
from SuperIcosahedron import SuperIcosahedron

# Subroutine
def mark_three_from_home(ic):
    ic.go_to('R')
    for i in range(3):
        ic.move()
    if ic.get_marker()=='R':
        mark_three_from_home(ic)
    else:
        ic.set_marker('G')

def main():
    # R - start
    # G - finish

    ic=SuperIcosahedron()
    ic.set_marker('R')
    mark_three_from_home(ic)

    # On opposite if distance between R and G is never <3
    num_tries=0
    while num_tries<100:
        num_tries+=1
        ic.go_to('G')
        move_num=0
        while ic.get_marker()!='R':
            ic.move()
            move_num+=1
        
        if move_num<3: #restart because cannot be opp
            # Remove the old marker
            ic.go_to('G')
            ic.remove_marker()

            mark_three_from_home(ic)
            num_tries=0

    ic.go_to('G')

    # print(ic)
    return ic

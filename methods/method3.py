import sys
sys.path.append('../icosahedron')
from SuperIcosahedron import SuperIcosahedron

# Helper
def marker_starts_with(ic, letter) -> bool:
    if ic.get_marker() is None:
        return False
    return ic.get_marker()[0]==letter

def is_head(ic) -> bool:
    # Once reached 3 unique 2.\d digits, return True
    unique_reached=set()
    while len(unique_reached)<3:
        ic.go_to('var')
        ic.move()
        if marker_starts_with(ic, '2'):
            unique_reached.add(ic.get_marker())
        else:
            ic.go_to('var')
            return False
    ic.go_to('var')
    return True

# Subroutine
def go_to_2_mid_neighbor(ic, closest='3-mid'): #closest: ('3-mid' | '3-mid-neighbor')
    while True:
        ic.go_to('2-mid')
        ic.move()
        if marker_starts_with(ic, '2'): #2-mid-neighbor
            # At this point, is a 2-mid-neighbor
            # We don't know if closest is 3-mid or 3-mid-neighbor
            curr_spot=ic.get_marker() #memorize current spot
            while True:
                ic.go_to(curr_spot)
                ic.move()
                if marker_starts_with(ic, '2'):
                    break
                if ic.get_marker()=='3-mid-neighbor' and closest=='3-mid-neighbor': #found 3-mid-neighbor
                    ic.go_to(curr_spot)
                    return
                if ic.get_marker()=='3-mid' and closest=='3-mid': #found 3-mid
                    ic.go_to(curr_spot)
                    return


def main():
    # Mark names:
    # 1
    # 2-mid
    # 2 (2-mid-neighbor closest to 3-mid or 3-mid-neighbor)
    # 3-mid
    # 3-mid-neighbor

    num_marked={
        "2": 0,
        "3-mid": 0,
        '3-mid-neighbor': 0
    }

    # First row
    ic=SuperIcosahedron()
    ic.set_marker('var') #can be 1 or 3-mid-neighbor
    
    # Second row
    ic.move()
    ic.set_marker('2-mid')
    ic.go_to('var')
    num_marked["2"]+=1
    while num_marked["2"]<5:
        ic.go_to('var')
        ic.move()
        if ic.get_marker()==None:
            ic.set_marker(f'2.{num_marked["2"]}')
            num_marked["2"]+=1
        
    # 3-mid
    while True: #mark 3-mid
        ic.go_to('2-mid')
        ic.move()
        if ic.get_marker()==None:
            ic.set_marker('3-mid')
            break
    while True: #mark 3-mid-neighbor
        ic.go_to('2-mid')
        ic.move()
        if ic.get_marker()==None:
            ic.set_marker('3-mid-neighbor')
            break


    ic.go_to('var') #remove head's var, paste elsewhere
    ic.remove_marker()

    while True:
        go_to_2_mid_neighbor(ic, '3-mid')
        ic.move()

        if ic.get_marker()==None:
            ic.set_marker('var')

            if is_head(ic): #if head, redo
                ic.remove_marker()
                continue
            break
        
        else: #hit an already existant marker
            continue

    while True:
        ic.go_to('3-mid')
        ic.move()
        if ic.get_marker()==None: #successfully reached opposite side
            return ic

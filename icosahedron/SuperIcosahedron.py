from Icosahedron import Icosahedron
import random
from connections import connections

class SuperIcosahedron(Icosahedron):
    def __init__(self, start=1):
        super(SuperIcosahedron, self).__init__(start)
        self.analytics={
            "num_moves": 0, #number of moves
            "num_markers": 0, #number of markers used
            "marker_types": set() #unique markers
        }
    
    # Subroutine
    def go_to(self, mark): 
        while self.get_marker()!=mark:
            self.move()

    # Overwrite basic methods with analytics
    def move(self): #moves to random side
        can_move_to=connections[self.location['num']]
        side_num=random.choice(can_move_to)
        self.location=self.sides[side_num]
        self.analytics['num_moves']+=1

    def set_marker(self, markName) -> None:
        self.location['marker']=markName
        self.analytics['marker_types'].add(markName)
    
    def analytics_report(self):
        # Cleaning
        if None in self.analytics['marker_types']: #remove None as a valid marker
            self.analytics['marker_types'].remove(None)
        
        for side in self.sides.values():
            if side['marker'] is not None:
                self.analytics['num_markers']+=1
        
        return self.analytics
    
    # Bonus
    def is_at_start(self):
        return self.location==1
    
    def get_location(self):
        return self.location

    def draw(self): #ASCII representation
        s=[0]
        for i in self.sides.values():
            if i['marker']==None:
                s.append(i['num'])
            else:
                # s.append(str(i['num'])+' ('+str(i['marker'])+')')
                s.append(f"{i['num']} ({i['marker']})")
        
        return f'''Front
        _-_.
     _-',{s[1]}. `-_.
 ._-' ,'   `.   `-_ 
{s[6]}`-_{s[2]}_________`{s[3]}':::{s[4]}
!   /\        /\::::
;  /  \      /..\:::
! /    \    /....\::
!/      \  /......\:
;--.___. \/_.__.--;; 
 {s[7]}-_  `{s[8]}!;;;;;;{s[9]}'
    `-_, :!;;;''
        `-{s[12]}'
Back
        _-_.
     _-',{s[1]}. `-_.
 ._-' ,'   `.   `-_ 
{s[3]}`-_{s[4]}_________`{s[5]}':::{s[6]}
!   /\        /\::::
;  /  \      /..\:::
! /    \    /....\::
!/      \  /......\:
;--.___. \/_.__.--;; 
 {s[9]}-_  `{s[10]}!;;;;;;{s[11]}'
    `-_, :!;;;''
        `-{s[12]}'
'''


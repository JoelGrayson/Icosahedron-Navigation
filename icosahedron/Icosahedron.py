import random
from connections import connections

class Icosahedron:
    def __init__(self, start=1):
        self.sides={}
        for i in range(1, 13):
            self.sides[i]={
                "num": i,
                "marker": None
            }
        if 1<=start<13: #valid side
            self.location=self.sides[start]
        else:
            self.location=self.sides[0]
        
        self.analytics={
            "num_moves": 0, #number of moves
            "num_markers": 0, #number of markers used
            "marker_types": set() #unique markers
        }

    def __str__(self) -> str:
        out=''
        for i in self.sides.values():
            item_str=''
            marker=i['marker']
            num=i['num']

            if marker is not None: #has marker
                item_str=f'{num} ({marker})'
            else:
                item_str=f'{num}'
            
            if num==self.location['num']: #bold if is location
                item_str=f'*{item_str}*\t'
            else:
                item_str=f' {item_str}\t' #surround with spaces
            
            out+=item_str
        return out

    def move(self): #moves to random side
        can_move_to=connections[self.location['num']]
        side_num=random.choice(can_move_to)
        self.location=self.sides[side_num]
        self.analytics['num_moves']+=1
        
    def set_marker(self, markName) -> None:
        self.location['marker']=markName
        self.analytics['marker_types'].add(markName)

    def get_marker(self):
        return self.location['marker']

    def remove_marker(self):
        self.set_marker(None)

    # Bonus
    def analytics_report(self):
        # Cleaning
        if None in self.analytics['marker_types']: #remove None as a valid marker
            self.analytics['marker_types'].remove(None)
        
        for side in self.sides.values():
            if side['marker'] is not None:
                self.analytics['num_markers']+=1
        
        return self.analytics

    def draw(self):
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


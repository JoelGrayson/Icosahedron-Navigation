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
        
    def set_marker(self, markName) -> None:
        self.location['marker']=markName

    def get_marker(self):
        return self.location['marker']

    def remove_marker(self):
        self.set_marker(None)


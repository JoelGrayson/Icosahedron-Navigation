from Icosahedron import Icosahedron

class SuperIcosahedron(Icosahedron):
    # Subroutine
    def go_to(self, mark): 
        while self.get_marker()!=mark:
            self.move()
    
    # Bonus
    def is_at_start(self):
        return self.location==1
    
    def get_location(self):
        return self.location

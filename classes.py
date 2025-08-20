class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Empty:
    def __init__(self):
        pass

    def __str__(self):
        return "Empty"
    
class Map:
    def __init__(self):
        pass

class Soldier:
    def __init__(self,pos:Vector2, map):
        self.pos = pos
        self.map = map
        self.map[pos.x,pos.y] = self


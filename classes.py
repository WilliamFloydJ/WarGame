import math, random, pygame, asyncio
from screen import space_size,screenDim
from functions import getLeader, getSubs
from names import generate_name
from utils import tupleAdd,emptyList
V2 = pygame.Vector2

border_color = (26, 14, 1)
space_color = (145, 75, 0)
border_thickness = math.floor(space_size*0.025)
    
class Map:
    def __init__(self,xLen,yLen,surface):
        self.map = []
        for y in range(yLen):
            row = []
            for x in range(xLen):
                row.append(Space((x,y),self))
            self.map.append(row)
        self.surface = surface

    def __str__(self):
        str_list = []
        for list in self.map:
            str_list.append(" ".join([str(obj) for obj in list]))
            str_list.append("\n")
        return "".join(str_list)

    def __getitem__(self,pos):
        x, y = pos
        return self.map[y][x]
    
    def __setitem__(self,pos,value):
        x, y = pos
        self.map[y][x] = value
    
    def draw(self):
        for y in self.map:
            for x in y:
                x.draw()

class Space:
    def __init__(self, pos:tuple, map:Map):
        self.pos = pos
        self.rect = pygame.Rect(pos[0]*space_size,pos[1]*space_size,space_size,space_size)
        self.map = map

    def __str__(self):
        return f"{tupleAdd(self.pos,(1,1))}"

    def draw(self):
        pygame.draw.rect(self.map.surface,space_color,self.rect)
        pygame.draw.rect(self.map.surface,border_color,self.rect,border_thickness)      

class Team:
    def __init__(self, color, name:str, map:Map, soldiers = None, soldiers_create = [], squads = None):
        self.color = color
        self.name = name
        self.map = map
        self.soldiers = emptyList(soldiers)
        self.squads = emptyList(squads)

        for squad_create in soldiers_create:
            squad = Squad([])
            for pos in squad_create:
                sol = Soldier(pos,map,self,0,squad)
                squad.soldiers.append(sol)
                self.soldiers.append(sol)
            self.squads.append(squad)

class Squad:
    def __init__(self, soldiers):
        self.soldiers = soldiers
    
    def __str__(self):
        string = ""
        for soldier in self.soldiers:
            string += str(soldier) + ";"
        return string

        

class Soldier:
    def __init__(self,pos:tuple, map:Map, team:Team, rank:int, squad, orders = None):
        self.pos = pos
        self.Map = map
        self.map = map.map
        self.Map[pos[0],pos[1]] = self
        self.rect = pygame.Rect(pos[0]*space_size,pos[1]*space_size,space_size,space_size)
        self.team = team
        self.squad = squad
        self.rank = rank
        self.name = generate_name()
        self.orders = emptyList(orders)
        self.speed = random.uniform(1,3) 

    def __str__(self):
        return f" {self.name} {tupleAdd(self.pos,(1,1))} {self.team.name} "

    def draw(self):
        pygame.draw.rect(self.Map.surface,self.team.color,self.rect)
        pygame.draw.rect(self.Map.surface,border_color,self.rect,border_thickness)
    
    def updatePos(self, pos):
        self.pos = pos
        self.rect.x = pos[0] * space_size
        self.rect.y = pos[1] * space_size

    def get_leader(self):
        return getLeader(self.squad.soldiers)
    
    def get_subs(self):
        return getSubs(self,self.squad.soldiers)
    
    async def move(self,amount:tuple):
        await asyncio.sleep(self.speed)
        x , y = self.pos
        self.Map[x,y] = Space((x,y),self.Map)

        self.updatePos(tupleAdd(self.pos,amount))

        x , y = self.pos
        self.Map[x,y] = self

    async def shoot(self, towards: V2, amount: int = 1):
        x , y = self.pos
        bullet = Bullet(self.Map.surface,V2(x,y),towards)
        await bullet.shoot()

    def give_orders(self):
        for sub in getSubs(self,self.squad.soldiers):
            orders = self.orders.copy()
            sub.orders.extend(orders)

    async def do_orders(self):
        for order in self.orders:
            await getattr(self,order.name)(*order.prop)

class Order:
    def __init__(self, name, prop):
        self.name = name
        self.prop = prop

class Bullet:
    def __init__(self, surface, startPos: V2, endPos: V2, speed = 1, power = 1):
        self.surface = surface
        self.rect = pygame.Rect(startPos[0],startPos[1],50,50)
        self.startPos = startPos
        self.endPos = endPos
        self.speed = speed
        self.power = power
    
    def move(self):
        direction = (self.startPos - self.endPos).normalize()
        vel = direction * 1 * self.speed
        self.rect.x += math.ceil(vel.x)
        self.rect.y += math.ceil(vel.y)
        self.draw()

    async def shoot(self):
        for i in range(screenDim[0]):
            self.move()

    def draw(self):
        pygame.draw.rect(self.surface,(255,255,255),self.rect)



            

        


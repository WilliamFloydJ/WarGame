import pygame
import copy
from classes import Soldier, Map, Team, Order
from screen import screenDim, map_len

pygame.init()
pygame.display.set_caption("War Game")
screen = pygame.display.set_mode((screenDim[0], screenDim[1]))

print("Shall we play a game?")

map = Map(map_len[0],map_len[0],screen)

US_Squads = [[(2,1),(4,1),(6,1),(8,1),(10,1),(12,1)]]
US = Team((87, 179, 2),"US",map,[],US_Squads)
US.squads[0].soldiers[0].rank = 1
US.squads[0].soldiers[0].orders = [Order("move",(0,1))]
US.squads[0].soldiers[0].give_orders()
for solder in US.squads[0].soldiers:
    solder.do_orders()

CA_Squads = [[(2,15),(4,15),(6,15),(8,15),(10,15),(12,15)]]
CA = Team((187, 179, 222),"CA",map,[],CA_Squads)


clock = pygame.time.Clock()  

def main_loop():
    pass

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pass
    map.draw()
    main_loop()
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()
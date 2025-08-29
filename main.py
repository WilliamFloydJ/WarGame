import pygame
import asyncio
import copy
from classes import Soldier, Map, Team, Order
from screen import screenDim, map_len
V2 = pygame.Vector2

pygame.init()
pygame.display.set_caption("War Game")
screen = pygame.display.set_mode((screenDim[0], screenDim[1]))

print("Shall we play a game?")

map = Map(map_len[0],map_len[0],screen)

US_Squads = [[(2,1),(4,1),(6,1),(8,1),(10,1),(12,1)]]
US = Team((87, 179, 2),"US",map,[],US_Squads)

CA_Squads = [[(2,15),(4,15),(6,15),(8,15),(10,15),(12,15)]]
CA = Team((187, 179, 222),"CA",map,[],CA_Squads)

US.squads[0].soldiers[0].rank = 1
US.squads[0].soldiers[0].orders = [Order("move",[(0,1)]),Order("shoot",[CA.squads[0].soldiers[0].pos])]
US.squads[0].soldiers[0].give_orders()
async def run():
   await asyncio.gather(*(s.do_orders() for s in US.squads[0].soldiers))

clock = pygame.time.Clock()  

async def main_loop():
    await asyncio.sleep(0)

async def main():
    asyncio.create_task(run())
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pass
        map.draw()
        await main_loop()
        pygame.display.flip()
        clock.tick(60)


    pygame.quit()

asyncio.run(main())
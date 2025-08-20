import pygame
import numpy as np
from classes import Soldier, Vector2, Empty

print("Shall we play a game?")

map_xLen = 20
map_yLen = 20

map = np.empty((map_xLen, map_yLen),dtype=object)

s1 = Soldier(Vector2(5,5),map)

print(map)
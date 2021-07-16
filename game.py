import sys
import os

import pygame
from pygame.locals import QUIT

pygame.init()
windows_surface = pygame.display.set_mode((500, 700))
pygame.display.set_caption('兔兔養成遊戲')
windows_surface.fill((136, 212, 247))

# head_font = pygame.font.SysFont(None, 60)
# text_surface = head_font.render('Hello', True, (0, 0, 0))
# windows_surface.blit(text_surface, (10, 10))

#主要兔子
rabit_main = pygame.image.load('image/rabbit.png')
rabit_main = pygame.transform.scale(rabit_main, (200, 150))
rabit_main.convert()
windows_surface.blit(rabit_main, (150, 300))

#功能圖標
color = (128, 209, 167)
y_location = 10
i = 0
while i < 4:
    pygame.draw.rect(windows_surface, color, [10, y_location, 80, 80])
    y_location = y_location + 100
    i = i + 1

image_dict = {}
def load_image(path_to_dic):
    for filename in os.listdir(path_to_dic):
            if filename.endswith('.png'):
                path = os.path.join(path_to_dic, filename)
                key = filename[:-4]
                image_dict[key] = pygame.image.load(path)
    return image_dict
load_image('function_icon')

for key in image_dict:
	image_dict[key] = pygame.transform.scale(image_dict[key], (55, 55))
	print(key)

windows_surface.blit(image_dict['carrot'], (20, 20))
windows_surface.blit(image_dict['ball'], (20, 120))
windows_surface.blit(image_dict['hare'], (20, 220))
windows_surface.blit(image_dict['house'], (20, 320))





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

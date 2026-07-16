import pygame
import math
pygame.init()
running =True
drawing=False
symmetry=input("Enter the type of Symmetry \n 1)Vertical \n 2)Rotational \n 3)Radial:\n ")
while not (symmetry=="Vertical" or symmetry=="Rotational" or symmetry=="Radial"):
    symmetry=input("Wrong Selection! \nEnter Again: ")
color= input("Pick a color between Red, Green, and Blue:\n")
while not (color=="Red" or symmetry=="Green" or symmetry=="Blue"):
    color=input("Wrong Selection! \nEnter Again: ")
if color=="Red":
    color=(255,0,0)
elif color=="Green":
    color = (0,255,0)
elif color == "Blue":
    color=(0,0,255)
screen = pygame.display.set_mode((800,800))
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing=True
        if event.type==pygame.MOUSEBUTTONUP:
            drawing=False
    if drawing==True:
        x,y=pygame.mouse.get_pos()
        if symmetry=="Vertical":
            pygame.draw.circle(screen,color,(x,y),3,0)
            pygame.draw.circle(screen,color,(800-x,y),3,0)
        elif  symmetry=="Rotational":

            for i in range(8):
                pygame.draw.circle(screen,color,(400+(math.sqrt((400-x)**2+(400-y)**2)*math.cos(math.atan2(400-y,x-400)+i*math.radians(45))),400-(math.sqrt((400-x)**2+(400-y)**2)*math.sin(math.atan2(400-y,x-400)+i*math.radians(45)))),3,0)
        elif  symmetry=="Radial":

            for i in range(8):

                pygame.draw.circle(screen,color,(400+(math.sqrt((400-x)**2+(400-y)**2)*math.cos((-1)**i*math.atan2(400-y,x-400)+i*math.radians(45))),400-(math.sqrt((400-x)**2+(400-y)**2)*math.sin((-1)**i*math.atan2(400-y,x-400)+i*math.radians(45)))),3,0)
    pygame.display.flip()
pygame.quit()

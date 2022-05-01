import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Test Pygame")

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.draw.circle(win,(255,0,0),(50,50),20)
    pygame.display.update()
pygame.quit()



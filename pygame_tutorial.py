import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Test Pygame")
x=50
y=50
rad =20
vel= 10
run=True
isjump = False
jumpcount=10
while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.draw.circle(win,(255,0,0),(x,y),rad)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>25:
        x-=vel
    if keys[pygame.K_RIGHT] and x<475:
        x +=vel
    if not(isjump):
        if keys[pygame.K_DOWN] and y<475:
            y += vel
        if keys[pygame.K_UP] and y>25:
            y -= vel
        if keys[pygame.K_SPACE]:
            isjump =True
    else:
        if jumpcount >=-10 :
            neg =1
            if jumpcount<0:
                neg=-1
            y -= (jumpcount)**2 *0.5 *neg
            jumpcount-=1
        else:
            isjump=False
            jumpcount=10
    win.fill((0,0,0))
pygame.quit()



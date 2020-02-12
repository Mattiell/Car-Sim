import pygame 

#Starts the game. You always have to do this for every pygame program.
pygame.init()

#Setting up a window screen. Also gives name.
screensize = (900, 900)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Parking Simulator")

#Making an variables. (CAR), screen, etc. attributes.

black = (0, 0, 0)
red = (255, 0, 0)
x = 50
y = 50
width = 40
height = 60
vel = 5

def drawcar():     
    screen.fill(black)    
    pygame.image.load('car.png')
    pygame.draw.rect(screen, (red), (x, y, width, height))
    pygame.display.update()

#vel = rate of change. Isn't a function, just a variabe.

#Main loop. From start of game to end. For loop is a list of all things that the loop has to check.
gamerun = True
while gamerun:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False

    keys = pygame.key.get_pressed()

   
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:    
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    pygame.draw.rect(screen, (red), (x, y, width, height))
    pygame.display.update(1)
    

#"Car" Character. Arguments (window that you want it to show up on, (R,G,B Values) (x, y, dimensions, more dimensions))
#Refresh rate so that all arguments in the loop continue to execute.
#Very end of loop. Terminates program.

pygame.quit()            

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
cloud_x = 100


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    cloud_x += 1
    colour_change_speed= 1



    # DRAWING
    red=25
    green=133
    blue=46
   
    lightgreen= (54, 191, 81)
    midgreen= (45, 156, 67)
    darkgreen=(red, green, blue)
    brown= (150, 75, 29)
    darkbrown= (92, 57, 19)
    pine= (19, 92, 45)
    
    screen.fill((135, 206, 235))  # always the first drawing command
 
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x, 100), 40)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 34, 80), 40)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 45, 100), 40)
 #landscape
    pygame.draw.circle(screen, (darkgreen), (153, 209), 100)
    pygame.draw.circle(screen, (darkgreen), (404, 130), 100)
    pygame.draw.circle(screen, (lightgreen), (50, 350), 150)
    pygame.draw.circle(screen, (midgreen), (300, 300), 150)
    pygame.draw.circle(screen, (lightgreen), (550, 300), 200)
    pygame.draw.circle(screen, (darkgreen), (622, 286), 100)
    pygame.draw.rect(screen, (lightgreen), ( 0, 296, WIDTH, HEIGHT//3*2))
    pygame.draw.ellipse(screen, (65, 183, 209), ( -10, 389, 300, 150))
   
#trees
    pygame.draw.polygon(screen, (pine), [(101, 121), (41, 288), (172, 293)])
    pygame.draw.polygon(screen, (pine), [(408, 67), (286, 295), (454, 287)])
    
    pygame.draw.circle(screen, (lightgreen), (167, 213), 50)
    pygame.draw.rect(screen, (brown), (163, 238, 15, 70))
#cottage
    pygame.draw.rect(screen, (brown), ( 310, 219, 300, 100))
    pygame.draw.polygon(screen, (darkbrown), [(457, 130), (637, 219), (278, 218)])
    pygame.draw.polygon(screen, (darkbrown), [(372, 234), (455, 173), (546, 236)])
    pygame.draw.rect(screen, (darkbrown), (430, 249, 50, 75))

while green > 0:
        green-=colour_change_speed


while red < 255:
        red+=colour_change_speed
    
    # Must be the last two lines
    # of the game loop
pygame.display.flip()
clock.tick(30)

#duck

    #---------------------------


pygame.quit()

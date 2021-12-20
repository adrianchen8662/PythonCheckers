'''
====INSTRUCTIONS ON HOW TO PLAY====
Cursor movement is really hard to code, so movement is done using the keyboard
The checkerboard is on a 8 by 8 checkerboard, and a display on the right will show where your selection is from (0,0) to (8,8)
To move a checkerpiece off the board, press the button "T"
To reset the game, press the button "R"
To change between a king and a regular piece, press the button "E"
To close the game, press the exit button for the window

The logic section would have added much more to the code, so currently, the movement is on an honor system
This shouldn't be a problem either way because the current game was two-player anyways

Occasionally, the game will glitch and crash on startup. If this happens, close the program and wait for the console to restart
Once the instance is reset to In [1], run again
'''

# Import Statments
import checkerboard_items as ch
import pygame
import pygame.locals
from checkerpiece_controller import blackcp, whitecp, kingwhitecp, kingblackcp

# Various variables used later
selection = [0,0]
selected = True

# Reloads images for checkerpieces and checkerboard
ch.whitecp()
ch.checkerboard()
ch.blackcp()
ch.kingwhitecp()
ch.kingblackcp()

# Initialization of pygame for visuals and control
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption('Checkers Game - Adrian Chen ENGR 13300')
pygame.display.toggle_fullscreen()

# Counters for checkerpieces left on either side
blackcpcount = 0
whitecpcount = 0
kingblackcpcount = 0
kingwhitecpcount = 0

# Text for the menu and game
checkerboard = pygame.image.load('checkerboard.jpg')
myfont = pygame.font.SysFont('Times New Roman', 30)

title = myfont.render('===Checkers Game===', True, (0,0,0))
restart = myfont.render('Restart - Press R', True, (0,0,0))

blackcheckercounter = myfont.render("{}={}".format("Black Checker Count", blackcpcount), True, (0,0,0))
whitecheckercounter = myfont.render("{}={}".format("White Checker Count", whitecpcount), True, (0,0,0))
blackkingcheckercounter = myfont.render("{}={}".format("Black King Checker Count", kingblackcpcount), True, (0,0,0))
whitekingcheckercounter = myfont.render("{}={}".format("White King Checker Count", kingwhitecpcount), True, (0,0,0))

# Loads the checkerpieces
blackcp = blackcp()
whitecp = whitecp()
kingwhitecp = kingwhitecp()
kingblackcp = kingblackcp()

# Fill the background with white and creates the static parts of the screen
screen.fill((255, 255, 255))
screen.blit(checkerboard, (0,0))
screen.blit(title, (820,10))
screen.blit(restart, (820,750))

# Generates the first set of checkerpieces
screen.blit(kingblackcp.image, (100,0))
screen.blit(blackcp.image, (300,0))
screen.blit(blackcp.image, (500,0))
screen.blit(blackcp.image, (700,0))
screen.blit(blackcp.image, (000,100))
screen.blit(blackcp.image, (200,100))
screen.blit(blackcp.image, (400,100))
screen.blit(blackcp.image, (600,100))
screen.blit(blackcp.image, (100,200))
screen.blit(blackcp.image, (300,200))
screen.blit(blackcp.image, (500,200))
screen.blit(blackcp.image, (700,200))

screen.blit(whitecp.image, (0,500))
screen.blit(whitecp.image, (200,500))
screen.blit(whitecp.image, (400,500))
screen.blit(whitecp.image, (600,500))
screen.blit(whitecp.image, (100,600))
screen.blit(whitecp.image, (300,600))
screen.blit(whitecp.image, (500,600))
screen.blit(whitecp.image, (700,600))
screen.blit(whitecp.image, (0,700))
screen.blit(whitecp.image, (200,700))
screen.blit(whitecp.image, (400,700))
screen.blit(whitecp.image, (600,700))

# Run until the user asks to quit
running = True
while running:

    # Exit the loop if the exit button is pressed on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # If the R button is pressed, reset all the checkerpieces back to where they were
    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        screen.blit(blackcp.image, (100,0))
        screen.blit(blackcp.image, (300,0))
        screen.blit(blackcp.image, (500,0))
        screen.blit(blackcp.image, (700,0))
        screen.blit(blackcp.image, (000,100))
        screen.blit(blackcp.image, (200,100))
        screen.blit(blackcp.image, (400,100))
        screen.blit(blackcp.image, (600,100))
        screen.blit(blackcp.image, (100,200))
        screen.blit(blackcp.image, (300,200))
        screen.blit(blackcp.image, (500,200))
        screen.blit(blackcp.image, (700,200))
        
        screen.blit(whitecp.image, (0,500))
        screen.blit(whitecp.image, (200,500))
        screen.blit(whitecp.image, (400,500))
        screen.blit(whitecp.image, (600,500))
        screen.blit(whitecp.image, (100,600))
        screen.blit(whitecp.image, (300,600))
        screen.blit(whitecp.image, (500,600))
        screen.blit(whitecp.image, (700,600))
        screen.blit(whitecp.image, (0,700))
        screen.blit(whitecp.image, (200,700))
        screen.blit(whitecp.image, (400,700))
        screen.blit(whitecp.image, (600,700))
        
    # Moves the selection
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        if selection[0] != 0:
            selection[0] -= 1
            print(selection)
    if event.type == pygame.KEYDOWN and event.key == pygame.k_RIGHT:
        if selection[1] != 8:
            selection[1] += 1
            print(selection)
    if event.type == pygame.KEYDOWN and event.key == pygame.k_DOWN:
        if selection[0] != 8:
            selection[1] += 1
            print(selection)
    if event.type == pygame.KEYDOWN and event.key == pygame.k_LEFT:
        if selection[1] != 0:
            selection[1] -= 1
            print(selection)
    if event.type == pygame.KEYDOWN and event.key == pygame.k_SPACE:
        if selected == True:
            selected == False
            print(selected)
        else:
            selected == True
            print(selected)
            
    # Adds checker type counters
    blackcheckercounter = myfont.render("{}={}".format("Black Checker Count", blackcpcount), True, (0,0,0))
    whitecheckercounter = myfont.render("{}={}".format("White Checker Count", whitecpcount), True, (0,0,0))
    blackkingcheckercounter = myfont.render("{}={}".format("Black King Checker Count", kingblackcpcount), True, (0,0,0))
    whitekingcheckercounter = myfont.render("{}={}".format("White King Checker Count", kingwhitecpcount), True, (0,0,0))
    selectionblit = myfont.render("{}={}".format("Selection", selection), True, (0,0,0))
    screen.blit(blackcheckercounter, (820,40))
    screen.blit(whitecheckercounter, (820,70))
    screen.blit(blackkingcheckercounter, (820,100))
    screen.blit(whitekingcheckercounter, (820,130))
    screen.blit(selectionblit, (820,160))
    pygame.display.flip()
    
#Exits the program
pygame.quit()
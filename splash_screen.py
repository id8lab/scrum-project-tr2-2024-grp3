import pygame as pyga
import thorpy as thor

pyga.init()

# Set up the screen
screen = pyga.display.set_mode((1200, 700))
thor.init(screen, thor.theme_classic)

# Load the background image
background = pyga.image.load("assets/bg_main.jpg")
background = pyga.transform.scale(background, (1200, 700))

# Widgets - main
startbtn = thor.Button("Start")
settbtn = thor.Button("Settings")
splash = thor.Text("-Name-")

# Widget - setting
testchk = thor.Checkbox("test")

# Main Screen
mainscreen = thor.Box([splash, startbtn, settbtn])
mainscreen.sort_children(margins=(40, 40))
mainscreen.set_resizable(False, False)
mainscreen.center_on(screen)

# Setting Screen
settscreen = thor.Box([testchk])

# Defines
def at_refresh():
    screen.blit(background, (0, 0))
    # No need to fill the screen with white here

def gamestart():
    print('start')

def settings():
    settscreen.set_screen()
    print('settings')

# Button functions
startbtn.at_unclick = gamestart
settbtn.at_unclick = settings

# Launch the main screen
mainscreen.get_updater().launch(at_refresh)

input()
pyga.quit()


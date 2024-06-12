import pygame as pyga
import thorpy as thor
pyga.init()

screen = pyga.display.set_mode((1200,700))
thor.init(screen,thor.theme_classic)

# Widgets - main
startbtn = thor.Button("Start")
settbtn = thor.Button("Settings")
splash = thor.Text("-Name-")

# Widget - settting
testchk = thor.Checkbox("test")

# Main Screen
mainscreen = thor.Box([splash,startbtn,settbtn])
mainscreen.sort_children(margins=(40,40))
mainscreen.set_resizable(False,False)
mainscreen.center_on(screen)

# Setting
settscreen = thor.Box([testchk])

# Defines
def at_refresh():
    screen.fill((255,)*3)

def gamestart():
    print('start')

def settings():
    settscreen.set_screen()
    print('settings')
    
# Btn func
startbtn.at_unclick = gamestart
settbtn.at_unclick = settings

mainscreen.get_updater().launch(at_refresh)

input()
pygame.quit()

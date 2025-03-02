import pygame as py
import random

# Initialize Pygame
py.init()

# Set up the display
size = (1000, 900)
screen = py.display.set_mode(size)

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_animated_circle(screen, color, pos, final_radius):
    for radius in range(1, final_radius + 1):
        py.draw.circle(screen, color, pos, radius)
        py.display.flip()
        py.time.delay(5)

# Main loop
while True:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            exit()
        if ev.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            col = get_random_color()
            draw_animated_circle(screen, col, pos, 20)
    
    py.display.flip()  # Update the entire display

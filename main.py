import pygame
from objects import *
from ui import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

triangle = RightTriangle((100, 620), 500, math.radians(30))

colors = {
    "bg": (0, 0, 0),
    "base": (255, 0, 0),
    "alt": (0, 255, 0),
    "hyp": (0, 0, 255)
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(colors["bg"])

    # Draw the triangle.
    pygame.draw.line(screen, colors["base"], triangle.points[0], triangle.points[1], width=1) # Base.
    pygame.draw.line(screen, colors["alt"], triangle.points[1], triangle.points[2], width=1) # Alt.
    pygame.draw.line(screen, colors["hyp"], triangle.points[2], triangle.points[0], width=1) # Hyp.

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
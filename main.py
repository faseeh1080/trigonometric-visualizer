import pygame
from objects import *
from ui import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0

triangle = RightTriangle((100, 620), 500, math.radians(30))

colors = {
    "bg": (0, 0, 0),
    "primary": (180, 180, 180),
    "base": (255, 0, 0),
    "alt": (0, 255, 0),
    "hyp": (0, 0, 255)
}

segoeui_font = pygame.font.SysFont("segoeui", 12, False, False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(colors["bg"])

    # HUD
    hud_text_surfaces = [
        segoeui_font.render("scene: 1", False, colors["primary"], None),
        segoeui_font.render(f"delta_time: {delta_time}ms", False, colors["primary"], None)
    ]

    blit_surfaces_as_list(hud_text_surfaces, screen, (10, 10), 2)

    # Draw the triangle.
    pygame.draw.line(screen, colors["base"], triangle.points[0], triangle.points[1], width=1) # Base.
    pygame.draw.line(screen, colors["alt"], triangle.points[1], triangle.points[2], width=1) # Alt.
    pygame.draw.line(screen, colors["hyp"], triangle.points[2], triangle.points[0], width=1) # Hyp.

    pygame.display.flip()

    delta_time = clock.tick(60) # `clock.tick(60)` also limits the frame rate to 60 FPS.

pygame.quit()
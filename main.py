import pygame
from objects import *
from ui import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0

triangle = RightTriangle((100, 620), 500, 30)

colors = {
    "bg": (0, 0, 0),
    "primary": (180, 180, 180),
}

segoeui_font = pygame.font.SysFont("segoeui", 12, False, False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(colors["bg"])

    # Handle input.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        triangle.increment_angle(15, delta_time)
    elif keys[pygame.K_DOWN]:
        triangle.increment_angle(-15, delta_time)

    # HUD
    hud_text_surfaces = [
        segoeui_font.render("Use up and down arrow keys to control the triangle.", False, colors["primary"], None),
        segoeui_font.render("scene: 1", False, colors["primary"], None),
        segoeui_font.render(f"delta_time: {delta_time}ms", False, colors["primary"], None)
    ]

    blit_surfaces_as_list(hud_text_surfaces, screen, (10, 10), 2)

    triangle.draw(screen)

    pygame.display.flip()

    delta_time = clock.tick(60) # `clock.tick(60)` also limits the frame rate to 60 FPS.

pygame.quit()
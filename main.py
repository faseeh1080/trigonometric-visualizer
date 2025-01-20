import pygame
from objects import *
from ui import *
from scenes import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0

colors = {
    "bg": (0, 0, 0),
    "primary": (180, 180, 180),
}

scenes_list = [TrigonometricFunctions, PythagoreanTheorem]
current_scene_no = 0
current_scene = scenes_list[current_scene_no]() # Default.
def go_to_next_or_prev_scene(direction: int) -> None:
    """direction: +ve to go forward and -ve to go backward."""
    global current_scene_no
    global current_scene
    if direction > 0: # Go forward.
        current_scene_no += 1
        if current_scene_no >= len(scenes_list):
            current_scene_no = 0
    elif direction < 0: # Go backward.
        current_scene_no -= 1
        if current_scene_no < 0:
            current_scene_no = len(scenes_list) - 1
    else: # If its zero.
        return
    
    current_scene = scenes_list[current_scene_no]()

show_help = False
help_text = "Use the up and down arrows to adjust the angle. Use the left and right arrows to switch scenes."
help_surface = segoeui_medium.render(help_text, True, (255, 255, 255), None)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                go_to_next_or_prev_scene(1)
            if event.key == pygame.K_LEFT:
                go_to_next_or_prev_scene(-1)
            if event.key == pygame.K_h:
                show_help = not show_help

    screen.fill(colors["bg"])

    keys = pygame.key.get_pressed() # Used by the refresh method in scenes.

    # HUD
    hud_text_surfaces = [
        segoeui_small.render(f"scene: {current_scene.name}", False, colors["primary"], None),
        segoeui_small.render(f"delta_time: {delta_time}ms", False, colors["primary"], None),
        segoeui_small.render("Press H for help.", False, colors["primary"], None)
    ]

    blit_surfaces_as_list(hud_text_surfaces, screen, (10, 10), 2)
    if show_help:
        screen.blit(help_surface, (10, 688))

    current_scene.refresh(screen, delta_time, keys)

    keys_prev_frame = keys

    pygame.display.flip()

    delta_time = clock.tick(60) # `clock.tick(60)` also limits the frame rate to 60 FPS.

pygame.quit()
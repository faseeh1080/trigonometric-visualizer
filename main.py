import pygame
from objects import *
from ui import *
from scenes import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0

ui = pygame.Surface((1280, 720), pygame.SRCALPHA)
viewport = pygame.Surface((1280, 720), pygame.SRCALPHA)

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                go_to_next_or_prev_scene(1)
            if event.key == pygame.K_LEFT:
                go_to_next_or_prev_scene(-1)

    screen.fill(colors["bg"])
    ui.fill((0, 0, 0, 0))
    viewport.fill((0, 0, 0, 0))

    keys = pygame.key.get_pressed() # Used by the refresh method in scenes.

    # HUD
    hud_text_surfaces = [
        segoeui_small.render(f"scene: {current_scene.name}", False, colors["primary"], None),
        segoeui_small.render(f"delta_time: {delta_time}ms", False, colors["primary"], None),
        segoeui_small.render("Press H for help.", False, colors["primary"], None)
    ]

    blit_surfaces_as_list(hud_text_surfaces, ui, (10, 10), 2)

    current_scene.refresh(viewport, delta_time, keys)

    screen.blit(ui, (0, 0))
    screen.blit(viewport, (0, 0))

    keys_prev_frame = keys

    pygame.display.flip()

    delta_time = clock.tick(60) # `clock.tick(60)` also limits the frame rate to 60 FPS.

pygame.quit()
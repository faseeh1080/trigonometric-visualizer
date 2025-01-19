import pygame

def blit_surfaces_as_list(
        sources: list[pygame.Surface],
        target: pygame.Surface,
        position: tuple[int, int],
        padding = int
) -> None:
    """The Surface(s) in `sources` are drawn onto the `target` Surface from top to bottom"""
    x_position = position[0]
    current_y_position = position[1]
    for source in sources:
        target.blit(source, (x_position, current_y_position))
        current_y_position += source.get_height() + padding

def blit_surface_in_the_middle_of_two_points(
    source: pygame.Surface,
    target: pygame.Surface,
    point1: tuple[int, int],
    point2: tuple[int, int],
    offset: tuple[int, int] = (0, 0)
) -> None:
    
    center = (
        (point1[0] + point2[0]) / 2,
        (point1[1] + point2[1]) / 2
    )

    source_position = (
        center[0] - (source.get_width() / 2) + offset[0],
        center[1] - (source.get_height() / 2) + offset[1]
    )

    target.blit(source, source_position)
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
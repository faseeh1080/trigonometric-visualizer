import pygame

def blit_surfaces_as_list(
        sources: list[pygame.Surface],
        target: pygame.Surface,
        position: tuple[int, int],
        padding: int = 0
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

def draw_square_from_two_points(
        surface: pygame.Surface,
        point0: tuple[int, int],
        point1: tuple[int, int],
        border_color: tuple[int, int, int],
        border_width: int = 1,
        fill_color: None | tuple[int, int, int, int] = None
) -> tuple:
    """Returns the points of the square"""

    point2 = (point1[0] - (point1[1] - point0[1]), point1[1] + (point1[0] - point0[0]))
    point3 = (point0[0] - (point1[1] - point0[1]), point0[1] + (point1[0] - point0[0]))

    if fill_color:
        temp_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
        pygame.draw.polygon(temp_surface, fill_color, [point0, point1, point2, point3])
        surface.blit(temp_surface, (0, 0))
        # The draw method erases the pixels behind even if we give it a semitransparent color.
        # To draw transparent squares, create a temporary surface object and draw the square 
        # with an RGBA color. Then blit the temporary surface into the target surface.
    pygame.draw.lines(surface, border_color, True, [point0, point1, point2, point3], border_width)

    return point0, point1, point2, point3
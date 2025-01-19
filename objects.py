import math
import pygame

pygame.font.init()
# pygame.init() initializes all pygame modules.
# Use pygame.font.init() to initialize the `font` module only.
segoeui_font = pygame.font.SysFont("segoeui", 12, False, False)

class RightTriangle:
    def __init__(self, position, hyp, angle):
        self.position = position
        self.hyp = hyp # The length of the hypotenuse.
        self.angle = math.radians(angle)
        self.points = [(0, 0), (0, 0), (0, 0)]

        self.refresh_points()
        
    def refresh_points(self):
        self.points[0] = self.position

        base_length = math.cos(self.angle) * self.hyp
        self.points[1] = (self.position[0] + base_length, self.position[1])

        altitude = math.sin(self.angle) * self.hyp
        self.points[2] = (self.points[1][0], self.position[1] - altitude)

    def increment_angle(self, value: float, delta_time: float):
        """`value` in degrees. Can be positive or negative."""
        self.angle += math.radians(value) * delta_time / 1000
        self.refresh_points()

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.line(surface, (255, 0, 0), self.points[0], self.points[1], width=1) # Base.
        pygame.draw.line(surface, (0, 255, 0), self.points[1], self.points[2], width=1) # Alt.
        pygame.draw.line(surface, (0, 0, 255), self.points[2], self.points[0], width=1) # Hyp.
import pygame
from objects import *

class Default:
    def __init__(self):
        self.name = "Triangle"
        self.triangle = RightTriangle((100, 620), 500, 30)
    
    def refresh(self, surface: pygame.Surface, delta_time: float, keys) -> None:
        """Handles input and draws the triangle to the `surface`.
        Get `keys` from pygame.key.get_pressed()"""
        # Handle Input.
        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.triangle.increment_angle(15, delta_time)
        elif keys[pygame.K_DOWN]:
            self.triangle.increment_angle(-15, delta_time)

        # Draw the triangle.
        self.triangle.draw(surface)

class PythagoreanTheorem:
    def __init__(self) -> None:
        self.name = "Pythagorean Theorem"
        self.triangle = RightTriangle((320, 360), 320, 30)
    
    def refresh(self, surface: pygame.Surface, delta_time: float, keys) -> None:
        """Handles input and draws the triangle to the `surface`.
        Get `keys` from pygame.key.get_pressed()"""
        # Handle Input.
        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.triangle.increment_angle(15, delta_time)
        elif keys[pygame.K_DOWN]:
            self.triangle.increment_angle(-15, delta_time)

        # Draw the triangle.
        self.triangle.draw(surface)
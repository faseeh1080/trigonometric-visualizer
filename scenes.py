import pygame
import math
import my_math
from objects import *
from ui import *

class TrigonometricFunctions:
    def __init__(self):
        self.name = "Trigonometric Functions"
        self.triangle = RightTriangle((640, 360), 350, 30)
    
    def refresh(self, surface: pygame.Surface, delta_time: float, keys) -> None:
        """Handles input and draws the triangle to the `surface`.
        Get `keys` from pygame.key.get_pressed()"""

        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.triangle.increment_angle(25, delta_time)
        elif keys[pygame.K_DOWN]:
            self.triangle.increment_angle(-25, delta_time)

        self.triangle.draw(surface)

        sin_value = math.sin(self.triangle.angle)
        cos_value = math.cos(self.triangle.angle)
        sin_surface_1 = segoeui_medium.render(f"sinΘ = {round(sin_value, 3)}", True, (255, 0, 0), None)
        cos_surface_1 = segoeui_medium.render(f"cosΘ = {round(cos_value, 3)}", True, (0, 255, 0), None)
        unity_surface = segoeui_medium.render("1.0", True, (0, 0, 255), None)
        blit_surface_in_the_middle_of_two_points(
            sin_surface_1, surface, self.triangle.points[0], self.triangle.points[1], (0, 10)
        )
        blit_surface_in_the_middle_of_two_points(
            cos_surface_1, surface, self.triangle.points[1], self.triangle.points[2], (0, 10)
        )
        blit_surface_in_the_middle_of_two_points(
            unity_surface, surface, self.triangle.points[2], self.triangle.points[0], (0, 10)
        )

        tan_value, csc_value, sec_value, cot_value = my_math.tan_csc_sec_cot_from_sin_cos(sin_value, cos_value)
        text_color = (255, 255, 255)
        sin_surface = segoeui_small.render(f"sinΘ = {sin_value}", True, text_color, None)
        cos_surface = segoeui_small.render(f"cosΘ = {cos_value}", True, text_color, None)
        tan_surface = segoeui_small.render(f"tanΘ = {tan_value}", True, text_color, None)
        csc_surface = segoeui_small.render(f"cscΘ = {csc_value}", True, text_color, None)
        sec_surface = segoeui_small.render(f"secΘ = {sec_value}", True, text_color, None)
        cot_surface = segoeui_small.render(f"cotΘ = {cot_value}", True, text_color, None)
        info_surfaces = (sin_surface, cos_surface, tan_surface, csc_surface, sec_surface, cot_surface)
        blit_surfaces_as_list(info_surfaces, surface, (1270, 10), 2, align_right=True)
        

class PythagoreanTheorem:
    def __init__(self) -> None:
        self.name = "Pythagorean Theorem"
        self.triangle = RightTriangle((480, 360), 240, 30)
    
    def refresh(self, surface: pygame.Surface, delta_time: float, keys) -> None:
        """Handles input and draws the triangle to the `surface`.
        Get `keys` from pygame.key.get_pressed()"""
        
        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.triangle.increment_angle(20, delta_time)
        elif keys[pygame.K_DOWN]:
            self.triangle.increment_angle(-20, delta_time)

        self.triangle.draw(surface)

        base_square_points = draw_square_from_two_points(surface, self.triangle.points[0], self.triangle.points[1], (255, 0, 0), fill_color=(255, 0, 0, 50))
        alt_square_points = draw_square_from_two_points(surface, self.triangle.points[1], self.triangle.points[2], (0, 255, 0), fill_color=(0, 255, 0, 50))
        hyp_square_points = draw_square_from_two_points(surface, self.triangle.points[2], self.triangle.points[0], (0, 0, 255), fill_color=(0, 0, 255, 50))

        sin_value = math.sin(self.triangle.angle)
        cos_value = math.cos(self.triangle.angle)

        cos = segoeui_medium.render(f"cos^2 Θ = {round(cos_value ** 2, 3)}", True, (255, 0, 0), None)
        sin = segoeui_medium.render(f"sin^2 Θ = {round(sin_value ** 2, 3)}", True, (0, 255, 0), None)
        unity = segoeui_medium.render("1.0", True, (0, 0, 255), None)

        blit_surface_in_the_middle_of_two_points(
            cos, surface, base_square_points[0], base_square_points[2]
        )
        blit_surface_in_the_middle_of_two_points(
            sin, surface, alt_square_points[0], alt_square_points[2]
        )
        blit_surface_in_the_middle_of_two_points(
            unity, surface, hyp_square_points[0], hyp_square_points[2]
        )
import math

class RightTriangle:
    def __init__(self, position, hyp, angle):
        self.position = position
        self.hyp = hyp # The length of the hypotenuse.
        self.angle = angle # In radians.
        self.points = [(0, 0), (0, 0), (0, 0)]

        self.refresh_points()
        
    def refresh_points(self):
        self.points[0] = self.position

        base_length = math.cos(self.angle) * self.hyp
        self.points[1] = (self.position[0] + base_length, self.position[1])

        altitude = math.sin(self.angle) * self.hyp
        self.points[2] = (self.points[1][0], self.position[1] - altitude)
        
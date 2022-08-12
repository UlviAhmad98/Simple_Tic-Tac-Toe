class Sphere:
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = ((self.PI * pow(radius, 3) * 4) / 3)


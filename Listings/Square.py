class Square():
    
    def __init__(self, sidelength=1):
        self.length = sidelength

    def calculate_circumference(self):
        return 4*self.length

    def calculate_area(self):
        return self.length**2

q = Square(sidelength=25)
print(q.calculate_circumference())
print(q.calculate_area())

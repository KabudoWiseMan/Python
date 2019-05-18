class Iv:
    def __init__(self, *args):
        if len(args) == 2:
            self.l = args[0]
            self.r = args[1]
        elif len(args) == 1:
            self.r = self.l = args[0]
    def __add__(self, iv):
        return [self.l + iv.l, self.r + iv.r]
    def __sub__(self, iv):
        return [self.l - iv.l, self.r + iv.r]
    def __mul__(self, iv):
        return [min(self.l * iv.l, self.l * iv.r, self.r * iv.l, self.r * iv.r),
                max(self.l * iv.l, self.l * iv.r, self.r * iv.l, self.r * iv.r)]
    def __truediv__(self, iv):
        if iv.l <= 0 <= iv.r:
            raise ZeroDivisionError
        return [min(self.l / iv.l, self.l / iv.r, self.r / iv.l, self.r / iv.r),
                max(self.l / iv.l, self.l / iv.r, self.r / iv.l, self.r / iv.r)]

print(Iv(1.0,2.0) + Iv(2.0,4.0))
print(Iv(1.0,2.0) - Iv(2.0,4.0))
print(Iv(1.0,2.0) * Iv(2.0,4.0))
print(Iv(1.0,2.0) * Iv(2.0))
print(Iv(9.5,10.5) / Iv(-1.0, 1.0))

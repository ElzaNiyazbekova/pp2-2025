class sh():
    def __init__(self):
        pass
    def area(self):
        return 0

class rec():
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
rec= rec(11, 5)
print(rec.area())
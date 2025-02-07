class sh():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class sq(sh):
        def __init__(self, length):
            self.length = length
        def area(self):
            return self.length**2
s = sh()

sq = sq(11)
print(sq.area())

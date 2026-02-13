class p():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sh(self):
        print(self.x, self.y) 
    def move(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x += self.x1
        self.y += self.y1
    def dist(self):
        return self.x-self.x1
    
p = p(11, 12)
p.move(8, 9)
# print()
p.sh()


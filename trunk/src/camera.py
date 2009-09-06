class Camera(object):
    
    game = None
    
    def __init__(self, h, w):
        self.height = h
        self.width = w
        self.x = 0
        self.y = 0
        self.edge = 7
    
    def is_in_view(self, x, y):
        if x >= self.x and x <= self.x + self.width:
            if y >= self.y and y <= self.y + self.height:
                return True
        return False    
    
    def adjust(self, x, y):
        adj=False
        #adjust to down
        if y - self.y > self.height - self.edge:
            self.y += 1
            adj=True
        #adjust to up
        if y - self.y < self.edge:
            self.y -= 1
            adj=True
            
        #adjust to right
        if x - self.x > self.width - self.edge:
            self.x += 1
            adj=True
        #adjust to up
        if x - self.x < self.edge:
            self.x -= 1
            adj=True
        return adj
class Coockie:
    def __init__(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Coockie('green')
cookie_two = Coockie('blue')

print(cookie_one.get_color())
cookie_one.set_color('red')
print(cookie_one.get_color())
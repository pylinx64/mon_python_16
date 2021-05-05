import pyxel

# класс приложения 
class App:
    # конструктор
    def __init__(self, x_screen, y_screen):
        # берем параметры экрана
        self.x_screen = x_screen 
        self.y_screen = y_screen
        # создаем экран
        pyxel.init(self.x_screen, self.y_screen, caption='Hello program')
        pyxel.run(self.update, self.draw)

    # обновление экрана
    def update(self):
        pass
       
    # рисование
    def draw(self):
        pass
   

App(160, 160)



   
#-пример----------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
pt1 = Point(10, 15)
pt2 = Point(20, 20)
#print( pt1.x )
#print( pt2.x )

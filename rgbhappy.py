from rgb_matrix import RGB_Matrix
import time

# class_labels = {0: 'Angry', 1: 'Fear', 2: 'Happy', 3: 'Neutral', 4: 'Sad', 5: 'Surprise'}
class RGBHappy():
    def __init__(self):
        self.rr = RGB_Matrix(0X74)
   
  
    def neutral(self):
        colors = [
            (0,0,0),
            (255,255,255),
            (255,255,255),
        ]
        shape = [
            [0,1,0,0,0,0,1,0],
            [1,2,1,0,0,1,2,1],
            [0,1,0,0,0,0,1,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0],
        ]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                self.rr.draw_point((y, x), colors[shape[y][x]])
        self.rr.display()


    def happy(self):
        colors = [
            (0,0,0),
            (128,128,20),
            (255,255,255),
        ]
        shape = [
            [0,1,0,0,0,0,1,0],
            [1,2,1,0,0,1,2,1],
            [0,1,0,0,0,0,1,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,1,0,0,0,0,1,0],
            [0,1,0,0,0,0,1,0],
            [0,0,1,1,1,1,0,0],
        ]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                self.rr.draw_point((y, x), colors[shape[y][x]])
        self.rr.display()


    def sad(self):
        colors = [
            (0,0,0),
            (0,64,255),
        ]
        shape = [
            [0,0,1,0,0,1,0,0],
            [0,1,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,1,0,0,0,0,1,0],
        ]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                self.rr.draw_point((y, x), colors[shape[y][x]])
        self.rr.display()
        
        
    def angry(self):
        colors = [
            (0,0,0),
            (255,0,0),
        ]
        shape = [
            [0,1,0,0,0,0,1,0],
            [0,0,1,0,0,1,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,1,0,0,0,0,1,0],
        ]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                self.rr.draw_point((y, x), colors[shape[y][x]])
        self.rr.display()
    
    
    def fear(self):
        colors = [
            (0,0,0),
            (64,64,255),
        ]
        shape = [
            [0,0,1,0,0,1,0,0],
            [1,1,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,1,0,0,0,0,1,0],
        ]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                self.rr.draw_point((y, x), colors[shape[y][x]])
        self.rr.display()


    def surprise(self):
        colors = [
            (0,0,0),
            (64,64,255),
        ]
        shape = [
            [0,1,0,0,0,0,1,0],
            [1,0,1,0,0,1,0,1],
            [0,1,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,0,1,1,0,0,0],
         ]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                self.rr.draw_point((y, x), colors[shape[y][x]])
        self.rr.display()


if __name__ == "__main__":
    rgb = RGBHappy()
    while True:
        rgb.neutral()
        time.sleep(0.5)
        rgb.happy()
        time.sleep(0.5)
        rgb.sad()
        time.sleep(0.5)
        rgb.angry()
        time.sleep(0.5)
        rgb.fear()
        time.sleep(0.5)
        rgb.surprise()
        time.sleep(0.5)

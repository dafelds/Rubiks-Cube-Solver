import numpy as np
from abc import ABC, abstractmethod

class SyntheticColor(ABC):
    red: int
    green: int
    blue: int
    
    @abstractmethod
    def synthesize_color(self):
        pass

    
class SyntheticRed(SyntheticColor):
    def __init__(self):
        self.synthesize_color()
    
    def synthesize_color(self) -> None:
        self.red = np.random.randint(127,256)
        self.green = np.random.randint(0, self.red/2)
        if self.green >= self.red/4:
            self.blue = self.green
        else:
            self.blue = np.random.randint(0, self.red/4)

            
class SyntheticBlue(SyntheticColor):
    def __init__(self):
        self.synthesize_color()
    
    def synthesize_color(self) -> None:
        self.blue = np.random.randint(127,256)
        self.green = np.random.randint(0, self.blue/2)
        if self.green >= self.blue/4:
            self.red = self.green
        else:
            self.red = np.random.randint(0, self.blue/4)

            
class SyntheticGreen(SyntheticColor):
    def __init__(self):
        self.synthesize_color()
    
    def synthesize_color(self) -> None:
        self.green = np.random.randint(63,256)
        self.blue = np.random.randint(0, self.green*2/3)
        if self.blue >= self.green/3:
            self.red = self.blue
        else:
            self.red = np.random.randint(0, self.green/3)
       
    
class SyntheticWhite(SyntheticColor):
    def __init__(self):
        self.synthesize_color()
    
    def synthesize_color(self) -> None:
        self.red, self.blue, self.green = [np.random.randint(224,256)]*3
    
    
class SyntheticBlack(SyntheticColor):
    def __init__(self):
        self.synthesize_color()
    
    def synthesize_color(self) -> None:
        self.red, self.blue, self.green = [np.random.randint(0,32)]*3

        
class SyntheticYellow(SyntheticColor):
    def __init__(self):
        self.synthesize_color()
    
    def synthesize_color(self) -> None:
        self.red, self.green = [np.random.randint(224,256)]*2
        self.blue = np.random.randint(0,32)
        
        
class SyntheticOrange(SyntheticColor):
    def __init__(self):
        self.synthesize_color()
    
    def synthesize_color(self) -> None:
        self.red = np.random.randint(224,256)
        self.green = np.random.randint(0.65*self.red,0.75*self.red)
        self.blue = np.random.randint(self.red/4)
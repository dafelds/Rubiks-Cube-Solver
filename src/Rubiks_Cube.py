import numpy as np
from copy import deepcopy

class Cube:
    
    position = {
        'U': (0,3),
        'L': (3,0),
        'F': (3,3),
        'R': (3,6),
        'B': (3,9),
        'D': (6,3)
    }
    
    
    def __init__(self, num_grid = False, color_grid = False):
        if color_grid:
            self.color_grid = color_grid
            self.num_grid = num_grid
        else:
            self.color_grid = self.build_color_grid()
            self.num_grid = self.build_num_grid()

        
    @staticmethod
    def build_num_grid():
        a = np.empty((3,3))
        a[:] = np.nan
        b = []
        for i in range(1,47,9):
            b.append(np.array(range(i, i+9)).reshape((3,3,)))
            
        return np.vstack((
            np.hstack((a, b[0], a, a)),
            np.hstack(b[1:5]),
            np.hstack((a, b[5], a, a))
        ))
    
    
    @staticmethod
    def build_color_grid():
        color_grid = np.empty((9,12)).astype('object')
        color_grid[:] = np.nan
        for key, coord in Cube.position.items():
            y, x = coord
            color_grid[y:y+3, x:x+3] = key
        
        return color_grid
    
    
    @staticmethod
    def _cycle(face, grid, rotation = 1):

        if face == 'U':
            for _ in range(rotation):
                grid[3] = np.r_[grid[3,3:], grid[3,:3]]
        if face == 'D':
            for _ in range(rotation):
                grid[5] = np.r_[grid[5,9:12], grid[5,:9]]
        if face == 'L':
            for _ in range(rotation):
                temp = grid[8:5:-1,3].copy()
                grid[:,3] = np.r_[grid[5:2:-1,11], grid[:6,3]]
                grid[3:6,11] = temp
        if face == 'R':
            for _ in range(rotation):
                temp = grid[2::-1,5].copy()
                grid[:,5] = np.r_[grid[3:,5], grid[5:2:-1,9]]
                grid[3:6,9] = temp
        if face == 'F':
            for _ in range(rotation):
                temp = grid[2, 3:6].copy()
                grid[2, 3:6] = grid[5:2:-1, 2].copy()
                grid[3:6, 2] = grid[6, 3:6].copy()
                grid[6, 3:6] = grid[5:2:-1, 6].copy()
                grid[3:6, 6] = temp
        if face == 'B':
            for _ in range(rotation):
                temp = grid[0, 3:6].copy()
                grid[0, 3:6] = grid[3:6, 8].copy()
                grid[3:6, 8] = grid[8, 5:2:-1].copy()
                grid[8, 3:6] = grid[3:6, 0].copy()
                grid[3:6, 0] = temp[::-1]

                
    @staticmethod
    def _rotate(grid, x, y, rotation):
        return np.rot90(grid[y:y+3, x:x+3], -rotation)

    
    def rotate(self, operation: str):
        
        face = operation[0]
        try:
            rotation = int(operation[1])
        except IndexError:
            rotation = 1 if operation == operation.upper() else -1
        face = face.upper()
        y = self.position[face][0]
        x = self.position[face][1]
        self.num_grid[y:y+3, x:x+3] = self._rotate(self.num_grid, x, y, rotation)
        self.color_grid[y:y+3, x:x+3] = self._rotate(self.color_grid, x, y, rotation)
        self._cycle(face, self.color_grid, (rotation+4)%4)
        self._cycle(face, self.num_grid, (rotation+4)%4)
import numpy as np
from copy import deepcopy
from Rubiks_Cube import Cube

class Solution:
    def __init__(self, color_grid: np.array):
        self.color_grid = color_grid
        self.num_grid = deepcopy(self.color_grid)
        self._build_num_grid()
        self.cube = Cube(num_grid = self.num_grid, color_grid = self.color_grid)
        self.cube.num_grid = self.cube.num_grid.astype('float64')
        del self.color_grid
        del self.num_grid
    
    def _corners(self):
        corner_coordinate_sets = (
            {(0,3), (3,0), (3,11)},
            {(0,5), (3,8), (3,9)},
            {(2,3), (3,2), (3,3)},
            {(2,5), (3,5), (3,6)},
            {(6,3), (5,2), (5,3)},
            {(6,5), (5,5), (5,6)},
            {(8,3), (5,0), (5,11)},
            {(8,5), (5,8), (5,9)}
        )
        
        corner_color_dict = {
            (9, 28, 21): ('W', 'R', 'G'),
            (3, 30, 37): ('W', 'R', 'B'),
            (7, 12, 19): ('W', 'O', 'G'),
            (1, 10, 39): ('W', 'O', 'B'),
            (48, 34, 27): ('Y', 'R', 'G'),
            (54, 36, 43): ('Y', 'R', 'B'),
            (46, 18, 25): ('Y', 'O', 'G'),
            (52, 16, 45): ('Y', 'O', 'B')
        }
        
        for coordinate_set in corner_coordinate_sets:
            self._write_to_num_grid(coordinate_set, corner_color_dict)
        
        
    def _edges(self):
        edge_coordinate_sets = (
            {(0,4), (3,10)},
            {(1,3), (3,1)},
            {(1,5), (3,7)},
            {(2,4), (3,4)},
            {(4,0), (4,11)},
            {(4,2), (4,3)},
            {(4,5), (4,6)},
            {(4,8), (4,9)},
            {(6,4), (5,4)},
            {(7,3), (5,1)},
            {(7,5), (5,7)},
            {(8,4), (5,10)},
        )
        
        edge_color_dict = {
            (6, 29): ('W', 'R'),
            (4, 11): ('W', 'O'),
            (8, 20): ('W', 'G'),
            (2, 38): ('W', 'B'),
            (31, 24): ('R', 'G'),
            (33, 40): ('R', 'B'),
            (15, 22): ('O', 'G'),
            (13, 42): ('O', 'B'),
            (51, 35): ('Y', 'R'),
            (49, 17): ('Y', 'O'),
            (47, 26): ('Y', 'G'),
            (53, 44): ('Y', 'B'),
        }
       
        for coordinate_set in edge_coordinate_sets:
            self._write_to_num_grid(coordinate_set, edge_color_dict)
                 
 
    def _write_to_num_grid(self, coordinate_set: set, color_dict: dict):
                
        color_set = set([self.color_grid[coordinate] for coordinate in coordinate_set])
        
        for key, value in color_dict.items():
            if set(value) != color_set:
                continue
            for coordinate in coordinate_set:
                i = value.index(self.color_grid[coordinate])
                self.num_grid[coordinate] = key[i]
            return
    
    
    def _build_num_grid(self):

        self.num_grid[1,4] = 5
        self.num_grid[4,1] = 14
        self.num_grid[4,4] = 23
        self.num_grid[4,7] = 32
        self.num_grid[4,10] = 41
        self.num_grid[7,4] = 50

        self._corners()
        self._edges()
"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""


# top solution 
# loop over the matrix and count the number of islands;
# if the current dot is an island, count if it has any right neighbour or down neighbour;
# the result is islands * 4 - neighbours * 2
"""
every adjacent islands made two sides disappeared
+--+     +--+                   +--+--+
|  |  +  |  |          ->       |     |
+--+     +--+                   +--+--+
4 + 4 - ? = 6  -> ? = 2
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands, neighbours = 0, 0
        
        for i in range(len(grid)):  # i: row
            for j in range(len(grid[i])):  # j: column
                if grid[i][j] == 1:
                    islands += 1
                    if i < len(grid) - 1 and grid[i+1][j] == 1: # count down neighbours 
                        neighbours += 1
                    if j < len(grid[i]) - 1 and grid[i][j+1] == 1: # count right neighbors 
                        neighbours += 1
        return islands * 4 - neighbours * 2   


# improvement 
# add 4 for each land and remove 2 for each internal edge
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        
        for i in range(len(grid)):  # i: row
            for j in range(len(grid[i])):  # j: column
                if grid[i][j] == 1:
                    result += 4
                    if i < len(grid) - 1 and grid[i+1][j] == 1: # count down neighbours 
                        result -= 2
                    if j < len(grid[i]) - 1 and grid[i][j+1] == 1: # count right neighbors 
                        result -= 2
        return result           
                        

# top solution                         
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):  # row i 
            for j in range(len(grid[i])):   # column j 
                if grid[i][j] == 0:
                    continue       
                # island: grid[i][j] == 1 
                # upper bar: row 0 or no island above  
                if i == 0 or grid[i-1][j] == 0: result += 1 
                # bottom bar: last row or no island below
                if i == len(grid) - 1 or grid[i+1][j] == 0: result += 1
                # left bar: most left column or no island left 
                if j == 0 or grid[i][j-1] == 0: result += 1
                # right bar: most right column or no island right 
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                 result += 1 
        return result          
        
# pythonic         
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def water_around(y, x):
            return (
            (x == 0 or grid[y][x-1]==0) +  # left column or no island left 
            (x == len(grid[0]) - 1 or grid[y][x+1]==0) +  # right column or no island right 
            (y == 0 or grid[y-1][x]==0) + # row 0 or no island above 
            (y == len(grid) - 1 or grid[y+1][x]==0) # last row or no island below
            )
        return sum(water_around(y, x) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x])
        
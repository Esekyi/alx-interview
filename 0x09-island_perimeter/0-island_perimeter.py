#!/usr/bin/python3
"""Module to calculate the Perimeter of an Island"""


def island_perimeter(grid):
    """
    Module to calculate the Perimeter of an Island
    Args:
        grid (list of list of int): A 2D grid representation where:
            0 represents water
            1 represents land
    Returns:
        int: the perimeter of the island
    """

    perimeter = 0
    cols = len(grid[0])
    rows = len(grid)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1
    return perimeter

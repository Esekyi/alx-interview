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

    for row in range(len(grid)):
        for col in cols:
            if grid[row][col] == 1:
                perimeter += 4
            if row > 0 and grid[row - 1][col] == 1:
                perimeter -= 1
            if row < range(len(grid)) - 1 and grid[row + 1][col] == 1:
                perimeter -= 1
            if col > 0 and grid[row][col - 1] == 1:
                perimeter -= 1
            if col < cols - 1 and grid[row][col + 1] == 1:
                perimeter -= 1
    return perimeter

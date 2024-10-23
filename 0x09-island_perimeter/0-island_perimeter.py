#!/usr/bin/python3
"""
This module defines the island_perimeter function
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.
    Args:
        grid (List[List[int]]): A list of lists representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

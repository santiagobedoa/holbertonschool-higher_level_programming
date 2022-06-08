#!/usr/bin/python3
''' Module for pascal_triangle func '''


def pascal_triangle(n):
    ''' Returns list that represents a pascal triangle of n size '''

    triangle = list()
    for row in range(0, n):
        if row == 0:
            triangle.append([1])
        elif row == 1:
            triangle.append([1, 1])
        else:
            tmp = []
            for i in range(0, row + 1):
                try:
                    if (i - 1) < 0:
                        raise ValueError("Index out of range")
                    tmp.append(triangle[row - 1][i - 1] + triangle[row - 1][i])
                except Exception:
                    tmp.append(1)
            triangle.append(tmp)

    return triangle

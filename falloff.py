import numpy as np
from math import sqrt


def circularMask(x, y, width, height):

    distance_x = abs(x - width * 0.5)
    distance_y = abs(y - height * 0.5)
    distance = sqrt(distance_x * distance_x + distance_y * distance_y)

    edgeMargin = max(width, height) * 0.05
    maxDistance = max(width, height) * 0.5 - edgeMargin

    scale = distance / maxDistance

    # Other interpolation function can be added here
    alpha = 3.0
    gradient = scale ** alpha

    return max(0.0, 1.0 - gradient)


def squareMask(x, y, width, height):

    distance_x = abs(x - width * 0.5)
    distance_y = abs(y - height * 0.5)
    distance = distance_x + distance_y

    edgeMargin = max(width, height) * 0.5
    maxDistance = (width + height) * 0.5 - edgeMargin

    scale = distance / maxDistance

    alpha = 1.0
    gradient = scale ** alpha

    return max(0.0, 1.0 - gradient)


def genericFalloff(width, height, falloffFunction):
    falloff = np.zeros((width, height))

    for y in range(height):
        for x in range(width):
            falloff[y, x] = falloffFunction(x, y, width, height)

    return falloff


def circularFalloff(width, height):
    return genericFalloff(width, height, circularMask)


def squareFalloff(width, height):
    return genericFalloff(width, height, squareMask)

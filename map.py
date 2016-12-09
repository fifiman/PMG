import numpy as np
import noise
import random


def generateNoiseMap(width, height, octaves, scale,
                     seed=None, persistance=0.5, lacunarity=2.0,
                     low=0.0, high=1.0):
    """
    Generates a 2D simplex noise map.

    Keyword arguments:

    width -- width of generated map, in pixels.
    height -- height of generated map, in pixels.
    octaves -- number of octaves used. More octaves = more fine details.
    scale -- scale at which the noise is sampled.
    seed -- random number generator seed for reproducability.
    persistance -- factor for scaling successive amplitudes.
    lacunarity -- factor for scaling successive frequencies.
    low, high -- map all noise values to range [low, high].
    """

    if seed is not None:
        random.seed(seed)  # For reproducability

    # Sample noise from different areas
    randomOffsets = []
    for _ in range(octaves):
        randomOffsets.append(random.random() * min(width, height))

    noiseMap = np.zeros((width, height))

    for y in range(height):
        for x in range(width):

            maxAmp = 0.0
            amp = 1.0
            freq = float(scale)
            currentNoiseValue = 0.0
            noiseValue = 0.0

            for i in range(octaves):
                currentNoiseValue = noise.snoise2(x * freq + randomOffsets[i],
                                                  y * freq + randomOffsets[i])
                currentNoiseValue *= amp
                noiseValue += currentNoiseValue

                maxAmp += amp
                amp *= persistance
                freq *= lacunarity

            noiseValue /= maxAmp

            noiseMap[y, x] = noiseValue

    noiseMap = noiseMap * (high - low) / 2.0 + (high + low) / 2.0

    return noiseMap

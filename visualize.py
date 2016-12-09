import numpy as np
import Image


def write_grayscale(arr, directory):

    maxi = np.max(arr)
    mini = np.min(arr)

    temp = ((arr - mini) / (maxi - mini) * 255.9).astype(np.uint8)

    img = Image.fromarray(temp)
    img.save(directory)


def write_color(arr, directory):


    DARK_BLUE = (0, 0, 139)
    LIGHT_BLUE = (0, 0, 255)
    SAND = (255, 184, 77)
    SNOW = (255, 255, 255)
    LIGHT_BROWN = (153, 102, 51)
    DARK_BROWN = (102, 51, 0)
    LIGHT_GREEN = (51, 204, 51)
    DARK_GREEN = (0, 153, 0)

    regions = [(DARK_BLUE, 0.3), (LIGHT_BLUE, 0.35),
               (SAND, 0.40), (LIGHT_GREEN, 0.55),
               (DARK_GREEN, 0.6), (DARK_BROWN, 0.75),
               (SNOW, 1.00)]

    regions.sort(key = lambda x : x[1])

    img = Image.new("RGB", arr.shape)
    pixels = img.load()

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):

            for regionColor, regionHeight in regions:

                if arr[i,j] <= regionHeight:
                    pixels[i,j] = regionColor
                    break

    img.save(directory)

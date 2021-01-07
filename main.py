from __future__ import print_function
import ccvwrapper
import numpy as np
from skimage import draw
from skimage.io import imread, imshow, imsave
#from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


def rectangle_perimeter(r0, c0, width, height, shape=None, clip=False):
    rr, cc = [r0, r0 + width, r0 + width, r0], [c0, c0, c0 + height, c0 + height]

    return draw.polygon_perimeter(rr, cc, shape=shape, clip=clip)


if __name__ == "__main__":
    image_name = "instrumentB.jpg"
    bytes = open(image_name, "rb").read()
    swt_result_raw = ccvwrapper.swt(bytes, 1024, 1360) #NEW
    swt_result_array = np.asarray(swt_result_raw).astype(int)

    swt_result = np.reshape(swt_result_array, (len(swt_result_array) / 4, 4))

    image = imread(image_name, as_gray=False)
    for x, y, width, height in swt_result:
        for i in range(0, 3): # just to make lines thicker
            rr, cc = rectangle_perimeter(y + i, x + i, height, width, shape=image.shape, clip=True)
            image[rr, cc] = (255, 0, 0)

    #imshow(image)
    imsave("result.jpg", image)
    plt.show()
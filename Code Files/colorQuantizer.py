# Gurkan Demir
# 2015400177
# ggurkandemir@gmail.com
# CmpE537 - Assignment 1

import sys
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

##
# Method in order to execute K-Means algorithm.
# Converts input image into a matrix of pixels.
# Picks K initial colors to begin quantization.
# Assignes each pixel to closest cluster.
# Finds clusters' new R, G, B values.
##
def k_means_algo(img, K, points, width, height):
    
    # Converts input image into a matrix of pixels.
    pixels = np.array(img.getdata())

    # Picks K initial colors.
    cluster_values = np.zeros(shape = (K, 3))

    for i in range(0, K):
        cluster_values[i] = img.getpixel((int(points[i][0]), int(points[i][1])))

    for counter in range(0, 10):
        temp = []
        # Finds pixels distances to each cluster.
        for i in range(0, K):
            temp.append(np.sum(np.power(pixels-cluster_values[i], 2), axis = 1))
        
        distances = np.stack(temp, axis = 1)
        # Assignes each pixel to closest cluster.
        assigned_clusters = np.argmin(distances, axis=1)

        # Finds clusters' new R, G, B values.
        for i in range(0, K):
            cluster_values[i] = np.mean(pixels[assigned_clusters == i], axis = 0)

    return Image.fromarray(cluster_values[assigned_clusters].reshape(height,width, -1).astype('uint8'), 'RGB')

##
# Method in order to decide cluster's initial points.
# Then calls K-Means Algorithm.
##
def quantize(img, K):
    cond = int(sys.argv[3])
    width, height = img.size

    # If clusters' inital coordinate chosen by clicking on image.
    if(cond is 1):
        plt.imshow(img)
        points = plt.ginput(K,show_clicks=True)
        
    # If clusters' initial coordinate chosen by randomly.
    else:
        points = []
        for i in range(0, K):
            points.append([])
            x = int(np.random.uniform(0, width))
            y = int(np.random.uniform(0, height))
            points[i].append(x)
            points[i].append(y)

    return k_means_algo(img, K, points, width, height)

##
# Main function, reads image and K value from arguments.
# Calls necessary function to execute K-Means Algorithm.
# Then according to result it saves output image.
##
if __name__ == '__main__':
    im = Image.open(sys.argv[1])
    K = int(sys.argv[2])
    
    img = quantize(im, K)
    img.save("output.png")

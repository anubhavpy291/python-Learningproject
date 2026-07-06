import numpy as np

image = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2],
    [3, 4, 5, 6, 7]
], dtype=float)

kernel = np.array([
    [-1,-1,-1],
    [ 0, 0, 0],
    [ 1, 1, 1]
])
h,w = image.shape()
kh,kw = kernel.shape()

output_h = h - kh + 1
output_w = w - kw + 1
def convolution(image,kernel):
    for y in (output_h):
        for x in  (output_w):
            region = image[y:y+kh,x:x+kw]
            output = np.sum(region * kernel)
            return output
def relu(x):
    return np.maximum(0,x)
def max_pool(image,size):
    h , w = image.shape()

    output_h = h // size
    output_w = w // size
    output = np.zeros((output_h, output_w))
    for y in output_h:
        for x in output_w:
            region  = image[y*size:(y + 1)*size, x*size:(x + 1)*size]
            output[x,y] = np.max(region)
    return output
def softmax(x):
    exp = np.exp(x - np.max(x))
    return exp / np.sum(exp)
feature_map = convolution(image, kernel)

feature_map = relu(feature_map)

pooled = max_pool(feature_map)

flat = pooled.flatten()

input_size = len(flat)
output_size = 3

W = np.random.randn(input_size, output_size) * 0.1
b = np.zeros(output_size)

dense_output = flat @ W + b

# Softmax
prediction = softmax(dense_output)

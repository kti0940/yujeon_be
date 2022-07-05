import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import random

net_list = [
    "starry_night.t7",
    "la_muse.t7",
    "the_wave.t7",
    "composition_vii.t7",
    "feathers.t7",
    "mosaic.t7",
    "the_scream.t7",
    "composition_vii.t7"
]
n = len(net_list)
rand_num = random.randint(0,n-1)
net = cv2.dnn.readNetFromTorch(f'models/{net_list[rand_num]}')
img = cv2.imread(f'../media/uploads/input.jpg')

h, w, c = img.shape
img = cv2.resize(img, dsize=(500, int(h / w * 500)))

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))
output += MEAN_VALUE

output = np.clip(output, 0, 255)
output = output.astype('uint8')

cv2.imwrite('../media/uploads/result.jpeg', output)

# cv2.waitKey(0)



import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import random
# def get_input_image(request):
#     INPUT_IMAGE = request.session['input_image']    
#     print(f"INPUT_IMAGE->{INPUT_IMAGE}")
#     return INPUT_IMAGE


net_list = [
    "starry_night.t7",
    "la_muse.t7",
    "the_wave.t7",
    "composition_vii.t7",
    "feathers.t7",
    "mosaic.t7",
    "the_scream.t7",
    "udine.t7",
    "composition_vii.t7"
]
n = len(net_list)
rand_num = random.randint(0,n-1)
print(net_list[rand_num])
net = cv2.dnn.readNetFromTorch(f'models/{net_list[rand_num]}')
print(f"랜덤 모델 -> {net}")


# img = cv2.imread('imgs/01.jpg')

img = cv2.imread(f'../media/uploads/input.jpg')

h, w, c = img.shape
img = cv2.resize(img, dsize=(500, int(h / w * 500)))
print(img.shape) # (325, 500, 3)

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

print(blob.shape) # (1, 3, 325, 500)
net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))
output += MEAN_VALUE

output = np.clip(output, 0, 255)
output = output.astype('uint8')

cv2.imwrite('../media/uploads/result.jpeg', output)

# cv2.imshow('img', img)
# cv2.imshow('result', output)
cv2.waitKey(0)



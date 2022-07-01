import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def get_input_image(request):
    INPUT_IMAGE = request.session['input_image']    
    print(f"INPUT_IMAGE->{INPUT_IMAGE}")
    return INPUT_IMAGE

# net = cv2.dnn.readNetFromTorch('models/eccv16/starry_night.t7')
net = cv2.dnn.readNetFromTorch('models/eccv16/la_muse.t7')
# net = cv2.dnn.readNetFromTorch('models/eccv16/the_wave.t7')
# net = cv2.dnn.readNetFromTorch('models/eccv16/composition_vii.t7')
# net = cv2.dnn.readNetFromTorch('models/feathers.t7')
# img = cv2.imread('imgs/01.jpg')

INPUT_IMAGE=get_input_image()
img = cv2.imread(f'../media/uploads/{INPUT_IMAGE}')

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



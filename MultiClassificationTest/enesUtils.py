#TODO find a better numpy array to image function, discoloration is crazy

import cv2
import numpy as np
import scipy.misc
#import logger

def split_image(img, x, y):
    #logging.basicConfig(level=logging.DEBUG)
    #logger.debug("swag-1")
    h = img.shape[0]
    w = img.shape[1]
    width_cutoff = w // x
    imgs = []
    for i in range(x):
        imgs.append(img[:,width_cutoff*i:width_cutoff*(i+1)])
    
    imgs1 = []
    for im in imgs:
        imgg = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)

        h = imgg.shape[0]
        w = imgg.shape[1]
        width_cutoff = w // y

        for j in range(y):
            imgs1.append(imgg[:,width_cutoff*j:width_cutoff*(j+1)])

    split_images = []
    for im1 in imgs1:
        split_images.append(cv2.rotate(im1, cv2.ROTATE_90_COUNTERCLOCKWISE))
        
    labels = []
    
    for i in range(x):
        for j in range(y):
            labels.append(x*(y-j-1) + i + 1)

    return split_images, labels
    
def npa_to_img(npa):
    imgs = []
    for i in npa:
        imgs.append(scipy.misc.toimage(i))
        
    return imgs
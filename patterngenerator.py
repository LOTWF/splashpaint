from PIL import Image
import numpy as np
import cv2
import random
from scipy import ndimage
def splash(data,prop,col,spread):
    sat=125
    for i in range(spread):
        x=(prop[0]+random.randint(-1,1))%w
        y=(prop[1]+random.randint(-1,1))%h
        prop=(x,y)
        data[prop][col]=sat
        sat=(sat+random.randint(-20,20))%255
if __name__ == '__main__':
    w, h = 512, 512
    data = np.zeros((h, w, 3), dtype=np.uint8)
    #data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
    prop=(20,20)
    s=1000000
    splash(data,prop,0,s)
    splash(data,prop,1,s)
    splash(data,prop,2,s)
    img = Image.fromarray(data, 'RGB')
    #img.save('my.png')
    img.show()

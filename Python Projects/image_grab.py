import PIL
from PIL import ImageGrab
from PIL import Image
import os
import time
import random


time.sleep(1)
while True:
    try:
        print('start')
        img = ImageGrab.grab()

        if img:
            # change the path as per your machine in line 17 and 21
            if os.path.exists(r"C:\\Users\\91817\\PycharmProjects\\opencv\\images"):
                x = random.randint(1,10000)
                y = random.randint(2,100001)
                s = str(x) + str(y) + '.' + 'jpg'
                pat = r"C:\\Users\\91817\\PycharmProjects\\opencv\\images"
                r = os.path.join(pat,s)
                print(r)

                img.save(r)
            else:
                print('FILE NOT FOUND!')
    except:
        pass

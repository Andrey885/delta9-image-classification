from PIL import ImageDraw, Image
import os
import pandas as pd
import numpy as np
import time

os.chdir('C:/')
os.chdir(r'images2_4256')
image = Image.open(r'C:/Users/004256.jpg')
im1=image
#print(image)
draw = ImageDraw.Draw(image)

df = pd.read_csv(r'C:/Users/Home/tensorflow-for-poets-2/filename407.csv')

x1=y1=0
images = df.image
gun = np.array(df.gun)

#print (len(images))
for n in range(len(images)):
    if abs(gun[n]-0.9999972581863404)>0.0000025 :
        print(n)
        y1= (n//20)*20
        x1=(n-((n//20)*20))*20
        print(x1,y1)
        for i in range(20):
            for j in range(10):
                xy=[x1+i,y1+2*j]
                
                draw.point(xy, fill='red')
        
    if abs(gun[n]-0.9999972581863404)>0.000002 and abs(gun[n]-0.9999972581863404)<0.0000025 :
        print(n)
        y1= (n//20)*20
        x1=(n-((n//20)*20))*20
        print(x1,y1, 'add')
        for i in range(10):
            for j in range(10):
                xy=[x1+2*i,y1+2*j]
                
                draw.point(xy, fill='red')
           
        #image.save(st, "JPEG")
#del draw
st=str(time.time())+'.jpg'
image.show()
image.save(st, "JPEG")


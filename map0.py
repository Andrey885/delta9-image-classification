from PIL import ImageDraw, Image
import os

os.chdir('C:/')

os.chdir(r'images4256')
image = Image.open(r'C:/Users/004256.jpg')
print(image)

#draw.line((0, 0) + image.size, fill=128)
#draw.line((0, image.size[1], image.size[0], 0), fill=128)
x1=x2=0
y1=y2=0
x=x1
y=y1
xy=[x1,y1]
file= r'C:/images4256'
for m in range(17):
    y1=20*m
    x1=0
    for n in range(24):
        image = Image.open(r'C:/Users/004256.jpg')
        draw = ImageDraw.Draw(image)
        for i in range(20):
            y=i
            for j in range(20):
                x=j
                xy=[x1+x,y1+y]
                draw.point(xy, fill='white')
        
    #filename=file+str(n)
        st=str(m)+'x'+str(n)+'.jpg'
        image.save(st, "JPEG")
        x1+=20
    #y1+=20
        x=y=0
        del draw
#image.save(st, "JPEG")
#image.show()

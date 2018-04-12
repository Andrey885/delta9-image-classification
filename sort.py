import shutil
import pandas as pd
import numpy as np
train = pd.read_csv(r'C:\Users\Home\Desktop\Python\train.csv')
filename=r'C:\Users\Home\Desktop\Python\train\ '
outAdress = r'C:\Users\Home\tensorflow-for-poets-2\tf_files\glasses'
mas = np.array(train[train.glasses == 1].image)
print(mas.size)
for i in range(mas.size):
    shutil.copy(r'C:\\Users\\Home\\Desktop\\Python\\train\\' +mas[i], outAdress)



import pandas as pd
import numpy as np
import scipy.io
import random, math
from sklearn.decomposition import PCA
from sklearn import manifold
from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os
import glob


path = 'Datasets\ALOI\Pics'
path2 = 'Datasets\ALOI\Pics2'

sample = []
num_files = len([f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))])
for i in range(1,num_files-1,1):
    file_name = 'Datasets/ALOI/Pics/'
    file_name += '32_r'+ str(i*5) + '.png'
    img = misc.imread(file_name)
    X = (img/255.0).reshape(-1)
    sample.append(X)
num_files = len([f for f in os.listdir(path2)
                 if os.path.isfile(os.path.join(path2, f))])

for i in range (1,num_files-1,1):
    file_name = "Datasets/ALOI/Pics2/"
    file_name += '32_i' + str(i * 10 +100) + '.png'
    img = misc.imread(file_name)
    X = (img / 255.0).reshape(-1)
    sample.append(X)
df = pd.DataFrame.from_records(sample)


iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
T = iso.transform(df)
print T[1]
import pandas as pd
import numpy as np
import scipy.io
import random, math
from sklearn.decomposition import PCA
from sklearn import manifold
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def Plot2d(T, title, x, y, num_to_plot=40):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))

  x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
  y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
  for i in range(num_to_plot):
    img_num = int(random.random() * num_images)
    x0, y0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.
    x1, y1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.
    img = df.iloc[img_num,:].reshape(num_pixels, num_pixels)
    ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))
  ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7)
mat = scipy.io.loadmat('Datasets/face_data.mat')
df = pd.DataFrame(mat['images']).T
print df
num_images, num_pixels = df.shape
num_pixels = int(math.sqrt(num_pixels))

for i in range(num_images):
  df.loc[i,:] = df.loc[i,:].reshape(num_pixels, num_pixels).T.reshape(-1)


pca = PCA(n_components=3)
pca.fit(df)
PCA(copy=True, n_components=3, whiten=False)
T = pca.transform(df)
Plot2d(T, "test", 0,1)

iso = manifold.Isomap(n_neighbors=3, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2d(T,'iso test',0,1)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime
from mpl_toolkits.mplot3d import Axes3D
from plyfile import PlyData, PlyElement
from sklearn.decomposition import PCA, RandomizedPCA

reduce_factor = 100

plt.style.use("ggplot")

plyfile = PlyData.read("Datasets/stanford_armadillo.ply")
armadillo = pd.DataFrame({
    'x':plyfile['vertex']['z'][::reduce_factor],
    'y': plyfile['vertex']['x'][::reduce_factor],
    'z': plyfile['vertex']['y'][::reduce_factor]
})

def do_PCA(armadillo):
    pca = PCA(n_components=2)
    pca.fit(armadillo)
    PCA(copy=True, n_components=2, whiten=False)
    T = pca.transform(armadillo)



    return T

def do_RandomizedPCA(armadillo):
    pca = RandomizedPCA(n_components=2)
    pca.fit(armadillo)
    RandomizedPCA(copy=True, n_components=2, whiten=False)
    T = pca.transform(armadillo)
    return T

fig = plt.figure()
ax= fig.add_subplot(111, projection='3d')
ax.set_title('Armadillo 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(armadillo.x,armadillo.y,armadillo.z,c='green', marker='.',alpha=0.5)

t1=datetime.datetime.now()
for i in range(5000): pca = do_PCA(armadillo)
time_delta = datetime.datetime.now() - t1

if not pca is None:
    fig = plt.figure()
    ax= fig.add_subplot(111)
    ax.set_title('PCA, build time: ' + str(time_delta))
    ax.scatter(pca[:,0], pca[:,1], c='blue',marker='.',alpha=0.75)

t1=datetime.datetime.now()
for i in range(5000): rpca = do_RandomizedPCA(armadillo)
time_delta = datetime.datetime.now() - t1

if not rpca is None:
    fig = plt.figure()
    ax= fig.add_subplot(111)
    ax.set_title('RandomizedPCA, build time: ' + str(time_delta))
    ax.scatter(pca[:,0], pca[:,1], c='blue',marker='.',alpha=0.75)

plt.show()
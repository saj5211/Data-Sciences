import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('ggplot')
df = pd.read_csv('Datasets/wheat.data')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')
ax.scatter(df.area, df.perimeter, df.asymmetry, c='red')

bx = fig.add_subplot(111, projection='3d')
bx.set_xlabel('width')
bx.set_ylabel('groove')
bx.set_zlabel('length')
bx.scatter(df.width, df.groove, df.length, c='green')
plt.show()
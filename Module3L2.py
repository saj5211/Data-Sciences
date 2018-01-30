import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')
df = pd.read_csv('Datasets/wheat.data')

df.plot.scatter(x='area',y='perimeter')
df.plot.scatter(x='groove',y='asymmetry')
df.plot.scatter(x='compactness',y='width')

plt.show()


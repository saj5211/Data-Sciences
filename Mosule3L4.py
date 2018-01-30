import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

plt.style.use('ggplot')

df = pd.read_csv('Datasets/wheat.data')
df = df.drop(labels=['id', 'area', 'perimeter'], axis=1)
plt.figure()
parallel_coordinates(df, 'wheat_type')
plt.show()
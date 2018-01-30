import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves
plt.style.use('ggplot')

df = pd.read_csv('Datasets/wheat.data')
#df = df.drop(labels=['id', 'area', 'perimeter'], axis=1)
plt.figure()
andrews_curves(df, 'wheat_type')
plt.show()
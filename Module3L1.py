import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')
df = pd.read_csv('Datasets/wheat.data')

# plot 1
dataframe_1 = df[['area','perimeter']]
dataframe_1.plot.hist(alpha=0.75)
dataframe_2 = df[['groove','asymmetry']]
dataframe_2.plot.hist(alpha=0.75)

plt.show()
print df

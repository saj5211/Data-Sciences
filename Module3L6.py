import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')
df=pd.read_csv('Datasets/wheat.data')
df=df.drop(labels=['id'], axis=1)
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.yticks(tick_marks, df.columns, rotation='vertical')
plt.xticks(tick_marks, df.columns)
plt.show()
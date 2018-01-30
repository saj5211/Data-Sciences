import pandas as pd

df = pd.read_csv('Datasets/tutorial.csv')
print df

df = df.loc[2:4, 'col3']
print df
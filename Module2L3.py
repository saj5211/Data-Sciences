import pandas as pd

df = pd.read_csv('Datasets/servo.data', names = ['motor', 'screw', 'pgain', 'vgain', 'class'])

df = df[df['pgain'] == 4]
df = df['vgain'].mean()
print df

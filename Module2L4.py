import pandas as pd

df = pd.concat(pd.read_html("http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2"))

df = df.drop(0, axis=0).drop(0,axis=1).dropna(axis=0,thresh=4)
for i in range(3,17,1):
    df[i] = pd.to_numeric(df[i], errors="coerce")


df = df.dropna(axis=0)
df.columns = ['PLAYER', 'TEAM','GP', 'G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','G','A','G','A']

print df
print df.dtypes
print df.PCT.value_counts()
print df.GP[16] + df.GP[17]
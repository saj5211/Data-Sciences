import pandas as pd

df = pd.read_csv("Datasets/pharmterms4.csv")
df = df.loc[df['tld'] == '.ORG']
total = 0.0
totalTrue = 0.0

for i in df['redirects']:
    if i == True:
        totalTrue += 1
        total+=1
    else:
        total +=1

# print total
# print totalTrue
# average = totalTrue/total*100
# print average

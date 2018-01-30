import pandas as pd
from joblib import Parallel, delayed
import multiprocessing
from urlparse import urlparse
j = ""
sites = []
df = pd.read_csv('Datasets/top-1m.csv', names=['index', 'site'])
df2 = pd.read_csv('Datasets/pharmterms4.csv')
# df2 = df2.loc[df2['redirects'] == True]
results2 = []
count = 0
total = 0
def filtering(i):
    i = urlparse(i)
    i = i.netloc.replace("www.", "")
    return i

def processInput(i):
    i = filtering(i)
    if i in sites:
        None
    else:
        sites.append(i)


    return sites

def processInput2(i, sites, count):
    if i in sites:
        count += 1
        print"                          found one"
    else:
        print " continuing" + "                              " + i + "                    " + str(count)
    return count
if __name__ == '__main__':
    num_cores = multiprocessing.cpu_count()
    results = Parallel(n_jobs=num_cores)(delayed(processInput)(i)
                                             for i in df2['URL'])
    last_position = len(results)-1
    sites = results[last_position]

    print " list composed"
    count = count
    results2 = Parallel(n_jobs=num_cores)(delayed(processInput2)(i, sites,count, )
                                                          for i in df['site'])

    results2 = results2
    print" finsihed processing"
print" onto counting"
total = len(results2)
print results2
for i in results2:
    count += results2[i]

count  = total - count
print count
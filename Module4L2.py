import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import Module4L2_helper as helper
from sklearn.decomposition import PCA
import numpy as np
matplotlib.style.use("ggplot")

scaleFeatures=False

df = pd.read_csv("Datasets/kidney_disease.csv")
df = df.dropna()


labels = ["red" if i=="ckd" else "green" for i in df.classification]


df = df.loc[:, "bgr":"rc"]
df = df.drop(labels=["bu","sc","sod","pot","hemo","pcv"], axis=1)

df.wc = pd.to_numeric(df.wc, errors="coerce")
df.rc = pd.to_numeric(df.rc, errors="coerce")
print labels
#if scaleFeatures: df = helper.scaleFeatures(df)
df.replace("", np.nan, inplace = True);
pca = PCA(n_components=2)
pca.fit(df)
PCA(copy=True, n_components=2, whiten=False)
T=pca.transform(df)

ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ["component1", "component2"]
T.plot.scatter(x="component1", y="component2", marker="o", c=labels, alpha=0.75, ax=ax)
plt.show()
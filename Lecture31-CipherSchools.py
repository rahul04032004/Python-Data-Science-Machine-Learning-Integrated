# k means aims to partation into k clusters
# k means is an unsupervised learning algorithm
# k means is a clustering algorithm
# k means is a centroid based algorithm

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#generating data
x, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60,random_state=0)

#Training
model = KMeans(n_clusters=4)
y_pred= model.fit_predict(x)

#plotting result

plt.scatter(x[:,0], x[:,1],c=y_pred,cmap='rainbow')
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], s=300, c='black',marker='X')
plt.show()




# heirarrchy in form of  trees called dendogram(node)
#two approaches-> 
# 1) Agglomerative - bottom up
# 2) Divisive - top down

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

#generating data
x, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60,random_state=0)

#train

model=AgglomerativeClustering(n_clusters=4)
y_pred=model.fit_predict(x)

#plotting result
plt.scatter(x[:,0], x[:,1],c=y_pred,cmap='rainbow')
plt.title("Hierarchical Clustering")
plt.show()



# Principal component analysis is a versatile statistical method for reducing a cases-by-variables data table to its essential features, called principal components. basicall dimensionally reduction algorithm to new coordinate system.

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris= load_iris()
X= iris.data 
y= iris.target

#Analysing PCA
pca= PCA(n_components=2)
X_pca= pca.fit_transform(X)

#ploting
plt.scatter(X_pca[:,0], X_pca[:,1], c=y, cmap='rainbow')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA on Iris dataset')
plt.show()

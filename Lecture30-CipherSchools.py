############ Linear Regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Generating synthetic data
import numpy as np
x=np.random.rand(100,1)*10
y=2.5*x+np.random.randn(100,1)*2


#spliting data into training and testing sets...
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)  


#Training the model
model=LinearRegression()
model.fit(x_train,y_train)
#Predicting the test set results
y_pred=model.predict(x_test)
#Calculating the mean squared error (EVALUATION)
mse=mean_squared_error(y_test,y_pred)
print("mse->",mse)

#print(y_test)




##############Logistic Regression
#Logistic Regression is a classification algorithm that is used to assign observations to a discrete set of classes

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#loading iris data
iris = load_iris()
x=iris.data
y=iris.target

#using  2 classes only  for binary classification
x=x[y!=2]
y=y[y!=2]

#splitting of data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)  

#training of model
model=LogisticRegression()
model.fit(x_train,y_train)

#predictions
y_pred =model.predict(x_test)
#evaluation
print("accuracy")
print(accuracy_score(y_test,y_pred))
print(y_test)
print(y_pred)




#############Decision Tree
#classification based
#identify mimp features
#identify the best classifier
# it is non parametric supervised learning method used for cassiification and regression
    #it is used for both classification and regression


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#data
iris=load_iris()
x=iris.data
y=iris.target


#split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#model
model=DecisionTreeClassifier()
model.fit(x_train,y_train)

#prediction
y_pred=model.predict(x_test)

#evaluation
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)




############### SVM's
# CLASSIFY DATA POINTS WE CREATE A DECISION MARGIN A LINE
# SVM'S ARE A CLASS OF LINEAR CLASSIFIERS
# bw support margins we draw deceison margin more the gap it is easier
# 3 PLANES  MAX MARGIN HYPERPLANE
# MAXIMUM MARGIN
# POSITIVE HYPER PLANE


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#loading data
iris=load_iris()
x=iris.data
y=iris.target


#split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#model
model=SVC()
model.fit(x_train,y_train)
#prediction
y_pred=model.predict(x_test)
#accuracy
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy",accuracy)

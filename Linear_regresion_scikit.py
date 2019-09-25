import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score


from sklearn.datasets import load_boston


boston=load_boston()


df_x=pd.DataFrame(boston.data,columns=boston.feature_names)
df_y=pd.DataFrame(boston.target)
df_x.describe()

reg = linear_model.LinearRegression()
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size=0.2,random_state=4)
reg.fit(x_train,y_train)
reg.coef_
y_test.shape
a= reg.predict(x_test)
a.shape
y_test

np.mean((a-y_test)**2)

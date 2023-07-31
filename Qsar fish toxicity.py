#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score


# In[57]:


data = pd.read_csv('qsar_fish_toxicity.csv', sep=';', header=None, names=['CICo', 'SM1', 'GATS1i', 'NdsCH', 'NdssC', 'MLOGP', 'LC50'])


# In[58]:


data.head()


# In[59]:


type(data)


# In[60]:


data.info()


# In[61]:


data.hist("LC50")


# In[62]:


sns.heatmap(data.corr(),annot=True)


# In[63]:


data.plot(kind="scatter", x = "MLOGP" , y = "LC50")


# In[64]:


data.plot(kind="scatter", x = "GATS1i" , y = "LC50")


# In[65]:


data.plot(kind="scatter", x = "SM1" , y = "LC50")


# In[ ]:





# In[ ]:





# In[66]:


from sklearn.preprocessing import PolynomialFeatures


# In[ ]:





# In[67]:


X = data.drop('LC50', axis=1).values
Y = data['LC50'].values


# In[68]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# In[69]:


model = make_pipeline(StandardScaler(), SVR())


# In[70]:


model.fit(X_train, Y_train)


# In[71]:


param_grid = {
    'svr__C': [0.1, 1, 10],  # Regularization parameter
    'svr__kernel': ['linear', 'rbf', 'poly'],  # Kernel type
    'svr__degree': [2, 3],  # Degree for polynomial kernel (if used)
    'svr__gamma': ['scale', 'auto'],  # Kernel coefficient (if applicable)
}


# In[72]:


grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, Y_train)


# In[73]:


best_model = grid_search.best_estimator_
best_params = grid_search.best_params_


# In[74]:


Y_pred = best_model.predict(X_test)


# In[75]:


mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)


# In[76]:


print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)


# In[77]:


print("Best Hyperparameters:", best_params)


# In[ ]:
import joblib
joblib.dump(best_model, 'best_svr_model.joblib')





"""""
-------------------------------------
@Author: Brandonlee Santos
@Date: 06_21_23
/// Contains data pipeline functions 
/// Oversample Ordinal Label Hot Outlier Pipeline 
-------------------------------------
"""""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from imblearn.over_sampling import SMOTE


def ValCnt(df,f):
    
    fval = df[f].value_counts()
    print(fval)
    
class OrdinalT(BaseEstimator,TransformerMixin):
    
    def __init__(self, cat):
        
        self.catfeat = cat

    def fit(self,X, y=None):
        
        return self

    def transform(self,X,y=None):
    
        X[self.catfeat] = OrdinalEncoder().fit_transform(X[self.catfeat])
        
        return X
    

class LabelT(BaseEstimator,TransformerMixin):
    
    def __init__(self, target):
        
        self.targ = target

    def fit(self,X, y=None):
        
        return self

    def transform(self,X,y=None):
    
        X[self.targ] = LabelEncoder().fit_transform(X[self.targ])
        
        return X
    

class HotT(BaseEstimator,TransformerMixin):
    
    def __init__(self, cat):
        
        self.catfeat = cat

    def fit(self,X, y=None):
        
        return self

    def transform(self,X,y=None):
        
        Xh = OneHotEncoder().fit_transform(X[self.catfeat])
        X = X.drop(self.catfeat,axis = 1)
        X = pd.concat([X,Xh],axis =1 )
        
        return X
    

class OutlierRemover(BaseEstimator, TransformerMixin):
    
    def __init__(self,numcol ):
        
        self.feat_with_outliers = numcol
    
    def fit(self,X):
        
        return self
    
    def transform(self,X):
        
        # remove outlier in numerical feat
        if (set(self.feat_with_outliers).issubset(X.columns)):
            # 25% quantile
            Q1 = X[self.feat_with_outliers].quantile(.25)
            # 75% quantile
            Q3 = X[self.feat_with_outliers].quantile(.75)
            IQR = Q3 - Q1
            # keep the data within 1.5 IQR
            X = X[~((X[self.feat_with_outliers] < (Q1 - 3 * IQR)) |(X[self.feat_with_outliers] > (Q3 + 3 * IQR))).any(axis=1)]
            
            return X
        
        else:
            
            print("One or more features are not in the dataframe")
            
            return X

class OversampleSMOTE(BaseEstimator,TransformerMixin):
    
    def __init__(self,target):
        self.targ = target
    
    def fit(self,df):
        return self
    
    def transform(self,X, y):
        
            # SMOTE function to oversample the minority class to fix the imbalance data
        smote = SMOTE()
        X, y = smote.fit_resample(X,y)
        return X, y
      

    


    

    



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
from sklearn.preprocessing import StandardScaler, LabelEncoder, OrdinalEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from imblearn.over_sampling import SMOTE

apprec = pd.read_csv('/Users/teacher/Desktop/tests/application_record.csv')
crec = pd.read_csv('/Users/teacher/Desktop/tests/credit_record.csv')
   
    
catf = [c for c in apprec.columns if apprec[c].dtype =='O']
numf = [c for c in apprec.drop('CNT_FAM_MEMBERS',axis=1).columns if (apprec[c].dtype =='float')]
timecol = 'MONTHS_BALANCE'

def ValCnt(df,f):
    
    fval = df[f].value_counts()
    print(fval)


#---------------------------------------------------------------------------------------------------

class Merge(BaseEstimator,TransformerMixin):
    
    def __init__(self):

        pass
    
    def fit(self,X1,X2= None):
        
        return self
    
    def fit_transform(self,X1,X2=None):
        
        #self.fit(X1)
        X = pd.concat([X1,X2],axis = 1)
        
        return X

#---------------------------------------------------------------------------------------------------
   
class OrdinalT(BaseEstimator,TransformerMixin):
    
    def __init__(self, cat=catf):
        
        self.catfeat = cat

    def fit(self,X, y=None):
        
        return self

    def transform(self,X,y=None):
        
        #self.fit(X)
        X[self.catfeat] = OrdinalEncoder().fit_transform(X[self.catfeat])
        
        return X
    

#---------------------------------------------------------------------------------------------------

class LabelT(BaseEstimator,TransformerMixin):
    
    def __init__(self):
       
        pass

    def fit(self,X, y=None):
        
        return self

    def fit_transform(self,X,y=None):
        
        self.fit(X)
        y = LabelEncoder().fit_transform(y)
        
        return y

 
#---------------------------------------------------------------------------------------------------
       
class HotT(BaseEstimator,TransformerMixin):
    
    def __init__(self, cat=catf):
        self.catfeat = cat
        pass

    def fit(self,X, y=None):
        
        return self

    def transform(self,X,y=None):
        #self.fit(X)
        Xh = OneHotEncoder().fit_transform(X[self.catfeat])
        X = X.drop(self.catfeat,axis = 1)
        X = pd.concat([X,Xh],axis =1 )
        
        return X
    
 
#---------------------------------------------------------------------------------------------------
   
class StandardT(BaseEstimator,TransformerMixin):
    
    def __init__(self,numcol=numf):
        
        self.numcol = numcol
        pass
    
    def fit(self,X, y =None):
        
        return self
    
    def transform(self,X):
        #self.fit(X)
        
        X.loc[:, self.numcol] = StandardScaler().fit_transform(X.loc[:,self.numcol])
        return X 
    

#---------------------------------------------------------------------------------------------------

class OutlierRemover(BaseEstimator, TransformerMixin):
    
    def __init__(self,numcol=numf ):
        
        self.feat_with_outliers = numcol
        pass
    
    def fit(self,X,y=None):
        
        return self
    
    def transform(self,X,y=None):
        #self.fit(X)
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

#---------------------------------------------------------------------------------------------------

class OverSampleSMOTE(BaseEstimator,TransformerMixin):
    
    def __init__(self):
        
        pass
    
    def fit(self,X,y=None):
        
        return self
    
    def transform(self,X, y=None):
        #self.fit(X)
        # SMOTE function to oversample the minority class to fix the imbalance data
        smote = SMOTE()
        X, y = smote.fit_resample(X,y)
        return X, y
  
#---------------------------------------------------------------------------------------------------
  
class TimeHandler(BaseEstimator,TransformerMixin):

    def __init__(self,timecol=timecol):
        
        self.timecol = timecol

    def fit(self,X,y=None):
        
        return self
    
    def transform(self,X,y=None):
        #self.fit(X)
        X[self.timecol] = X[self.timecol].abs()
        return X
 
#---------------------------------------------------------------------------------------------------
   
class DropID(BaseEstimator,TransformerMixin):
    
    def __init__(self):
        
        pass

    def fit(self,X, y=None):
        
        return self

    def fit_transform(self,X,y=None):
        
        self.fit(X)
        X = X.drop('ID',axis =1 )
        return X






    


    

    



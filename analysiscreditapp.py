"""""
-------------------------------------
@Author: Brandonlee Santos
@Date: 06_21_23
/// credit app analysis + data processing
/// custom  sklearn pipeline feat eng 
-------------------------------------
"""""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Pipefuncapp import TimeHandler, OrdinalT, LabelT, HotT, OutlierRemover, OverSampleSMOTE,Merge,DropID, StandardT
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.metrics import classification_report
from statsmodels.discrete.discrete_model import MNLogit
def PlotBar(df,catf):
    
    fig,axs = plt.subplots(len(catf))

    for cnt, c in enumerate(catf):
        
        sns.barplot( df[c].value_counts(),ax = axs[cnt])
        axs[cnt].set_xlabel(c)
        axs[cnt].set_ylabel('Counts')
        axs[cnt].set_title('Counts of ' + c)

#---------------------------------------------------------------------------------------------------

def PlotHist(df,numf):

    if len(numf)==1: 
        print(numf)
        bins = 50
        fig,axs = plt.subplots(len(numf))
   
        sns.histplot( df[numf[0]],kde = True,ax = axs,bins = 50)
        axs.set_xlabel(numf[0])
        axs.set_ylabel('Density')
        axs.set_title('Density of ' + numf[0])


    else:
    
        bins = 50
        fig,axs = plt.subplots(len(numf))

        for cnt, c in enumerate(numf):
            
            sns.histplot( df[c],kde = True,ax = axs[cnt],bins = 50)
            axs[cnt].set_xlabel(c)
            axs[cnt].set_ylabel('Density')
            axs[cnt].set_title('Density of ' + c)

#---------------------------------------------------------------------------------------------------

def PlotBox(df,numf):
    
    if len(numf)==1:
         
        fig,axs = plt.subplots(len(numf))  
        sns.boxplot( df[numf[0]],ax = axs)
        axs.set_ylabel(numf[0])
        axs.set_title('BoxPlot of ' + numf[0])

    else:
        
        fig,axs = plt.subplots(len(numf))

        for cnt, c in enumerate(numf):
            
            sns.boxplot( df[c],ax = axs[cnt])
            
            axs[cnt].set_ylabel(c)
            axs[cnt].set_title('BoxPlot of ' + c)

#---------------------------------------------------------------------------------------------------

def main():
    
    apprec = pd.read_csv('/Users/teacher/Desktop/tests/application_record.csv')
    crec = pd.read_csv('/Users/teacher/Desktop/tests/credit_record.csv')
    d =DropID()
    targ = 'STATUS'
    optsolver = 'bfgs'
    regmef = 'l1_cvxopt_cp'
    maxiter = 1000
    
    apprec = d.fit_transform(apprec)

    d =DropID()
    
    crec = d.fit_transform(crec)
    print('b4')
    print(apprec.isnull().sum())
    print(crec.isnull().sum())
    #apprec = apprec.dropna()
    apprec['OCCUPATION_TYPE'] = apprec['OCCUPATION_TYPE'].replace(np.nan,'Other')
    apprec['CNT_FAM_MEMBERS'] = apprec['CNT_FAM_MEMBERS'].astype('int')

    print('af ')

    print(apprec.isnull().sum())
    
    catf = [c for c in apprec.columns if apprec[c].dtype =='O']
    numf = [c for c in apprec.drop('CNT_FAM_MEMBERS',axis=1).columns if (apprec[c].dtype =='float')]

    for c in catf:
        print(apprec[c].value_counts())


    PlotBar(apprec,catf)
    PlotHist(apprec,numf)
    PlotBox(apprec,numf)
    print(apprec.info())
    print(crec.info())

    m = Merge()
    
    X = m.fit_transform(apprec,X2= crec)
    y=X[targ]
    X=X.drop(targ,axis =1)
    
    lb = LabelT()
    
    y= np.array(lb.fit_transform(X,y = y)).reshape(-1,1)
    y=pd.DataFrame(y)
    
    LassoPipeline =[
        
        ('Time',TimeHandler()),
        ('Ordinal',OrdinalT()),
        ('Standard',StandardT()),
        ('Outlier',OutlierRemover())

    ]

    LP = Pipeline(LassoPipeline)
  
    X = LP.fit_transform(X)
   
    print(y)
    print(X.head())
    print(X.isnull().sum())


  #  print(X.head())
    fit_l = MNLogit(y, X).fit_regularized(method=regmef,maxiter= maxiter)

    print(fit_l.summary())

    predtl = fit_l.predict(X).round()

    print(predtl)

    print((predtl).round())

    print(classification_report(y, predtl))    

    fprtl, tprtl, thresholdst = metrics.roc_curve(y, predtl)
    auctrl = metrics.auc(fprtl, tprtl)
    print(' On training set nonroll AUC: {} '.format(auctrl))

    plt.show()
    
    
   
main()

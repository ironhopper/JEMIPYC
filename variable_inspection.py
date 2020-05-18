import pandas as pd
import numpy as np
from sklearn import datasets

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
tab = '__'
yy = np.array([1,2,3,4,5,6])

def df(x):
  x = pd.DataFrame(x)
  display(x)

def df2(x,y):
  row=x.shape[0]
  x = pd.DataFrame(x)
  y = pd.DataFrame(y)
  blank = ['']*row
  blank = pd.DataFrame(blank,columns=[tab])
  df_concat = pd.concat([x,blank,y], axis=1)
  display(df_concat)

def dfm(*x):
  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    blank = pd.DataFrame(blank,columns=[tab])
    xx = pd.DataFrame(x[i])
    if(i==0):
      df_concat = xx
    else:
      df_concat = pd.concat([df_concat,blank,xx], axis=1)
  display(df_concat)

def dfmn(*x):
  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    tabn = '_('+str(i)+')_'
    blank = pd.DataFrame(blank,columns=[tabn])
    xx = pd.DataFrame(x[i])
    if(i==0):
      df_concat = xx
    else:
      df_concat = pd.concat([df_concat,blank,xx], axis=1)
  display(df_concat)
  
# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target

# Usage
# dfmn(X,Y,X)

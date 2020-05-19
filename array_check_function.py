# import sys
# sys.path.append('mlstudy')
# from array_check_function import df,dfx,dfn,dfnx

import pandas as pd
import numpy as np

# naming considering / dfm? dfs? multi or single
tab = '__'

def df1(x):
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

# no-extension , number of parameters is not limited, 2 or 3, whatever you want.
# ex) df(A,B,C,D,...,Z...)
# of course you just put one parameter. 
def df(*x):
  pd.reset_option('display.max_columns')
  pd.reset_option('display.max_rows')
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
  # df_concat.replace(Null, 'test')
  # df_concat.fillna(0)
  # df_concat.info()
  df_concat.replace(np.nan, '', inplace=True)
  display(df_concat)

def dfn(*x): 
  pd.reset_option('display.max_columns')
  pd.reset_option('display.max_rows')
  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    tabn = '('+str(i+1)+')'
    blank = pd.DataFrame(blank,columns=[tabn])
    xx = pd.DataFrame(x[i])
    # xx.replace(' NaN','')
    if(i==0):
      df_concat = pd.concat([xx,blank], axis=1)
    else:
      df_concat = pd.concat([df_concat,xx,blank], axis=1)
  df_concat.replace(np.nan, '', inplace=True)
  display(df_concat)

# extension
def dfx(*x):
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)

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
  df_concat.replace(np.nan, '', inplace=True)
  display(df_concat)

def dfnx(*x):
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)

  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    tabn = '('+str(i+1)+')'
    blank = pd.DataFrame(blank,columns=[tabn])
    xx = pd.DataFrame(x[i])
    if(i==0):
      df_concat = pd.concat([xx,blank], axis=1)
    else:
      df_concat = pd.concat([df_concat,xx,blank], axis=1)
  df_concat.replace(np.nan, '', inplace=True)
  display(df_concat)

### Usage
# df(X,Y,Z)
# dfx(X,Y,Z)
# dfn(X,Y,Z)
# dfnx(X,Y,Z)

### example
# from sklearn import datasets
# iris = datasets.load_iris()
# X = iris.data[:, :2]  # we only take the first two features. whatever you want.
# Y = iris.target
# Z = np.array([[1,2],[3,4]])
# A = np.zeros(100)
# B = [1,2,3,4]
# df(X,Y,Z,A,B)

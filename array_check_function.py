# import sys
# sys.path.append('mlstudy')
# from array_check_function import df,dfn,dfv,dfx,dfnx,dfvx

import pandas as pd
import numpy as np

# naming considering / dfm? dfs? multi or single
tab = '__'

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

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
    tabn = '{'+str(i+1)+'}'
    blank = pd.DataFrame(blank,columns=[tabn])
    xx = pd.DataFrame(x[i])
    # xx.replace(' NaN','')
    if(i==0):
      df_concat = pd.concat([xx,blank], axis=1)
    else:
      df_concat = pd.concat([df_concat,xx,blank], axis=1)
  df_concat.replace(np.nan, '', inplace=True)
  display(df_concat)

def dfv(*x):
  pd.reset_option('display.max_columns')
  pd.reset_option('display.max_rows')
  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    # print(x.title)
    blank = ['']*row
    vname = namestr(x[i], globals())
    # print(vname)
    tabv = '<('+str(vname[0])+')'
    blank = pd.DataFrame(blank,columns=[tabv])
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
    tabn = '{'+str(i+1)+'}'
    blank = pd.DataFrame(blank,columns=[tabn])
    xx = pd.DataFrame(x[i])
    if(i==0):
      df_concat = pd.concat([xx,blank], axis=1)
    else:
      df_concat = pd.concat([df_concat,xx,blank], axis=1)
  df_concat.replace(np.nan, '', inplace=True)
  display(df_concat)

def dfvx(*x):
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)

  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    # print(x.title)
    blank = ['']*row
    vname = namestr(x[i], globals())
    # print(vname)
    tabv = '<('+str(vname[0])+')'
    blank = pd.DataFrame(blank,columns=[tabv])
    xx = pd.DataFrame(x[i])
    # xx.replace(' NaN','')
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

## example
# from sklearn import datasets
# iris = datasets.load_iris()
# X_iris_data = iris.data[:, :2]  # we only take the first two features. whatever you want.
# Y_iris_target = iris.target
# Z = np.zeros(100)
# A = np.array([[1,2,3,4],[5,6,7,8]])
# B = [1,2,3,4,5,6,7,8]
# C = [[1],[2],[3],[4],[5],[6],[7],[8]]
# D = np.array([[1,2,3,4,5,6,7,8]])
# E = np.array([1,2,3,4,5,6,7,8])
# F = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
# G = [[1,2,3,4,5,6,7,8]]
# df(A,B,C,D,E,F,G)
# dfn(B,A,X_iris_data,Y_iris_target)
# dfv(B,A,X_iris_data,Y_iris_target)
# dfx(X,Y,Z,A,B)

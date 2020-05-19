# import sys
# sys.path.append('mlstudy')
# from variable_inspection import df,dfx

import pandas
import numpy

# naming considering / dfm? dfs? multi or single
tab = '__'

def df1(x):
  x = pandas.DataFrame(x)
  display(x)

def df2(x,y):
  row=x.shape[0]
  x = pandas.DataFrame(x)
  y = pandas.DataFrame(y)
  blank = ['']*row
  blank = pandas.DataFrame(blank,columns=[tab])
  df_concat = pandas.concat([x,blank,y], axis=1)
  display(df_concat)

# no-extension , number of parameters is not limited, 2 or 3, whatever you want.
# ex) df(A,B,C,D,...,Z...)
# of course you just put one parameter. 
def df(*x):
  pandas.reset_option('display.max_columns')
  pandas.reset_option('display.max_rows')

  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    blank = pandas.DataFrame(blank,columns=[tab])
    xx = pandas.DataFrame(x[i])
    if(i==0):
      df_concat = xx
    else:
      df_concat = pandas.concat([df_concat,blank,xx], axis=1)
  display(df_concat)

def dfn(*x): 
  pandas.reset_option('display.max_columns')
  pandas.reset_option('display.max_rows')

  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    tabn = '('+str(i)+')'
    blank = pandas.DataFrame(blank,columns=[tabn])
    xx = pandas.DataFrame(x[i])
    if(i==0):
      df_concat = xx
    else:
      df_concat = pandas.concat([df_concat,blank,xx], axis=1)
  display(df_concat)

# extension
def dfx(*x):
  pandas.set_option('display.max_columns', None)
  pandas.set_option('display.max_rows', None)

  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    blank = pandas.DataFrame(blank,columns=[tab])
    xx = pandas.DataFrame(x[i])
    if(i==0):
      df_concat = xx
    else:
      df_concat = pandas.concat([df_concat,blank,xx], axis=1)
  display(df_concat)

def dfnx(*x):
  pandas.set_option('display.max_columns', None)
  pandas.set_option('display.max_rows', None)

  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    tabn = '('+str(i)+')'
    blank = pandas.DataFrame(blank,columns=[tabn])
    xx = pandas.DataFrame(x[i])
    if(i==0):
      df_concat = xx
    else:
      df_concat = pandas.concat([df_concat,blank,xx], axis=1)
  display(df_concat)

# Usage
# df(X,Y)
# dfx(X,Y)
# dfn(X,Y)
# dfnx(X,Y)

#import sys
#sys.path.append('mlstudy')
# Considering your module contains a function called my_func, you could import it:
# from variable_inspection import dfm

import pandas
import numpy

pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)

tab = '__'

def df(x):
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

def dfm(*x):
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

def dfmn(*x):
  leng = len(x)
  df_concat = []
  for i in range(leng):
    row=len(x[0])
    blank = ['']*row
    tabn = '_('+str(i)+')_'
    blank = pandas.DataFrame(blank,columns=[tabn])
    xx = pandas.DataFrame(x[i])
    if(i==0):
      df_concat = xx
    else:
      df_concat = pandas.concat([df_concat,blank,xx], axis=1)
  display(df_concat)

# Usage
# dfmn(X,Y,X)
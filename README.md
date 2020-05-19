# mlstudy
for machine learning study/ custom algorithm included


>0519 update
>
>adding and editing,simplifying functions
>
>_
>
>only df:
>
>pandas.reset_option('display.max_columns')
>
>=> reset options
>
>_
>
>dfx: extended
>
>pandas.set_option('display.max_columns', None)
>
>=> max row and col
>


<hr>

## Setting

1. 사용하기전 깃 클론 먼저 하시고
(google colab 사용시엔 앞에 !(느낌표)를 붙일것)

`!git clone https://github.com/ironhopper/mlstudy.git`

2. 사용시
아래 헤더파일을 복사하여 원하는 프로젝트에 붙여줍니다.
```python
import sys
sys.path.append('mlstudy')
from array_check_function import dfm
```

3.  df(X,Y) 
    dfx(X,Y)
이런식으로 사용합니다.
df -> 간단하게 볼때
dfx -> extended table(전체 데이터 확인용) 입니다.

variable inspector 대용으로 만들었습니다.


<hr>

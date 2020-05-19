# mlstudy
for machine learning study/ custom algorithm included


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

3. dfm(X,Y)
이런식으로 사용합니다.
variable inspector 대용으로 만들었습니다.



>0519 update
>
>adding and editing,simplifying functions
>
>
>only df:
>
>pandas.reset_option('display.max_columns')
>
>=> reset options
>
>
>dfx: extended
>
>pandas.set_option('display.max_columns', None)
>
>=> max row and col
>

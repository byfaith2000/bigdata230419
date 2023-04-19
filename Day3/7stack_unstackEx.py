import numpy as np
import pandas as pd


frame = pd.DataFrame(np.arange(6).reshape(2,3),
                    # 보통 리스트로 만드나 아래와 같이 직접 만들면 이름을 붙여줄 수 있다.
                     index=pd.Index(['seoul','busan'], name='state'),
                     columns = pd.Index(['one','two','three'], name='number'))
print(frame)
print()
print('---------------------------------------')
# stack : 데이터의 칼럼(열)을 로우(행)로 회전시킴
result = frame.stack()
print(result)
print()

# unstack : 데이터의 로우(행)을 칼럼(열)으로 회전시킴
result = frame.unstack()
print(result)
print()

#state를 돌려줌
# level -1은 마지막을 뜻함
result = frame.unstack(level=0)
print(result)
print()

print(result.unstack('state'))

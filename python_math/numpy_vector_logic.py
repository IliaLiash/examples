import numpy as np

V1 = np.array(list(map(int, input().split(','))))
V2 = np.array(list(map(int, input().split(','))))

V = V1[V1 % V2[-2] == 0] / V2[-2]

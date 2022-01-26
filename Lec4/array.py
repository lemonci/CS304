"""
Low-level array

Referential array

Compact array
1) Less memory usage
2) Performance: direct assess, principle of locality
"""

import sys
import matplotlib.pyplot
import numpy as np
%matplotlib auto

data = []
n_bytes = []

for k in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0: 3d}; Size in bytes: {1: 4d}'.format(a, b))
    data.append(None)
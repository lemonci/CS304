# CORRECT WAY TO CREATE MULTIDIMENSIONAL ARRAY IN PYTHON
l = [[9] * 10 for j in range(5)]
l[0][3] = 5

# WRONG WAY
# l = [[9]*10]*5

# numpy arrays
import numpy as np
z = np.zeros((10, 10))

nums1 = [1,2,3,0,0]
nums2 = [0,1]
m = 3
n = 2

l = []

mcount = 0
ncount = 0

new = []

while mcount < m and ncount < n:
    if nums1[mcount] <= nums2[ncount]:
        l.append(nums1[mcount])
        mcount += 1
    else:
        l.append(nums2[ncount])
        ncount += 1
        
while mcount < m:
    new.append(nums1[mcount])
    mcount += 1
    
while ncount < n:
    new.append(nums1[ncount])
    ncount += 1
for i in range(m+n):
    nums1[i] = new[i]

d ={'a':1,'b':2,'c':3}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

print(list(range(2,10)))

value = [x*x for x in range(1,11) if x%2==0]
print(value)

value2 = [m+n for m in 'ABC' for n in 'xyz']
print(value2)

import os
print([d for d in os.listdir('.')])

L = ['Hello','World','IBM','Apple','Chiyuze']
l = [s.lower() for s in L]
print(L)
print(l)
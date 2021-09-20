import os
import glob
dir = 'test/textGrid'
c=0
for filename in glob.glob(os.path.join(dir, '*')):
    c+=1
print(c)
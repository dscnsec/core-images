import sys
import cv2
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(sys.path[0]) if isfile(join(sys.path[0], f))]
print(onlyfiles)

a=0
for files in onlyfiles:
    #print(type(files))
    a +=1
    if( 'jpg' in files or 'jpeg' in files):
        image = cv2.imread(files,1)
        length = 959
        breadth = 962

        resized = cv2.resize(image,(length,breadth))
        cv2.imwrite(files,resized)
        print(resized.shape)
print(a)
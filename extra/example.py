import cv2
import numpy as np

'''
 lerp for numbers
'''
def lerp(A:float,B:float,t:float):
    return A+t*(B-A)

'''
lerp for numpy arrays
'''
def lerpArray(A:np.ndarray,B:np.ndarray,t:float):
    return np.add(A,np.multiply(t,np.subtract(B,A)))

# LOAD THE IMAGE WITH ALPHA CHANNEL — 'IMREAD_UNCHANGED' DOES THAT FOR US
img = cv2.imread('lerp_it.png',cv2.IMREAD_UNCHANGED)

# Before we change anything lets print img
print(img)


# GENERATE OUTPUT IMAGE DUMMY
output = np.zeros((4,4)) #ONLY doing first row

###===! HARD CODED CODE AHEAD !===###

# RETURNING ONLY THE FIRST ROW
first_row_input = img[0]
# TREATING FIRST PIXEL AS START AND LAST PIXEL AS END
# Start and End pixel to lerp
_start = first_row_input[0]
_end = first_row_input[3]

# Lerp the pixels and update the output
for i in range(0,len(first_row_input)):
    _t = i/(len(first_row_input)-1) # Gets the t value for the pixels
    output[i] = lerpArray(_start,_end,_t)

# SET NEWLY GENERATED FIRST_ROW OF GRADIENT TO ORIGINAL IMAGE
img[0] = output

# LETS PRINT THE MODIFIED IMG
print("="*50)
print("\t\t\tModified image")
print("="*50)

print(img)


# SAVE THE OUTPUT TO A FILE
cv2.imwrite('lerped_it.png', img)

########## MAIN FILE ENDS HERE










############ OTHER STUFF I WAS TESTING WITH NUMPY


# print(lerp([0,0,0],[255,255,255],0.5))

# x1 = np.full(3,255)         #outputs:   [255,255,255]
# x1 = np.full((1,3),255)     #outputs:   [[255 255 255]] 
# x1 = np.zeros(3)            #outputs:   [0. 0. 0.] 

# arr0 = np.zeros(3)
# arr1 = np.full(3,255)

# # result = np.multiply(arr0,arr1)
# result = lerpArray(arr0,arr1,0.5)
# print(result)
import cv2
import numpy as np


def colored(r, g, b, text):
    return '\033[38;2;{};{};{}m{} \033[38;2;255;255;255m'.format(r, g, b, text)

'''
 lerp for numbers
'''
def lerp(A:float,B:float,t:float):
    return ((B-A)*t)+A

'''
lerp for numpy arrays
'''
def lerpArray(A:np.ndarray,B:np.ndarray,t:float):
    return np.add(A,np.multiply(t,np.subtract(B,A)))

def lerpRGB(A:np.ndarray,B:np.ndarray,t:float):
    # lerp R
    lerped_R = lerp(int(A[0]),int(B[0]),t)
    lerped_G = lerp(int(A[1]),int(B[1]),t)
    lerped_B = lerp(int(A[2]),int(B[2]),t)
    return np.array([lerped_R,lerped_G,lerped_B,255])

'''
    Name "getAPIsRow" is short for "Get Alpha Pixel Indexes In an Img Row(cv2 numpy array)"
    Description:
        Gets the indexes in array of pixels where alpha is greater than 0
    Example:
        img_row_array = [[0,0,0,255],[0,0,0,0],[0,0,0,255]]
        getAPIsRow(img_row_array) will output: [0,2]
'''
def getAPIsRow(img_row) -> list:
    alphaPixels = []
    # loop through all pixels in a row and get their indexes if alpha > 0
    for pIndex in range(0,len(img_row)):
        current_pixel_alpha = img_row[pIndex][3] # 3rd element is alpha value of the pixel array
        if (current_pixel_alpha>0):
            # append index to alphaPixels
            alphaPixels.append(pIndex)
    
    # Discard row if alphaPixels has less than two elements
    if (len(alphaPixels)<2):
        return -1 # Return error flag
    
    return alphaPixels


# LOAD THE IMAGE WITH ALPHA CHANNEL — 'IMREAD_UNCHANGED' DOES THAT FOR US
img = cv2.imread('demo_10.png',cv2.IMREAD_UNCHANGED)
# Before we change anything lets print img
# print(img)

# GENERATE OUTPUT IMAGE DUMMY
output = np.zeros(img.shape) 
output = output[0]  #ONLY doing first row
###===! HARD CODED CODE AHEAD !===###

# RETURNING ONLY THE FIRST ROW
first_row_input = img[0]
# get alphaIndexes for start and end
alphaIndexes = getAPIsRow(first_row_input)
# Loop through all the indexes to get start and end pixels
# Use those start and end indexes to lerp pixels in start and end range
for index in range(0,len(alphaIndexes)):
    _start = alphaIndexes[index]    # eg: 0
    _end = alphaIndexes[index+1]    # eg: 3

    # Debug print
    # Start pixel
    _r = int(first_row_input[_start][0])
    _g = int(first_row_input[_start][1])
    _b = int(first_row_input[_start][2])
    # End pixel
    _r_ = int(first_row_input[_end][0])
    _g_ = int(first_row_input[_end][1])
    _b_ = int(first_row_input[_end][2])

    col_start = colored(_r,_g,_b,f'[{int(first_row_input[_start][0])} \t {int(first_row_input[_start][1])} \t {int(first_row_input[_start][2])} \t {first_row_input[_start][3]}]')
    col_end = colored(_r_,_g_,_b_,f'[{int(first_row_input[_end][0])} \t {int(first_row_input[_end][1])} \t {int(first_row_input[_end][2])} \t {first_row_input[_end][3]}]')

    print(f'start: {_start} end: {_end} startPixel: {col_start} \t endPixel: {col_end}')

    for i in range(_start,_end):
        _t = round(((i-_start)/(_end-_start)),2)
        output[i] = lerpRGB(first_row_input[_start],first_row_input[_end],_t)
        
        # # Debug print
        r = int(output[i][0])
        g = int(output[i][1])
        b = int(output[i][2])
        colored_output = colored(r,g,b,f'[{int(output[i][0])} \t {int(output[i][1])} \t {int(output[i][2])} \t {output[i][3]}]')
        print(f'i: {i}\t(i-_start): {i-_start}\t_t: {_t} \t pixelVal: {colored_output}')

    # break the loop if we are at second last item cause
    # second last index will account for last index using "index+1"
    if(index == len(alphaIndexes)-2):
        break

# SET NEWLY GENERATED FIRST_ROW OF GRADIENT TO ORIGINAL IMAGE
img[0] = output

# LETS PRINT THE MODIFIED IMG
# print("="*50)
# print("\t\t\tModified image")
# print("="*50)

# for i in img[0]:
#     for j in i:
#         if(j>255):
#             print("===========ERROR VALUE ABOVE 255=============")
#     print(i)


# SAVE THE OUTPUT TO A FILE
cv2.imwrite('done.png', img)

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
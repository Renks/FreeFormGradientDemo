from array import array
import cv2
import numpy as np

'''
author      :   Renks
Description :   Lerps Image pixels Horizontally (Left-to-Right)
Date        :   08/10/2022 (dd-mm-yyyy)
Inspired By :   Clip Studio Paint's freeform gradient tool
Comments    :   I have no idea how freeform gradient's algo works I'm just playing around here
'''



## IMAGE MUST BE A PNG FILE WITH ALPHA CHANNEL AVAILABLE

## INPUT IMAGE LOCATION
IN_IMAGE = "lerp_it_4.png"
OUT_IMAGE = "lerped_it_4.png"

########### CODE ##############
'''
    lerp for numpy arrays
'''
def lerpArray(A:np.ndarray,B:np.ndarray,t:float):
    return np.add(A,np.multiply(t,np.subtract(B,A)))

'''
    Name "getAPIsRow" is short for "Get Alpha Pixel Indexes In an Img Row(cv2 numpy array)"
    Description:
        Gets the indexes in array of pixels where alpha is greater than 0
    Example:
        img_row_array = [[0,0,0,255],[0,0,0,0],[0,0,0,255]]
        getAPIsRow(img_row_array) will output: [0,2]
'''
def getAPIsRow(img_row) -> array:
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
img = cv2.imread(IN_IMAGE,cv2.IMREAD_UNCHANGED)
# print(getAPIsRow(img[0]))
# exit()


# GENERATE OUTPUT IMAGE DUMMY
output = np.zeros(img.shape)

for y in range(0,len(img)):
    # y = row_index, img[y] = current_row
    
    # get alphaIndexes for start and end
    alphaIndexes = getAPIsRow(img[y])
    # If row can't be lerped then go to the next row
    if(alphaIndexes == -1):
        continue
    # Loop through all the indexes to get start and end pixels
    # Use those start and end indexes to lerp pixels in start and end range
    for index in range(0,len(alphaIndexes)):
        _start = alphaIndexes[index]    # eg: 0
        _end = alphaIndexes[index+1]    # eg: 3
        
        print(f'start: {_start} end: {_end}')
        # img[y][_start] = Start pixel  eg: [0 0   0 255]
        # img[y][_end] = End pixel      eg: [0 255 0 255]

        # MAIN LOOP
        # Lerp the pixels and update the output
        # Checkout the "example.py" to understand how the following loop works
        for i in range(_start,_end):
            _t = round(((i-_start)/(_end-_start)),3) # Gets the t value for the pixels
            print(f'i: {i} (i-_start): {i-_start} _t: {_t}')
            output[y][i] = lerpArray(img[y][_start],img[y][_end],_t)

        # break the loop if we are at second last item cause
        # second last index will account for last index using "index+1"
        if(index == len(alphaIndexes)-2):
            break

    # for x in range(0,len(img[y])):
    #     # x = pixel_index, treat it as a column index of 'y' row
    #     # img[y][x] will output individual pixel eg: [0,255,0,255] aka red pixel
    #     print(img[y][x])

    # OUTER FOR LOOP ENDS HERE

# print(output)
# # SAVE THE OUTPUT TO A FILE
img_float32 = np.float32(output)
# color correction
lab_image = cv2.cvtColor(img_float32, cv2.COLOR_BGRA2RGBA)
cv2.imwrite(OUT_IMAGE,img_float32)

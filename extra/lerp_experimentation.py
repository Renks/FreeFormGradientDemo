import numpy as np

def lerp(A:float,B:float,t:float):
    return A+t*(B-A)

'''
lerp for numpy arrays
'''
def lerpArray(A:np.ndarray,B:np.ndarray,t:float):
    return np.add(A,np.multiply(t,np.subtract(B,A)))

def lerpRGB(A:np.ndarray,B:np.ndarray,t:float):
    # lerp R
    lerped_R = lerp(A[0],B[0],t)
    lerped_G = lerp(A[1],B[1],t)
    lerped_B = lerp(A[2],B[2],t)
    return np.array([lerped_R,lerped_G,lerped_B,255])


print(lerp(255.0,89.0,0.5))
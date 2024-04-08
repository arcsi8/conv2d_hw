import numpy as np
import matplotlib.pyplot as plt
import sys
import getopt as go
import cv2 as cv
from PIL import Image as pil





def addPadding(matrix,padType):
    
    def defpadding(lng,wd,mrx,pad):
        for i in range(len(pad[1::])):
                for k in range(len(pad[i])):
                    if i >= 1 and k >= 1 and i < lng+1 and k < wd+1:
                        pad[i][k] = mrx[i-1][k-1]
        return pad
    def padStretch(l,w,pad):
        for i in range(len(pad[0][1::])):
            pad[0][i] = pad[1][i]
            
        for k in range(len(pad[length][1::])):
            pad[l+1][k] = pad[l][k]
            
        for k in range(len(pad)):
            pad[k][0] = pad[k][1]
            
        for k in range(len(pad)):
            pad[k][w+1] = pad[k][width]
        return pad

    
    length = len(matrix)
    width = len(matrix[0])
    padded = [[0 for i in range(width+2)] for k in range(length+2)]

    match padType:
        case 0:
            padded = defpadding(length,width,matrix,padded)  
            for i in range(len(padded)):
                print(padded[i])
        case 1:
            padded_m = defpadding(length,width,matrix,padded) 
            padded = padStretch(length,width,padded_m)
            for i in range(len(padded)):
                print(padded[i])
            
    return padded

def conv2d(arr,kernel):

    result = np.array([[0 for i in range(len(arr[1])-2)]for l in range(len(arr)-2)])
   
    """ kernel = np.array([[0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,0.5,0.5]])
    kernel2 = np.array([[1,1,1],[1,1,1],[1,1,1]]) """
    print("---------------------------------------")
    
    
    for i in range(1,arr.shape[0]-1):
        #print(arr[i][1:arr.shape[1]-1:])
        for k in range(1,arr.shape[1]-1):
            sm = 0
            for x in range(len(kernel)):
                for y in range(len(kernel[x])):
                    sm += kernel[x,y] * arr[(i-1)+x,(k-1)+y]
            result[i-1,k-1] = sm
    
    for l in range(result.shape[0]):
        print(result[l])

    return result
    

kerl = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])               
img = cv.imread("parrot.png",cv.IMREAD_GRAYSCALE)


#Matrix = [[np.random.randint(10) for i in range(15)] for l in range(15)]
#Matrix = np.array(Matrix)

mx2 = np.array(addPadding(img,1))

mx3 = conv2d(mx2,kernel=kerl)

cv.imwrite("out.png",mx3)


'''for i in range(len(mx2)):
   for k in range(len(mx2)):
        if Matrix[i][k] > 0:
            print(Matrix[i][k])'''
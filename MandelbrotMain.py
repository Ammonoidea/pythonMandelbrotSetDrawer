'''
Created on May 10, 2014

@author: akira
'''

import Image
import time

def escapeTime(xSize, ySize):
    img = Image.new('RGB',(xSize,ySize),'white')
    pix = img.load()
        
    xScale = 3.5/img.size[0]
    yScale = float(2.0/img.size[1])
    
    for Px in xrange(0, img.size[0]):
        for Py in xrange(0, img.size[1]):
            z = 0
            c = complex(-2.5 + xScale*Px, 1 - Py*yScale )
            iterations = 100
            i = 0
            while abs(z) < 2 and i < iterations:
                z = z*z + c
                i+= 1
                pix[Px, Py] = (255 - int(i*2.55), 255 - int(i*2.55), 255 - int(i*2.55))
    
    img.show()


if __name__ == '__main__':
    startTime = time.clock()
    escapeTime(1500,1000)
    print(time.clock()-startTime)
            

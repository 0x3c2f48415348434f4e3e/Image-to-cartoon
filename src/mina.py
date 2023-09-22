#Starting with a prototype:
'''
That is no window for now, once we get things working, then we can implement it within
a window
'''

import cv2


class cartoon:
    def __init__(self, path) -> None:
        img = cv2.imread(f'{path}')
        #cv2.imshow("Image",self.scaleDownImage(self,img.shape[1],img.shape[0],img))
        #steps we are going to take includes:
        '''
        1.) Resize our image
        2.) Blur our image
        '''
        
        #reassign img to take the new scaled down image
        resized = self.scaleDownImage(self,img.shape[1],img.shape[0],img)
        
        #reassign img to take resized image as well as blurred image
        imgR = self.edgedet(self,self.GrayScaleImage(self,self.bluringImage(self,resized)))
        cv2.imshow("Image",imgR)
        cv2.imshow("second",resized)
        cv2.waitKey(0)

#Using self within a static method kinda defeats the purpose, but at least it works
    @staticmethod
    def scaleDownImage(self,width,height,frame):
        scaleSize = 0.5
        self.width = width
        self.height = height
        self.frame = frame
        self.width = int(self.width * scaleSize)
        self.height = int(self.height * scaleSize)
        dimension = (self.width,self.height)
        return cv2.resize(self.frame,dimension,interpolation=cv2.INTER_AREA)
    
    @staticmethod
    def bluringImage(self,frame):
        self.frame = frame
        img = cv2.GaussianBlur(self.frame,(3,3,),cv2.BORDER_DEFAULT)
        #bluring removes soem of the nose
        return img
    
    @staticmethod
    def GrayScaleImage(self,frame):
        self.frame = frame
        img = cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)
        return img

    @staticmethod
    def edgedet(self,frame):
        self.frame = frame
        return cv2.Canny(self.frame, 125, 175)

first = cartoon('C:/Users/benja/Downloads/businessman_PNG6582.png')


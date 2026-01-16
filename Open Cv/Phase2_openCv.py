'''
In this phase we will learn about how to 
deal with Image transformation
and manipulation
1. Resizing and Scaling
2. Crop :-> Using slicing
3. Rotating and flipping of an image
4. Drawing shapes:-> Lines,circles,rectangles
5. Adding text :-> text placement and font selection
'''

# 1. Resizing :-> resized = cv2.resize(src,dsize,fx,fy,interpolation)
'''
1.src->Original image loaded
2.dsize->Dimensions in pixels (1 width then height)
3.fx:-> scale factors 
4.fy:-> scale factors
5.interpolation:-> scale fctors 
these 3,4,5 are resizing factors for pixels and optional
'''

import cv2

image2 = cv2.imread("Open Cv/rajanFilter.jpeg",-1)

if image2 is None:
    print('image is not found')
else:
    print('image loaded successfully')
    
    resize = cv2.resize(image2,(300,300))
    cv2.imshow("Original image",image2)
    cv2.imshow("resized_image",resize)
#always save resized image 
    cv2.imwrite("resized_output.webp",resize,[cv2.IMWRITE_WEBP_QUALITY,90])
    cv2.waitKey(0)
    cv2.destroyAllWindows

#2. Cropping an image using slicing in OpenCV
'''
Images in open Cv is just a matrices of pixels
that 2d or 3d array
basically understand this:-.
Y-axis:-> rows = top to bottom
X-axis:-> columns = left to right
Syntax:->
image[startY:endY,startX:endX]
'''
if image2 is not None:
    cropped = image2[100:200,50:150]
    cv2.imshow("originalImage",image2)
    cv2.imshow('croppedImage',cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#3. Image Rotation and flipping
'''
ROTATION
M = cv2.getRotationMatrix2D(center,angle,scale)
rotated_image = cv2.warpAffine(image,M,(width,height))

1. M = cv2.getRotationMatrix2D(center,angle,scale):->
This line creates a matrix to give instrux=ction to open Cv that is how
to rotate
Parameters:->
center:-> tell how to rotate as centre clock or anticlock
angle(in degrees):-> how much angle from axis you want to rotate
                  90-> clock wise
                 -90:-> anticlock wise
scale:-> How much to zoom in or zoom out while rotation
1.0:-> same size
0.5:-> half of tht 
2.0:-> double of that 
To get center point = (width//2,height//2)

2. rotated_image = cv2.warpAffine(image,M,(width,height)):->
this function apply the rotatio on image
image;-> originnal image
m :-> matrix instruction for rotation
(width,height)-> new width and height of output image
'''

if image2 is None:
    print("image could not load")
else:
    (h,w) = image2.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(image2,M,(w,h))

    cv2.imshow('originalIamge',image2)
    cv2.imshow("rotatedImage",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows


'''
FLIPPING
flipped = cv2.flip(image,flipcode):-> Mirror's the image across line
flipcode:->
0:-> flip vertically - top to bottom
1:-> flip orizontally - left to right
-1:-> flip both horizontally and vertically
'''

if image2 is None:
    print("image is not found")
else:
    flippedH = cv2.flip(image2,1)
    flippedV = cv2.flip(image2,0)
    flippedboth = cv2.flip(image2,-1)

    cv2.imshow('Original image',image2)
    cv2.imshow('horizontalFlip',flippedH)
    cv2.imshow('VerticalFlip',flippedV)
    cv2.imshow('Flipped both(h,v)',flippedboth)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#4. Drawing shapes(line,circlesand rectangle)

'''
1.Drawing lines over an image 
cv2.line(image,pt1,pt2,color,thickness)
image:-> original image
pt1:-> start point
pt2:-> end point of line
color:-> color of line
thickness:-> thickness of that line
'''


#LINE:->
if image2 is None:
    print('image is not found')

else:
    print('imageis loaded')
    pt1 = (50,100)
    pt2 = (200,100)
    color = (255,0,0)
    thickness = 4

    cv2.line(image2,pt1,pt2,color,thickness)
    cv2.imshow('Line drawn',image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""
RECTANGLE:-> these rectangles are used to detect faces and objects in images
cv2.rectangle(image,pt1,pt2,color,thickness)
pt1:-> top left corner of rectangle(x1,y1)
pt2:-> bottom right corner of rectangle(x2,y2)
"""

if image2 is None:
    print('image not found')
else:
    print('image is loaded')

    pt1 = (100,300)
    pt2 = (300,500)
    color = (0,250,0)
    thickness = 6

    cv2.rectangle(image2,pt1,pt2,color,thickness)
    cv2.imshow('Rectangle Drawn',image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''
CIRCLE:->
cv2.circle(image,center,radius,color,thickness)
center:-> (x,y)
radius:-> in pixels 
'''

if image2 is None:
    print('image is not found')
else:
    print('image found')
    cv2.circle(image2,(400,400),300,(0,250,0),6)

    cv2.imshow('Circle in imge',image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#5. Adding text in the image
'''
cv2.puText(img,text,org,font,fontScale,color,thickness)
org -> (x,y) :-> bottom left point to start with
font:-> fonttype
fontscale:-> text size (1.0-normal, 2.0-big)
'''
if image2 is None:
    print('image is not found')
else:
    print('image found')
    cv2.putText(image2,"Hellow!",(50,300),cv2.FONT_HERSHEY_SIMPLEX,
                1.2,(0,255,255),3)

    cv2.imshow('Text on the image',image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()










    



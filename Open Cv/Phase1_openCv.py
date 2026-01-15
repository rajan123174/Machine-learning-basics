import cv2
#print(cv2.__version__) :-> for checking version
'''
in this phase we will learn :->
Image Handling:->
1.Reading an image
2.Displaying an imag
3.Saving an image
4.Image dimensions
5.ColorChannels
6.Grayscale Conversions
Projects :->
Load image
Convert to Grayscale
Save image

Basics for an image :->
1.Image :-> 2d grid of pixels(that is a matrix of pixels)
2.Pixels:-> smallest unit of image unites to make an image
Each pixel contains RGB Channels that defines color of that 
pixel ranges from 0-255
3.Width and Height:-> width is total no of pixels in horizontal(l->r)
Height:-> otal number of pixels in vertical(
Gives resolution of an image
4.Color channel:-> a channel that stores the one part of information
of a color in one pixel
5.Image format:-> .jpg, *.png, .bmp, *WebP these are image encoding 
techniques to save an image in a file  
'''

# Reading an image :-> cv2.imread("filename",flag)
'''
flag(Optional):->
1= colorful
0 = grayscale(Black and white)
-1 = Unchanged'''
image = cv2.imread("Open Cv/Rajan.jpeg",-1)

if image is None:
    print("image not found")
else:
    print("image loaded successfully")

# To display image that has been loaded 
'''
cv2.imshow(Title(for image),image(variable stored image))
cv2.waitKey(0):-> untill any key pressed in keyboard display window
cv2.destroyAllWindows()
'''
if image is not None:
    cv2.imshow("Rajan's image",image)# open window
    cv2.waitKey(0) # wait for a key
    cv2.destroyAllWindows()# close the window
else:
    print("could'nt load the image")


# To save an Image 
'''
cv2.imwrite("filename.jpg",image)
'''

if image is not None:
    success = cv2.imwrite("edited_image.webp",image,[cv2.IMWRITE_WEBP_QUALITY, 90])
    if success:
        print("Image saved successfully")
    else:
        print("Failed to save")
else:
    print("Error: could not load image")

#4 . Image dimensions b=very important
'''
image.shape():-> this is an attribute to get :->
height,width,color channel
(height,  width,  channel)
(480,640,3)
channels:-> 3 like BGR 
channel is missing in gray scale images
'''

if image is not None:
    h, w, c = image.shape
    print(f"image Loaded:\nHeight: {h}\nWidth: {w}\nChannel: {c}")

else:
    print("could not load image")


# 5. To convert an image to gray scale(Black and white)
'''
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
'''
if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image Rajan",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows
else:
    print("could'nt load the image")


import cv2

#loading the image
image = cv2.imread("Open Cv/rajanFilter.jpeg",-1)
if image is None:
    print("image is not found")
else:
    print("image is loaded successfully")

# GrayScaleing the image

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("grayImage RajanFilter",gray)# show
    cv2.waitKey(0)
    cv2.destroyAllWindows

    cv2.imwrite("rajanFilterimage2.webp",gray,[cv2.IMWRITE_WEBP_QUALITY, 90])
else:
    print("mage could not loaded")

# saving the Grayscale image



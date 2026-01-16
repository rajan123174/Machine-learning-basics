'''
In this phase we will dealing with Video and webcam
Components of a video :->
1. What is a Video
2. What is a Webcam
3. Frame-by-Frame Processing 
1Frame -:> 1 image 
1 video :-> many frames


cap = cv2.VideoCapture(source):->
to read framss/a video 
for computer/laptop webcam - 0
external webcam - 1
'''
import cv2

cap = cv2.VideoCapture(0)# open webcam

while True:
    ret, frame = cap.read()# ret= True/False  frame=image
    if not ret:
        print('could not read frame')
        break
    cv2.imshow("webcam Feed",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):# 113 == 113  True
        print('Quitting....')
        break

cap.release()# close webcam
cv2.destroyAllWindows()

'''
Saving webcam Video to a file with OpenCV
cv2.VideoWriter(filename, codec, fps, frame_size):->
saves in .mp4 or .avi
filename:-> to save video in a file 
codec:-> commpression format
fps:-> frames per second
frame_size:-> (w,h)
'''

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter.fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.mp4",codec,30,(frame_width,frame_height))

while True :
    success, image = camera.read()

    if not success:
        break
    recorder.write(image)
    cv2.imshow("recording live ....",image)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()



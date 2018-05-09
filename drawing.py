import numpy
import cv2

cap = cv2.VideoCapture('video.MOV')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.MOV',fourcc, 20.0, (640,480))
while(1):

    _,frame = cap.read()


    cv2.line(frame, (500, 400), (640, 480),(0,255,0), 3)


    cv2.putText(frame, "test!",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(225,0,0))
    out.write(frame)
    #if key pressed is 'Esc', exit the loop
    cv2.imshow('frame',frame)

    if cv2.waitKey(33)== 27:
        break
out.release()

cv2.destroyAllWindows()

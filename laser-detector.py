import numpy as np
import matplotlib.pyplot as plt
import cv2
import serial
import time

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

scans = []
cap = cv2.VideoCapture(0)
target = open("./output.obj",  'w')

#ser = serial.Serial('/dev/tty.usbmodem1421', 19200)

# Allows the user to setup the frame
while(True):
    ret, frame = cap.read()
    height, width, chans = frame.shape
    cv2.line(frame, (0, int(height - (height/3))), (int(width), int(height - (height/3))), (0,0,255),5)
    cv2.line(frame, (int(width / 2), 0), (int(width / 2), int(height)), (255,0,0),1)
    cv2.imshow("Initial", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

# Begins to capture the frame
for k in range(160):
    print k + 10
    ser.write(str(k + 10))
    time.sleep(0.5)

    line = []
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY);
    # Display

    height, width = thresh.shape
    for i in range(height - (height/300)):
        for j in range(width):
            #if j == width:

            #    line.append(0)
            #    break

            if thresh[i,j] == 255:
    	    #    line.append(j)
                x, y = pol2cart((width/2 - j), np.radians(k))
                z = i
                target.write("v ")
                target.write(str(x/float(100)))
                target.write(" ")
                target.write(str(y/float(100)))
                target.write(" ")
                target.write(str(z/float(100)))
                target.write("\n")


                break
    #cv2.imshow('frame', thresh)
    #plt.plot(line)
    #plt.show()
    #scans.append(line[:])

#target.write(str(scans))
target.close()

cap.release()

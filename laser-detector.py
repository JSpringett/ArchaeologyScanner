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

ser = serial.Serial('/dev/tty.usbmodem1421', 19200)

while(True):
    ret, frame = cap.read();
    frame = cv2.line(frame, (0, int(cap.get(4)) - 100), (int(cap.get(3)), int(cap.get(4)) - 100), (0,0,255),5)  
    frame = cv2.line(frame, (int(cap.get(3) / 2), 0), (int(cap.get(3) / 2), int(cap.get(4))), (255,0,0),1)  
    cv2.imshow("Initial", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


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
    for i in range(height - 100):
        for j in range(width):
            #if j == width:

            #    line.append(0)
            #    break

            if thresh[i,j] == 255:
    	    #    line.append(j)
                x, y = pol2cart((width/2 - j), np.radians(k))
                z = i
                target.write("v ")
                target.write(str(x/float(100))
                target.write(" ")
                target.write(str(y/float(100))
                target.write(" ")
                target.write(str(z/float(100))
                target.write("\n")
                cv2.imshow('jhgjh', thresh)


                break
    #cv2.imshow('frame', thresh)
    #plt.plot(line)
    #plt.show()
    #scans.append(line[:])

#target.write(str(scans))
target.close()

cap.release()

#https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv
import cv2

"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="wustl_inst",
  password="wustl_pass"
)

print(mydb)
"""

cv2.namedWindow("preview")
vc = cv2.VideoCapture(1) #depends on the computer and what port USB is connected to

if vc.isOpened(): # try to get the first frame
    state, frame = vc.read()
else:
    state = False

while state:
    cv2.imshow("preview", frame)
    state, frame = vc.read()

    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        print("saved image")
        cv2.imwrite('TelXScope/images/images3.png',frame)
        #put file path inside mysql database
        cv2.destroyAllWindows()
        break
    if cv2.waitKey(1) & 0xFF == ord('q'): #exits the program
        cv2.destroyAllWindows()
        break
vc.release()
cv2.destroyWindow("preview")
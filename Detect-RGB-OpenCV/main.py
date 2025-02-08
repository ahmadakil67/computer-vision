import cv2
import numpy as np

vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = vid.read()

    if not ret:
        print("End of video or error reading frame.")
        break

    cv2.imshow("frame", frame)

    b = frame[:, :, 0]  
    g = frame[:, :, 1]  
    r = frame[:, :, 2]  

    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    if b_mean > g_mean and b_mean > r_mean:
        print("Blue")
    elif g_mean > r_mean and g_mean > b_mean:
        print("Green")
    else:
        print("Red")

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release()
cv2.destroyAllWindows()
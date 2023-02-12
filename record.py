import cv2
import mss
from PIL import Image
import numpy as np
import time

# record video of screen using cv2
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (5120, 1440))
mon = {'left': 0, 'top': 0, 'width': 5120, 'height': 1440}
with mss.mss() as sct:
   while True:
       img = sct.grab(mon)
       frame = Image.frombytes(
           'RGB', 
           (img.width, img.height), 
           img.rgb, 
       )
       frame = np.array( frame)
       out.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
       time.sleep(1/fps)
out.release()
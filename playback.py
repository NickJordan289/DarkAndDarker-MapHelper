import cv2
import argparse

# get video name from argparser
parser = argparse.ArgumentParser()
parser.add_argument('video', help='video file to play')
args = parser.parse_args()

map1 = cv2.imread('Crypt_01_N.png')
map1_grey = cv2.cvtColor(map1, cv2.COLOR_BGR2GRAY)
MIN_CONFIDENCE = 0.5

#with open('Crypt_01_N.json') as f:
#    markers = json.load(f)['markers']
#    for marker in markers:
#        cv2.circle(map1, (int(marker['coordinates']['lng']), int(marker['coordinates']['lat'])), 5, (0, 255, 0), -1)

video = cv2.VideoCapture(args.video)
while True:
    ret, frame_orig = video.read()
    if ret:
        frame = cv2.cvtColor(frame_orig, cv2.COLOR_RGB2GRAY) # video is in reverse color
        frame = frame[1100:1405, 4780:5085] # crop to map
        frame = cv2.resize(frame, (470, 470)) # resize to reference map size
        result = cv2.matchTemplate(map1_grey, frame, cv2.TM_CCOEFF_NORMED)
        if result.max() > MIN_CONFIDENCE:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            # draw players location on reference map
            cv2.circle(map1, (max_loc[0] + int(frame.shape[1]/2), max_loc[1] + int(frame.shape[0]/2)), 5, (0, 0, 255), -1) 
        
        # resize map1 to 50%
        map1_scaled = cv2.resize(map1, (0,0), fx=0.5, fy=0.5)
        cv2.imshow('map', map1_scaled)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
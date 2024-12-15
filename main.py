import cv2
import Hand_tracking_module as htm
import time
import numpy as np
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cv2.namedWindow("Volume Control", cv2.WINDOW_AUTOSIZE)


detector = htm.handDetector(maxhands=1, detectionCon=0.8, trackingCon=0.8)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)


# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-19.0, None)
minVol = volRange[0]
maxVol = volRange[1]
cVol = volume.GetMasterVolumeLevel()
volBar = np.interp(cVol, [minVol, maxVol], [300, 150])
volPercent = np.interp(cVol, [minVol, maxVol], [0, 100])

pTime = 0
while cv2.waitKey(50) != 27:

    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4])
        # print(lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)

        cv2.circle(img, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (0, 255, 0), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Hand Range 30 - 300
        vol = np.interp(length, [30, 300], [minVol, maxVol])
        cVol = volume.GetMasterVolumeLevel()
        volBar = np.interp(cVol, [minVol, maxVol], [300, 150])
        volPercent = np.interp(cVol, [minVol, maxVol], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)
        # print(volBar)
        # print(length)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        else:
            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

    cv2.rectangle(img, (50, 150), [75, 300], (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), [75, 300], (255, 0, 0), cv2.FILLED)
    cv2.putText(
        img,
        f"{int(volPercent)}%",
        (40, 350),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 0, 0),
        2,
    )

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, f"FPS : {int(fps)}", (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2
    )
    cv2.imshow("Volume Control", img)

cap.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import time
import sys
import random


class handDetector:
    def __init__(
        self,
        mode=False,
        maxhands=2,
        model_complexity=1,
        detectionCon=0.5,
        trackingCon=0.5,
    ):
        self.mode = mode
        self.maxhands = maxhands
        self.model_complexity = model_complexity
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpHands = mp.solutions.hands  # creating object to use model
        self.hands = self.mpHands.Hands(
            self.mode,
            self.maxhands,
            self.model_complexity,
            self.detectionCon,
            self.trackingCon,
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    # to get points and draw iline to connect them
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS
                    )
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            if handNo < len(self.results.multi_hand_landmarks):
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    # print(id, lm)
                    h, w, c = img.shape
                    # getting location(in pixels) of every points.
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id, cx, cy)
                    lmList.append([id, cx, cy])
                    if draw:
                        #  Drawing circle at the tip of every finger.
                        cv2.circle(
                            img,
                            (cx, cy),
                            10,
                            (
                                random.randrange(0, 255),
                                random.randrange(0, 255),
                                random.randrange(0, 255),
                            ),
                            cv2.FILLED,
                        )

        return lmList


def main():
    s = 0

    if len(sys.argv) > 1:
        s = 2

    cap = cv2.VideoCapture(2)
    detector = handDetector()
    pTime = 0
    cTime = 0

    while cv2.waitKey(1) != 27:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img, draw=True)

        lmList = detector.findPosition(img=img, handNo=1)
        # print(lmList)

        # To get FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3
        )

        cv2.imshow("Image", img)

    cv2.destroyAllWindows()
    cap.release()
    # cv2.waitKey(1)


if __name__ == "__main__":
    main()

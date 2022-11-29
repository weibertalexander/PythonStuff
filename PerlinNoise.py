import cv2
import numpy as np
import noise
import random

image = np.zeros((1000, 1000, 3), np.uint8)
lines = image.copy()
thickness = 1
time = 1
alpha = .3


def drawCurve(numberOfPoints, offset):
    global time
    global image
    global lines
    global alpha
    global newOffset

    points = []
    r = random.random()
    for n in range(numberOfPoints):
        x = abs(int(noise.pnoise1(time + n * offset) *
                    image.shape[0]//2 + image.shape[0]//2))
        y = abs(int(noise.pnoise1((time + n * offset + newOffset)) *
                    image.shape[1]//2 + image.shape[1]//2))
        points.append((x, y))

    time += 0.005
    # print(col)
    for i in range(len(points) - 1):
        noiseColor = abs(
            int(noise.pnoise1(r/100+time*4 + noise.pnoise1(3*i)) * 256)) + 128
        colors = (255, noiseColor, 0)
        # print(points[i])
        image = cv2.line(image, (points[i]), points[i+1],
                         colors, thickness, cv2.LINE_AA)
        if i == len(points) - 2:
            image = cv2.line(image, points[-1], points[0],
                             colors, thickness, cv2.LINE_AA)
    # image = cv2.addWeighted(lines, 1 - alpha, image, alpha, 0)
    # lines = cv2.addWeighted(empty, alpha, image, 1-alpha, 0)
    cv2.imshow("window", image)
    # image = np.zeros((1000, 1000, 3), np.uint8)


def main():
    global image
    global newOffset
    newOffset = 1455
    while True:
        drawCurve(2, 52)
        key = cv2.waitKey(1)
        newOffset += 0.0001
        if key == ord("q"):
            break
    cv2.destroyAllWindows()


if (__name__ == '__main__'):
    main()

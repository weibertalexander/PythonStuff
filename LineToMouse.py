import cv2
import numpy as np

dimensions = (1000, 1000)

thickness = 1

image = np.zeros((dimensions[0], dimensions[1], 3), np.uint8)
i = 0
# Draw a line from the center of the image to the given point x, y.
def drawLine(x, y):
    global i
    center = (dimensions[1]//2, dimensions[0]//2)
    dist = np.sqrt((center[0] - x)**2 + (center[1] - y)**2)
    dist += 0.1
    mapped = 255 - (255 / dimensions[1]) * dist
    i+=1
    cv2.line(image,
             (center[0], center[1]),
             (x, y),
             (0,
              mapped,
              255 * (np.cos(mapped) + 50)),
             thickness,
             lineType=cv2.LINE_AA)


# On Mouse event: draws a line when mouse is moving.
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        drawLine(x, y)


cv2.imshow("window", image)
cv2.setMouseCallback("window", onMouse)


def main():
    while True:
        cv2.imshow("window", image)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    cv2.destroyAllWindows()


if (__name__ == '__main__'):
    main()

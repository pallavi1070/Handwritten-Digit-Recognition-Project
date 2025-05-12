import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

# Constants
WINDOWSIZEX = 640
WINDOWSIZEY = 480
BOUNDARYINC = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

IMAGESAVE = False

# Load trained model
Model = load_model("bestmodel.h5")

Labels = {
    0: "Zero", 1: "One", 2: "Two",
    3: "Three", 4: "Four", 5: "Five", 6: "Six",
    7: "Seven", 8: "Eight", 9: "Nine"
}

# Initialize Pygame
pygame.init()
FONT = pygame.font.Font("freesansbold.ttf", 18)
DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
pygame.display.set_caption("Digit Board")

isWriting = False
img_cnt = 1
Predict = True
number_xcord = []
number_ycord = []

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Start drawing
        if event.type == MOUSEBUTTONDOWN:
            isWriting = True

        # Stop drawing and predict
        if event.type == MOUSEBUTTONUP:
            isWriting = False

            if number_xcord and number_ycord:
                number_xcord = sorted(number_xcord)
                number_ycord = sorted(number_ycord)

                rect_min_x = max(number_xcord[0] - BOUNDARYINC, 0)
                rect_max_x = min(WINDOWSIZEX, number_xcord[-1] + BOUNDARYINC)
                rect_min_y = max(number_ycord[0] - BOUNDARYINC, 0)
                rect_max_y = min(WINDOWSIZEY, number_ycord[-1] + BOUNDARYINC)

                img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x:rect_max_x, rect_min_y:rect_max_y].T.astype(np.float32)

                number_xcord = []
                number_ycord = []

                if IMAGESAVE:
                    cv2.imwrite(f"image{img_cnt}.png", img_arr)
                    img_cnt += 1

                if Predict:
                    image = cv2.resize(img_arr, (28, 28))
                    image = np.pad(image, ((10, 10), (10, 10)), mode='constant', constant_values=0)
                    image = cv2.resize(image, (28, 28)) / 255.0

                    prediction = Model.predict(image.reshape(1, 28, 28, 1))
                    label = str(Labels[np.argmax(prediction)])

                    textSurface = FONT.render(label, True, RED, WHITE)
                    textRecObj = textSurface.get_rect()
                    textRecObj.left, textRecObj.bottom = rect_min_x, rect_max_y

                    DISPLAYSURF.blit(textSurface, textRecObj)

        # Capture coordinates while drawing
        if event.type == MOUSEMOTION and isWriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord), 4, 0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)

        # Clear screen with 'n' key
        if event.type == KEYDOWN:
            if event.unicode == "n":
                DISPLAYSURF.fill(BLACK)

    pygame.display.update()

'''
car = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw Pac-Man (a filled yellow ellipse with a missing wedge to simulate the mouth)
center = (250, 250)  # center of the circle
radius = 200
color = (255, 255,)  # Yellow in BGR
thickness = -1  # filled

# Draw an arc to create the Pac-Man shape (270 degrees)
cv.ellipse(img, center, (radius, radius), 0, 30, 330, color, thickness)

# Draw the eye (a small filled black circle)
eye_center = (250, 150)
eye_radius = 20
cv.circle(img, eye_center, eye_radius, (0, 0, 0), -1)

# Show the result
imshow('Pac-Man', img)'''
import cv2 as cv
import numpy as np

# Create a black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw Pac-Man (a filled yellow ellipse with a missing wedge to simulate the mouth)
center = (250, 250)  # center of the circle
radius = 200
color = (0, 255, 255)  # Yellow in BGR
thickness = -1  # filled

# Draw an arc to create the Pac-Man shape (270 degrees)
cv.ellipse(img, center, (radius, radius), 0, 30, 330, color, thickness)

# Draw the eye (a small filled black circle)
eye_center = (250, 150)
eye_radius = 20
cv.circle(img, eye_center, eye_radius, (0, 0, 0), -1)

# Show the result
cv.imshow('Pac-Man', img)
cv.waitKey(0)
cv.destroyAllWindows()

import cv2

file = cv2.imread("solar-system.jpg")


font = cv2.FONT_HERSHEY_TRIPLEX
color = (255, 255, 255)

cv2.putText(file, "The Sun", (0, 200), font, 0.8, color, 2)
cv2.putText(file, "Mercury", (125, 200), font, 0.3, color, 1)
cv2.putText(file, "Venus", (200, 200), font, 0.5, color, 1)
cv2.putText(file, "Earth", (285, 210), font, 0.6, color)
cv2.putText(file, "Moon", (320, 180), font, 0.3, color, 1)
cv2.putText(file, "Mars", (380, 200), font, 0.7, color)
cv2.putText(file, "Jupiter", (480, 200), font, 1, color)
cv2.putText(file, "Saturn", (730, 200), font, 0.8, color)
cv2.putText(file, "Uranus", (900, 200), font, 1, color, 2)
cv2.putText(file, "Neptune", (1100, 200), font, 1, color)


cv2.imshow("Solar System", file)
cv2.waitKey(0)
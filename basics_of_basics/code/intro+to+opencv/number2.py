import cv2

cap = cv2.VideoCapture(0)  # Replace with your file or 0 for webcam
while True:
    ret, frame = cap.read()
    print(ret)
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2

def detect_shape(approx):
    corners = len(approx)
    if corners == 3:
        return "Triangle"
    elif corners == 4:
        # Could be square or rectangle
        x, y, w, h = cv2.boundingRect(approx)
        ratio = w / float(h)
        return "Square" if 0.95 < ratio < 1.05 else "Rectangle"
    elif corners > 5:
        return "Circle"
    return "Polygon"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blur = cv2.GaussianBlur(frame, (5, 5), 1)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            shape = detect_shape(approx)
            x, y, w, h = cv2.boundingRect(approx)

            cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
            cv2.putText(frame, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255, 0, 0), 2)

    cv2.imshow("Real-Time Shape Hunter", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

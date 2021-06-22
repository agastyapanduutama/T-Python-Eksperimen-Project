import cv2

video = "/home/pandu/Documents/eksperimen/video/s_cuci_tangan11.mp4"

cap = cv2.VideoCapture(video)

while True:
    ret, frame = cap.read()
    cv2.imshow("vi", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

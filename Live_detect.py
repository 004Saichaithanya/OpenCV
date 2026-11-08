import cv2 as cv

# Load Haar Cascade for face detection
haar_cascade = cv.CascadeClassifier('frontal_face.xml')

# Start video capture (0 for default webcam)
capture = cv.VideoCapture(0)

# Check if webcam opened successfully
if not capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read frame-by-frame
    isTrue, frame = capture.read()

    if not isTrue:
        print("Failed to capture frame. Exiting...")
        break

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the frame
    face_rect = haar_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in face_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    # Show the frame with detections
    cv.imshow('Live Face Detection', frame)

    # Break loop on pressing 'q'
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
capture.release()
cv.destroyAllWindows()

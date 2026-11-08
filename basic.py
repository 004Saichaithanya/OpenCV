from ultralytics import YOLO
import cv2

# Load image
img = cv2.imread('images/street2.jpg')
if img is None:
    print("Error: Image not found.")
    exit()

# Resize image
img = cv2.resize(img, (640, 480))  # width=640, height=480

# Load YOLO model
model = YOLO('yolov8n.pt')

# Run detection on resized image
results = model(img)[0]

# Draw boxes
img_with_boxes = results.plot()

# Display
cv2.imshow('Detected Objects', img_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()

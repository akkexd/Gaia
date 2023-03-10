import cv2
import urllib.request
import numpy as np

# Load the YOLOv4 model
net = cv2.dnn.readNet('C:/Users/User/PycharmProjects/pythonProject/yolov4.weights', 'C:/Users/User/PycharmProjects/pythonProject/yolov4.cfg')
url = 'https://github.com/AlexeyAB/darknet/raw/master/data/coco.names'
filename = 'coco.names'
urllib.request.urlretrieve(url, filename)

# Define the classes for the YOLOv4 model
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Set the input size for the YOLOv4 model
input_size = 608

# Define the colors for the bounding boxes
colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 255), (255, 255, 0)]

# Set the confidence threshold and non-maximum suppression threshold
conf_threshold = 0.5
nms_threshold = 0.4

# Load the input image
img = cv2.imread('saved_img.jpg')

# Create a blob from the input image
blob = cv2.dnn.blobFromImage(img, 1/255.0, (input_size, input_size), swapRB=True, crop=False)

# Set the input blob for the YOLOv4 model
net.setInput(blob)

# Forward pass through the YOLOv4 model
outputs = net.forward(net.getUnconnectedOutLayersNames())

# Initialize the lists for the bounding boxes, confidences, and class IDs
boxes = []
confidences = []
class_ids = []

# Iterate over each output from the YOLOv4 model
for output in outputs:
    # Iterate over each detection in the output
    for detection in output:
        # Get the class ID and confidence for the detection
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        # Check if the confidence is greater than the threshold
        if confidence > conf_threshold:
            # Get the center, width, and height of the bounding box
            center_x = int(detection[0] * img.shape[1])
            center_y = int(detection[1] * img.shape[0])
            width = int(detection[2] * img.shape[1])
            height = int(detection[3] * img.shape[0])
            # Calculate the top-left corner of the bounding box
            x = int(center_x - (width / 2))
            y = int(center_y - (height / 2))
            # Append the bounding box, confidence, and class ID to their respective lists
            boxes.append([x, y, width, height])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non-maximum suppression to remove overlapping bounding boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

# Draw the bounding boxes and class labels on the input image
if len(indices) > 0:
    for i in indices.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[class_ids[i] % len(colors)]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Display the output image
cv2.imshow('Object Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

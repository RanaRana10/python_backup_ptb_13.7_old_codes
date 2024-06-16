import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load your image
image = cv2.imread('a.png')

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Count the number of faces detected
num_faces = len(faces)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle around the face

# Print the number of faces detected
print(f'Number of Faces: {num_faces}')

# Display the image with rectangles
cv2.imshow('Image with Face Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

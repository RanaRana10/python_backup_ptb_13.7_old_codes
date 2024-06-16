import cv2

def detect_faces(image_path):
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image_path = "file_6.jpg"
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show the image with rectangles around faces
    cv2.imshow('Detected Faces', image)
    
    # Wait for a key event and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the number of faces detected
    return len(faces)

# Replace 'your_image_path.jpg' with the actual path of the image you want to analyze
image_path = 'your_image_path.jpg'

# Call the detect_faces function
num_faces = detect_faces(image_path)

# Print the result
print(f"Number of faces detected: {num_faces}")

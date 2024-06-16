import ocrolib

# Load the image
image = ocrolib.read_image('a.png')


# Preprocess the image if needed (e.g., binarization, deskewing, etc.)
# You can use OCRopus functions for preprocessing as required.

# Perform OCR on the image
text = ocrolib.ocr(image)

# Print the extracted text
print(text)

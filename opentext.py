import cv2
from PIL import Image
import pytesseract

def capture_image():
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        cv2.imshow('Press s to capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('captured_image.jpg', frame)
            break
    
    camera.release()
    cv2.destroyAllWindows()

def read_text():
    # Path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Load the captured image
    image = Image.open('captured_image.jpg')

    # Perform OCR to extract text
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print("Extracted text:")
    print(text)

if __name__ == "__main__":
    # Step 1: Capture an image from the webcam
    capture_image()

    # Step 2: Read text from the captured image
    read_text()

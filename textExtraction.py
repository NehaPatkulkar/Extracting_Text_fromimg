import cv2
import pytesseract

# Set the correct path for Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define the image path
image_path = (
    r"C:\Users\Admin\Downloads\WhatsApp Image 2025-02-24 at 20.45.13_4ca0d786.jpg"
)


def extract_text(image_path):
    """
    Extracts text from an image using Tesseract OCR.
    """
    try:
        # Load the image
        img = cv2.imread(image_path)

        if img is None:
            raise FileNotFoundError(f"Error: Unable to load image '{image_path}'")

        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply thresholding for better OCR
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(gray)

        return extracted_text.strip()

    except Exception as e:
        return f"Error processing image '{image_path}': {str(e)}"


# Run the function and print the extracted text
extracted_text = extract_text(image_path)
print("Extracted Text:", extracted_text)

import os
import pytesseract # pip install pytesseract
import cv2 # pip install opencv-python
from PlateRecognitionAlgorithm import plateRecognize

# Download https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

# Load pre-trained Haar cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Folder containing images
folder_path = "plates_img"

# Iterate over images in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Read image
        image_path = os.path.join(folder_path, filename)
        frame = cv2.imread(image_path)
        
        # Detect and recognize plates
        txt, crop, img = plateRecognize(frame)
        if(txt == ""):
            continue

        # Display the plate number
        print(txt)

        # Display the croped image
        # cv2.imshow('License Plate Recognition', crop)

        # Display the frame
        cv2.imshow('License Plate Recognition', img)
        
        # Press any key to move to the next image
        cv2.waitKey(0)

cv2.destroyAllWindows()
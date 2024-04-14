import os
import pytesseract # pip install pytesseract
import cv2 # pip install opencv-python
from PlateRecognitionAlgorithm import plateRecognize

# Download pytesseract https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

# Start video capture
cap = cv2.VideoCapture("plates_videos/license_plate.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Display the frame
    # cv2.imshow('License Plate Recognition', frame)

    # Detect and recognize plates
    plate_number, croped_img, img = plateRecognize(frame)
    
    # plate number min 7 max 8 characters
    if len(plate_number) > 6 and len(plate_number) < 9:
        
        # Display the plate number
        print(plate_number)

        # Display the frame
        cv2.imshow('License Plate Recognition', croped_img)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# https://github.com/EdaNurKaramuk/PlakaTanimaSistemi/blob/master/PlateRecognitionAlgorithm.py

import cv2 # pip install opencv-python
import imutils # pip install imutils
import numpy as np # pip install numpy
import pytesseract # pip install pytesseract
import re


def plateRecognize(imgparam):

    img = imgparam
    
    # Resize the frame to speed up the detection process and improve accuracy
    img = cv2.resize(img, (620,480))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 13, 15, 15)

    # canny edge detection algorithm
    cany = cv2.Canny(gray, 30, 200)
    
    # get contours
    contours = cv2.findContours(cany.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    # get the largest 10 contours
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None

    for c in contours: # -> https://stackoverflow.com/questions/62274412/cv2-approxpolydp-cv2-arclength-how-these-works

        _ = cv2.arcLength(c, True)
        #https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#ga8d26483c636be6b35c3ec6335798a47c
        approx = cv2.approxPolyDP(c, 0.018 * _, True)

        # get the contour with 4 corners
        if len(approx) == 4:
            screenCnt = approx
            break

    # screenCnt is none or zero
    if screenCnt is None:
        detected = 0
    else:
        detected = 1

    resultPlateText = ""
    Cropped = None
    
    if detected == 1:
        cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3) # Kontür çizilir.

        # mask palate
        mask = np.zeros(gray.shape,np.uint8)
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(img,img,mask=mask)
        (x, y) = np.where(mask == 255)

        # crop the plate 
        (tx, ty) = (np.min(x), np.min(y))
        (bx, by) = (np.max(x), np.max(y))
        Cropped = gray[tx:bx+1, ty:by+1] 
        
        # Read the plate number
        custom_config = r'-l eng --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        text = pytesseract.image_to_string(Cropped, config=custom_config)

        # clean the text
        plateNoFix = text.replace("\n","")
        plateNoFix2 = plateNoFix.replace("\f", "")
        plateNoFix3 = plateNoFix2.strip("#")
        resultPlateText = re.sub('[()"{}<>!-]', '', plateNoFix3)

        # Draw the plate number
        img = cv2.resize(img,(500,300))
        
        # Croped the plate number
        Cropped = cv2.resize(Cropped,(200,70))

    return resultPlateText, Cropped, img
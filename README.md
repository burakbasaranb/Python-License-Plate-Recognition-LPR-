# Python License Plate Recognition (LPR)

This Python project aims to recognize license plates from images or live camera feeds using computer vision techniques. The system utilizes the Tesseract OCR engine for text recognition and OpenCV for image processing tasks.

## Installation

### 1. Install Python

Make sure you have Python installed on your system. You can download and install Python from the official Python website. This project is compatible with Python 3.x.
 
### 2. Install Tesseract OCR

Download and install Tesseract OCR from the official GitHub repository. Tesseract is an open-source OCR engine maintained by Google. Follow the installation instructions provided for your operating system.

After installing Tesseract, you need to define the path to the Tesseract executable in your Python code. Modify the following line in your code to reflect the correct path:

https://github.com/UB-Mannheim/tesseract/wiki

```
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different
```
Replace 'C:/Program Files/Tesseract-OCR/tesseract.exe' with the path to the Tesseract executable on your system.

### 3. Install Python Dependencies

Install the required Python packages using pip, the Python package manager. Navigate to the root directory of your project and execute the following command:

```
pip install -r requirements.txt
```

This command will install all the necessary dependencies listed in the requirements.txt file.

### Usage

1. Clone or download this repository to your local machine.
2. Place images containing license plates in the plates_img folder within the project directory.
3. Run the lpr.py script to start the License Plate Recognition system for images.

```
python lpr.py
```
4. Run the lpr_camera.py script to start the License Plate Recognition system for camera.
```
python lpr_camera.py
``` 

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License

This project is licensed under the MIT License.
import cv2


import pytesseract


print(pytesseract.image_to_string(cv2.imread('/home/annaniks/Desktop/OpenCV_3_License_Plate_Recognition_Python/LicPlateImages/1.png')))

# # French text image to string
# print(pytesseract.image_to_string(Image.open('/home/annaniks/Desktop/OpenCV_3_License_Plate_Recognition_Python/LicPlateImages/vano4.jpg'), lang='fra'))
#
# # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# # NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('/home/annaniks/Desktop/OpenCV_3_License_Plate_Recognition_Python/LicPlateImages/vano4.jpg'))
#
# # Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('/home/annaniks/Desktop/OpenCV_3_License_Plate_Recognition_Python/LicPlateImages/vano4.jpg'))

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('/home/annaniks/Desktop/OpenCV_3_License_Plate_Recognition_Python/LicPlateImages/vano4.jpg')))
#
# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('/home/annaniks/Desktop/OpenCV_3_License_Plate_Recognition_Python/LicPlateImages/vano4.jpg')))
#
# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('/home/annaniks/Desktop/OpenCV_3_License_Plate_Recognition_Python/LicPlateImages/vano4.jpg')))
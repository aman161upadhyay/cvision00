import cv2

image = cv2.imread('batman.jpeg')

while True:
    cv2.imshow('Application', image)

    text = "The Dark Knight"
    cv2.putText(image, text, (5,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 1)

    cv2.rectangle(image, (50, 50), (500, 500), (0, 0, 255), 2)

    cv2.imshow('output_batman.jpg', image)

    key= cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
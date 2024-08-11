import cv2
import numpy as np

def regularize_shape(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regularized_images = []
    canvas_size = (200, 200)  

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        regularized_img = np.zeros((canvas_size[1], canvas_size[0], 3), dtype=np.uint8)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            cropped = image[y:y+h, x:x+w]
            cropped_size = (w, h)
            resized = cv2.resize(cropped, canvas_size, interpolation=cv2.INTER_AREA)
            regularized_img[:resized.shape[1], :resized.shape[0]] = resized
        elif len(contour) >= 5:
            if len(approx) > 5:
                ellipse = cv2.fitEllipse(contour)
                center, axes, _ = ellipse
                major_axis, minor_axis = axes
                x, y = int(center[0]), int(center[1])
                cropped = image[int(y-minor_axis/2):int(y+minor_axis/2), int(x-major_axis/2):int(x+major_axis/2)]
                cropped_size = (major_axis, minor_axis)
                resized = cv2.resize(cropped, canvas_size, interpolation=cv2.INTER_AREA)
                regularized_img[:resized.shape[1], :resized.shape[0]] = resized

        regularized_images.append(regularized_img)

    return regularized_images

def classify_and_regularize_shape(image_path):
    image = cv2.imread(image_path)
    regularized_images = regularize_shape(image)

    for i, reg_img in enumerate(regularized_images):
        cv2.imshow(f'Regularized Shape {i+1}', reg_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'solution\\rec.png'
classify_and_regularize_shape(image_path)

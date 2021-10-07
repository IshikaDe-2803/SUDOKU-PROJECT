from ip2 import transformed
import cv2 as cv
import numpy as np
import operator
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, MaxPool2D
from keras import backend as K
import matplotlib.pyplot as plt


# image_url = ".\sudoku_3.jpg"
# image_url2 = ".\sudoku-puzzle-games.jpg"


# def image_processing(img2, dilation=True):
#     img = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#     gauss_img = cv.GaussianBlur(img.copy(), (9, 9), 0)
#     threshold_img = cv.adaptiveThreshold(
#         gauss_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
#     invert_color_img = cv.bitwise_not(threshold_img, threshold_img)
#     if dilation:
#         kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
#         return cv.dilate(invert_color_img, kernel)
#     return invert_color_img


def display_img(img):
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# def find_largest_contour(img):
#     external_contours = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     external_contours = external_contours[0] if len(external_contours) == 2 else external_contours[1]
#     external_contours = sorted(external_contours, key=cv.contourArea, reverse=True)
#     return external_contours


# """
# Ramer Doughlas Peucker algorithm:
# We will use max(list, key) for the right side corners as there x-value is greater. Likewise, we will use min(list, key) for the left side corners.
# operator is a built-in module providing a set of convenient operators. In two words operator.itemgetter(n) constructs a callable that assumes an iterable object (e.g. list, tuple, set) as input, and fetches the n-th element out of it.
# """


# def find_corners(polygon):
#     # bottom_right, _ = max(enumerate([point[0][0] + point[0][1] for point in
#     #                                  polygon]), key=operator.itemgetter(1))
#     # top_left, _ = min(enumerate([point[0][0] + point[0][1] for point in
#     #                              polygon]), key=operator.itemgetter(1))
#     # bottom_left, _ = min(enumerate([point[0][0] - point[0][1] for point in
#     #                                 polygon]), key=operator.itemgetter(1))
#     # top_right, _ = max(enumerate([point[0][0] - point[0][1] for point in
#     #                               polygon]), key=operator.itemgetter(1))
#     # all_contours = [polygon[top_left][0], polygon[top_right]
#     #                 [0], polygon[bottom_right][0], polygon[bottom_left][0]]
#     # return all_contours
#     for c in polygon:
#         peri = cv.arcLength(c, True)
#         # cv2.approxPolyDP(curve, epsilon, closed[, approxCurve])
#         # Curve-> hers is the largest contour
#         # epsilon -> Parameter specifying the approximation accuracy. This is the maximum distance between the original curve and its approximation.
#         # closed – If true, the approximated curve is closed. Otherwise, it is not closed.
#         # approxPolyDP returns the approximate curve in the same type as the input curve
#         approx = cv.approxPolyDP(c, 0.015 * peri, True)
#         if len(approx) == 4:
#             # Here we are looking for the largest 4 sided contour
#             return approx


# def order_corner_points(corners):
#     # Corners[0],... stores in format [[x y]]
#     # Separate corners into individual points
#     # Index 0 - top-right
#     #       1 - top-left
#     #       2 - bottom-left
#     #       3 - bottom-right
#     corners = [(corner[0][0], corner[0][1]) for corner in corners]
#     top_r, top_l, bottom_l, bottom_r = corners[0], corners[1], corners[2], corners[3]
#     return top_l, top_r, bottom_r, bottom_l

# # Crop the image
# def perspective_transform(image, corners):
#     # Order points in clockwise order
#     ordered_corners = order_corner_points(corners)
#     top_l, top_r, bottom_r, bottom_l = ordered_corners

#     # Determine width of new image which is the max distance between
#     # (bottom right and bottom left) or (top right and top left) x-coordinates
#     width_A = np.sqrt(((bottom_r[0] - bottom_l[0]) ** 2) + ((bottom_r[1] - bottom_l[1]) ** 2))
#     width_B = np.sqrt(((top_r[0] - top_l[0]) ** 2) + ((top_r[1] - top_l[1]) ** 2))
#     width = max(int(width_A), int(width_B))

#     # Determine height of new image which is the max distance between
#     # (top right and bottom right) or (top left and bottom left) y-coordinates
#     height_A = np.sqrt(((top_r[0] - bottom_r[0]) ** 2) + ((top_r[1] - bottom_r[1]) ** 2))
#     height_B = np.sqrt(((top_l[0] - bottom_l[0]) ** 2) + ((top_l[1] - bottom_l[1]) ** 2))
#     height = max(int(height_A), int(height_B))

#     # Construct new points to obtain top-down view of image in
#     # top_r, top_l, bottom_l, bottom_r order
#     dimensions = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1],
#                            [0, height - 1]], dtype="float32")

#     # Convert to Numpy format
#     ordered_corners = np.array(ordered_corners, dtype="float32")

#     # calculate the perspective transform matrix and warp
#     # the perspective to grab the screen
#     grid = cv.getPerspectiveTransform(ordered_corners, dimensions)

#     # Return the transformed image
#     return cv.warpPerspective(image, grid, (width, height))

# def distance_between(point1, point2):
#     a = point2[0] - point1[0]
#     b = point2[1] - point1[1]
#     return np.sqrt((a ** 2) + (b ** 2))


# def crop_and_warp(img, all_contours):
#     top_left, top_right, bottom_right, bottom_left = all_contours[
#         0], all_contours[1], all_contours[2], all_contours[3]
#     # Explicitly set the data type to float32 or `getPerspectiveTransform` will throw an error
#     src = np.array([top_left, top_right, bottom_right,
#                    bottom_left], dtype='float32')
#     side = max([distance_between(bottom_right, top_right), distance_between(top_left, bottom_left),
#                distance_between(bottom_right, bottom_left), distance_between(top_left, top_right)])
#     # Describe a square with side of the calculated length, this is the new perspective we want to warp to
#     square_length = np.array(
#         [[0, 0], [side - 1, 0], [side - 1, side - 1], [0, side - 1]], dtype='float32')
#     # Gets the transformation matrix for skewing the image to fit a square by comparing the 4 before and after points
#     matrix = cv.getPerspectiveTransform(src, square_length)
#     # Performs the transformation on the original image
#     return cv.warpPerspective(img, matrix, (int(side), int(side)))


def create_image_grid(img):
    grid = np.copy(img)
    # not all sudoku out there have same width and height in the small squares so we need to consider differnt heights and width
    edge_h = np.shape(grid)[0]
    edge_w = np.shape(grid)[1]
    celledge_h = edge_h // 9
    celledge_w = np.shape(grid)[1] // 9

    # grid = cv.cvtColor(grid, cv.COLOR_BGR2GRAY)

    # Adaptive thresholding the cropped grid and inverting it
    # grid = cv.bitwise_not(cv.adaptiveThreshold(grid, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 101, 1))
    display_img(grid)

    tempgrid = []
    for i in range(celledge_h, edge_h + 1, celledge_h):
        for j in range(celledge_w, edge_w + 1, celledge_w):
            rows = grid[i - celledge_h:i]
            tempgrid.append([rows[k][j - celledge_w:j]
                            for k in range(len(rows))])

    # Creating the 9X9 grid of images
    finalgrid = []
    for i in range(0, len(tempgrid) - 8, 9):
        finalgrid.append(tempgrid[i:i + 9])

    # Converting all the cell images to np.array
    for i in range(9):
        for j in range(9):
            finalgrid[i][j] = np.array(finalgrid[i][j])

    try:
        for i in range(9):
            for j in range(9):
                np.os.remove("BoardCells1/cell" + str(i) + str(j) + ".jpg")
    except:
        pass
    for i in range(9):
        for j in range(9):
            cv.imwrite(str("BoardCells1/cell" + str(i) +
                       str(j) + ".jpg"), finalgrid[i][j])

    return finalgrid


"""Keras requires you to set the input_shape of the network. This is the shape of a single instance of your data which would be (28,28). However, Keras also needs a channel dimension thus the input shape for the MNIST dataset would be (28,28,1).
Colored images typically have three channels, for the pixel value at the (row, column) coordinate for the red, green, and blue components.
Deep learning neural networks require that image data be provided as three-dimensional arrays.
This applies even if your image is grayscale. In this case, the additional dimension for the single color channel must be added."""

"""x_train: uint8 NumPy array of grayscale image data with shapes (60000, 28, 28), containing the training data. Pixel values range from 0 to 255.
y_train: uint8 NumPy array of digit labels (integers in range 0-9) with shape (60000,) for the training data.
x_test: uint8 NumPy array of grayscale image data with shapes (10000, 28, 28), containing the test data. Pixel values range from 0 to 255.
y_test: uint8 NumPy array of digit labels (integers in range 0-9) with shape (10000,) for the test data."""


def preprocess_training_data():

    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()

    # Reshape to be samples*pixels*width*height
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')

    # One hot Cpde
    Y_train = np_utils.to_categorical(Y_train)
    Y_test = np_utils.to_categorical(Y_test)

    # convert from integers to floats
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    # normalize to range [0, 1]
    X_train = (X_train / 255.0)
    X_test = (X_test / 255.0)

    return X_test, Y_test, X_train, Y_train


def create_CNN_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu',
              kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu',
              kernel_initializer='he_uniform'))
    model.add(Conv2D(64, (3, 3), activation='relu',
              kernel_initializer='he_uniform'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(10, activation='softmax'))
    # print(model.summary())

    # compile model
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    X_test, Y_test, X_train, Y_train = preprocess_training_data()
    model.fit(X_train, Y_train, validation_data=(
        X_test, Y_test), epochs=10, batch_size=200)
    model.save("model1.h5")
    return model

# def scale_and_centre(img, size, margin=20, background=0):
#     """Scales and centres an image onto a new background square."""
#     h, w = img.shape[:2]

#     def centre_pad(length):
#         """Handles centering for a given length that may be odd or even."""
#         if length % 2 == 0:
#             side1 = int((size - length) / 2)
#             side2 = side1
#         else:
#             side1 = int((size - length) / 2)
#             side2 = side1 + 1
#         return side1, side2

#     def scale(r, x):
#         return int(r * x)

#     if h > w:
#         t_pad = int(margin / 2)
#         b_pad = t_pad
#         ratio = (size - margin) / h
#         w, h = scale(ratio, w), scale(ratio, h)
#         l_pad, r_pad = centre_pad(w)
#     else:
#         l_pad = int(margin / 2)
#         r_pad = l_pad
#         ratio = (size - margin) / w
#         w, h = scale(ratio, w), scale(ratio, h)
#         t_pad, b_pad = centre_pad(h)

#     img = cv.resize(img, (w, h))
#     img = cv.copyMakeBorder(img, t_pad, b_pad, l_pad, r_pad, cv.BORDER_CONSTANT, None, background)
#     return cv.resize(img, (size, size))

# def extract_digits(img_grid):
#     sudoku = [[0 for i in range(9)] for j in range(9)]

#     for i in range(9):
#         for j in range(9):
#             image = img_grid[i][j]
#             image = cv.resize(image, (28, 28))
#             thresh = 128
#             # original = image.copy()

#             gray = cv.threshold(image, thresh, 255, cv.THRESH_BINARY)[1]

#             # Find contours
#             cnts = cv.findContours(
#                 gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#             cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#             #cnts = sorted(cnts, key=cv.contourArea)
#             #cnts = cnts[0]
#             for c in cnts:
#                 x, y, w, h = cv.boundingRect(c)

#                 if (x < 3 or y < 3 or h < 3 or w < 3):
#                     # Note the number is always placed in the center
#                     # Since image is 28x28
#                     # the number will be in the center thus x >3 and y>3
#                     # Additionally any of the external lines of the sudoku will not be thicker than 3
#                     continue
#                 ROI = gray[y:y + h, x:x + w]
#                 # display_img(ROI)
#                 ROI = scale_and_centre(ROI, 120)
#                 # Writing the cleaned cells
#                 # cv.imwrite("CleanedBoardCells/cell{}{}.png".format(i, j), ROI)
#                 sudoku[i][j] = predict(ROI)

#     return sudoku


def predict(img_grid):
    image = img_grid.copy()
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)[1]
    image = cv.resize(image, (28, 28))
    # display_image(image)
    image = image.astype('float32')
    image = image.reshape(1, 28, 28, 1)
    image /= 255
    model = load_model('model1.h5')
    pred = model.predict(image.reshape(1, 28, 28, 1), batch_size=1)
    return pred.argmax()


def guess(cells):
    grid = []
    for i in range(9):
        for j in range(9):
            contours, hierarchy = cv.findContours(
                image=cells[i][j], mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
            if len(contours) != 2:
                p = predict(cells[i][j])
                grid.append(p)
            else:
                grid.append(0)
            # if p == 2:
            #     grid.append(0)
            # else:
            #     grid.append(p)
    print(grid)
# display_img(image_processing(image_url))
# img = cv.imread(image_url)
# process_img = image_processing(img)


# model = create_CNN_model()
# corners = find_corners(find_largest_contour(process_img))
# img_cropped = perspective_transform(img, corners)
# transformed = cv.resize(img_cropped, (450, 450))
cells = create_image_grid(transformed)
# test = cells[4][4]
# test1 = cells[4][1]
# display_img(test)
# contours, hierarchy = cv.findContours(
#     image=cells[4][4], mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
# print(len(contours))
# contours1, hierarchy1 = cv.findContours(
#     image=cells[4][1], mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
# print(len(contours1))
# display_img(test1)
# print(test is None)
# display_img(cells[0][0])
guess(cells)
# contours = find_corners(find_largest_contour(img))
# img_cropped = crop_and_warp(img, contours)
# cells = create_image_grid(img_cropped)

# print(extract_digits(cells))
# all_squares = infer_grid(img_cropped)
# display_img(img_cropped)

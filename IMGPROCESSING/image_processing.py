import numpy as np
import cv2
import operator
import numpy as np
IMAGE_URL = "./sudoku_1.jpg"
SUDOKU_SIZE = 9


def display_image(img):
    cv2.imshow('Sudoku', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


def preprocess(img, skip_dilate=False):
    blur_img = cv2.GaussianBlur(img.copy(), (9, 9), 0)
    threshold_img = cv2.adaptiveThreshold(
        blur_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    processed_img = cv2.bitwise_not(threshold_img, threshold_img)
    if not skip_dilate:
        kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
        processed_img = cv2.dilate(processed_img, kernel)
    return processed_img


def find_corners_of_largest_polygon(img):
    contours, hierarchy = cv2.findContours(
        img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours
    contours = sorted(contours, key=cv2.contourArea,
                      reverse=True)  # Sort by area, descending
    largest_polygon = contours[0]
    bottom_right = max(enumerate([point[0][0] + point[0][1]
                       for point in largest_polygon]), key=operator.itemgetter(1))[0]
    top_left = min(enumerate([point[0][0] + point[0][1]
                   for point in largest_polygon]), key=operator.itemgetter(1))[0]
    bottom_left = min(enumerate([point[0][0] - point[0][1]
                      for point in largest_polygon]), key=operator.itemgetter(1))[0]
    top_right = max(enumerate([point[0][0] - point[0][1]
                    for point in largest_polygon]), key=operator.itemgetter(1))[0]
    return [largest_polygon[top_left][0], largest_polygon[top_right][0], largest_polygon[bottom_right][0], largest_polygon[bottom_left][0]]


def distance(point1, point2):
    a = point2[0] - point1[0]
    b = point2[1] - point1[1]
    return np.sqrt((a ** 2) + (b ** 2))


def crop_and_warp(img, corners):
    top_left, top_right, bottom_right, bottom_left = corners[0], corners[1], corners[2], corners[3]
    img_float32 = np.array(
        [top_left, top_right, bottom_right, bottom_left], dtype='float32')
    side_length = max([distance(bottom_right, top_right),
                       distance(top_left, bottom_left),
                       distance(bottom_right, bottom_left),
                       distance(top_left, top_right)])
    new_perspective = np.array([[0, 0], [side_length - 1, 0], [side_length - 1,
                               side_length - 1], [0, side_length - 1]], dtype='float32')
    transformed_img = cv2.getPerspectiveTransform(img_float32, new_perspective)
    return cv2.warpPerspective(img, transformed_img, (int(side_length), int(side_length)))


def all_cell_coordinates(img):
    squares = []
    side = img.shape[:1]
    side = side[0] / SUDOKU_SIZE
    for j in range(SUDOKU_SIZE):
        for i in range(SUDOKU_SIZE):
            p1 = (i * side, j * side)
            p2 = ((i + 1) * side, (j + 1) * side)
            squares.append((p1, p2))
    return squares


def get_digit_cell(img, cell):
    return img[int(cell[0][1]):int(cell[1][1]), int(cell[0][0]):int(cell[1][0])]


"""DIDNT UNDERSTAND"""


def find_largest_feature(inp_img, scan_tl=None, scan_br=None):
    """
    Uses the fact the `floodFill` function returns a bounding box of the area it filled to find the biggest
    connected pixel structure in the image. Fills this structure in white, reducing the rest to black.
    """
    img = inp_img.copy()  # Copy the image, leaving the original untouched
    height, width = img.shape[:2]

    max_area = 0
    seed_point = (None, None)

    if scan_tl is None:
        scan_tl = [0, 0]

    if scan_br is None:
        scan_br = [width, height]

    # Loop through the image
    for x in range(scan_tl[0], scan_br[0]):
        for y in range(scan_tl[1], scan_br[1]):
            # Only operate on light or white squares
            # Note that .item() appears to take input as y, x
            if img.item(y, x) == 255 and x < width and y < height:
                area = cv2.floodFill(img, None, (x, y), 64)
                if area[0] > max_area:  # Gets the maximum bound area which should be the grid
                    max_area = area[0]
                    seed_point = (x, y)

    # Colour everything grey (compensates for features outside of our middle scanning range
    for x in range(width):
        for y in range(height):
            if img.item(y, x) == 255 and x < width and y < height:
                cv2.floodFill(img, None, (x, y), 64)

    # Mask that is 2 pixels bigger than the image
    mask = np.zeros((height + 2, width + 2), np.uint8)

    # Highlight the main feature
    if all([p is not None for p in seed_point]):
        cv2.floodFill(img, mask, seed_point, 255)

    top, bottom, left, right = height, 0, width, 0

    for x in range(width):
        for y in range(height):
            if img.item(y, x) == 64:  # Hide anything that isn't the main feature
                cv2.floodFill(img, mask, (x, y), 0)

            # Find the bounding parameters
            if img.item(y, x) == 255:
                top = y if y < top else top
                bottom = y if y > bottom else bottom
                left = x if x < left else left
                right = x if x > right else right

    bbox = [[left, top], [right, bottom]]
    return img, np.array(bbox, dtype='float32'), seed_point


def scale_and_centre(img, size, margin=0, background=0):
    """Scales and centres an image onto a new background square."""
    h, w = img.shape[:2]

    def centre_pad(length):
        """Handles centering for a given length that may be odd or even."""
        if length % 2 == 0:
            side1 = int((size - length) / 2)
            side2 = side1
        else:
            side1 = int((size - length) / 2)
            side2 = side1 + 1
        return side1, side2

    def scale(r, x):
        return int(r * x)

    if h > w:
        t_pad = int(margin / 2)
        b_pad = t_pad
        ratio = (size - margin) / h
        w, h = scale(ratio, w), scale(ratio, h)
        l_pad, r_pad = centre_pad(w)
    else:
        l_pad = int(margin / 2)
        r_pad = l_pad
        ratio = (size - margin) / w
        w, h = scale(ratio, w), scale(ratio, h)
        t_pad, b_pad = centre_pad(h)

    img = cv2.resize(img, (w, h))
    img = cv2.copyMakeBorder(img, t_pad, b_pad, l_pad,
                             r_pad, cv2.BORDER_CONSTANT, None, background)
    return cv2.resize(img, (size, size))


def extract_digit(img, cell, size):
    """Extracts a digit (if one exists) from a Sudoku square."""

    # Get the digit box from the whole square
    digit = get_digit_cell(img, cell)

    # Use fill feature finding to get the largest feature in middle of the box
    # Margin used to define an area in the middle we would expect to find a pixel belonging to the digit
    height, width = digit.shape[:2]
    margin = int(np.mean([height, width]) / 2.5)  # NO IDEA WHY DIV BY 2.5
    _, bbox, seed = find_largest_feature(
        digit, [margin, margin], [width - margin, height - margin])
    digit = get_digit_cell(digit, bbox)

    # Scale and pad the digit so that it fits a square of the digit size we're using for machine learning
    width = bbox[1][0] - bbox[0][0]
    height = bbox[1][1] - bbox[0][1]

    # Ignore any small bounding boxes
    if width > 0 and height > 0 and (width * height) > 100 and len(digit) > 0:
        return scale_and_centre(digit, size, 4)
    else:
        return np.zeros((size, size), np.uint8)


def get_digits(img, cell_coordinates, size):
    digits = []
    img = preprocess(img.copy(), skip_dilate=True)
    for cell in cell_coordinates:
        digits.append(extract_digit(img, cell, size))
    return digits


def show_digits(digits, colour=255):
    grid = []
    with_border = [cv2.copyMakeBorder(
        img.copy(), 1, 1, 1, 1, cv2.BORDER_CONSTANT, None, colour) for img in digits]
    for i in range(SUDOKU_SIZE):
        row = np.concatenate(
            with_border[i * SUDOKU_SIZE:((i + 1) * SUDOKU_SIZE)], axis=1)
        grid.append(row)
    img = display_image(np.concatenate(grid))
    return img


def extract_sudoku(path):
    original_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    display_image(original_img)
    processed_img = preprocess(original_img)
    corners = find_corners_of_largest_polygon(processed_img)
    cropped = crop_and_warp(original_img, corners)
    cell_coordinates = all_cell_coordinates(cropped)
    digits = get_digits(cropped, cell_coordinates, 28)
    final_image = show_digits(digits)
    return final_image


transformed = extract_sudoku(IMAGE_URL)

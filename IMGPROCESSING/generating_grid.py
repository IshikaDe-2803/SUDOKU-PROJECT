from image_processing import transformed
import cv2 as cv
import numpy as np
from keras.models import load_model


def display_img(img):
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def create_image_grid(img):
    grid = np.copy(img)
    # not all sudoku out there have same width and height in the small squares so we need to consider differnt heights and width
    grid_height = np.shape(grid)[0]
    grid_width = np.shape(grid)[1]
    cell_height = grid_height // 9
    cell_width = np.shape(grid)[1] // 9

    temp_grid = []
    for i in range(cell_height, grid_height + 1, cell_height):
        for j in range(cell_width, grid_width + 1, cell_width):
            rows = grid[i - cell_height:i]
            temp_grid.append([rows[k][j - cell_width:j]
                              for k in range(len(rows))])

    # Creating the 9X9 grid of images
    finalgrid = []
    for i in range(0, len(temp_grid) - 8, 9):
        finalgrid.append(temp_grid[i:i + 9])

    # Converting all the cell images to np.array
    for i in range(9):
        for j in range(9):
            finalgrid[i][j] = np.array(finalgrid[i][j])
    display_img(finalgrid[0][4])
    return finalgrid


def predict(cell_img):
    cell_img = cv.resize(cell_img, (28, 28))
    cell_img = cell_img.astype('float32')
    cell_img = cell_img.reshape(1, 28, 28, 1)
    cell_img /= 255
    model = load_model('model1.h5')
    pred = model.predict(cell_img.reshape(1, 28, 28, 1), batch_size=1)
    return pred.argmax()


def generate_sudoku_grid(cells):
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            contours, hierarchy = cv.findContours(
                image=cells[i][j], mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
            if len(contours) != 2:
                digit = predict(cells[i][j])
                row.append(digit)
            else:
                row.append(0)
        grid.append(row)
    return grid


cells = create_image_grid(transformed)
sudoku_puzzle = generate_sudoku_grid(cells)

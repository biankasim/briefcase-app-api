from PIL import Image
from colorthief import ColorThief
import webcolors
import statistics
from scipy.spatial import distance
import numpy as np

def get_color_name(rgb_color):
    try:
        closest_name = webcolors.rgb_to_name(rgb_color)
        return closest_name
    except ValueError:
        closest_color_name = find_closest_color(rgb_color)
        return closest_color_name
        
def find_closest_color(rgb_color):

    all_color_names = list(webcolors.HTML4_NAMES_TO_HEX)
    
    #calculate the Euclidean distances between the given color and all named colors
    distances = [distance.euclidean(rgb_color, webcolors.name_to_rgb(name)) for name in all_color_names]
    closest_color_index = np.argmin(distances)
    
    closest_color_name = all_color_names[closest_color_index]
    return closest_color_name

def get_average_color(image_path):
    #open and find middle pixel of image
    img = Image.open(image_path)
    width, height = img.size
    center_x, center_y = width // 2, height // 2

    #define the region around the middle pixel
    left = max(0, center_x - 50)
    upper = max(0, center_y - 50)
    right = min(width - 1, center_x + 50)
    lower = min(height - 1, center_y + 50)

    #extract RGB values of the pixels in the specified region
    pixels = list(img.crop((left, upper, right, lower)).getdata())

    #calculate the average RGB values
    average_color = (
        sum([pixel[0] for pixel in pixels]) // len(pixels),
        sum([pixel[1] for pixel in pixels]) // len(pixels),
        sum([pixel[2] for pixel in pixels]) // len(pixels)
    )

    return average_color
    

def get_mode_color(image_path):
    #open and find middle pixel of image
    img = Image.open(image_path)
    width, height = img.size
    center_x, center_y = width // 2, height // 2

    #define the region around the middle pixel
    left = max(0, center_x - 100)
    upper = max(0, center_y - 100)
    right = min(width - 1, center_x + 100)
    lower = min(height - 1, center_y + 100)

    #extract RGB values of the pixels in the specified region
    pixels = list(img.crop((left, upper, right, lower)).getdata())

    #calculate the mode RGB values
    mode_color = (
        int(statistics.mode([pixel[0] for pixel in pixels])),
        int(statistics.mode([pixel[1] for pixel in pixels])),
        int(statistics.mode([pixel[2] for pixel in pixels]))
    )

    return mode_color


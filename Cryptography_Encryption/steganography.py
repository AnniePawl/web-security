"""
Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# Secret image hidden in LSB of red channel pixels. Value of LSB of each red pixel is 1 if hidden image was 1 at that location, and 0 if hidden image was also 0 

# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image

def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
   
    # Iterate thru each pixel in encoded image, set decoded_image pixel to either (0,0,0) or (255,255,255) depending on value of LSB. 
    # Think of image like matrix, double for loop
    for i in range(0,x_size):
      for j in range(0,y_size):
        if pixels


    # for i in range(0, x_size):
    #   for j in range(0,y_size):
    #     only check red channel ([0])
    #     if pixels[i,j][red_channel] % 2 == 0:
    #       pixels[i,j] = (0,0,0) 
    #     else:
    #       pixels[i,j] = (255,255,255)

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

if __name__ == "__main__":
  decode_image('encoded_image.png')

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os.path

# example -> C:\Users\xyz\OneDrive\Desktop\project\image.jpg
img_path = input("Enter the path here: ")
img = Image.open(img_path)

# convert our image into a numpy array
img = np.asarray(img)
# print(img.shape)
# put pixels in a 1D array by flattening out img array
flat = img.flatten()

# create our own histogram function


def get_histogram(image, bins):
    # array with size of bins, set to zeros
    histogram = np.zeros(bins)

    # loop through pixels and sum up counts of pixels
    for pixel in image:
        histogram[pixel] += 1

    # return our final result
    return histogram


# execute our histogram function
hist = get_histogram(flat, 256)

# execute the fn
cumulative_sum = np.cumsum(hist)

# numerator & denomenator
normalized_intensity = (cumulative_sum - cumulative_sum.min()) * 255
N = cumulative_sum.max() - cumulative_sum.min()

# re-normalize the cumsum
cumulative_sum = normalized_intensity / N

# cast it back to uint8 since we can't use floating point values in images
cumulative_sum = cumulative_sum.astype('uint8')

# get the value from cumulative sum for every index in flat, and set that as img_new
img_new = cumulative_sum[flat]

# put array back into original shape since we flattened it
img_new = np.reshape(img_new, img.shape)

# set up side-by-side image display
fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

# display the real image
fig.add_subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Image 'Before' Contrast Adjustment")

# display the new image
fig.add_subplot(1, 2, 2)
plt.imshow(img_new, cmap='gray')
plt.title("Image 'After' Contrast Adjustment")
filename = os.path.basename(img_path)

plt.savefig("./Image Contrast Adjusting Filter/(Contrast Adjusted)"+filename)

plt.show()

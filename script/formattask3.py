import cv2
import numpy as np
from skimage import filters
from scipy.ndimage import binary_fill_holes
import matplotlib.pyplot as plt

# Read original image
I = cv2.imread(r"C:\Users\UMAR.TECH\Downloads\Format3-Task3 (1).png")
I_rgb = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(14, 10))

plt.subplot(4, 4, 1)
plt.imshow(I_rgb)
plt.title('Original image')
plt.axis('off')

# Convert to grayscale
gray_image = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
plt.subplot(4, 4, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('gray image')
plt.axis('off')

# Histogram equalization
hist_eq = cv2.equalizeHist(gray_image)
plt.subplot(4, 4, 3)
plt.imshow(hist_eq, cmap='gray')
plt.title('histogram equalization')
plt.axis('off')

# Canny edge detection
# (fixed: original used the undefined 'binary_image' here; using hist_eq instead)
BW = cv2.Canny(hist_eq, threshold1=50, threshold2=150)
BW = BW.astype(bool)
plt.subplot(4, 4, 4)
plt.imshow(BW, cmap='gray')
plt.title('filtered image')
plt.axis('off')

# Fill holes (equivalent of imfill(BW, 'holes'))
BW2 = binary_fill_holes(BW)
plt.subplot(4, 4, 5)
plt.imshow(BW2, cmap='gray')
plt.title('Filled Image')
plt.axis('off')

# Binarize the histogram-equalized image (equivalent of im2bw)
thresh = filters.threshold_otsu(hist_eq)
BW3 = hist_eq > thresh
plt.subplot(4, 4, 6)
plt.imshow(BW3, cmap='gray')
plt.title('Disease in the image')
plt.axis('off')

BW2_float = BW2.astype(np.float64)
gamma = 25
BW4 = np.power(BW2_float, gamma)

plt.subplot(4, 4, 5)
plt.imshow(BW2, cmap='gray')
plt.title('segment brain tumor')
plt.axis('off')

plt.subplot(4, 4, 7)
plt.imshow(BW4, cmap='gray')
plt.title('segment brain tumor (BW4, corrected)')
plt.axis('off')

plt.tight_layout()
plt.savefig('formattask3_output.png', dpi=150)
plt.show()

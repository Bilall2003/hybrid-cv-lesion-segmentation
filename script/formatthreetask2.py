import cv2
import numpy as np
from skimage import filters
from skimage.morphology import binary_erosion
import matplotlib.pyplot as plt

# Read original image
I = cv2.imread(r"C:\Users\UMAR.TECH\Downloads\Format3-Task2 (1).jpg")
I_rgb = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 10))

plt.subplot(4, 4, 1)
plt.imshow(I_rgb)
plt.title('Original Image')
plt.axis('off')

# Convert to grayscale
gray_image = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
plt.subplot(4, 4, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('')
plt.axis('off')

# Histogram equalization
hist_eq = cv2.equalizeHist(gray_image)
plt.subplot(4, 4, 3)
plt.imshow(hist_eq, cmap='gray')
plt.title('histogram equalization')
plt.axis('off')

# Binarize (equivalent of imbinarize)
thresh = filters.threshold_otsu(hist_eq)
BW = hist_eq > thresh
plt.subplot(4, 4, 4)
plt.imshow(BW, cmap='gray')
plt.title('Original Image Binarized')
plt.axis('off')

# Remove interior pixels, keep only boundary outline (equivalent of bwmorph(BW,'remove'))
eroded = binary_erosion(BW, footprint=np.ones((3, 3)))
BW2 = BW & ~eroded
plt.figure()
plt.imshow(BW2, cmap='gray')
plt.title('BW2 (bwmorph remove equivalent)')
plt.axis('off')

# Perimeter using 8-connectivity (equivalent of bwperim(BW2, 8))
eroded2 = binary_erosion(BW2, footprint=np.ones((3, 3)))
BW3 = BW2 & ~eroded2

# Side-by-side montage comparison (equivalent of imshowpair(BW, BW2, 'montage'))
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(BW, cmap='gray')
axes[0].axis('off')
axes[1].imshow(BW2, cmap='gray')
axes[1].axis('off')
plt.tight_layout()
plt.show()

# Area of segmented leaf pattern (equivalent of bwarea(BW3))
# NOTE: bwarea returns a scalar, not an image, so it cannot be passed to
# imshow (the original .m line "imshow(total)" would error in MATLAB).
# We print the value instead.
total = np.sum(BW3)
print('Area of segmented leaf pattern:', total)

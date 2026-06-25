import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector
from matplotlib.path import Path
from skimage.segmentation import chan_vese
from skimage.measure import label
from skimage.morphology import remove_small_objects, binary_erosion

# Read image and convert to grayscale
I = cv2.cvtColor(cv2.imread(r"C:\Users\UMAR.TECH\Downloads\Format3-Task1 (1).png"), cv2.COLOR_BGR2GRAY)

fig, ax = plt.subplots()
ax.imshow(I, cmap='gray')
ax.set_title('Click points to draw ROI polygon, close it to finish')

# --- Interactive ROI polygon selection (equivalent of roipoly) ---
roi_points = []

def onselect(verts):
    global roi_points
    roi_points = verts

selector = PolygonSelector(ax, onselect)
plt.show()  # user draws polygon interactively, then closes the window

# Build a binary mask from the selected polygon (equivalent of roipoly's output)
mask = np.zeros(I.shape, dtype=bool)
if len(roi_points) > 0:
    path = Path(roi_points)
    y, x = np.mgrid[0:I.shape[0], 0:I.shape[1]]
    points = np.vstack((x.ravel(), y.ravel())).T
    mask = path.contains_points(points).reshape(I.shape)

plt.figure()
plt.subplot(4, 4, 1)
plt.imshow(I, cmap='gray')
plt.axis('off')

plt.subplot(4, 4, 2)
plt.imshow(mask, cmap='gray')
plt.axis('off')

# Active contour segmentation (Chan-Vese), equivalent of:
# bw = activecontour(I, mask, maxIterations, 'Chan-Vese')
maxIterations = 15
I_norm = I.astype(np.float64) / 255.0
bw = chan_vese(I_norm, mu=0.25, lambda1=1, lambda2=1,
                tol=1e-3, max_num_iter=maxIterations,
                dt=0.5, init_level_set=mask.astype(np.float64) - 0.5,
                extended_output=False)

# Connected component labeling (equivalent of bwlabel)
labels = label(bw, connectivity=2)

# id = labels(81,120) in MATLAB -> 0-indexed in Python: row 80, col 119
id_ = labels[80, 119]
tumor = (labels == id_)

plt.subplot(4, 4, 3)
plt.imshow(tumor, cmap='gray')
plt.axis('off')

# Remove small objects smaller than 50 pixels (equivalent of bwareaopen(bw, 50))
arearemoval = remove_small_objects(bw.astype(bool), min_size=50)

# Area of the remaining region (equivalent of bwarea)
area = np.sum(arearemoval)
print('area =', area)

# Perimeter of the region using 8-connectivity (equivalent of bwperim(arearemoval, 8))
eroded = binary_erosion(arearemoval, footprint=np.ones((3, 3)))
BW2 = arearemoval & ~eroded

plt.subplot(4, 4, 4)
plt.imshow(BW2, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.savefig('formatthreetask1_output.png', dpi=150)
plt.show()

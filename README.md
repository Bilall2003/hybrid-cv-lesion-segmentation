#  Digital Image Processing



## Overview

This project covers four fundamental Digital Image Processing (DIP) tasks implemented in MATLAB. Each task demonstrates a core image processing technique — from basic color space manipulation to filtering, histogram analysis, and image blending.

---

## Tasks

### Task 1 — RGB Channel Separation & Recombination

Loads an RGB image and separates it into its individual Red, Green, and Blue channels. Each channel is displayed as a grayscale image to visualize the intensity contribution of that color. The three channels are then recombined to reconstruct the original image.

**Concepts:** Color channel decomposition, `cat()` function for channel merging, MATLAB `subplot` visualization.

---

### Task 2 — Frequency Domain Filtering (FFT-based Low-Pass Filter)

Applies a low-pass filter to an image in the frequency domain using the Fast Fourier Transform (FFT). The image is first converted to grayscale, then transformed to the frequency domain. A circular mask is applied to retain only the low-frequency components (removing high-frequency details/noise), and the result is transformed back using the inverse FFT (IFFT).

**Concepts:** 2D FFT (`fft2`), `fftshift`, frequency domain masking, IFFT (`ifft2`), low-pass filtering, image sharpness vs. smoothness trade-offs.

---

### Task 3 — Histogram Analysis & Equalization

Computes and displays the histogram of a grayscale image to analyze its intensity distribution. Histogram equalization is then applied to enhance image contrast by redistributing pixel intensities more uniformly across the full range.

**Concepts:** `imhist`, `histeq`, contrast enhancement, CDF-based equalization, before/after comparison.

---

### Task 4 — Alpha Blending (Image Blending)

Blends two images together using a weighted alpha value. Both images are resized to a common resolution and converted to `double` for arithmetic operations. The blend formula `alpha * img1 + (1 - alpha) * img2` is applied pixel-wise, and the result is displayed alongside the two originals.

**Concepts:** Alpha compositing, image resizing (`imresize`), type casting (`im2double`, `uint8`), linear interpolation between images.

---

## Requirements

- MATLAB (R2018b or later recommended)
- Image Processing Toolbox

---

## How to Run

1. Open MATLAB and navigate to the project folder.
2. Place your input images in the working directory.
3. Run each task script individually:
   - `task1.m` — RGB channel separation
   - `task2.m` — FFT low-pass filtering
   - `task3.m` — Histogram equalization
   - `task4.m` — Alpha blending
4. Output images and figures will display in MATLAB figure windows.

---

## Key MATLAB Functions Used

| Function | Purpose |
|---|---|
| `imread` / `imshow` | Read and display images |
| `rgb2gray` | Convert RGB to grayscale |
| `fft2` / `ifft2` / `fftshift` | Frequency domain transform |
| `imhist` / `histeq` | Histogram analysis and equalization |
| `imresize` | Resize images to common dimensions |
| `im2double` / `uint8` | Type conversion for arithmetic |
| `subplot` | Display multiple images in one figure |

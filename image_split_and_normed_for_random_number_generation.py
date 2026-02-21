# -*- coding: utf-8 -*-
"""
Improved image split and normalization script
Generates a correlation-based random value from split image halves.
"""

import numpy as np
import cv2
import sys


def safe_normalize(image: np.ndarray) -> np.ndarray:
    """
    Normalize image safely to unit vector.
    Prevents division by zero.
    """
    norm = np.linalg.norm(image)
    if norm == 0:
        raise ValueError("Image norm is zero. Cannot normalize.")
    return image / norm


def split_image(image: np.ndarray):
    """
    Split image vertically into two halves.
    """
    height, width = image.shape[:2]
    width_cutoff = width // 2
    return image[:, :width_cutoff], image[:, width_cutoff:]


def compute_correlation_random_value(img1: np.ndarray, img2: np.ndarray) -> float:
    """
    Compute normalized dot product between two images.
    """
    img1_norm = safe_normalize(img1.astype(np.float64))
    img2_norm = safe_normalize(img2.astype(np.float64))

    correlation = np.sum(img1_norm * img2_norm)

    if correlation == 0:
        raise ValueError("Correlation is zero. Cannot compute inverse.")

    return 100.0 / correlation


def main(image_path: str):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not read image at {image_path}")
        sys.exit(1)

    print(f"Image shape: {img.shape}")

    # Split without re-writing to disk
    left_half, right_half = split_image(img)

    # Compute value
    random_value = compute_correlation_random_value(left_half, right_half)

    print(f"Generated random-like value: {random_value}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_split_and_normed_for_random_number_generation.py <image_path>")
        sys.exit(1)

    main(sys.argv[1])
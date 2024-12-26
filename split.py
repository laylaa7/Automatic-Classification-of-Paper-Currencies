import os
import shutil
from math import ceil
import random

# Paths
input_dir = "data/splitted/"  # Folder with all the resized images
output_dir = "data/split_dataset/"  # Directory to save the split dataset
os.makedirs(output_dir, exist_ok=True)

# Subsets
subsets = ["train", "val", "test"]
ratios = {"train": 0.7, "val": 0.15, "test": 0.15}

# Create subdirectories for each subset
for subset in subsets:
    os.makedirs(os.path.join(output_dir, subset), exist_ok=True)

# Function to split and move images for each class
def split_images(category, images, output_dir):
    random.shuffle(images)  # Shuffle the images for randomness
    
    num_images = len(images)
    train_count = ceil(num_images * ratios["train"])
    val_count = ceil(num_images * ratios["val"])
    test_count = num_images - train_count - val_count

    split_counts = {"train": train_count, "val": val_count, "test": test_count}

    start_idx = 0
    for subset, count in split_counts.items():
        subset_dir = os.path.join(output_dir, subset, category)
        os.makedirs(subset_dir, exist_ok=True)
        for i in range(start_idx, start_idx + count):
            shutil.copy(images[i], os.path.join(subset_dir, os.path.basename(images[i])))
        start_idx += count

# Iterate over each class (category) folder and split its images
for category in os.listdir(input_dir):
    category_path = os.path.join(input_dir, category)
    
    if os.path.isdir(category_path):  # Check if it's a folder
        images = [os.path.join(category_path, f) for f in os.listdir(category_path) if f.endswith((".jpg", ".png", ".jpeg"))]
        split_images(category, images, output_dir)

print("Dataset has been split into train, val, and test subsets!")

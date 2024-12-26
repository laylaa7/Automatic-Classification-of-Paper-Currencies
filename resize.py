import cv2
import os

# Input and output directories
input_dir = "data/raw/"  # Folder containing the original images
output_dir = "data/resized/"  # Folder to save resized images
os.makedirs(output_dir, exist_ok=True)

# Function to resize images
def resize_image(image_path, output_path, size=(255, 255)):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not read {image_path}. Skipping...")
        return

    # Resize the image
    resized_img = cv2.resize(img, size)

    # Save the resized image
    cv2.imwrite(output_path, resized_img)

# Walk through the raw directory and process images
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith((".jpg", ".png", ".jpeg")):  # Ensure valid image file types
            # Full paths for input and output
            input_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_path, input_dir)
            output_path = os.path.join(output_dir, relative_path)

            # Create the output subdirectory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # Resize and save the image
            resize_image(input_path, output_path)

print("All images resized and saved to 'resized/' directory!")

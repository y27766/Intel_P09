import os
import pandas as pd
from PIL import Image

# Function to pixelate an image
def pixelate(image, pixel_size):
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image

# Directory containing original images
image_folder = 'Ferrari'  # Use raw string for Windows paths

# Directory to save pixelated images
pixelated_folder = './Ferrari_pixelated'
os.makedirs(pixelated_folder, exist_ok=True)

# Lists to store image paths and labels for CSV
image_numbers = []
image_paths = []
labels = []

# Process each image in the folder
for i, filename in enumerate(os.listdir(image_folder)):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image
        original_path = os.path.join(image_folder, filename)
        img = Image.open(original_path)

        # Save original image path and label
        image_numbers.append(i)
        image_paths.append(original_path)
        labels.append(1)  # Label 1 for original

        # Pixelate the image
        pixelated_img = pixelate(img, pixel_size=5)

        # Save pixelated image
        pixelated_path = os.path.join(pixelated_folder, f'pixelated_{filename}')
        pixelated_img.save(pixelated_path)

        # Save pixelated image path and label
        image_numbers.append(i)
        image_paths.append(pixelated_path)
        labels.append(0)  # Label 0 for pixelated

# Create DataFrame for CSV
data = pd.DataFrame({
    'image_number': image_numbers,
    'image_path': image_paths,
    'label': labels
})

# Save DataFrame to CSV
csv_file ='../Ferrari_dataset.csv'
data.to_csv(csv_file, index=False)

print(f"Pixelated images and CSV dataset saved to '{csv_file}'.")

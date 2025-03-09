import os
from PIL import Image
import pillow_heif

input_folder = 'C:/Users/river/488/NewDendrites'
output_folder = 'C:/Users/river/488/NewDendrites'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.heic'):
        heic_path = os.path.join(input_folder, filename)
        # Read the HEIC file
        heif_file = pillow_heif.open_heif(heic_path)
        
        # Convert to a Pillow Image
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw"
        )

        # Build the output path (same filename but .jpg extension)
        jpg_filename = os.path.splitext(filename)[0] + '.jpg'
        output_path = os.path.join(output_folder, jpg_filename)

        # Save as JPG
        image.save(output_path, format="JPEG", quality=95)

        print(f"Converted {filename} to {jpg_filename}")
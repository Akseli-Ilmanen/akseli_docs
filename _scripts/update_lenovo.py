import os
import re
import shutil

# Set the path to the source directory containing images
source_directory = r"C:\Users\User\OneDrive\02_Akseli_Vault\Z-Admin\image"
# Set the destination directory for copied images
destination_directory = os.path.join(os.getcwd(), 'images')

# Create the destination directory if it does not exist
os.makedirs(destination_directory, exist_ok=True)

# Regular expression to match Markdown image references
image_reference_pattern = r'!\[\[([^]]+)\]\]'

# Get a list of all Markdown files in the current directory
markdown_files = [f for f in os.listdir('.') if f.endswith('.md')]

# Iterate through each Markdown file
for md_file in markdown_files:
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Find all image references
        image_matches = re.findall(image_reference_pattern, content)
        
        # Copy each referenced image to the destination directory
        for image_name in image_matches:
            image_path = os.path.join(source_directory, image_name)
            if os.path.isfile(image_path):
                # Copy the image to the destination folder
                shutil.copy(image_path, destination_directory)
                print(f"Copied: {image_name} to {destination_directory}")
                
                # Update the Markdown reference to point to the new location
                new_reference = f"![[images/{image_name}]]"
                content = content.replace(f"![[{image_name}]]", new_reference)
            else:
                print(f"Image not found: {image_path}")
    
    # Write the modified content back to the original Markdown file
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(content)

print("Image extraction and Markdown update complete.")

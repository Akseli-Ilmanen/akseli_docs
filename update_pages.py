import os
import re
import shutil

# Set the path to the source directory containing images
# Get the current working directory
curr_directory = os.getcwd()
print("Current Directory:", curr_directory)

# Navigate two levels up
two_levels_up = os.path.abspath(os.path.join(curr_directory, "../../"))

source_directory = os.path.join(two_levels_up, 'Z-Admin', 'image')


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

            else:
                print(f"Image not found: {image_path}")
    


print("Image extraction complete.")


# Set the source and destination directories
source_directory2 = os.getcwd()
destination_directory = os.path.join(source_directory2, 'md_changed')

# Create the destination directory if it does not exist
os.makedirs(destination_directory, exist_ok=True)

# Regular expressions for the replacements
replacements = {
    r'- !': '- ⚠️',
    r'- no': '- ❌',
    r'- \?': '- ❓',
    r'- yes': '- ✅',
    r'- &': '- 📚',
    r'!\[\[images/([^]]+)\]\]': r'![image](images/\1)'
}

# Get a list of all Markdown files in the source directory
markdown_files = [f for f in os.listdir(source_directory2) if f.endswith('.md')]

# Iterate through each Markdown file
for md_file in markdown_files:
    source_path = os.path.join(source_directory2, md_file)
    destination_path = os.path.join(destination_directory, md_file)
    
    with open(source_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Apply the replacements
        for pattern, replacement in replacements.items():
            content = re.sub(pattern, replacement, content)
    
    # Write the modified content to the destination file
    with open(destination_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Markdown files have been processed and saved to the 'md_changed' folder.")

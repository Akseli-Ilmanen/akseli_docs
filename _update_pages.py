import os
import re
import shutil

# Get the current working directory
curr_directory = os.getcwd()

# Step 1: COPY IMAGES TO DESTINATION FOLDER AND EDIT MARKDOWN FILES

# Navigate two levels up
three_levels_up = os.path.abspath(os.path.join(curr_directory, "../../../"))
print(f"Two levels up: {three_levels_up}")

# Get path to the source directory containing images
source_directory = os.path.join(three_levels_up, 'Z-Admin', 'image')

# Set the destination directory for copied images
destination_directory = os.path.join(os.getcwd(), 'images')

# Create the destination directory if it does not exist
os.makedirs(destination_directory, exist_ok=True)

# Regular expression to match Markdown image references
image_reference_pattern = r'!\[\[([^]]+)\]\]'

# Get directory of markdown files to be copied
os.chdir(os.path.join(three_levels_up, 'Projects', 'Copy to github pages'))
print("Current Directory:", os.getcwd())

# Get a list of all Markdown files in the current directory
markdown_files = [f for f in os.listdir('.') if f.endswith('.md')]

# Regular expressions for the replacements
replacements = {
    r'- !': '- ⚠️',
    r'- no': '- ❌',
    r'- \?': '- ❓',
    r'- yes': '- ✅',
    r'- &': '- 📚',
    r'!\[\[([^]]+)\]\]': r'![image](images/\1)'
}

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
        
        # Apply the replacements
        for pattern, replacement in replacements.items():
            content = re.sub(pattern, replacement, content)
        
        # # Add 'usemathjax: true' below the first '---'
        # content = re.sub(r'^(---\s*\n)', r'\1usemathjax: true\n', content, count=1)
    
    # Write the modified content to the destination file
    destination_path = os.path.join(curr_directory, md_file)
    with open(destination_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Image extraction and markdown file processing complete.")

import os
import re
import shutil

# Set the source and destination directories
source_directory = os.getcwd()
destination_directory = os.path.join(source_directory, 'md_changed')

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
markdown_files = [f for f in os.listdir(source_directory) if f.endswith('.md')]

# Iterate through each Markdown file
for md_file in markdown_files:
    source_path = os.path.join(source_directory, md_file)
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
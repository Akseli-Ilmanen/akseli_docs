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

# Get a list of all Markdown files in the current directory except index.md
markdown_files = [f for f in os.listdir('.') if f.endswith('.md') and f != 'index.md']

# Regular expressions for the replacements
replacements = {
    r'- !': '- ⚠️',
    r'- no': '- ❌',
    r'- \?': '- ❓',
    r'- yes': '- ✅',
    r'- &': '- 📚',
    r'!\[\[([^]]+)\]\]': r'![image](images/\1)',  # Convert image references to the new format
    r'# ': '<br/><br/># ',
    r'## ': '<br/><br/>##',
    r'###': '<br/><br/>##',
    r'####': '<br/><br/>###',
    r'#####': '<br/><br/>####',
    r'######': '<br/><br/>#####',
    r'#######': '<br/><br/>######',
    r'########': '<br/><br/>#######'

    
}

# Function to process math blocks by temporarily replacing $$ blocks
def process_math_blocks_first(content):
    # Replace $$ blocks with unique placeholders
    content = re.sub(r'(\n?)\$\$(.*?)\$\$', r'\1{{MATH_BLOCK}}\2{{/MATH_BLOCK}}', content, flags=re.DOTALL)
    return content

# Function to process math blocks by replacing single $...$ with $$...$$ and restoring $$ blocks
def process_math_blocks_second(content):
    # Replace single $...$ with $$...$$
    content = re.sub(r'(?<!\$)\$(.*?)\$(?!\$)', r'$$\1$$', content)

    # Restore the $$ blocks back to their original format
    content = content.replace('{{MATH_BLOCK}}', '\n$$').replace('{{/MATH_BLOCK}}', '\n$$\n')
    
    return content



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

        # Apply the replacements for other patterns (such as - !, - no, etc.)
        for pattern, replacement in replacements.items():
            content = re.sub(pattern, replacement, content)

        # Step 1: Process math blocks by replacing $$ blocks with placeholders
        content = process_math_blocks_first(content)

        # Optional: Add 'title: filename' below the first '---' in the frontmatter
        content = re.sub(r'^(---\s*\n)', 
                         rf'\1title: {os.path.splitext(md_file)[0]}\nlayout: default \nmathjax: true\n', 
                         content, 
                         count=1)


    # Write the adjusted markdown file after the first processing step
    adjusted_md_file = os.path.join(curr_directory, f"{md_file}")
    with open(adjusted_md_file, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"First processing step complete for {md_file}. Adjusted markdown saved as {adjusted_md_file}")

    # Step 2: Now, read the adjusted markdown file and apply the second processing step
    with open(adjusted_md_file, 'r', encoding='utf-8') as file:
        adjusted_content = file.read()

        # Step 2: Replace single $...$ with $$...$$ and restore $$ blocks
        adjusted_content = process_math_blocks_second(adjusted_content)

    # Write the final modified content back to the original file or new file
    final_md_file = os.path.join(curr_directory, f"{md_file}")
    with open(final_md_file, 'w', encoding='utf-8') as file:
        file.write(adjusted_content)

    print(f"Second processing step complete for {md_file}. Final markdown saved as {final_md_file}")

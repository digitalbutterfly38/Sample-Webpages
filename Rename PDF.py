import os
import re

def rename_pdf_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            new_filename = re.sub(r'[^\w\s.-]', ' ', filename)  # Replace special characters with spaces
            new_filename = new_filename.replace(' ', '_')        # Replace spaces with underscores (optional)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)

# Specify the directory containing the PDF files you want to rename
directory = '/path/to/pdf/files'

# Call the function to rename the PDF files
rename_pdf_files(directory)

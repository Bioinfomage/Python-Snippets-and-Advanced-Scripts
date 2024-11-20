# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:29:56 2024

@author: kanmani
"""

import sys
from pathlib import Path

# Accept the file list from command line arguments
ifile = sys.argv[1:]

# Function to delete temporary files
def del_temp_files(list_of_temp_files):
    for filename in list_of_temp_files:
        file_path = Path(filename)  # Use pathlib for file handling
        try:
            if file_path.exists():
                file_path.unlink()  # Delete the file
                print(f"Deleted: {filename}")
            else:
                print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")

# Call the function to delete files
del_temp_files(ifile)

print("\nThe raw netMHC files are removed.")

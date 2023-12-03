"""
Script Name: DumpExif.py
Author: Zailani
Version: 1.0.0
Description: 
    This Python script exif meta data from an image file.
Dependencies:
    exifread
"""

# Import the required modules
import exifread
import os
import sys

def dump_metadata(jpg_file):
    # Open the image file
    img = open(jpg_file, "rb")

    # Get the EXIF metadata
    exif = exifread.process_file(img)

    # Loop through the tags and print the property name and value
    for tag in exif.keys():
        #Exclude thumbnail tag
        if "thumbnail" not in tag.lower():
            # Get the tag value
            value = exif[tag]
            # Print the property name and value
            print(f"{tag:25}: {value}")

    # Close the image file
    img.close()

if __name__ == "__main__":
    # Check if the file name is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please provide the file name as a command line argument.")
        sys.exit(1)

    # Get the file name from the command line argument
    jpg_file = sys.argv[1]

    # Call the dump_metadata function with the specified file name
    dump_metadata(jpg_file)
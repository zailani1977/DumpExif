# DumpExif

## Description
This Python script dumps the EXIF metadata from an image file. EXIF metadata is information about the image, such as the camera model, date and time, GPS location, etc. The script uses the exifread module to read the metadata and prints it to the standard output.

## Dependencies
- Python 3.x
- exifread

## Usage
To use the script, you need to provide the image file name as a command line argument. For example:

```bash
python DumpExif.py sample.jpg
```

The script will print the metadata properties and values, excluding the thumbnail tag. For example:

```text
Image Make                : Canon
Image Model               : Canon EOS 600D
Image XResolution         : 72
Image YResolution         : 72
Image ResolutionUnit      : Pixels/Inch
Image Software            : Adobe Photoshop CS6 (Windows)
Image DateTime            : 2023:03:22 15:16:54
Image Artist              : Zailani
Image ExifOffset          : 182
...
```

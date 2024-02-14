import os
import subprocess

# replace user for personal use otherwise directory will not exist!
user = "pinke"
desktop_dir = f"C:/Users/{user}/Desktop"

if __name__ == "__main__":
    while True: # continuously running as background script
        desktop_files = os.listdir(desktop_dir)

        for file in desktop_files:
            # desktop.ini cannot be manipulated
            if file != 'desktop.ini':
                # extra conditional to deal with potential errors where filenames include
                # a space or apostrophe character
                if ' ' in file:
                    file = f"\"{file}\""
                
                # construct the absolute pathname and change 'hidden' attribute
                file_path = desktop_dir + '/' + file
                process = os.popen(f"attrib +h {file_path}")
                t = process.read()
                process.close()

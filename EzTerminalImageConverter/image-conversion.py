import os
import argparse

from PIL import Image
from terminalcolor import White, LightGreen, Yellow, LightYellow, LightCyan, LightBlue, Red

true = True
false = False

def image_conversion(all, extension, quality=100):
    dir = os.listdir(".")
    filenames = []

    if not all:
        temp_files = []
        i = 0
        print(White("\nFiles:\n"))
        for file in dir:
            try:
                with Image.open(file) as im:
                    print(LightBlue(f"{i}. '{file}'"))
                    temp_files.append(im.filename)
                    i += 1
            except OSError:
                pass


        while True:
            try:
                ids_input = input(LightGreen("\nEnter file id(s). For multiple files, separate each id with a space. Enter 'q' to quit: "))
                
                if ids_input.lower() == 'q':
                    return
                
                ids = list(map(int, ids_input.split()))
                
                for id in ids:
                    filenames.append(temp_files[id])

                break
                
            except (ValueError, IndexError):
                print(Red("Invalid input. Please enter a valid input."))
                filenames = []
           
    else:
        for file in dir:
            try:
                with Image.open(file) as im:
                    filenames.append(im.filename)
            except OSError:
                pass

    for f in filenames:
        new_filename = f"{f.split(".")[0]}.{extension}"

        print(f"Converting {Yellow(f.split("\\")[-1])} to {LightYellow(new_filename.split("\\")[-1])}")
        
        img = Image.open(f)  # Create a copy of the Image object
        img.save(new_filename, extension.upper(), quality=quality)

    print(LightCyan("Done."))
    
             


def main():

    # Set up argument parser
    parser = argparse.ArgumentParser(prog="Ez Image Converter",description='Convert images to other formats!')
    parser.add_argument('extension', type=str, help='File output extension type.')
    parser.add_argument('--all', '--a', action='store_true', help='Manually pick files (use --no-all) or all image files in directory.')
    parser.add_argument('--quality', '--q', type=int, default=100, help='Quality of the WEBP output (0-100).')

    args = parser.parse_args()

    # Use the current directory as the base for finding and converting images
    image_conversion(all=args.all, extension=args.extension, quality=args.quality)

if __name__ == "__main__":
    main()

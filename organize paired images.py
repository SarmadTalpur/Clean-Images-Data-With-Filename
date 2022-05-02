# rename and keep paired eye images i.e., left and right eye images of a patient captured on a same date and move them to separate folder.

# importing python modules
import os
import re
import shutil

def rename(folder):
    '''Function to rename paired images of patient by checking patient name, left_right eye pair and date of examination in the file'''
    # temporary variable just to check if match was found for a image, it shouldn't be matched with further images 
    previous = 0
    # renaming file number
    i = 0
    # loop through all the files in the directory
    for count, filename in enumerate(os.listdir(folder)):
        # if image already had match with previous image, move to the next image for checking
        if previous == 1:
            # changing temporary variable back to zero so the next new image doesn't go in this previous match condition
            previous = 0
            continue
        # loop through all the files in the directory again for pair checking
        for count2, filename2 in enumerate(os.listdir(folder)):
            # compare image filenames (image to the next image) by only the patient name and date of examination
            if count == count2-1:
                file1 = re.search("^([^_]+)_", filename).group(0)
                file2 = re.search("^([^_]+)_", filename2).group(0)
                # if the pair is of left and right eye, only then rename files accordingly
                if (file1 == file2) and ((("Color_L" in filename) and ("Color_R" in filename2)) or (("Color_R" in filename) and ("Color_L" in filename2))):
                    if "Color_L" in filename:
                        dst = f"{i}_left.jpg"
                        dst2 = f"{i}_right.jpg"
                    # else rename should be i_right i.e., 00_right
                    else:
                        dst = f"{i}_right.jpg"
                        dst2 = f"{i}_left.jpg"
                    # foldername/filename, if .py file is outside folder
                    src =f"{folder}/{filename}"
                    dst =f"{folder}/{dst}"
                    src2 =f"{folder}/{filename2}"
                    dst2 =f"{folder}/{dst2}"
                    os.rename(src, dst)
                    os.rename(src2, dst2)
                    i+=1
                    previous = 1
                else:
                    continue
                break


# move the paired images to a separate folder
def move(src_folder, dest_folder):
    '''Function to move unpaired files'''
    # create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for count, filename in enumerate(os.listdir(src_folder)):
        if (("_left" in filename) or ("_right" in filename)):
            shutil.move(src_folder + "\\" + filename, dest_folder + "\\" + filename)

folder = "F:\\experiment"
move_to = "F:\\Renamed_Pairs"
rename(folder)
move(folder, move_to)
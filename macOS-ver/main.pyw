import os
import shutil

# define globals - replace user with your own profile!!
user = 'erickang'
screenshot_dir = f'/Users/{user}/Pictures/Screenshots'
desktop_dir = f'/Users/{user}/Desktop'
months = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec',
}

# function that checks the existence of a directory
# if it doesn't exist, create it
def dir_check(dir_pathname):
    if not os.path.exists(dir_pathname):
        os.makedirs(dir_pathname)
        print(f"Making new directory: {dir_pathname}")

dir_check(screenshot_dir)
# checks all files on desktop and relocates file if it is a screenshot
while True: # continuous script that runs in background
    desktop_files = os.listdir(desktop_dir)
    for file in desktop_files:
        if file.startswith('Screenshot') and file.endswith('.png'):
            # finds old pathname
            cur_path = desktop_dir + '/' + file
            # extracts necessary fields to categorise and organise screenshots chronologically
            file_month = file[16:18]
            file_day = file[19:21]
            # prepares for file relocation
            new_path = screenshot_dir + '/' + months[file_month] + '/' + file_day
            dir_check(new_path)
            # relocates file with output to terminal
            shutil.move(cur_path, new_path)
            print(f"Moving screenshot: {file} to {new_path}")


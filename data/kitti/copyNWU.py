import os
import shutil

# Define your source and destination folders
mysource_folder = "/media/qhc/Ubuntu 22.0/kitti/data_odometry_velodyne"
mydestination_folder = "/media/qhc/Ubuntu 22.0/kitti/data_odometry_velodyne_NWU"

# Loop through all files and subdirectories in source folder
for item in os.listdir(mysource_folder):

    # Create full path for the item
    myitem_path = os.path.join(mysource_folder, item)

    # Check if item is a file
    if os.path.isfile(myitem_path):

        # Copy the file to the destination folder
        shutil.copy2(myitem_path, mydestination_folder)

    # Check if item is a directory
    elif os.path.isdir(myitem_path):

        # Loop through all files and subdirectories in the directory
        for subitem in os.listdir(myitem_path):

            # Create full path for the subitem
            mysubitem_path = os.path.join(myitem_path, subitem)

            # Copy the subitem to the destination folder
            shutil.copy2(mysubitem_path, mydestination_folder)

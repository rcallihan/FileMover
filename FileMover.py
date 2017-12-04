import os
import shutil

#directory of all files
file_loc = r'C:\Users\rcallihan\Documents\Dev\FileMover\data'

#text file with list of completed file names
finished_file = r'C:\Users\rcallihan\Documents\Dev\FileMover\FilesToMove.txt'

#location where 'other' files should be moved
completed_location = r'C:\Users\rcallihan\Documents\Dev\FileMover\skipped'

# this reads in the files from the file_loc directory and puts them into a list.
file_list = os.listdir(file_loc)

with open(finished_file) as f:
    content = f.readlines()
content = [x.strip() for x in content]

content_set = set(content)
file_list_set = set(file_list)

set_difference = file_list_set.difference(content_set)

for move_file in set_difference:

    #create full path names for the origin and destination. Full paths are necessary for the file copy function (shutil)
    origin_path = os.path.join(file_loc, move_file)
    to_move_path = os.path.join(completed_location, move_file)

    #copy the file from the origin to the destination path.
    shutil.copy(origin_path, to_move_path)

    print("Moved %s to %s" % (move_file, to_move_path))

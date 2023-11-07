import os
import subprocess


def get_file_names(file_path, file_type='.mp3'):
    '''Function: Get the name of files with specified type in a folder.

    Parameters:
        file_path <str> -- The path of files.
        file_type <str> -- The type of files. Default is '.mp3'.

    Return:
        file_names <list> -- The name of files with extension.
    '''
    file_names = []
    files = [file for file in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, file))]

    for file in files:
        if file_type in file:
            file_names.append(file)

    return file_names


# Part 1 Set the path of input and output media.

PATH_CLIPS = 'mid/'
FILE_CLIPS = 'List_Audio.txt'
FILE_MERGE = 'Demo_new.mp3'


# Part 2 Write media list to a TXT file.

file_names = get_file_names(PATH_CLIPS)
file_names.sort(reverse=False)

with open(FILE_CLIPS, 'w') as ff:
    for file_name in file_names:
        content = 'file \'' + PATH_CLIPS + file_name + '\'' + '\n'
        ff.write(content)


# Part 3 Merge media clips with FFmpeg command.

# $ ffmpeg -f concat -i media_list.txt out.mpn
# 'media_list.txt' - It contains the path of each media clip.
# Note:
#     The path of one clip is 'media_clips/media_clip_1.mpn'.
#     It has the same parent folder 'PATH_MEDIA' as 'media_list.txt'.
# Note:
#     Removing 'copy' re-encodes clips and avoids black screen/frames.
#     Removing 'copy' leads to high CPU load and long operating time.
# Generate the command for processing input media.
cmd = 'ffmpeg -f concat -i ' + FILE_CLIPS + ' ' + FILE_MERGE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)

#ffmpeg -i name.m4a -c:v copy -c:a libmp3lame -q:a 4 name.mp3
#https://github.com/HeZhang1994/video-audio-tools/blob/master/VideoAudio_Editing/run_Audio_02Merge.py

import os
import re
import shutil
import subprocess

def milliseconds_to_time(milliseconds):
    # Calculate hours, minutes, and seconds
    total_seconds = milliseconds // 1000
    seconds = total_seconds % 60
    total_minutes = total_seconds // 60
    minutes = total_minutes % 60
    hours = total_minutes // 60
    other = milliseconds % 1000

    # Format the time string as HH:MM:SS
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{other:03d}"
    return time_str


INPUT_MEDIA = 'name.m4a'
# Download link: Null (The length of input video in this demo should be longer than 12min).
OUTPUT_PATH = './'
OUTPUT_NAME = 'name_clips_'
OUTPUT_TYPE = '.m4a'

# Part 2 Set the cutting points of original media.

LIST_START = []
LIST_END = []
# The start points of clips.
for line in open('name_test.tsv'):
    line = line.strip().split()
    LIST_START.append(line[0])
    LIST_END.append(line[1])

#LIST_START = ['00:00:45', '00:02:07', '00:10:02', '00:11:17']
# The end points of clips.
#LIST_END = ['00:01:29', '00:02:40', '00:10:30', '00:11:51']

# Check the start and end points of original media.
if len(LIST_START) != len(LIST_END):
    print('Error: Start points are not matched with end points.')
else:
    num_clip = len(LIST_START)


# Part 3 Cut original media with FFmpeg command.

# $ ffmpeg -i in.mpn -ss [start] -to [end] out.mpn
# Note:
#    '[start]' - The start point of original media 'in.mpn'.
#    '[start]' - The format is 'hh:mm:ss.xxx' or 'nnn', '00:01:15.000' or '75'.
#    '[end]'   - The end point of original media 'in.mpn'.
#    '[end]'   - The format is 'hh:mm:ss.xxx' or 'nnn', '00:01:25.000' or '85'.
# Note:
#     Setting '-i in.mpn' before '-ss [start]' avoids inaccurate clips.
#     Removing 'copy' re-encodes clips and avoids black screen/frames.
#     Removing 'copy' leads to high CPU load and long operating time.

for t in range(num_clip):
    #    tag_start = LIST_START[t] + '.000'
#    tag_end = LIST_END[t] + '.000'
    tag_start = milliseconds_to_time(int(LIST_START[t]))
    tag_end = milliseconds_to_time(int(LIST_END[t]))
    print(tag_start, tag_end)
    # Generate the path for saving output media.
    output_file = OUTPUT_PATH + OUTPUT_NAME + str(t + 1) + OUTPUT_TYPE

    # Generate the command for processing input media.
    cmd = 'ffmpeg -i ' + INPUT_MEDIA + ' -ss ' + tag_start + ' -to ' + tag_end + ' ' + output_file

    # Execute the (Terminal) command within Python.
    subprocess.call(cmd, shell=True)

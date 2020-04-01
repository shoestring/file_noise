#!/usr/bin/python3
#
# Generate random files in a temp directory of a certain size.
# Repeat for specified time.
#
# Mike Cammilleri  Tue Mar 31 13:25:38 CDT 202
#
import subprocess
import os
import argparse
import tempfile
import time

# Create random string for directory and cd to it.
# Create argparse options with defaults for path name, file size, and time to run.
td = tempfile.TemporaryDirectory()
randomdir = td.name
os.chdir(randomdir)

parser = argparse.ArgumentParser(description='Create random files of size repeatedly until done.')
parser.add_argument('-p', '--path', required=False, default=randomdir, help='Set the path where the random\
 files should exist.')
parser.add_argument('-s', '--filesize', required=False, default=1024, help='Specify size of each file.')
parser.add_argument('-t', '--runtime', required=False, default=1, help='Specify length of time to run in minutes.')
args = parser.parse_args()

path = args.path
filesize = 'bs=' + str(args.filesize)
runtime = 60*args.runtime

# TO DO Create files of certain size (big-ish)
# TO DO range needs to be a variable

end = time.time() + runtime
while time.time() < end:
    tfn = tempfile.NamedTemporaryFile(dir='.')
    filename = tfn.name
    dd_filename = 'of=' + filename
    bigfiles = subprocess.run(['/bin/dd', 'if=/dev/zero', dd_filename, 'count=400', filesize])
    
# TO DO Then remove files of certain age, or perhaps after they grow to X size. This
# loop should not surpass a certain max_size.


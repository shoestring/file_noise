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

# Create random string for directory and cd to it.
# Create argparse options with defaults for path name, file size, and time to run.
td = tempfile.TemporaryDirectory()
randomdir = td.name
os.chdir(randomdir)

parser = argparse.ArgumentParser(description='Create random files of size repeatedly until done.')
parser.add_argument('-p', '--path', required=False, default=randomdir, help='Set the path where the random\
 files should exist.')
parser.add_argument('-s', '--filesize', required=False, default=1024, help='Specify size of each file.')
parser.add_argument('-t', '--time', required=False, default=10, help='Specify length of time to run.')
args = parser.parse_args()

path = args.path
filesize = args.file
time = args.time

# TO DO Create files of certain size (big-ish)
# TO DO filename needs to be a string or something that subprocess.run can read in. check conversions
for i in range(5):
    tfn = tempfile.NamedTemporaryFile(dir='.')
    filename = str(tfn.name)
    bigfiles = subprocess.run(['/bin/dd', 'if=/dev/zero', 'of=', filename, 'count=400', 'bs=', str(filesize)])

# TO DO Then remove files of certain age, or perhaps after they grow to X size. This
# loop should not surpass a certain max_size.


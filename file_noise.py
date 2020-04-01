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
parser.add_argument('-m', '--maxdirsize', required=False, default='50' help='Maximum directory size in MB.')
parser.add_argument('-s', '--filesize', required=False, default=1024, help='Specify size of each file.')
parser.add_argument('-t', '--runtime', required=False, default=1, help='Specify length of time to run in minutes.')
args = parser.parse_args()

path = args.path
maxdirsize = args.maxdirsize
filesize = 'bs=' + str(args.filesize)
runtime = 60*args.runtime

# Create all the files and don't remove any until the end.
# TO DO set count using a variable or remove it. Need to constrain total disk space used
# so we can't accidentally fill up a partition. Does this happen with /dev/zero? check it
#try:
# Get the current, temporary directory size
dirsize = sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])
# Convert from bytes to MB
current_dirsize = dirsize / 1024 / 2024
# Run the loop
end = time.time() + runtime
while time.time() < end:
    while current_dirsize < maxdirsize:
        tfn = tempfile.NamedTemporaryFile(dir='.', delete=False, prefix='zz')
        filename = tfn.name
        dd_filename = 'of=' + filename
        bigfiles = subprocess.run(['/bin/dd', 'if=/dev/zero', dd_filename, 'count=400', filesize])
    tfn.close()
#except:
#    print("Something went wrong!")
    




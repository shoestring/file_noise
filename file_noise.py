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
td = tempfile.TemporaryDirectory()
randomdir = td.name
os.chdir(randomdir)

# Create argparse options with defaults for path name, file size, and time to run.
parser = argparse.ArgumentParser(description='Create random files of size repeatedly until done.')
parser.add_argument('-p', '--path', required=False, default=randomdir, help='Set the path where the random\
 files should exist.')
parser.add_argument('-m', '--maxdirsize', required=False, default=50000000, help='Maximum directory size in bytes.')
parser.add_argument('-s', '--filesize', required=False, default=4096, help='Specify size of each file.')
parser.add_argument('-t', '--runtime', required=False, default=1, help='Specify length of time to run in minutes.')
args = parser.parse_args()

path = args.path
maxdirsize = args.maxdirsize
filesize = 'bs=' + str(args.filesize)
runtime = 60 * args.runtime

# Get the current, temporary directory size
dirsize = sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])

# Run the loop to do the stuff
try:
    end = time.time() + runtime
    while time.time() < end:
        tfn = tempfile.NamedTemporaryFile(dir='.', delete=False, prefix='zz')
        filename = tfn.name
        dd_filename = 'of=' + filename
        bigfiles = subprocess.run(['/bin/dd', 'if=/dev/zero', dd_filename, 'count=200', filesize])
        # Update the dir size and check if we reached max
        dirsize = sum([os.path.getsize(f) for f in os.listdir(randomdir) if os.path.isfile(f)])
        if dirsize > maxdirsize:
            filelist = os.listdir(randomdir)
            for files in filelist:
                os.unlink(randomdir + "/" + files)
except:
    print("Something went wrong!")

#print("Finished in " + str(runtime/60) + " minutes.")


#!/usr/bin/python3
#
# Generate random files in the temp directory a with specified size limit.
# Repeat for a specified time. Written and tested with python3.6. Uses /dev/zero
# unless you use the -r flag to set it to /dev/urandom.
# Probably not gonna work with old pythons (2.x). Probably could 
# be done more elegant. I promise nothing.
#
# Author:  Mike Cammilleri  
# Date:    Sun Apr  5 22:31:37 CDT 2020

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
parser = argparse.ArgumentParser(description='Create random files using /dev/zero or /dev/urandom repeatedly until done.\
 Redirect stdout to a file if you don\'t want to see all the garbage.')
parser.add_argument('-p', '--path', required=False, default=randomdir, help='Set the path where the random\
 files should exist.')
parser.add_argument('-m', '--maxdirsize', required=False, default=50000000, type=int,\
                    help='Maximum directory size in bytes.')
parser.add_argument('-f', '--filesize', required=False, default=4096, help='Specify size of each file.')
parser.add_argument('-t', '--runtime', required=False, default=1, type=int,\
                    help='Specify length of time to run in minutes.')
parser.add_argument('-r', '--nonzero', required=False, action='store_true',\
                    help='Use /dev/urandom for non-zeroed files.')
args = parser.parse_args()

path = args.path
maxdirsize = args.maxdirsize
filesize = 'bs=' + str(args.filesize)
runtime = 60 * args.runtime
if args.nonzero is True:
    device = 'if=/dev/urandom'
else:
    device = 'if=/dev/zero'

# Get the current, temporary directory size
dirsize = sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])

# Run the loop and do the stuff
try:
    end = time.time() + runtime
    while time.time() < end:
        tfn = tempfile.NamedTemporaryFile(dir='.', delete=False, prefix='zz')
        filename = tfn.name
        dd_filename = 'of=' + filename
        bigfiles = subprocess.run(['/bin/dd', device, dd_filename, 'count=200', filesize])
        # Update the dir size and check if we reached max
        dirsize = sum([os.path.getsize(f) for f in os.listdir(randomdir) if os.path.isfile(f)])
        if dirsize > maxdirsize:
            filelist = os.listdir(randomdir)
            for files in filelist:
                os.unlink(randomdir + "/" + files)
except:
    print("Something went wrong!")

print("Finished in " + str(runtime/60) + " minutes.")

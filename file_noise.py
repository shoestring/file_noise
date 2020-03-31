import subprocess
from os import path
import argparse
import tempfile

# TO DO Create argparse options with defaults for path name, file size, and time to run.

filename = tempfile.NamedTemporaryFile()
parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('-p', '--path', required=False, default='/tmp/randomfiles', help='Set the path where the random files should exist.')
parser.add_argument('-s', '--file', required=False, default=1024, help='Specify size of each file.')
parser.add_argumet('-t', '--time', required=False, default=10, help='Specify length of time to run.')
args = parser.parse_args()


# Create temporary directory with random name

with tempfile.TemporaryDirectory() as td:
    os.mkdir(td)




# TO DO Create files of certain size (big-ish) perhaps by streaming data into them?
# Can use subprocess 'dd' to create empty files of 'size.' Randomize file names using
# random().
bigfiles = subprocess.run(['/bin/dd', 'if=/dev/zero', 'of=./data.bin', 'count=400', 'bs=1024'])

# TO DO Then remove files of certain age, or perhaps after they grow to X size. This
# loop should not surpass a certain max_size.


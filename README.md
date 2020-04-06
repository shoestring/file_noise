```
usage: file_noise.py [-h] [-p PATH] [-m MAXDIRSIZE] [-f FILESIZE] [-t RUNTIME]
                     [-r]

Create random files using /dev/zero or /dev/urandom repeatedly until done.
Redirect stdout to a file if you don't want to see all the garbage.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Set the path where the random files should exist.
  -m MAXDIRSIZE, --maxdirsize MAXDIRSIZE
                        Maximum directory size in bytes.
  -f FILESIZE, --filesize FILESIZE
                        Specify size of each file.
  -t RUNTIME, --runtime RUNTIME
                        Specify length of time to run in minutes.
  -r, --nonzero         Use /dev/urandom for non-zeroed files.              

Create a bunch of random files of a certain size and keep doing it for a specified amount of time. The idea is to create file noise and keep a disk busy to aid in other tests/troubleshooting.

```
usage: file_noise.py [-h] [-p PATH] [-m MAXDIRSIZE] [-f FILESIZE] [-t RUNTIME]

Create random files of size repeatedly until done. Redirect stdout to a file
if you don't want to see all the garbage.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Set the path where the random files should exist.
  -m MAXDIRSIZE, --maxdirsize MAXDIRSIZE
                        Maximum directory size in bytes.
  -f FILESIZE, --filesize FILESIZE
                        Specify size of each file.
  -t RUNTIME, --runtime RUNTIME
                        Specify length of time to run in minutes.
 ```                      

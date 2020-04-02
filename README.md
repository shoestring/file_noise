Create a bunch of random files of a certain size and keep doing it for a specified amount of time. The idea is to create file noise and keep a disk busy to aid in other tests/troubleshooting.

``````usage: file_noise.py [-h] [-p PATH] [-s FILESIZE] [-t RUNTIME]
4
​
5
Create random files of size repeatedly until done.
6
​
7
optional arguments:
8
  -h, --help            show this help message and exit
9
  -p PATH, --path PATH  Set the path where the random files should exist.
10
  -s FILESIZE, --filesize FILESIZE
11
                        Specify size of each file.
12
  -t RUNTIME, --runtime RUNTIME
13
                        Specify length of time to run in minutes.
 ```                      

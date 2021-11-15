import os.path
import filecmp

ncso="/home/ubuntu/tbb/not_connected_started_once/tor-browser_en-US/"
ns="/home/ubuntu/tbb/never_started/tor-browser_en-US/"

def dircomp(dir1, dir2):
    cmp = filecmp.dircmp(dir1, dir2)
    cmp.report()

def main():
    dircomp(ncso, ns)

if __name__ == '__main__':
    main()
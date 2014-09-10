#!/usr/bin/env python

import random   # Random number generator
import os       # Crossplatform OS rutines
import sys      # interpreter tools
import argparse # parse command-line arguments

legal_chars = "abcdefghijklmnopqrstuvwxyz"+\
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"0123456789_"

def random_string(length=6, prefix="", legal_chars=legal_chars):
    """
Create a random string of text.

Parameters
----------
length : int
    Length of the string (minus the prefix part).
prefix : string
    Prefix the string with some text.
legal_chars : string
    A string of charracter that are allowed to be used in the
    output.

Returns
-------
rnd_str : str
    """
    chars = []
    for i in xrange(length):
        chars += random.choice(legal_chars)
    res = prefix+''.join(chars)
    return res


def generate_tree(target, dirs=3, rec_depth=2, verbose=False):
    """
Genereate a random folder structure with random names.

Parameters
----------
target : str
    Path to the root where folders are to be created.
dirs : int
    Maximum number of directories to be created per directory.
rec_depth : int
    Maximum directory depth.
verbose : bool
    Be loud about what to do.
    """
    if rec_depth > 0:
        for i in xrange(random.randint(0, dirs+1)):
            new_dir = target + random_string(6) + "/"
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
                if verbose:
                    print("Creating directory: " + new_dir)
            generate_tree(new_dir, dirs, rec_depth-1, verbose)
    return
    

def populate_tree(target, files=5, size=800, start_time=1388534400,
        end_time=1406851201000, verbose=False):
    """
Generate random files with random content.

Parameters
----------
target : str
    Path to the file tree where the files are being created.
files : int
    Maximum number of directories to be created.
size : int
    Maximum size in kilobyte for each file.
start_time : int
    Lower bound for access time (atime) and modified time (mtime)
    allowed in each file.
    Denoted in Unix time format.
end_time : int
    Same as start_time, but for upper bound.
verbose : bool
    Be loud about what to do.
    """
    
    def walk_function(arg, dirname, fnames):
        """
    Function used in os.path.walk

    Following the logic of Python scoping, this is a local function,
    only visible inside of populate_tree.
    This function should be passed to os.path.walk.
        
    Parameters
    ----------
    arg : obj
        Arbitrary argument specified at initialization.
    dirname : str
        Name of a directory in file tree (changes with each call.
    fnames : list
        List of filenames in file tree.
        """
        # Fill in code for walk function
        for i in xrange(random.randint(0, files+1)+1):
            cur_file = dirname + "/" +random_string(6)
            if verbose:
                print ("Creating file: " + cur_file)
            with open(cur_file, "w") as f:
                f.write(random_string(random.randint(1, size+1)*1024))
                os.utime(cur_file, (random.randint(start_time, end_time+1), random.randint(start_time, end_time+1)))
    os.path.walk(target, walk_function, None)


# If-test to ensure code only executed if ran as stand-alone app
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create a random file tree")
    parser.add_argument("target", help="target folder")
    parser.add_argument("folders", help="max. # of folders created at each level")
    parser.add_argument("files", help="max. # of files created at each level")
    parser.add_argument("-s", "--size", help="file size")
    parser.add_argument("-d", "--depth", help="recursion depth")
    parser.add_argument("-S", "--start", help="mtime/atime start")
    parser.add_argument("-e", "--end", help="mtime/atime end")
    parser.add_argument("--seed", help="seed for the RNG")
    parser.add_argument("-v", "--verbose", action="store_true", help="print info")
    args = parser.parse_args()

    # Fix the random seed (if not None):
    random.seed(args.seed)    

    generate_tree(args.target, int(args.folders or 3) , int(args.depth or 5), args.verbose)
    populate_tree(args.target, int(args.files or 5), int(args.size or 800), 
                  int(args.start or 1388534400),int(args.end or 1406851201000), args.verbose)





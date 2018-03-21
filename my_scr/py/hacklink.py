#!/usr/bin/env python3
# .py
# ------------------------------------------------------------------------------
# Version:  1.0
# Author:   Alfie
# Desc:
#
# -*- coding: utf-8 -*-
cmd_doc="""
    Usage:
"""

# ==============================================================================
# Import Library
import argparse
#import getopt
import logging
import math
import os
import re
import shutil
import sys
import time

# --------------------------------------
# Extended Library

# ==============================================================================
# Module Varaible
src_file=""

# ------------------------------------------------------------------------------
# Setting Parser
#parser = argparse.ArgumentParser(description='Process argument')
## positional arguments
#parser.add_argument("echo")

# optional arguments
#parser.add_argument('-v', '--verbose', action="store_true", help="increase output verbosity")
#parser.add_argument('-v', '--verbose', type=int, choices=[0, 1, 2], help="increase output verbosity")

#parser.add_argument('-a', action="store_true", default=False, help="haha")
#parser.add_argument('-b', action="store", dest="b")
#parser.add_argument('-c', action="store", dest="c", type=int)
#parser.add_argument('-f', action="store", dest="src_file")


#print(parser.parse_args(['-a', '-bval', '-c', '3']))
#parser.parse_args()
#args = parser.parse_args()

#print(args.echo)
#if args.verbose:
#    print("verbosity turned on")

# ------------------------------------------------------------------------------
# Setting logger
# set up logging to console
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(pathname)s,%(lineno)-04d [%(levelname)s] %(funcName)s::%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# set up logging to file
log_n = 'python_exec.log'
log_n_bu = log_n + ".bu"
if os.path.isfile(log_n): shutil.move(log_n,log_n_bu)
f_handler = logging.FileHandler(log_n)
f_handler.setLevel(logging.DEBUG)
f_formatter = logging.Formatter('[%(asctime)s] %(pathname)s,%(lineno)-04d %(name)s [%(levelname)s] %(funcName)s::%(message)s','%H:%M:%S')
f_handler.setFormatter(f_formatter)
logger.addHandler(f_handler)
# ==============================================================================
# Class


# ==============================================================================
# Function



# ==============================================================================
# Main Process

def main():
    print("Main")
    print(src_file)
    dst_file = src_file + '.new'
    src_o = open(src_file, 'r')
    dst_o = open(dst_file, 'w')

    for line in src_o:
        pattern = '/gpfs.*gold.*\.v'
        result = re.search(pattern,line)
        if result:
            #print(result.group())
            cmd = 'readlink ' + result.group()
            link = os.popen(cmd,"r")
            print(link.readline())


# ==============================================================================
#
if __name__ == "__main__":
    #av = sys.argv[1:]
    src_file =  sys.argv[1];
    #print getopt(sys.argv[1:], "a:b", ["alpha=", "beta"])
    #if av:
    #else:
    main()



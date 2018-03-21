#!/usr/local/bin/python3.3
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
import getopt
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



# ==============================================================================
# Class


# ==============================================================================
# Function


def find_smallest():
    # 'is' and 'is not' is similar to, but stronger than '=='
    # use it to check True or False
    smallest = None
    for value in [3,41,12,9,74,15]:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
        print("%d, %d" %(smallest, value) )

    print("Afer %d" %smallest)

def print_str(inp_str):
    ##
    #idx = 0
    #while idx < len(inp_str):
    #    letter = inp_str[idx]
    #    print(idx,letter)
    #    idx = idx + 1

    # Better
    for letter in inp_str:
        print(letter)

    print(inp_str[:2])
    print(inp_str[2:])

def file_op(filename):
    try:
        file_h = open(filename)
    except:
        print("File cannpt openned:",filename)
        exit()
    cnt = 0
    for line in file_h:
        line = line.rstrip()
        print(line)
        #if line.startswith("From:"):
        #    continue
        #if not "@uct.at.za" in line:
        #    continue
        cnt = cnt + 1
    print("Line Count: %d" %cnt)


def exam_list():
    friends = ['Joe','Ryan','Amy']

    print("")
    print("Start of function exam_list")
    print(range(len(friends)))
    type(friends)
    dir(friends)
    for friend in friends:
        print("Hello::%s" %friend)
    for i in range(len(friends)):
        print("Goodbye::%s" %friends[i])

def hw8_4():
    #fname = raw_input("Enter file name: ")
    fname = "romeo.txt"
    fh = open(fname)
    lst = list()
    for line in fh:
        #print(line.rstrip())
        words = line.split()
        #print(len(words))
        for word in words:
            lst.append(word)
    lst = sorted(set(lst))
    print(lst)

# ==============================================================================
# Main Process

def main():
    #find_smallest()
    #print_str("apple pie")
    #file_op("test_for_py")
    #file_op("test_for_bad")
    #exam_list()
    hw8_4()

# ==============================================================================
#
if __name__ == "__main__":
    av = sys.argv[1:]
    #if av:
    #else:
    main()


